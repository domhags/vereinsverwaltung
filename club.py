import csv
from member import Member
from address import Address


class Club:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.members = []
        self.events = []

    def addMember(self, member):
        self.members.append(member)

    def removeMember(self, member_to_remove):
        self.members.remove(member_to_remove)

    def findMember(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    def getMembers(self):
        return self.members

    def addEvent(self, event):
        self.events.append(event)

    def removeEvent(self, event_to_remove):
        self.events.remove(event_to_remove)

    def findEvent(self, event_id):
        for event in self.events:
            if event.event_id == event_id:
                return event
        return None

    def getEvents(self):
        return self.events

    def export_members_to_csv(self, filename, officer_only=False):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Schreibe Header-Zeile
            writer.writerow(
                ["Vorname", "Nachname", "Geburtsdatum", "Straße", "Hausnummer", "PLZ", "Stadt", "Mitgliedsnummer",
                 "Funktionär"])
            # Schreibe Daten der Mitglieder in die CSV-Datei
            for member in self.members:
                if officer_only and not member.is_officer:
                    continue
                writer.writerow([member.first_name, member.last_name, member.birth_date,
                                 member.address.street, member.address.house_number, member.address.zip_code,
                                 member.address.city, member.member_id, "Ja" if member.is_officer else "Nein"])

    def import_members_from_csv(self, filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Überspringe Header-Zeile
            for row in reader:
                # Extrahiere Daten aus der CSV-Datei
                first_name, last_name, birth_date, street, house_number, zip_code, city, member_id, is_officer = row
                is_officer = True if is_officer.lower() == 'ja' else False
                # Erstelle Address-Objekt
                address = Address(street, house_number, zip_code, city)
                # Erstelle Member-Objekt und füge es der Mitgliederliste hinzu
                member = Member(first_name, last_name, birth_date, address, member_id, is_officer)
                self.members.append(member)
