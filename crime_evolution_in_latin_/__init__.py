"""Database on the evolution of crime in Latin America and the Caribbean during the period 2015-2024, c
DOI: https://github.com/juanmoisesd/crime-evolution-in-latin-america-2015-2024-database-by-categories | GitHub: https://github.com/juanmoisesd/crime-evolution-in-latin-america-2015-2024-database-by-categories"""
__version__="1.0.0"
__author__="de la Serna, Juan Moisés"
import pandas as pd,io
try:
    import requests
except ImportError:
    raise ImportError("pip install requests")

def load_data(filename=None):
    """Load dataset from Zenodo. Returns pandas DataFrame."""
    rid="https://github.com/juanmoisesd/crime-evolution-in-latin-america-2015-2024-database-by-categories".split(".")[-1]
    meta=requests.get(f"https://zenodo.org/api/records/{rid}",timeout=30).json()
    csvs=[f for f in meta.get("files",[]) if f["key"].endswith(".csv")]
    if not csvs:raise ValueError("No CSV found")
    f=next((x for x in csvs if filename and x["key"]==filename),csvs[0])
    return pd.read_csv(io.StringIO(requests.get(f["links"]["self"],timeout=60).text))

def cite():return f'de la Serna, Juan Moisés (2025). Database on the evolution of crime in Latin America and the Caribbean during the. Zenodo. https://github.com/juanmoisesd/crime-evolution-in-latin-america-2015-2024-database-by-categories'
def info():print(f"Dataset: Database on the evolution of crime in Latin America and the Caribbean during the\nDOI: https://github.com/juanmoisesd/crime-evolution-in-latin-america-2015-2024-database-by-categories\nGitHub: https://github.com/juanmoisesd/crime-evolution-in-latin-america-2015-2024-database-by-categories")