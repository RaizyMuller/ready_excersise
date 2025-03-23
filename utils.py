"""
Utilities for the project.
"""

import os
from datasets import Dataset


def create_dummy_dataset():
    """
    Create a dummy dataset for testing purposes.
    """
    data = {
        "text": [
            "Hello, world!",
            "This is a test sentence.",
            "I am a test sentence.",
            "This is a test sentence.",
            "I am a test sentence.",
        ],
        "label": [0, 1, 1, 1, 0],
    }
    dataset = Dataset.from_dict(data)
    return dataset

def preprocess_text(text):
    """
    Preprocess the text by converting it to lowercase and removing special characters.
    """
    text = text.lower()
    # Remove extra spaces
    text = " ".join(text.split()).strip()
    return text
