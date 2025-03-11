import requests
import logging
import xml.etree.ElementTree as ET
import pandas as pd
from typing import List, Dict
from pubmed_paper_fetcher.utils import extract_company_authors
from pubmed_paper_fetcher.constants import (
    SEARCH_URL, FETCH_URL, DEFAULT_MAX_RESULTS, DEFAULT_CSV_FILENAME, CSV_HEADERS
)

# Configure logging
logging.basicConfig(level=logging.INFO)

def fetch_papers(query: str, max_results: int = 20):
    """Fetches research papers from PubMed API."""

    logging.info(f"Sending query to PubMed: {query}") 

    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(SEARCH_URL, params=params)
    response.raise_for_status()
    
    paper_ids = response.json().get("esearchresult", {}).get("idlist", [])
    if not paper_ids:
        logging.warning("No papers found.")
        return []

    logging.info(f"Found {len(paper_ids)} papers. Fetching details...")

    # Fetch paper details
    fetch_params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "xml"
    }
    fetch_response = requests.get(FETCH_URL, params=fetch_params)
    fetch_response.raise_for_status()

    return parse_papers_xml(fetch_response.text)

def parse_papers_xml(xml_data: str) -> List[Dict]:
    """Parses PubMed XML response to extract paper details."""

    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.find(".//PMID").text if article.find(".//PMID") is not None else "N/A"
        title = article.find(".//ArticleTitle").text if article.find(".//ArticleTitle") is not None else "No title available"

        # Extract publication date
        pub_date_elem = article.find(".//PubDate")
        pub_date = "Unknown Date"
        if pub_date_elem is not None:
            year = pub_date_elem.find("Year")
            month = pub_date_elem.find("Month")
            day = pub_date_elem.find("Day")
            pub_date = f"{year.text if year is not None else ''}-{month.text if month is not None else ''}-{day.text if day is not None else ''}"

        # Extract authors and affiliations
        authors_data = []
        corresponding_email = None

        for author in article.findall(".//Author"):
            last_name = author.find("LastName")
            first_name = author.find("ForeName")
            affiliation = author.find(".//Affiliation")

            author_name = f"{first_name.text if first_name is not None else ''} {last_name.text if last_name is not None else ''}".strip()
            author_affiliation = affiliation.text if affiliation is not None else "Unknown Affiliation"

            authors_data.append((author_name, author_affiliation))

        # Check for corresponding author email
            if "@" in author_affiliation:
                corresponding_email = author_affiliation

        # Use utils.py to filter non-academic authors
        non_academic_authors, company_affiliations = extract_company_authors(authors_data)

        papers.append({
            "PubMedID": pubmed_id,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Authors": ", ".join(non_academic_authors),
            "Company Affiliations": ", ".join(company_affiliations),
            "Corresponding Author Email": corresponding_email if corresponding_email else "Not available"
        })

    return papers

def save_to_csv(papers: List[Dict], filename: str = DEFAULT_CSV_FILENAME):
    """Saves paper details to a CSV file."""
    
    if not papers:
        logging.warning("No data to save.")
        return
    
    df = pd.DataFrame(papers, columns=CSV_HEADERS)
    df.to_csv(filename, index=False)
    logging.info(f"Saved {len(papers)} papers to {filename}")

if __name__ == "__main__":
    query = input("Enter your search query: ")
    papers = fetch_papers(query, max_results=10)
    save_to_csv(papers)
    print(f"CSV file '{DEFAULT_CSV_FILENAME}' created successfully!")
