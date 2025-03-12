import os 
from dotenv import load_dotenv 

load_dotenv()

API_KEY = os.getenv("PUBMED_API_KEY")

# Handle missing API key case
if not API_KEY:
    raise ValueError("Missing PUBMED_API_KEY! Set it in your .env file.")


# PubMed API Endpoints
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
SEARCH_URL = f"{BASE_URL}/esearch.fcgi"  
FETCH_URL = f"{BASE_URL}/efetch.fcgi"    

# Keywords to Identify Non-Academic Companies
COMPANY_KEYWORDS = [
    "Pharma", "Biotech", "Inc.", "Ltd", "Corporation", "Laboratories",
    "Genomics", "Therapeutics", "Biosciences", "Diagnostics", "Life Sciences",
    "Biomedical", "Biopharma", "Research Institute", "Technologies",
    "Neurosciences", "Health Solutions", "GmbH", "LLC", "S.A.", "Pvt Ltd"
]

# API Configuration
DEFAULT_MAX_RESULTS = 50  
REQUEST_TIMEOUT = 10   


# API Rate Limit Handling
MAX_RETRIES = 5  # Maximum retries when hitting rate limits
RETRY_BACKOFF = 2  # Exponential backoff multiplier (in seconds)

# CSV File Configurations
DEFAULT_CSV_FILENAME = "pubmed_papers.csv"
CSV_HEADERS = [
    "PubMedID", "Title", "Publication Date", "Non-academic Authors",
    "Company Affiliations", "Corresponding Author Email"
]
