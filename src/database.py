from similarity import calculate_cosine_similarity


# The InvoiceDatabase manages a collection of invoices and provides a method to find the most similar invoice based on text features using cosine similarity.
class InvoiceDatabase:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def find_most_similar(self, invoice_features):
        max_similarity = 0
        most_similar_invoice = None
        for invoice in self.invoices:
            similarity = calculate_cosine_similarity(
                invoice['text'], invoice_features['text'])
            if similarity > max_similarity:
                max_similarity = similarity
                most_similar_invoice = invoice
        return most_similar_invoice, max_similarity
