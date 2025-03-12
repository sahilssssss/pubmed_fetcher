import subprocess
import os
import pytest

# Define the absolute path to cli.py inside src/pubmed_paper_fetcher/
CLI_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src/pubmed_paper_fetcher/cli.py"))

def run_cli(args):
    """Run the CLI command and capture output."""
    return subprocess.run(["python", CLI_PATH] + args, capture_output=True, text=True)

def test_cli_fetch_papers():
    """Test fetching papers via CLI."""
    query = "diabetes AND hypertension AND 2021[Date - Publication]"
    result = run_cli(["--query", query, "--debug"])

    # Debug prints
    print("CLI Output:", result.stdout)
    print("CLI Error:", result.stderr)

    assert result.returncode == 0, "CLI should exit with code 0"


def test_cli_creates_csv():
    """Test if the CLI generates a CSV file."""
    query = "cancer therapy"
    filename = "test_output.csv"

    result = run_cli(["--query", query, "--file", filename])

    print("CLI Output:", result.stdout)
    print("CLI Error:", result.stderr)

    assert os.path.exists(filename), f"CSV file '{filename}' should be created"
    os.remove(filename)  # Cleanup after test

def test_cli_default_csv():
    """Test if CLI saves results in the default CSV file."""
    query = "COVID-19 OR SARS-CoV-2[Title/Abstract]"
    
    result = run_cli(["--query", query])

    assert os.path.exists("pubmed_papers.csv"), "Default CSV 'pubmed_papers.csv' should be created"
    os.remove("pubmed_papers.csv")  # Cleanup

def test_cli_invalid_query():
    """Test CLI with an invalid query (should return empty results)."""
    query = "@#$%^&*()"
    result = run_cli(["--query", query])

    print("CLI Output:", result.stdout)  # Debugging line
    print("CLI Error:", result.stderr)   # Debugging line

    # Check both stdout and stderr for any indication of empty results
    output = result.stdout + result.stderr
    assert "No papers found" in output or "⚠️ No papers found" in output, \
           "CLI should handle invalid queries gracefully"

def test_cli_no_query_provided():
    """Test behavior when no query is provided."""
    result = run_cli([])
    
    # Should show error and usage information
    assert result.returncode != 0, "CLI should exit with non-zero code when no query provided"
    assert "query" in result.stderr.lower(), "Error should mention missing query parameter"

def test_cli_no_results_query():
    """Test behavior when a valid but overly specific query returns no results."""
    # A very specific query unlikely to return results
    query = "unicorns AND dragons AND 1800[Date - Publication]"
    result = run_cli(["--query", query])
    
    # It should exit successfully but indicate no results
    assert result.returncode == 0
    assert "No papers found" in result.stdout or "No papers found" in result.stderr
    
    # No CSV should be created (or it should be empty)
    if os.path.exists("pubmed_papers.csv"):
        with open("pubmed_papers.csv", 'r') as f:
            content = f.read().strip()
        assert len(content.split('\n')) <= 1, "CSV should be empty or contain only headers"
        os.remove("pubmed_papers.csv")

def test_cli_help():
    """Test CLI --help flag."""
    result = run_cli(["--help"])

    print("CLI Output:", result.stdout)
    assert "Fetch PubMed papers with non-academic authors." in result.stdout, "CLI should show help text"
