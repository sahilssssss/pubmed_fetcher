# PubMed Paper Fetcher

This project is a command-line tool to fetch PubMed research papers, specifically highlighting papers with **non-academic authors**.
The tool uses the PubMed API to search for papers, extract relevant information, and save the results to a CSV file.

## 🚀 Features
✅ Fetch papers from PubMed using a search query  
✅ Identify non-academic authors and their company affiliations  
✅ Save results in a structured CSV file  
✅ Handle API rate limits with retries and backoff  

---

## 📂 Project Structure
# 🚀 How the Code is Organized

## 📌 `src/pubmed_paper_fetcher/`

| File | Description |
|------|-------------|
| `__init__.py` | Marks the directory as a Python package. |
| `cli.py` | CLI interface for fetching PubMed papers and saving them to CSV. |
| `fetch_papers.py` | Core logic for making PubMed API requests and parsing results. |
| `constants.py` | Stores constants like API endpoints and CSV headers. |
| `utils.py` | Utility functions for parsing and extracting data. |

## 📌 `test/`

| File | Description |
|------|-------------|
| `test_cli.py` | Unit tests for CLI functionality. |
| `test_fetch_papers.py` | Unit tests for fetching and parsing PubMed data. |
| `test_utils.py` | Unit tests for utility functions. |

## 🛠️ Dependencies

| Tool/Library | Purpose | Link |
|-------------|---------|------|
| **Python** | Core programming language | https://www.python.org |
| **Requests** | HTTP requests for PubMed API | https://docs.python-requests.org |
| **argparse** | Handling CLI arguments | https://docs.python.org/3/library/argparse.html |
| **pandas** | Data manipulation and CSV writing | https://pandas.pydata.org |
| **pytest** | Testing framework | https://docs.pytest.org |
| **python-dotenv** | Environment variable management | https://pypi.org/project/python-dotenv |


This project uses **Poetry** to manage dependencies. To install all the required dependencies, follow these steps:
**`pyproject.toml`**: Configuration file for Poetry, which is used to manage dependencies and project metadata.
### Prerequisites

- Make sure you have **Python 3.7+** installed on your system.
- Install **Poetry** if you haven't already: [use this command : pipx install poetry ]

### Installing Dependencies

1. Clone the repository:
    
   git clone <repository-url>
   cd pubmed_paper_fetcher

✅ Features
✔️ Fetches research papers from PubMed using a search query
✔️ Filters and highlights non-academic authors and company affiliations
✔️ Handles API rate limits and retries gracefully
✔️ Saves results to a CSV file
✔️ Command-line interface for ease of use
✔️ Unit tests for reliability


2. Install dependencies using Poetry:
poetry install [This will install all the necessary libraries listed in the pyproject.toml file.]

3. Set up environment variables:
Create a .env file in the root directory and add your PubMed API key:
Add the following content to .env:

**PUBMED_API_KEY=your-pubmed-api-key**

🔑 You can get a PubMed API key from:
👉 https://www.ncbi.nlm.nih.gov/account/settings/

4.Running the Program
After installing the dependencies, you can run the program from the command line.

>> To fetch papers with a specific query and save the results to a CSV file, run:
**poetry run python src/pubmed_paper_fetcher/cli.py --query "<your-query>"**

>> Example of a search for papers on "diabetes AND hypertension":
**poetry run python src/pubmed_paper_fetcher/cli.py --query "diabetes AND hypertension"**

>> By default, the program will save the results to a file called pubmed_papers.csv. To specify a different filename, use the --file option:
**poetry run python src/pubmed_paper_fetcher/cli.py --query "diabetes AND hypertension" --file "my_results.csv"**

## ✅ Arguments

## ✅ Arguments

| Argument | Description | Example |
|----------|-------------|---------|
| `--query`, `-q` | **(Required)** Search query for PubMed | `"cancer AND therapy"` |
| `--file`, `-f` | *(Optional)* Filename to save results as CSV | `"output.csv"` |
| `--debug`, `-d` | *(Optional)* Enable debug mode for detailed logs | `N/A` |
| `--help`, `-h` | *(Optional)* Displays help information about the CLI | `N/A` |


## 📊 Sample Output

| PubMed ID | Title | Publication Date | Non-academic Authors | Company Affiliations | Corresponding Author Email |
|-----------|-------|------------------|----------------------|----------------------|----------------------------|
| 12345678 | Cancer Research Study | 2023-05-21 | John Doe, Jane Smith | Biotech Corp, Pharma Inc. | johndoe@biotech.com |

5. Run Tests:
>> To run all tests using pytest:
**pytest tests/**

>>To run a specific test file:
**pytest test/test_cli.py**

>>To run tests with verbose output:
**pytest -v**

💡 Best Practices
Use a specific search query to avoid hitting rate limits.
Enable debug mode (--debug) for troubleshooting.
Use pytest to run unit tests before making changes.

🎯 Future Enhancements
✅ Add support for additional PubMed metadata fields
✅ Allow JSON output for better integration with other tools
✅ Improve error handling for network issues


