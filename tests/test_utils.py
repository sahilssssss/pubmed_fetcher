from pubmed_paper_fetcher.utils import extract_company_authors

def test_extract_company_authors():
    """Test if company-affiliated authors are correctly filtered"""
    authors = [
        ("John Doe", "Harvard University"),  # Academic
        ("Alice Smith", "Biotech Corp"),    # Company
        ("Bob Brown", "Pharma Inc.")        # Company
    ]
    
    non_academic, companies = extract_company_authors(authors)
    
    assert "Alice Smith" in non_academic, "Alice should be classified as non-academic"
    assert "Bob Brown" in non_academic, "Bob should be classified as non-academic"
    assert "Harvard University" not in companies, "Harvard should NOT be considered a company"
    assert "Biotech Corp" in companies, "Biotech Corp should be classified as a company"

    print(" Filtering test passed!")
