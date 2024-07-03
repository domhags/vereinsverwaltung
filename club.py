class Club:
    def __init__(self, club_name, club_address):
        self.club_name = club_name
        self.club_address = club_address
        self.members = []        # Liste für Mitglieder
        self.events = []   # Liste für Veranstaltungen

    def addMember(self, new_member):
        if new_member in self.members:
            print("Dieses Mitglied ist bereits im Verein vorhanden.")
        else:
            self.members.append(new_member)

    def removeMember(self, old_member):
        if old_member not in self.members:
            print("Dieses Mitglied wurde nicht gefunden.")
        else:
            self.members.remove(old_member)
            print("Mitglied entfernt")

    def addEvent(self, new_event):
        if any(event.event_id == new_event.event_id for event in self.events):
            print(f"Die Event-ID '{new_event.event_id}' ist bereits vergeben.")
        else:
            self.events.append(new_event)
            print("Veranstaltung hinzugefügt.")

    def removeEvent(self, old_event):
        if old_event not in self.events:
            print("Dieses Event wurde nicht gefunden.")
        else:
            self.events.remove(old_event)
            print("Event erfolgreich entfernt.")

    def findMember(self, search_member_id):
        return next((m for m in self.members if m.member_id == search_member_id), None)

    def findEvent(self, event_id):
        event_id = str(event_id)
        return next((event for event in self.events if event.event_id == event_id), None)

    def showMembers(self):
        if not self.members:
            print("Es sind keine Mitglieder vorhanden.")
            return
        else:
            print("--- Mitglieder ---")
            for member in self.members:
                print(member)

    def showEvents(self):
        if not self.events:
            print("Es sind keine Veranstaltungen vorhanden.")
        else:
            print("--- Veranstaltungen ---")
            for event in self.events:
                print(event)
