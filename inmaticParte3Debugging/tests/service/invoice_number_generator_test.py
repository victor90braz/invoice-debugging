from django.test import TransactionTestCase
from inmaticParte3Debugging.database.invoice_factory import InvoiceModelFactory
from inmaticParte3Debugging.service.invoice_number_generator import InvoiceNumberGenerator

class TestInvoiceNumberGenerator(TransactionTestCase):

    def setUp(self):
        # Create an invoice with a default last_number for all tests
        self.invoice = InvoiceModelFactory.create(last_number=10)

    def test_get_next_number(self):
        # Call the service to get the next number
        next_number = InvoiceNumberGenerator.get_next_number(self.invoice)

        # Verify that the next number is "F11"
        self.assertEqual(next_number, "F11")

        # Verify that the number has been incremented in the database
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.last_number, 11)

    def test_set_last_number(self):
        # Set the last number using the service
        InvoiceNumberGenerator.set_last_number(self.invoice, 200)

        # Verify that the number has been updated correctly
        self.invoice.refresh_from_db()
        self.assertEqual(self.invoice.last_number, 200)

        # Verify that the next number is "F201"
        next_number = InvoiceNumberGenerator.get_next_number(self.invoice)
        self.assertEqual(next_number, "F201")
