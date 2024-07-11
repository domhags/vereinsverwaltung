import tkinter as tk
from tkinter import messagebox, ttk, simpledialog
from event import Event
from address import Address
from member import Member
from club import Club
from datetime import datetime


class ClubApp:
    def __init__(self, main_windows):
        # Initialisierung der GUI und Variablen
        self.member_id = None
        self.address = None
        self.club_name_entry = None
        self.club_street_entry = None
        self.club_house_number_entry = None
        self.club_zip_code_entry = None
        self.club_city_entry = None
        self.root = main_windows
        self.root.title("Vereinsverwaltung")
        self.root.geometry("500x500")

        self.club = None  # Initiale Club-Instanz

        # Hauptframe der Applikation
        self.main_frame = tk.Frame(main_windows)
        self.main_frame.grid(row=0, column=0, sticky="nsew")

        # Grid-Konfiguration für responsive Layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Erstellen der initialen Widgets beim Start
        self.create_initial_widgets()

    def create_initial_widgets(self):
        # Labels und Entry-Felder für Vereinsinformationen
        tk.Label(self.main_frame, text="Vereinsname").grid(row=0, column=0, padx=10, pady=5)
        self.club_name_entry = tk.Entry(self.main_frame)
        self.club_name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Straße (ohne Hausnummer)").grid(row=1, column=0, padx=10, pady=5)
        self.club_street_entry = tk.Entry(self.main_frame)
        self.club_street_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Hausnummer").grid(row=2, column=0, padx=10, pady=5)
        self.club_house_number_entry = tk.Entry(self.main_frame)
        self.club_house_number_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="PLZ").grid(row=3, column=0, padx=10, pady=5)
        self.club_zip_code_entry = tk.Entry(self.main_frame)
        self.club_zip_code_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Stadt").grid(row=4, column=0, padx=10, pady=5)
        self.club_city_entry = tk.Entry(self.main_frame)
        self.club_city_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Button(self.main_frame, text="Verein erstellen",
                  command=self.create_club).grid(row=5, columnspan=2, padx=10, pady=5)

    def create_club(self):
        # Methode zum Erstellen des Vereins mit den eingegebenen Daten
        name = self.club_name_entry.get()
        street = self.club_street_entry.get()
        house_number = self.club_house_number_entry.get()
        zip_code = self.club_zip_code_entry.get()
        city = self.club_city_entry.get()

        address = Address(street, house_number, zip_code, city)
        self.club = Club(name, address)
        self.show_main_menu()

    def clear_frame(self):
        # Methode zum Löschen aller Widgets im Hauptframe
        for widget in self.main_frame.winfo_children():
            widget.grid_forget()

    def show_main_menu(self):
        # Anzeige des Hauptmenüs mit verschiedenen Buttons für Aktionen
        self.clear_frame()

        tk.Button(self.main_frame, text="Mitglied hinzufügen",
                  command=self.add_member).grid(row=0, column=0, padx=10, pady=5)
        tk.Button(self.main_frame, text="Mitglied entfernen",
                  command=self.remove_member).grid(row=0, column=1, padx=10, pady=5)
        tk.Button(self.main_frame, text="Veranstaltung hinzufügen",
                  command=self.add_event).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self.main_frame, text="Veranstaltung entfernen",
                  command=self.remove_event).grid(row=1, column=1, padx=10, pady=5)
        tk.Button(self.main_frame, text="Mitglieder anzeigen",
                  command=self.show_members).grid(row=2, column=0, padx=10, pady=5)
        tk.Button(self.main_frame, text="Veranstaltungen anzeigen",
                  command=self.show_events).grid(row=2, column=1, padx=10, pady=5)
        tk.Button(self.main_frame, text="Datei Exportieren",
                  command=self.export_file).grid(row=3, column=0, padx=10, pady=5)
        tk.Button(self.main_frame, text="Datei importieren",
                  command=self.import_file).grid(row=3, column=1, padx=10, pady=5)
        tk.Button(self.main_frame, text="Beenden",
                  command=self.root.quit).grid(row=4, columnspan=2, padx=10, pady=5)

    def add_member(self):
        # Methode zum Hinzufügen eines Mitglieds mit Eingabefeldern
        self.clear_frame()
        tk.Label(self.main_frame, text="Mitglied hinzufügen").grid(row=0, columnspan=2, pady=10)

        # Eingabefelder für Mitgliedsinformationen
        tk.Label(self.main_frame, text="Vorname").grid(row=1, column=0, padx=10, pady=5)
        first_name_entry = tk.Entry(self.main_frame)
        first_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Nachname").grid(row=2, column=0, padx=10, pady=5)
        last_name_entry = tk.Entry(self.main_frame)
        last_name_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Geburtsdatum (DD-MM-YYYY)").grid(row=3, column=0, padx=10, pady=5)
        birth_date_entry = tk.Entry(self.main_frame)
        birth_date_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Straße (ohne Hausnummer)").grid(row=4, column=0, padx=10, pady=5)
        street_entry = tk.Entry(self.main_frame)
        street_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Hausnummer").grid(row=5, column=0, padx=10, pady=5)
        house_number_entry = tk.Entry(self.main_frame)
        house_number_entry.grid(row=5, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="PLZ").grid(row=6, column=0, padx=10, pady=5)
        zip_code_entry = tk.Entry(self.main_frame)
        zip_code_entry.grid(row=6, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Stadt").grid(row=7, column=0, padx=10, pady=5)
        city_entry = tk.Entry(self.main_frame)
        city_entry.grid(row=7, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Mitgliedsnummer").grid(row=8, column=0, padx=10, pady=5)
        member_id_entry = tk.Entry(self.main_frame)
        member_id_entry.grid(row=8, column=1, padx=10, pady=5)

        # Checkbox für Funktionärsstatus
        is_officer_var = tk.IntVar()
        officer_checkbox = tk.Checkbutton(self.main_frame, text="Funktionär", variable=is_officer_var)
        officer_checkbox.grid(row=9, columnspan=2, padx=10, pady=5)

        def save_member():
            # Funktion zum Speichern des Mitglieds
            first_name = first_name_entry.get().strip()
            last_name = last_name_entry.get().strip()
            birth_date = birth_date_entry.get().strip()
            street = street_entry.get().strip()
            house_number = house_number_entry.get().strip()
            zip_code = zip_code_entry.get().strip()
            city = city_entry.get().strip()
            member_id = member_id_entry.get().strip()
            is_officer = bool(is_officer_var.get())

            # Validierung der Eingaben
            if not all([first_name, last_name, birth_date, street, house_number, zip_code, city, member_id]):
                messagebox.showerror("Fehler", "Alle Felder müssen ausgefüllt werden.")
                return

            if not self.validate_date(birth_date):
                messagebox.showerror("Fehler", "Ungültiges Geburtsdatum. Bitte im Format DD-MM-YYYY eingeben.")
                return

            if self.club.findMember(member_id):
                messagebox.showerror("Fehler", "Diese Mitgliedsnummer ist bereits vergeben.")
                return

            # Erstellen des Address-Objekts und des Member-Objekts
            address = Address(street, house_number, zip_code, city)
            member = Member(first_name, last_name, birth_date, address, member_id, is_officer)
            self.club.addMember(member)
            messagebox.showinfo("Erfolg", "Mitglied hinzugefügt.")
            self.show_main_menu()

        tk.Button(self.main_frame, text="Speichern",
                  command=save_member).grid(row=10, columnspan=2, padx=10, pady=5)
        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=11, columnspan=2, padx=10, pady=5)

    def remove_member(self):
        # Methode zur Entfernung eines Mitglieds mittels Dropdownfeld
        self.clear_frame()
        tk.Label(self.main_frame, text="Mitglied entfernen").grid(row=0, columnspan=2, pady=10)

        tk.Label(self.main_frame, text="Mitglied").grid(row=1, column=0, padx=10, pady=5)

        members_list = [f"{member.member_id} | {member.first_name} {member.last_name}" for member in
                        self.club.getMembers()]

        member_combobox = ttk.Combobox(self.main_frame, values=members_list)
        member_combobox['values'] = [f"{member.member_id} | {member.first_name} {member.last_name}" for member in
                                     self.club.members]
        member_combobox.current(0)
        member_combobox.grid(row=1, column=1, padx=10, pady=5)

        def delete_member():
            # Funktion zum Löschen eines Mitglieds
            selected_value = member_combobox.get()

            if not selected_value:
                messagebox.showerror("Fehler", "Bitte wählen Sie ein Mitglied aus.")
                return

            member_id = selected_value.split()[0]

            member = self.club.findMember(member_id)

            if not member:
                messagebox.showerror("Fehler", "Mitglied nicht gefunden.")
                return

            self.club.removeMember(member)
            messagebox.showinfo("Erfolg", "Mitglied entfernt.")
            self.show_main_menu()

        tk.Button(self.main_frame, text="Löschen",
                  command=delete_member).grid(row=2, columnspan=2, padx=10, pady=5)
        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=3, columnspan=2, padx=10, pady=5)

    def add_event(self):
        # Methode zum Hinzufügen einer Veranstaltung
        self.clear_frame()
        tk.Label(self.main_frame, text="Veranstaltung hinzufügen").grid(row=0, columnspan=2, pady=10)

        # Eingabefelder für Veranstaltungsinformationen
        tk.Label(self.main_frame, text="Name der Veranstaltung").grid(row=1, column=0, padx=10, pady=5)
        event_name_entry = tk.Entry(self.main_frame)
        event_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Datum (DD-MM-YYYY)").grid(row=2, column=0, padx=10, pady=5)
        event_date_entry = tk.Entry(self.main_frame)
        event_date_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="Ort der Veranstaltung").grid(row=3, column=0, padx=10, pady=5)
        event_location_entry = tk.Entry(self.main_frame)
        event_location_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(self.main_frame, text="ID der Veranstaltung").grid(row=4, column=0, padx=10, pady=5)
        event_id_entry = tk.Entry(self.main_frame)
        event_id_entry.grid(row=4, column=1, padx=10, pady=5)

        def save_event():
            # Funktion zum Speichern der Veranstaltung
            event_name = event_name_entry.get().strip()
            event_date = event_date_entry.get().strip()
            event_location = event_location_entry.get().strip()
            event_id = event_id_entry.get().strip()

            # Validierung der Eingaben
            if not all([event_name, event_date, event_location, event_id]):
                messagebox.showerror("Fehler", "Alle Felder müssen ausgefüllt werden.")
                return

            if not self.validate_date(event_date):
                messagebox.showerror("Fehler", "Ungültiges Datum. Bitte im Format DD-MM-YYYY eingeben.")
                return

            # Erstellen der Event-Instanz und Hinzufügen zum Verein
            event = Event(event_name, event_date, event_location, event_id)
            self.club.addEvent(event)
            messagebox.showinfo("Erfolg", "Veranstaltung hinzugefügt.")
            self.show_main_menu()

        tk.Button(self.main_frame, text="Speichern",
                  command=save_event).grid(row=5, columnspan=2, padx=10, pady=5)
        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=6, columnspan=2, padx=10, pady=5)

    def remove_event(self):
        # Methode zum Entfernen einer Veranstaltung
        self.clear_frame()
        tk.Label(self.main_frame, text="Veranstaltung entfernen").grid(row=0, columnspan=2, pady=10)

        tk.Label(self.main_frame, text="Veranstaltung").grid(row=2, column=0, padx=10, pady=5)

        events_list = [f"{event.event_id} | {event.event_name}" for event in self.club.getEvents()]

        event_combobox = ttk.Combobox(self.main_frame, values=events_list)
        event_combobox['values'] = [f"{event.event_id} | {event.event_name}" for event in self.club.events]
        event_combobox.current(0)
        event_combobox.grid(row=2, column=1, padx=10, pady=5)

        def delete_event():
            # Funktion zum Löschen der Veranstaltung
            selected_value = event_combobox.get()

            if not selected_value:
                messagebox.showerror("Fehler", "Bitte wählen Sie eine Veranstaltung aus.")
                return

            event_id = selected_value.split()[0]  # Hier wird von der ComboBox nur die ID ausgelesen
            event = self.club.findEvent(event_id)

            if not event:
                messagebox.showerror("Fehler", "Veranstaltung mit diesem Namen nicht gefunden.")
                return

            self.club.removeEvent(event)
            messagebox.showinfo("Erfolg", "Veranstaltung entfernt.")
            self.show_main_menu()

        tk.Button(self.main_frame, text="Löschen",
                  command=delete_event).grid(row=4, columnspan=2, padx=10, pady=5)
        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=5, columnspan=2, padx=10, pady=5)

    def show_members(self):
        # Methode zum Anzeigen aller Mitglieder
        self.clear_frame()

        members = self.club.getMembers()
        title = "Mitglieder"

        tk.Label(self.main_frame, text=title).grid(row=0, columnspan=2, pady=10)

        listbox = tk.Listbox(self.main_frame, width=100, height=20)
        listbox.grid(row=1, columnspan=2, padx=10, pady=10, sticky="nsew")

        scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=listbox.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")
        listbox.config(yscrollcommand=scrollbar.set)

        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=2, columnspan=2, padx=10, pady=5)

        if not members:
            messagebox.showinfo("Information", f"Es sind keine {title} vorhanden.")
            return

        # Anzeigen der Mitglieder in einer ListBox
        for member in members:
            status = "Funktionär" if member.is_officer else "Nicht Funktionär"
            listbox.insert(tk.END, f"{member.member_id} | {member.first_name} {member.last_name} | {status}")

    def show_events(self):
        # Methode zum Anzeigen aller Veranstaltungen
        self.clear_frame()

        events = self.club.getEvents()
        title = "Veranstaltungen"

        tk.Label(self.main_frame, text=title).grid(row=0, columnspan=2, pady=10)

        listbox = tk.Listbox(self.main_frame, width=80, height=20)
        listbox.grid(row=1, columnspan=2, padx=10, pady=10, sticky="nsew")

        scrollbar = tk.Scrollbar(self.main_frame, orient="vertical", command=listbox.yview)
        scrollbar.grid(row=1, column=2, sticky="ns")
        listbox.config(yscrollcommand=scrollbar.set)

        tk.Button(self.main_frame, text="Zurück",
                  command=self.show_main_menu).grid(row=2, columnspan=2, padx=10, pady=5)

        if not events:
            messagebox.showinfo("Information", f"Es sind keine {title} vorhanden.")
            return

        # Anzeigen der Veranstaltungen in einer ListBox
        for event in events:
            listbox.insert(tk.END, f"{event.event_id} | {event.event_name}")

    def export_file(self):
        # Methode zum Exportieren der Daten in eine Datei
        filename_export = simpledialog.askstring("Information", "Bitte geben Sie den Dateinamen an. (*.csv)")

        if filename_export:
            officer_only = messagebox.askyesno("Export Option", "Nur Funktionäre exportieren?")
            self.club.export_members_to_csv(filename_export, officer_only=officer_only)
            messagebox.showinfo("Erfolg", "Daten gespeichert.")
        else:
            messagebox.showwarning("Eingabefehler", "Dateinamen müssen angegeben werden.")

    def import_file(self):
        # Methode zum Importieren von Daten aus einer Datei
        filename_import = simpledialog.askstring("Information", "Bitte geben Sie den Dateinamen an (*.csv)")

        if filename_import:
            self.club.import_members_from_csv(filename_import)
            messagebox.showinfo("Erfolg", "Daten geladen.")
        else:
            messagebox.showwarning("Eingabefehler", "Dateinamen müssen angegeben werden.")

    @staticmethod
    def validate_date(date_string):
        # statische Methode zur Validierung eines Datums im Format DD-MM-YYYY
        try:
            datetime.strptime(date_string, "%d-%m-%Y")
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    root = tk.Tk()
    app = ClubApp(root)
    root.mainloop()
