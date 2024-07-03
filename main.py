from event import Event
from address import Address
from member import Member
from club import Club
from datetime import datetime


def main():
    print("--- Vereinsverwaltung ---")
    club_name = input("Geben Sie den Namen des Vereins ein: ")
    club_street = input("Geben Sie die Straße ein (ohne Hausnummer): ")
    club_house_number = input("Geben Sie die Hausnummer ein: ")
    club_zip_code = input("Geben Sie die Postleitzahl ein: ")
    club_city = input("Geben Sie die Stadt ein: ")

    club_address = Address(club_street, club_house_number, club_zip_code, club_city)
    new_club = Club(club_name, club_address)

    while True:
        print("\nWas möchten Sie tun?\n"
              "1. Mitglied hinzufügen\n"
              "2. Mitglied entfernen\n"
              "3. Veranstaltung hinzufügen\n"
              "4. Veranstaltung entfernen\n"
              "5. Mitglied zu Veranstaltung anmelden\n"
              "6. Mitglied von Veranstaltung abmelden\n"
              "7. Mitglieder anzeigen\n"
              "8. Veranstaltungen anzeigen\n"
              "9. Beenden")
        choice = input("Wählen Sie eine Option: ")

        # Punkt 1: Mitglied hinzufügen
        if choice == "1":
            add_member_to_club(new_club)
        # Punkt 2: Mitglied entfernen
        elif choice == '2':
            remove_member_from_club(new_club)
        # Punkt 3: Veranstaltung hinzufügen
        elif choice == "3":
            add_event_to_club(new_club)
        # Punkt 4: Veranstaltung entfernen
        elif choice == '4':
            remove_event_from_club(new_club)
        # Punkt 5: Mitglied zu Veranstaltung anmelden
        elif choice == '5':
            register_member_to_event(new_club)
        # Punkt 6: Mitglied von Veranstaltung abmelden
        elif choice == '6':
            deregister_member_from_event(new_club)
        # Punkt 7: Mitglieder anzeigen
        elif choice == '7':
            new_club.showMembers()
        # Punkt 8: Veranstaltungen anzeigen
        elif choice == '8':
            new_club.showEvents()
        # Punkt 9: Beenden
        elif choice == '9':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")


def add_member_to_club(club):
    print("\nMitglied hinzufügen:")
    m_first_name = input("Vorname: ").strip()
    m_last_name = input("Nachname: ").strip()
    m_birth_date = input("Geburtsdatum (DD-MM-YYYY): ").strip()
    m_street = input("Straße (ohne Hausnummer): ").strip()
    m_house_number = input("Hausnummer: ").strip()
    m_zip_code = input("PLZ: ").strip()
    m_city = input("Stadt: ").strip()
    m_member_id = input("Mitgliedsnummer: ").strip()

    # Überprüfen auf leere Felder
    if not all([m_first_name, m_last_name, m_birth_date, m_street, m_house_number, m_zip_code, m_city, m_member_id]):
        print("Alle Felder müssen ausgefüllt werden.")
        return

    if not validate_date(m_birth_date):
        print("Ungültiges Geburtsdatum. Bitte im Format DD-MM-YYYY eingeben.")
        return

    if club.findMember(m_member_id):
        print("Diese Mitgliedsnummer ist bereits vergeben.")
        return

    member_address = Address(m_street, m_house_number, m_zip_code, m_city)
    member = Member(m_first_name, m_last_name, m_birth_date, member_address, m_member_id)
    club.addMember(member)


def remove_member_from_club(club):
    club.showMembers()
    try:
        memberId = int(input("ID des zu entfernenden Mitglieds: ").strip())
        member_to_remove = club.findMember(str(memberId))
        if member_to_remove:
            confirmation = input(f"Sind Sie sicher, dass Sie {member_to_remove} entfernen möchten?"
                                 f"(j/n): ").strip().lower()
            if confirmation == 'j':
                club.removeMember(member_to_remove)
            else:
                print("Entfernen abgebrochen.")
        else:
            print("Ungültige ID.")
    except ValueError:
        print("Bitte eine gültige numerische ID eingeben.")


