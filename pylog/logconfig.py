import logging
from datetime import datetime, timedelta
import os
import time


def check_log_dir():
    path = "./logs"
    if not os.path.exists(path):
        os.makedirs(path)


def delete_old_logfiles(days=30):
    path = "./logs"
    check_log_dir()
    now = time.time()
    old = now - days * 24 * 60 * 60  # 30 days

    cnt = 0
    for filename in os.listdir(path):
        if filename.endswith(".log"):
            filepath = os.path.join(path, filename)
            if os.path.getmtime(filepath) < old:
                os.remove(filepath)
                cnt += 1

    if cnt == 0:
        logging.debug("No old log files to delete")
    else:
        logging.debug(f"Deleted {cnt} old log files")


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
    delete_old_logfiles()
