import os
import logging
import pytest
from libs.utils.logging_config import setup_logging


def test_setup_logging_creates_log_directory():

    if os.path.exists("logs/app.log"):
        os.remove("logs/app.log")
    if os.path.exists("logs"):
        os.rmdir("logs")
    
    setup_logging()
    
    assert os.path.exists("logs"), "The logs directory should be created."

def test_setup_logging_creates_log_file():

    if os.path.exists("logs/app.log"):
        os.remove("logs/app.log")
    if os.path.exists("logs"):
        os.rmdir("logs")
    
    setup_logging()
    
    assert os.path.exists("logs/app.log"), "The app.log file should be created."

def test_logging_configuration():
    setup_logging()
    logger = logging.getLogger()
    logger.info("Test logging")

    assert logger.level == logging.INFO , "The logger should have an INFO level."
    
    handlers = logger.handlers
    assert len(handlers) == 2, "There should be two handlers."
    assert any(isinstance(handler, logging.FileHandler) for handler in handlers), "There should be a FileHandler."
    assert any(isinstance(handler, logging.StreamHandler) for handler in handlers), "There should be a StreamHandler."