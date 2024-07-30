# Document Similarity Matching

This project implements a document similarity matching system to identify and match similar invoices based on their content and structure.

## Approach

### Document Representation

- **Text Extraction**: Extract text content from PDFs using PyPDF2.
- **Feature Extraction**: Extract relevant features such as keywords, invoice numbers, dates, and amounts.

### Similarity Calculation

- **Cosine Similarity**: Calculate the cosine similarity between the feature vectors of two invoices.

## Running the Code

1. Install the required packages

2. Run the similarity matching:
   ```sh
   python src/main.py
   ```

## Results

# Document Similarity Matching

## Overview

This project implements a document similarity matching system to identify and match similar invoices based on their content and structure. The system takes an input invoice (PDF format) and compares it to a database of existing invoices, outputting the most similar invoice along with a similarity score.

## Project Structure

```
document_similarity-matching/
│
├── data/                  # create Data Folder
│   ├── train              # create Train Folder and Input sample pdfs here
│   ├── test               # create Test Folder and Input to be tested pdfs here
│
├── src/
│   ├── main.py            # Main script to run the similarity matching
│   ├── text_extraction.py # Module for extracting text from PDFs
│   ├── feature_extraction.py # Module for extracting features from text
│   ├── similarity.py      # Module for calculating similarity between documents
│   ├── database.py        # Module for managing the invoice database
```

## Requirements

- Python 3.6 or higher
- PyPDF2
- scikit-learn
- numpy

## Modules and Functions

### `text_extraction.py`

- **extract_text_from_pdf(pdf_path)**:
  - Extracts text content from a given PDF file.
  - **Parameters**: `pdf_path` (str): Path to the PDF file.
  - **Returns**: Extracted text (str).

### `feature_extraction.py`

- **extract_features(text)**:

  - Extracts features from the text using TF-IDF vectorization.
  - **Parameters**: `text` (str): Text content of the invoice.
  - **Returns**: TF-IDF feature vectors.

- **extract_invoice_features(text)**:
  - Extracts specific invoice-related features such as invoice number, date, and total amount.
  - **Parameters**: `text` (str): Text content of the invoice.
  - **Returns**: Dictionary with extracted features.

### `similarity.py`

- **calculate_cosine_similarity(text1, text2)**:

  - Calculates the cosine similarity between two text strings.
  - **Parameters**: `text1` (str): First text string.
  - **Parameters**: `text2` (str): Second text string.
  - **Returns**: Cosine similarity score (float).

- **calculate_jaccard_similarity(set1, set2)**:
  - Calculates the Jaccard similarity between two sets of keywords.
  - **Parameters**: `set1` (set): First set of keywords.
  - **Parameters**: `set2` (set): Second set of keywords.
  - **Returns**: Jaccard similarity score (float).

### `database.py`

- **InvoiceDatabase**:

  - A class to manage a database of invoices.

  - **Methods**:
    - **add_invoice(invoice)**: Adds an invoice to the database.
      - **Parameters**: `invoice` (dict): Invoice data with text and features.
    - **find_most_similar(invoice_features)**: Finds the most similar invoice in the database based on cosine similarity.
      - **Parameters**: `invoice_features` (dict): Features of the input invoice.
      - **Returns**: Most similar invoice (dict) and similarity score (float).

### `main.py`

- **main(input_pdf_path, database_pdf_paths)**:
  - The main function to run the similarity matching process.
  - **Parameters**:
    - `input_pdf_path` (str): Path to the input PDF invoice.
    - `database_pdf_paths` (list of str): List of paths to the PDF invoices in the database.

## How to Run

1. **Clone the Repository or Download the Code**:

   Ensure you have the project files on your local machine.

2. **Set Up the Environment**:

   Create and activate a virtual environment (optional but recommended):

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:

   Install the required Python packages:

   ```sh
   pip install PyPDF2 sklearn
   ```

4. **Place Your PDF Invoices**:

   Ensure your input PDF invoice and other sample invoices are in the `data/` directory.

5. **Run the Script**:

   Execute the main script:

   ```sh
   python src/main.py
   ```

6. **View the Output**:

   The script will print the most similar invoice from the database along with the similarity score.
