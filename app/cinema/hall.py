from people import customer
from people import cinema_staff
import bar



class CinemaHall():
    def __init__(self, hall_number: int):
        self.hall_number = hall_number
        self.movie_name = None

    def movie_session(movie_name: str, customer: list, cleaning_staff: str):
        self.movie_name = movie_name
        watch = customer.Customer(customer)
        watch.watch_movie()
        cleaning_staff = cinema_staff.Cleaner(cleaning_staff)
        cleaning_staff.clean_hall(self.hall_number)

