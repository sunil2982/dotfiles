class OldPrinter:
    def old_print(self, text):
        return f"OLD: {text}"

class NewPrinter:
    def print(self, text):
        return f"NEW: {text}"


class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer
    
    def print(self, text):
        # Adapt old interface to new interface
        return self.old_printer.old_print(text)