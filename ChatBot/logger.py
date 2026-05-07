"""
Logging Configuration for RAG ChatBot
Provides consistent logging across all modules
"""

import logging
import sys
from pathlib import Path


def setup_logger(name: str = "RAGChatBot", level: int = logging.INFO) -> logging.Logger:
    """
    Configure and return a logger instance
    
    Args:
        name: Logger name (typically __name__ from calling module)
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    
    Returns:
        Configured logger instance
    """
    logger = logging.getLogger(name)
    
    # Avoid duplicate handlers
    if logger.handlers:
        return logger
    
    logger.setLevel(level)
    
    # Console handler with formatting
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(level)
    
    # Detailed format with colors for different levels
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    
    # Optional file handler for persistent logs
    log_dir = Path(__file__).parent / "logs"
    log_dir.mkdir(exist_ok=True)
    
    file_handler = logging.FileHandler(log_dir / "chatbot.log", encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)  # Log everything to file
    file_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    
    return logger


# Default logger for the application
default_logger = setup_logger()
