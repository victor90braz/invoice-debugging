import unittest
from inmaticParte3Debugging.service.accounting_invoice_service import AccountingInvoiceService

class TestAccountingInvoiceService(unittest.TestCase):

    def setUp(self):
        self.invoice = {
            'items': [
                {'price': 100, 'quantity': 2},  # Total = 200 (before VAT)
                {'price': 50, 'quantity': 3},   # Total = 150 (before VAT)
            ],
            'base_amount': 1000,  # Base amount
            'vat_amount': 210  # VAT (21% of 1000)
        }

    def test_calculate_totals(self):
        result = AccountingInvoiceService.calculate_totals(self.invoice)

        # Expected calculation
        expected_subtotal = (100 * 2) + (50 * 3)  # Total before VAT 
        expected_vat = expected_subtotal * 0.21  # VAT at 21% (350 * 0.21 = 73.5)
        expected_total = expected_subtotal + expected_vat  # Total with VAT (350 + 73.5 = 423.5)

        # Assert that the returned result matches the expected values
        self.assertEqual(result['vat'], expected_vat)  # Expected value: 73.5
        self.assertEqual(result['total'], expected_total)  # Expected value: 423.5
        self.assertEqual(result['total'] - result['vat'], expected_subtotal)  # Assert Subtotal

        # Debugging output
        print("\n--- Test Result ---")
        print(f"Returned Subtotal: {result['total'] - result['vat']}")
        print(f"Returned VAT: {result['vat']}")
        print(f"Returned Total: {result['total']}")
        print("-------------------\n")

    def test_calculate_expected_credit_for_provider(self):
        
        provider = AccountingInvoiceService.create_accounting_entry(self.invoice)

        # Expected credit for the Provider (base_amount + vat_amount)
        expected_provider_credit = self.invoice['base_amount'] + self.invoice['vat_amount'] # expected credit would be 1000 + 210 = 1210

        self.assertEqual(provider[2]['account'], '4000')  # Provider account
        self.assertEqual(provider[2]['debit'], 0)
        self.assertEqual(provider[2]['credit'], expected_provider_credit)  # Expected credit: 1210
