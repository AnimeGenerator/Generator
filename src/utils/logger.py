import logging
import os

def setup_logger():
    """Configure logging for the application"""
    logger = logging.getLogger("AnimeGenerator")
    logger.setLevel(logging.INFO)
    
    # Create handlers
    fh = logging.FileHandler("anime_generator.log")
    ch = logging.StreamHandler()
    
    # Create formatters and add to handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    # Add handlers to logger
    logger.addHandler(fh)
    logger.addHandler(ch)
    
    return logger
