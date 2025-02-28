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
            
    
        
    
