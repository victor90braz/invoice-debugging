class AccountingInvoiceService:

    @staticmethod
    def calculate_totals(invoice):
        total = 0
        for item in invoice['items']:
            item_total = item['price'] * item['quantity']
            itemVat = item_total * 0.21
            total += item_total + itemVat  # Add VAT for each item directly
        
        # VAT should not be recalculated again for the entire total, as it's already included for each item
        invoice['vat'] = total * 0.21  # VAT is 21% of the total (as in the original logic)
        invoice['total'] = total + invoice['vat']  # Total = item + item VAT + recalculated VAT (if needed)

        return invoice
    
    def calculate_totals_correctly(invoice):
        total = 0
        for item in invoice['items']:
            item_total = item['price'] * item['quantity']
            total += item_total

        # Calculate VAT only once, based on the total sum of items
        vat = total * 0.21
        invoice['vat'] = vat
        invoice['total'] = total + vat  # Total = item sum + VAT

        return invoice




