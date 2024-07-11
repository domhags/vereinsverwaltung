# member.py

class Member:
    def __init__(self, first_name, last_name, birth_date, address, member_id, is_officer=False):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.address = address
        self.member_id = member_id
        self.is_officer = is_officer  # True, wenn Funktionär, sonst False

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({'Funktionär' if self.is_officer else 'Mitglied'})"

    def set_officer_status(self, is_officer):
        self.is_officer = is_officer

    def is_officer(self):
        return self.is_officer
