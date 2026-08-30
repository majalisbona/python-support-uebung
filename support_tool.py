print("Willkommen im IT-Support-Tool")
print("Dieses Programm hilft bei einfachen Support-Aufgaben.")
print("Python Tag 1")
name = input("Bitte geben Sie Ihren Namen ein: ")
print(f"Hallo {name}, willkommen im IT-Support-Tool.")
while True:
    print("Bitte wählen Sie eine Aufgabe:")
    print("1) Neues Ticket aufnehmen")
    print("2) Systemstatus anzeigen")
    print("3) Benutzerinformationen anzeigen")
    print("4) Programm beenden")

    auswahl = input("Ihre Auswahl: ")

    if auswahl == "1":
        print("Ticketaufnahme wird gestartet...")
    elif auswahl == "2":
        print("Systemstatus wird geprüft...")
    elif auswahl == "3":
        print("Benutzerinformationen werden angezeigt...")
    elif auswahl == "4":
        print("Programm wird beendet.")
        break
    else:
        print("Ungültige Auswahl.")