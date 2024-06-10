from Crawler import Crawler


def main():
    url = "https://www.example.com"
    crawler = Crawler()
    result = crawler.fetch_news_with_keyword("python", src="naver")
    print(result)


if __name__ == "__main__":
    main()
