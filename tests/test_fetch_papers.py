import pytest
from pubmed_paper_fetcher.fetch_papers import fetch_papers
from pubmed_paper_fetcher.constants import DEFAULT_MAX_RESULTS

def test_fetch_papers_basic():
    """Test fetching papers with a basic query"""

    query = "blood transfusion"
    results = fetch_papers(query, max_results=5)
    
    assert isinstance(results, list), "Results should be a list"
    assert len(results) > 0, "Should return at least one result"
    assert "PubMedID" in results[0], "Each result should have a PubMedID"
    assert "Title" in results[0], "Each result should have a Title"

@pytest.mark.parametrize("query", [
    "cancer therapy AND 2022[Date - Publication]",
    "COVID-19 OR SARS-CoV-2[Title/Abstract]",
    "machine learning AND (radiology OR imaging)",
    "diabetes AND hypertension AND 2021[Date - Publication]",
    "(stroke OR myocardial infarction) AND aspirin"
])
def test_fetch_papers_with_pubmed_syntax(query):
    """Test fetching papers using different PubMed query syntaxes"""
    results = fetch_papers(query, max_results=3)

    # Check if results are returned as a list
    assert isinstance(results, list), "Results should be a list"

    # Ensure results are fetched (PubMed might return 0 for some queries)
    assert len(results) > 0, f"Query '{query}' should return at least one result"

    # Check structure of the first result
    first_paper = results[0]
    assert isinstance(first_paper, dict), "Each result should be a dictionary"
    assert "PubMedID" in first_paper, "Each result should have a PubMed ID"
    assert "Title" in first_paper, "Each result should have a Title"
    assert "Publication Date" in first_paper, "Each result should have a Publication Date"

    # Print the query being tested (useful for debugging)
    print(f" Passed test for query: {query}")

def test_fetch_papers_no_results():
    """Test query that returns no results"""
    query = "randomtextthatreturnsnothing"
    results = fetch_papers(query, max_results=5)

    assert isinstance(results, list), "Results should be a list"
    assert len(results) == 0, "No results should be returned for a nonsense query"

def test_fetch_papers_max_results():
    """Test fetching a specific number of results"""
    query = "machine learning"
    max_results = 3
    results = fetch_papers(query, max_results=max_results)

    assert len(results) == max_results, f"Should return exactly {max_results} results"

def test_fetch_papers_invalid_query():
    """Test invalid query handling (e.g., special characters)"""
    query = "@#$%^&*()"
    results = fetch_papers(query, max_results=5)

    assert isinstance(results, list), "Results should be a list"
    assert len(results) == 0, "Invalid queries should return no results"

