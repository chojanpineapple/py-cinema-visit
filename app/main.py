from app.customer import Customer
from app.cinema_hall import CinemaHall
from app.cinema_bar import CinemaBar
from app.cleaner import Cleaner



def cinema_visit(movie, customers, hall_number, cleaner):
    customer_objects = []

    # create customers & sell food
    for data in customers:
        customer = Customer(data["name"])
        customer_objects.append(customer)
        CinemaBar.sell_food(customer, data["food"])

    # create hall and start movie
    hall = CinemaHall(hall_number)
    hall.start_movie(movie, customer_objects)
    hall.end_movie(movie)

    # cleaning
    cleaner_obj = Cleaner(cleaner)
    cleaner_obj.clean_hall(hall)

