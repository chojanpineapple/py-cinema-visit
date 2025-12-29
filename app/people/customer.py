from cinema import hall, bar


class Customer():
    customer = None
    def __init__(self, name: str, food: str):
        self.name = name
        self.food = food
        Customer.customer = self

    def watch_movie(self):
        hall = hall.CinemaHall()
        print(f"{self.name} is watching {hall.movie_name}.")