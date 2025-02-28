#Rent Car
class Vehicle :
    def __rental__(user,brand,model,year,rental_price_per_day):
        user.brand = brand
        user.model = model
        user.year = year
        user.__rental_price_per_day = rental_price_per_day
        
    def get_rental_price_per_day(user):
        return user.__rental_price_per_day
    
    def set_rental_price_per_day(user, new_price):
        if new_price > 0 :
            user.__rental_price_per_day = new_price
        else :
            print("Rental price must be greater than 0.")
            
    def display_info(user) : 
        print(f"{user.brand} {user.model}, Year: {user.year}, Rental Price: ${user.__rental_price_per_day}/day")
        
    def calculate_rental_cost(user, days):
        return user.__rental_price_per_day* days
    
    
class Car(Vehicle):
    def __rental__(user, brand, model, year, rental_price_per_day, seating_capacity):
        super()__rental__(brand, model, year, rental_price_per_day)
        user.seating_capacity = seating_capacity
        
    def display_info(user):
             print(f"Car: {user.brand} {user.model}, Year: {user.year}, Seats: {user.seating_capacity}, Rental Price: ${user.get_rental_price_per_day()}/day")


class Bike(Vehicle):
    def __init__(user, brand, model, year, rental_price_per_day, engine_capacity):
        super().__rental__(brand, model, year, rental_price_per_day)
        user.engine_capacity = engine_capacity
        
    def display_info(self):
        print(f"Bike: {user.brand} {user.model}, Year: {user.year}, Engine: {user.engine_capacity}, Rental Price: ${user.get_rental_price_per_day()}/day")        
        

    def show_Vehicle_info(Vehicle):
    Vehicle.display_info()
    
    
