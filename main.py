from crawler.Crawler import Crawler
from pylog.logconfig import config_log


def main():
    config_log()

    crawler = Crawler()
    result = crawler.fetch_news_with_keyword("python", src="naver")
    print(result)


if __name__ == "__main__":
    main()
