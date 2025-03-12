# PubMed Paper Fetcher

A powerful command-line tool to fetch and analyze PubMed research papers, with a focus on identifying papers with **non-academic authors** and their affiliations.

## 🚀 Features

- ✅ Search PubMed using custom queries
- ✅ Identify non-academic authors and their company affiliations
- ✅ Export results to structured CSV files
- ✅ Handle API rate limits with intelligent retry mechanisms
- ✅ Comprehensive error handling and logging

## 📋 Installation

### Prerequisites

- Python 3.7+
- Poetry (dependency management)
  - Install with: `pipx install poetry`

### Quick Setup

```bash
# Clone the repository
git clone <repository-url>
cd pubmed-paper-fetcher

# Install dependencies
poetry install

# Set up environment variables
# Create a .env file with your PubMed API key
echo "PUBMED_API_KEY=your-pubmed-api-key" > .env
```

> 🔑 **Get your PubMed API key at:** https://www.ncbi.nlm.nih.gov/account/settings/

## 🖥️ Usage

### Basic Usage

```bash
poetry run python src/pubmed_paper_fetcher/cli.py --query "diabetes AND hypertension"
```

### Command-line Arguments

| Argument | Description | Default | Example |
|----------|-------------|---------|---------|
| `--query`, `-q` | Search query for PubMed | - | `"cancer AND therapy"` |
| `--file`, `-f` | Filename for CSV output | `pubmed_papers.csv` | `"results.csv"` |
| `--debug`, `-d` | Enable debug logging | `False` | - |
| `--help`, `-h` | Show help message | - | - |

### Examples

```bash
# Search for papers on cancer therapy
poetry run python src/pubmed_paper_fetcher/cli.py --query "cancer AND therapy"

# Save results to a custom file with debug output
poetry run python src/pubmed_paper_fetcher/cli.py --query "COVID-19 AND treatment" --file covid_papers.csv --debug
```

## 📊 Output Format

The tool generates a CSV file with the following columns:

| Column | Description |
|--------|-------------|
| PubMed ID | Unique identifier for the paper |
| Title | Paper title |
| Publication Date | Date of publication |
| Non-academic Authors | Authors from industry/commercial settings |
| Company Affiliations | Organizations associated with non-academic authors |
| Corresponding Author Email | Contact email for the corresponding author |

## 📂 Project Structure

```
pubmed-paper-fetcher/
├── src/pubmed_paper_fetcher/
│   ├── __init__.py       # Package initialization
│   ├── cli.py            # Command-line interface
│   ├── fetch_papers.py   # PubMed API interaction
│   ├── constants.py      # Project constants
│   └── utils.py          # Helper functions
├── tests/
│   ├── test_cli.py       # CLI tests
│   ├── test_fetch_papers.py  # API interaction tests
│   └── test_utils.py     # Utility function tests
├── pyproject.toml        # Poetry configuration
└── .env                  # Environment variables (not tracked in git)
```

## 🛠️ Dependencies

| Package | Purpose |
|---------|---------|
| Requests | HTTP client for API calls |
| pandas | Data manipulation and CSV export |
| pytest | Testing framework |
| python-dotenv | Environment variable management |

## 🧪 Testing

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_cli.py

# Run with verbose output
pytest -v
```

## 💡 Best Practices

- Use specific search queries to avoid hitting API rate limits
- Enable debug mode (`--debug`) when troubleshooting issues
- Run tests before making code changes

## 🔮 Future Enhancements

- [ ] Add support for additional PubMed metadata fields
- [ ] Implement JSON output format
- [ ] Create interactive mode for refined searches
- [ ] Add visualization capabilities for affiliation data
- [ ] Implement batch processing for large queries

## 📄 Author 
Sahil Dey
email:deysagar3001@gmail.com
