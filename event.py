class Event:
    def __init__(self, event_name, event_date, event_location, event_id):
        self.event_name = event_name
        self.event_date = event_date
        self.event_location = event_location
        self.event_id = event_id
        self.participants = []   # Liste für angemeldete Mitglieder

    def __str__(self):
        return f"{self.event_name} (ID: {self.event_id})"

    def register(self, new_member):
        # Meldet ein Mitglied zur Veranstaltung an
        if new_member not in self.participants:
            self.participants.append(new_member)
        else:
            print("Dieses Mitglied ist bereits für die Veranstaltung angemeldet.")

    def deregister(self, old_member):
        # Meldet ein Mitglied von der Veranstaltung ab
        if old_member in self.participants:
            self.participants.remove(old_member)
            print("Mitglied erfolgreich von der Veranstaltung abgemeldet.")
        else:
            print("Dieses Mitglied ist nicht für die Veranstaltung angemeldet.")
