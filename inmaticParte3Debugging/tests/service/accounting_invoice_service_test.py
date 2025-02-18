import unittest
from inmaticParte3Debugging.service.accounting_invoice_service import AccountingInvoiceService

class TestAccountingInvoiceService(unittest.TestCase):

    def setUp(self):
        self.invoice = {
            'items': [
                {'price': 100, 'quantity': 2},  # Total = 200 (before VAT)
                {'price': 50, 'quantity': 3},   # Total = 150 (before VAT)
            ]
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
