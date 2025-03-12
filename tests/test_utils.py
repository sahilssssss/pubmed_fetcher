import pytest
from pubmed_paper_fetcher.utils import extract_company_authors

@pytest.mark.parametrize("authors, expected_non_academic, expected_companies", [
    # Basic case: Mix of academic and company authors
    (
        [("John Doe", "Harvard University"), 
         ("Alice Smith", "Biotech Corp"), 
         ("Bob Brown", "Pharma Inc.")], 
        ["Alice Smith", "Bob Brown"], 
        ["Biotech Corp", "Pharma Inc."]
    ),

    # Edge case: Empty author list
    (
        [],
        [],
        []
    ),

    # Edge case: Only academic authors
    (
        [("John Doe", "Harvard University"), 
         ("Jane Roe", "MIT")], 
        [],
        []
    ),

    # Edge case: Only company-affiliated authors
    (
        [("Alice Smith", "Biotech Corp"), 
         ("Bob Brown", "Pharma Inc.")], 
        ["Alice Smith", "Bob Brown"], 
        ["Biotech Corp", "Pharma Inc."]
    ),

    # Edge case: Company name within a larger phrase
    (
        [("Charlie Johnson", "BioTech Pharmaceuticals Ltd")], 
        ["Charlie Johnson"], 
        ["BioTech Pharmaceuticals Ltd"]
    ),
])
def test_extract_company_authors(authors, expected_non_academic, expected_companies):
    """Test if company-affiliated authors are correctly filtered."""
    non_academic, companies = extract_company_authors(authors)

    assert sorted(non_academic) == sorted(expected_non_academic), f"Expected {expected_non_academic}, got {non_academic}"
    assert sorted(companies) == sorted(expected_companies), f"Expected {expected_companies}, got {companies}"
