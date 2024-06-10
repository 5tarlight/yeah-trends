import logging
from datetime import datetime
import os


def check_log_dir():
    path = "./logs"
    if not os.path.exists(path):
        os.makedirs(path)


def get_logfile_name():
    path = "./logs"
    check_log_dir()
    filename = datetime.now().strftime("%Y-%m-%d")
    return f"{path}/{filename}.log"


def config_log():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        filename=get_logfile_name(),
        filemode="a",
    )
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(name)-12s: %(levelname)-8s %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)
