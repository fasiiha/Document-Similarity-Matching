# Document Similarity Matching

This project implements a document similarity matching system to identify and match similar invoices based on their content and structure.

## Approach

### Document Representation

- **Text Extraction**: Extract text content from PDFs using PyPDF2.
- **Feature Extraction**: Extract relevant features such as keywords, invoice numbers, dates, and amounts.

### Similarity Calculation

- **Cosine Similarity**: Calculate the cosine similarity between the feature vectors of two invoices.

## Running the Code

1. Install the required packages:

   ```sh
   pip install -r requirements.txt
   ```

2. Run the similarity matching:
   ```sh
   python src/main.py
   ```

## Results

A screen recording of the demo, including similarity scores and matched invoices, can be found in `results_demo.mp4`.
