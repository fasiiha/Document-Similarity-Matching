import re
from sklearn.feature_extraction.text import TfidfVectorizer


# functions to extract text features using TF-IDF vectorization and extract specific invoice details like invoice number, date, and total amount from a given text.

def extract_features(text):
    vectorizer = TfidfVectorizer()
    features = vectorizer.fit_transform([text])
    return features


def extract_invoice_features(text):
    invoice_number_match = re.search(r'Rechnung Nr\.\s+(\d+)', text)
    date_match = re.search(r'Datum\s+(\d{2}\.\d{2}\.\d{4})', text)
    total_amount_match = re.search(
        r'Rechnungsbetrag EUR\s+(\d+,\d{2})', text)

    invoice_number = invoice_number_match.group(
        1) if invoice_number_match else None
    date = date_match.group(1) if date_match else None
    total_amount = total_amount_match.group(1) if total_amount_match else None
    return {
        'invoice_number': invoice_number,
        'date': date,
        'total_amount': total_amount
    }
