class Cleaner():
    cleaner = None
    def __init__(self, name: str):
        self.name = name
        Cleaner.cleaner = self
    
    def clean_hall(self, hall_number: int):
        print(f"Cleaner {self.name} is cleaning hall number {hall_number}.")