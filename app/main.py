from app.people.customer import Customer
from app.cinema.cinema_hall import CinemaHall
from app.cinema.cinema_bar import CinemaBar
from app.staff.cleaner import Cleaner




def cinema_visit(movie, customers, hall_number, cleaner):
    customer_objects = []

    for data in customers:
        customer = Customer(data["name"])
        customer_objects.append(customer)
        CinemaBar.sell_product(customer, data["food"])

    hall = CinemaHall(hall_number)
    cleaner_obj = Cleaner(cleaner)

    hall.movie_session(movie, customer_objects, cleaner_obj)