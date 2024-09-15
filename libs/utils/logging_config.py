# utils/logging_config.py
import logging
import os


def setup_logging():
    if not os.path.exists("logs"):
        os.mkdir("logs")
    elif not os.path.exists("logs/app.log"):
        open("logs/app.log", "w").close()
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler("logs/app.log"), logging.StreamHandler()],
        force=True,
    )
