import unittest

from inmaticParte3Debugging.service.accounting_invoice_service import AccountingInvoiceService

class TestAccountingInvoiceService(unittest.TestCase):

    def setUp(self):
        # Setup for tests: Use the same invoice for both methods
        self.invoice = {
            'items': [
                {'price': 100, 'quantity': 2},  # Total = 200 (before VAT)
                {'price': 150, 'quantity': 1},  # Total = 150 (before VAT)
            ]
        }

    def test_calculate_totals_with_duplicate_iva(self):
        # Running the method with duplicate VAT for each item
        result = AccountingInvoiceService.calculate_totals(self.invoice)
        
        # Correct VAT and total after duplicate VAT handling
        self.assertEqual(result['vat'], 88.935)  # VAT calculated as 21% of 423.5 (sum of item + VAT)
        self.assertEqual(result['total'], 512.435)  # Total = sum + VAT (423.5 + 88.935)
    
    def test_calculate_totals_correctly(self):
        # Running the method with correct calculation
        result = AccountingInvoiceService.calculate_totals_correctly(self.invoice)
        
        # Correct VAT and total after calculation
        self.assertEqual(result['vat'], 73.5)  # VAT is 21% of 350 (200 + 150)
        self.assertEqual(result['total'], 423.5)  # Total = 350 + 73.5 (VAT)
    

