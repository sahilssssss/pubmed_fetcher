import argparse
import csv
import logging
import sys  
from pubmed_paper_fetcher.fetch_papers import fetch_papers
from pubmed_paper_fetcher.constants import DEFAULT_CSV_FILENAME, CSV_HEADERS

# Logging configuration
logging.basicConfig(level=logging.INFO)

def save_to_csv(data, filename=DEFAULT_CSV_FILENAME):
    """Saves results to a CSV file, ensuring an empty CSV is created if no data is available."""
    
    if not data:
        logging.warning(" No data to save. Creating an empty CSV.")
        data = [[]]  #  Ensures empty CSV with headers
    
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(CSV_HEADERS)
        writer.writerows(data)
    
    logging.info(f" Results saved to {filename}")

def main():
    """Command-line interface for fetching PubMed papers."""
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("--query", "-q", required=True, help="Search query for PubMed")
    parser.add_argument("--file", "-f", help="Filename to save results as CSV")
    parser.add_argument("--debug", "-d", action="store_true", help="Enable debug mode")

    args = parser.parse_args()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    try:
        papers = fetch_papers(args.query)
        if not papers:
            print("No papers found")
            return []


        results = []
        for paper in papers:
            non_academic_authors = paper.get("Non-academic Authors", "").split(", ")
            company_affiliations = paper.get("Company Affiliations", "").split(", ")
            corresponding_email = paper.get("Corresponding Author Email", "Not available")

            results.append([
                paper["PubMedID"],
                paper["Title"],
                paper["Publication Date"],
                ", ".join(non_academic_authors),
                ", ".join(company_affiliations),
                corresponding_email
            ])

        output_file = args.file if args.file else DEFAULT_CSV_FILENAME
        save_to_csv(results, output_file)

        logging.info(f" Results saved to {output_file}")
        sys.exit(0)  #  Successfull exit code

    except Exception as e:
        logging.error(f" Error: {e}")
        sys.exit(1)  #  Ensure failure exit code if an error occurs

if __name__ == "__main__":
    main()
