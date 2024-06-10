from Crawler import Crawler


def main():
    url = "https://www.example.com"
    crawler = Crawler(url)
    print(crawler.fetch_url_content())


if __name__ == "__main__":
    main()
