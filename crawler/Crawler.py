import requests
from bs4 import BeautifulSoup
from pylog.Logger import Logger


class Crawler:
    def __init__(self, url=""):
        self.url = url
        self.content = None
        self.soup = None
        self.html_option = None
        self.logger = Logger("crawler.Crawler")

    def fetch_url_content(self):
        try:
            self.logger.info(f"Fetching URL: {self.url}")
            response = requests.get(self.url)
            # throw if failed
            response.raise_for_status()

            self.logger.debug(f"Response status code: {response.status_code}")
            self.soup = BeautifulSoup(response.content, "html.parser")

            if self.soup.body:
                self.content = self.soup.body.prettify()
                return self.content
            else:
                raise ValueError("No body tag found in the HTML content")
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching the URL: {e}")
            return f"Error fetching the URL: {e}"
        except ValueError as e:
            self.logger.error(f"Error parsing the HTML content: {e}")
            return f"Error parsing the HTML content: {e}"

    def fetch_news_with_keyword(self, keyword="", src=None, limit=None):
        if src == "naver":
            self.url = f"https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyword}"
            self.html_option = {"class": "news_tit"}
        else:
            raise ValueError("Invalid or unsupported news source")

        self.logger.info(f"Fetching news from source: {src}")
        self.fetch_url_content()
        if self.soup is None or self.soup.body is None:
            self.logger.warning("Fetching failed due to null atrributes")
            return []

        result = [a.text for a in self.soup.body.find_all("a", self.html_option)]
        self.logger.debug(f"Found {len(result)} news")
        return result
