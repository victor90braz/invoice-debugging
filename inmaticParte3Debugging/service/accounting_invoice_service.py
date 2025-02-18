class AccountingInvoiceService:

    @staticmethod
    def calculate_totals(invoice):
        total = 0
        for item in invoice['items']:
            item_total = item['price'] * item['quantity']
            total += item_total  # Add VAT for each item directly
        
        invoice['vat'] = total * 0.21  # Calculate VAT on the overall total
        invoice['total'] = total + invoice['vat']  # Add VAT to the overall total

        # Print the final result for debugging in a formatted way
        print("\n--- Service Returned ---")
        print(f"Subtotal: {total}")
        print(f"VAT (21%): {invoice['vat']}")
        print(f"Total (with VAT): {invoice['total']}")
        print("-------------------------\n")

        return invoice
