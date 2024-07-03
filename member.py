class Member:
    def __init__(self, first_name, last_name, birth_date, address, member_id):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.address = address
        self.member_id = member_id

    def __str__(self):
        return f"{self.first_name} {self.last_name} (ID: {self.member_id})"
