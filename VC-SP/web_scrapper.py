import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.page = None
        self.soup = None

    def fetch_page(self):
        """Fetches the web page content."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Will raise an exception for bad status codes
            self.page = response.text
            print("Page fetched successfully!")
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the page: {e}")
            self.page = None

    def parse_page(self):
        """Parses the fetched page using BeautifulSoup."""
        if self.page:
            self.soup = BeautifulSoup(self.page, 'html.parser')
            print("Page parsed successfully!")
        else:
            print("No page content to parse.")

    def extract_titles(self):
        """Extracts and prints article titles from the page."""
        if not self.soup:
            print("Page not parsed. Cannot extract titles.")
            return
        
        titles = self.soup.find_all('div')  
        for idx, title in enumerate(titles, start=1):
            print(f"{idx}. {title.get_text(strip=True)}")

    def run(self):
        """Runs the entire scraping process."""
        self.fetch_page()
        self.parse_page()
        self.extract_titles()


