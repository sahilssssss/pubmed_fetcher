import argparse
import csv
import logging
from pubmed_paper_fetcher.fetch_papers import fetch_papers
from pubmed_paper_fetcher.utils import extract_company_authors
from pubmed_paper_fetcher.constants import DEFAULT_CSV_FILENAME, CSV_HEADERS

# logging configurations

logging.basicConfig(level=logging.INFO)

def save_to_csv(data,filename=DEFAULT_CSV_FILENAME):
    """Saves results to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(CSV_HEADERS)
        writer.writerows(data)
    logging.info(f"Results saved to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("--query", "-q", required=True, help="Search query for PubMed")
    parser.add_argument("--file", "-f", help="Filename to save results as CSV")
    parser.add_argument("--debug", "-d", action="store_true", help="Enable debug mode")

    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    papers = fetch_papers(args.query)
    results = []

    for paper in papers:
        non_academic_authors, company_affiliations = extract_company_authors(paper.get("authors", []))
        corresponding_email = paper.get("Corresponding Author Email", "Not available")

        results.append([
            paper["PubMedID"],
            paper["Title"],
            paper["Publication Date"],
            ", ".join(non_academic_authors),
            ", ".join(company_affiliations),
            corresponding_email
        ])

    # Saving results to CSV file
    output_file = args.file if args.file else DEFAULT_CSV_FILENAME
    save_to_csv(results, output_file)
    logging.info(f"Results saved to {output_file}")

if __name__ == "__main__":
    main()
