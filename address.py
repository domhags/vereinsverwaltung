class Address:
    def __init__(self, street, house_number, zip_code, city):
        self.street = street
        self.house_number = house_number
        self.zip_code = zip_code
        self.city = city

    def __str__(self):
        return f"{self.street} {self.house_number}, {self.zip_code} {self.city}"
