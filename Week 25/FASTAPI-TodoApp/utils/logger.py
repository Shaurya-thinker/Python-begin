# utils/logger.py
import logging

# Create logger
logger = logging.getLogger("fastapi-app")
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(file_handler)
logger.addHandler(console_handler)
