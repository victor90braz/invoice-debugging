from typing import Dict, List
from inmaticParte3Debugging.app.service.accounting_invoice_service import AccountingInvoiceService
from inmaticParte3Debugging.models import InvoiceModel


class InvoiceResource:
    def __init__(self, accounting_service: AccountingInvoiceService):
        self.accounting_service = accounting_service

    def group_invoices_by_supplier_and_month(self, invoices: List[InvoiceModel]) -> Dict:
        return self.accounting_service.group_invoices_by_supplier_and_month(invoices)
