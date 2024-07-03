class Address:
    def __init__(self, street_name, house_number, postal_code, city_name):
        self.street_name = street_name
        self.house_number = house_number
        self.postal_code = postal_code
        self.city_name = city_name

    def __str__(self):
        return f"{self.street_name} {self.house_number}, {self.postal_code} {self.city_name}"
