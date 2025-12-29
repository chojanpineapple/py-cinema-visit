from people import customer

class CinemaBar():
    @staticmethod
    def sell_product(customer: customer, product : str) -> str:
        print(f"Cinema bar sold {product} to {customer}.")
