from tkinter import messagebox


class Event:
    def __init__(self, event_name, event_date, event_location, event_id):
        self.event_name = event_name
        self.event_date = event_date
        self.event_location = event_location
        self.event_id = event_id
        self.participants = []

    def __str__(self):
        return f"{self.event_id} - {self.event_name} | {self.event_date} | {self.event_location}"
