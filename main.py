from crawler.Crawler import Crawler
from pylog.logconfig import config_log
from pylog.Logger import Logger


def main():
    crawler = Crawler()
    result = crawler.fetch_news_with_keyword("Korea", src="cnn", count=100)
    print(result)


if __name__ == "__main__":
    config_log()
    logger = Logger("main")
    logger.debug("Start main()")
    logger.info("Initiating yeah trends...")

    main()
