import logging

class AppLogger:
    def __init__(self, log_file="app.log", level=logging.INFO):
        logging.basicConfig(
            filename=log_file,
            filemode="w",
            level=level,
            format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )

    def get_logger(self, name):
        return logging.getLogger(name)
