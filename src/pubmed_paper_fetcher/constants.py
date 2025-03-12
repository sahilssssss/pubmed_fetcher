# PubMed API Endpoints
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
SEARCH_URL = f"{BASE_URL}/esearch.fcgi"  
FETCH_URL = f"{BASE_URL}/efetch.fcgi"    

# Keywords to Identify Non-Academic Companies
COMPANY_KEYWORDS = [
    "Pharma", "Biotech", "Inc.", "Ltd", "Corporation", "Laboratories", "Synapse",
    "Genomics", "Therapeutics", "Biosciences", "Pathology","Diagnostics", "Life Sciences",
    "Biomedical", "Biopharma", "Research Institute", "Technologies","Laboratory",
    "Neurosciences", "Health Solutions", "GmbH", "LLC", "S.A.", "Pvt Ltd"
]

# API Configuration
DEFAULT_MAX_RESULTS = 50  
REQUEST_TIMEOUT = 10       

# CSV File Configurations
DEFAULT_CSV_FILENAME = "pubmed_papers.csv"
CSV_HEADERS = [
    "PubMedID", "Title", "Publication Date", "Non-academic Authors",
    "Company Affiliations", "Corresponding Author Email"
]
