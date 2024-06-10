import requests
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self, url):
        self.url = url
        self.content = None

    def fetch_url_content(self):
        try:
            response = requests.get(self.url)
            # throw if failed
            response.raise_for_status()

            soup = BeautifulSoup(response.content, "html.parser")

            if soup.body:
                self.content = soup.body.prettify()
                return self.content
            else:
                raise ValueError("No body tag found in the HTML content")
        except requests.exceptions.RequestException as e:
            return f"Error fetching the URL: {e}"
