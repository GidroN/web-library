from flask import session, redirect, request, url_for
from functools import wraps
import logging

logger = logging.getLogger('__app__')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('logs/logs.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

