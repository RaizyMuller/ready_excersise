"""Running a single experiment."""

import logging
from utils import create_dummy_dataset, preprocess_text

def main():

    # Set up logging
    logging.basicConfig(level=logging.INFO)

    # Create a dummy dataset
    dataset = create_dummy_dataset()
    logging.info("Created dummy dataset")

    # Preprocess the text
    dataset = dataset.map(lambda example: {"text": preprocess_text(example["text"])})
    logging.info("Preprocessed text")
if __name__ == "__main__":
    main()