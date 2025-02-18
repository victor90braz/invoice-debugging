class AccountingInvoiceService:

    @staticmethod
    def calculate_totals(invoice):
        total = 0
        for item in invoice['items']:
            item_total = item['price'] * item['quantity']
            total += item_total  # Add VAT for each item directly
        
        invoice['vat'] = total * 0.21  # Calculate VAT on the overall total
        invoice['total'] = total + invoice['vat']  # Add VAT to the overall total

        print("\n--- Service Returned ---")
        print(f"Subtotal: {total}")
        print(f"VAT (21%): {invoice['vat']}")
        print(f"Total (with VAT): {invoice['total']}")
        print("-------------------------\n")

        return invoice

    def create_accounting_entry(invoice):
        entries = []

        # Compras
        entries.append({
            'account': '6000',  
            'debit': invoice['base_amount'],  
            'credit': 0  
        })

        # IVA
        entries.append({
            'account': '4720',  
            'debit': invoice['vat_amount'],  
            'credit': 0  
        })

        # Proveedor
        entries.append({
            'account': '4000',  
            'debit': 0,  
            'credit': invoice['base_amount'] + invoice['vat_amount']  # Expected credit for the Provider (base_amount + vat_amount)
        })

        return entries