from typing import List, Tuple
from pubmed_paper_fetcher.constants import COMPANY_KEYWORDS

def extract_company_authors(authors: List[Tuple[str, str]]) -> Tuple[List[str], List[str]]:
    """Filters non-academic authors based on affiliations.

    Args:
        authors (List[Tuple[str, str]]): List of (author_name, affiliation).

    Returns:
        Tuple[List[str], List[str]]: (Non-academic authors, Company affiliations)
    """
    non_academic_authors = []
    company_affiliations = []

    for author, affiliation in authors:
        affiliation_clean = affiliation.strip().lower()  
        if any(keyword.lower() in affiliation_clean for keyword in COMPANY_KEYWORDS):
            non_academic_authors.append(author)
            company_affiliations.append(affiliation)

    return non_academic_authors, company_affiliations