def add_event_to_club(club):
    print("\nVeranstaltung hinzufügen:")
    event_name = input("Veranstaltungsname: ").strip()
    event_date = input("Datum (DD-MM-YYYY): ").strip()
    event_location = input("Ort: ").strip()
    event_id = input("ID: ").strip()

    if not all([event_name, event_date, event_location, event_id]):
        print("Alle Felder müssen ausgefüllt werden.")
        return

    if not validate_date(event_date):
        print("Ungültiges Datum. Bitte im Format DD-MM-YYYY eingeben.")
        return

    if club.findEvent(event_id):
        print("Diese Event-ID ist bereits vergeben.")
        return

    new_event = Event(event_name, event_date, event_location, event_id)
    club.addEvent(new_event)


def remove_event_from_club(club):
    club.showEvents()
    if not club.events:
        return
    try:
        event_id = int(input("ID der zu entfernenden Veranstaltung: ").strip())
        event_to_remove = club.findEvent(event_id)
        if event_to_remove:
            confirmation = input(f"Sind Sie sicher, dass Sie die Veranstaltung"
                                 f"'{event_to_remove.event_name}'"
                                 f"entfernen möchten? (j/n): ").strip().lower()
            if confirmation == 'j':
                club.removeEvent(event_to_remove)
                print("Veranstaltung entfernt.")
            else:
                print("Entfernen abgebrochen.")
        else:
            print("Ungültige ID.")
    except ValueError:
        print("Bitte eine gültige numerische ID eingeben.")


def register_member_to_event(club):
    club.showMembers()
    if not club.members:
        print("Es sind keine Mitglieder vorhanden.")
        return

    club.showEvents()
    if not club.events:
        print("Es sind keine Veranstaltungen vorhanden.")
        return

    try:
        registering_member_id = input("Mitgliedsnummer des anzumeldenden Mitglieds: ").strip()
        registering_event_id = int(input("ID der Veranstaltung: ").strip())

        event_to_register = club.findEvent(registering_event_id)
        if not event_to_register:
            print("Ungültige ID der Veranstaltung.")
            return

        member_to_register = club.findMember(registering_member_id)
        if not member_to_register:
            print("Mitglied mit dieser Mitgliedsnummer nicht gefunden.")
            return

        if member_to_register in event_to_register.participants:
            print(f"{member_to_register.first_name} {member_to_register.last_name} ist bereits für diese "
                  f"Veranstaltung angemeldet.")
        else:
            event_to_register.register(member_to_register)
            print(
                f"{member_to_register.first_name} {member_to_register.last_name} zur "
                f"Veranstaltung {event_to_register.event_name} angemeldet.")
    except ValueError:
        print("Ungültige Eingabe. Bitte eine numerische ID eingeben.")


def deregister_member_from_event(club):
    club.showMembers()
    if not club.members:
        print("Es sind keine Mitglieder vorhanden.")
        return

    club.showEvents()
    if not club.events:
        print("Es sind keine Veranstaltungen vorhanden.")
        return

    try:
        deregistering_member_id = input("Mitgliedsnummer des abzumeldenden Mitglieds: ").strip()
        deregistering_event_id = int(input("ID der Veranstaltung: ").strip())

        event_to_deregister = club.findEvent(deregistering_event_id)
        if not event_to_deregister:
            print("Ungültige ID der Veranstaltung.")
            return

        member_to_deregister = club.findMember(deregistering_member_id)
        if not member_to_deregister:
            print("Mitglied mit dieser Mitgliedsnummer nicht gefunden.")
            return

        if member_to_deregister not in event_to_deregister.participants:
            print(f"{member_to_deregister.first_name} {member_to_deregister.last_name} ist nicht "
                  f"für diese Veranstaltung angemeldet.")
        else:
            event_to_deregister.deregister(member_to_deregister)
            print(f"{member_to_deregister.first_name} {member_to_deregister.last_name} von der "
                  f"Veranstaltung {event_to_deregister.event_name} abgemeldet.")
    except ValueError:
        print("Ungültige Eingabe. Bitte eine numerische ID eingeben.")


def validate_date(date_to_check):
    try:
        datetime.strptime(date_to_check, "%d-%m-%Y")
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
