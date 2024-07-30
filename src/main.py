from text_extraction import extract_text_from_pdf
from feature_extraction import extract_invoice_features, analyze_invoice_structure
from database import InvoiceDatabase
import os


def get_pdf_files(directory):
    pdf_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files


def main(input_pdf_paths, database_pdf_paths):
    db = InvoiceDatabase()

    # Process and add each invoice in the database
    for pdf_path in database_pdf_paths:
        text = extract_text_from_pdf(pdf_path)
        features = extract_invoice_features(text, os.path.basename(pdf_path))
        structure = analyze_invoice_structure(text)
        db.add_invoice({'path': pdf_path, 'text': text,
                       'features': features, 'structure': structure})

    for input_path in input_pdf_paths:
        input_text = extract_text_from_pdf(input_path)
        input_features = extract_invoice_features(
            input_text, os.path.basename(input_path))
        input_structure = analyze_invoice_structure(input_text)

        similar_invoice, similarity_score = db.find_most_similar(
            {'text': input_text, 'features': input_features, 'structure': input_structure})

        print(f"Input invoice: {os.path.basename(input_path)}")
        print(f"Most similar invoice: {
              os.path.basename(similar_invoice['path'])}")
        print(f"Similarity score: {similarity_score:.2f}")


# Passing PDF Files to test
if __name__ == "__main__":
    train_base_path = "C:/Users/fasih/Desktop/Document Similarity Matching/data/train"
    test_base_path = "C:/Users/fasih/Desktop/Document Similarity Matching/data/test"
    input_pdf_paths = get_pdf_files(test_base_path)
    database_pdf_paths = get_pdf_files(train_base_path)

    main(input_pdf_paths, database_pdf_paths)
