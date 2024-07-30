from similarity import calculate_cosine_similarity, calculate_jaccard_similarity

# The InvoiceDatabase manages a collection of invoices and provides a method to find the most similar invoice based on text features using cosine similarity.


class InvoiceDatabase:
    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice):
        self.invoices.append(invoice)

    def find_most_similar(self, input_invoice):
        max_similarity = 0
        most_similar_invoice = None
        for invoice in self.invoices:
            # print(f"invoice['text'] {invoice['text']}")
            # print(f"input_invoice['text'] {input_invoice['text']}")

            text_similarity = calculate_cosine_similarity(
                invoice['text'], input_invoice['text'])
            structure_similarity = calculate_jaccard_similarity(
                set(str(invoice['structure'])), set(str(input_invoice['structure'])))
            feature_similarity = calculate_jaccard_similarity(
                set(invoice['features'].items()), set(input_invoice['features'].items()))

            combined_similarity = (
                0.6 * text_similarity) + (0.2 * structure_similarity) + (0.2 * feature_similarity)
            if combined_similarity > max_similarity:
                max_similarity = combined_similarity
                most_similar_invoice = invoice
        return most_similar_invoice, max_similarity
