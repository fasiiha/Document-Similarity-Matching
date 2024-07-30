import re


def extract_invoice_features(text, filename):
    features = {}
    invoice_number_match = re.search(r'invoice_(\d+)', filename, re.IGNORECASE)
    features['invoice_number'] = invoice_number_match.group(
        1) if invoice_number_match else None
    date_match = re.search(r'\b(\d{2}\.\d{2}\.\d{4})\b', text)
    features['date'] = date_match.group(1) if date_match else None

    total_amount_match = re.search(
        r'([\d,]+)\s+Gesamtsumme', text) or re.search(r'([\d,]+)\s+Rechnungsbetrag', text)
    features['total_amount'] = total_amount_match.group(
        1) if total_amount_match else None

    customer_info_match = re.search(
        r'(.*?)\d{5}\s+\w+\s*$', text, re.MULTILINE | re.DOTALL)
    features['customer'] = customer_info_match.group(
        1).strip() if customer_info_match else None
    return features


def analyze_invoice_structure(text):
    lines = text.split("\n")
    structure = {
        'header': [],
        'footer': [],
        'body': [],
        'tables': []
    }

    header_end = min(5, len(lines) // 4)
    structure['header'] = lines[:header_end]
    footer_start = max(-5, -len(lines) // 4)
    structure['footer'] = lines[footer_start:]
    structure['body'] = lines[header_end:footer_start]

    table_pattern = re.compile(r'\s{2,}')
    for line in structure['body']:
        if table_pattern.search(line):
            structure['tables'].append(line)
    return structure
