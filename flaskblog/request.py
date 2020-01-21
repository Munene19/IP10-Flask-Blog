import requests
from .models import Quote

url = "https://quotes.stormconsultancy.co.uk/random.json"

def get_quote():
    """
    Function to consume http request and return a Quote class instance
    """
    response = requests.get(url, verify=False).json()

    random_quote = Quote(response.get("author"), response.get("quote"))
    return random_quote