from inmaticParte3Debugging.models import InvoiceModel  

class InvoiceNumberGenerator:
    
    @staticmethod
    def get_next_number(invoice: InvoiceModel) -> str:
        
        invoice.last_number += 1
        invoice.save()
        return f"F{invoice.last_number}"

    @staticmethod
    def set_last_number(invoice: InvoiceModel, number: int) -> None:
        
        invoice.last_number = number
        invoice.save()
