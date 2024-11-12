from pyfiglet import Figlet
from tabulate import tabulate

willkommens_text = Figlet()
print(willkommens_text.renderText("Python Toleranzrechner"))
print("Willkommen zum Toleranzrechner!")
print("\nBitte beachten Sie die folgenden Hinweise:\n")
print("🔹 Toleranzklasse 1 = H6")
print("🔹 Toleranzklasse 2 = H8")
print("🔹 Toleranzklasse 3 = g6")
print("🔹 Toleranzklasse 4 = r6")
print("\n⚠️ Bei der Eingabe von Nennmaß darf man nicht die Einheit eingeben und das Nennmaß muss innerhalb des Intervalls [1-30] mm sein.\n")
print("🔍Hinweis: Dieser Rechner wurde getestet, aber die Genauigkeit der Ergebnisse kann nicht garantiert werden.")
print("\n" + "=" * 70)

# Methode für die Hauptmenü
def haupt_menu_anzeigen():
    print()
    print("Was möchten Sie tun?" + "\n" + "1. Berechnung starten" + "\n" + "2. Programm beenden\n")

# Methode für die verschiedenen Toleranzklassen
def toleranz_menu_anzeigen():
    print()
    print("Wählen Sie bitte die gewünschte Toleranzklasse aus:" + "\n" + "1. H6" + "\n" + "2. H8" + "\n" + "3. g6" + "\n" + "4. r6" + "\n" + "5. Zurück zum Hauptmenü\n")

# Die folgende Methode überprüft, ob das eingegebene Nennmaß innerhalb des gültigens Intervalls ist. [1-30] mm.
# Es gibt 2 Rückgabewerte:
# Falls das Nennmaß richtig ist, ist das Nennmaß der Rückgabewert.
# Falls das Nennmaß nicht innerhalb des Intervalls ist, wird eine Informationsmeldung angezeigt und nichts zurückgegeben.
def nennmass_ueberpruefen(nennmass):
    if nennmass >= 1 and nennmass <= 30:
        return nennmass
    else:
        print(f"Ungültiges Nennmaß!Das eingegebene Nennmaß von {nennmass} mm ist außerhalb des gültigen Intervalls [1-30].")
        return None

# Die Methode *tabelle_anzeigen* zeigt die Maßen und die Toleranz in einem Tabellenformat.
def tabelle_anzeigen(toleranzklasse,nennmass,oberes_abmass,unteres_abmass,formatiertes_hoechstmass,formatiertes_mindestmass,toleranz):
    # Tabellenformat
    tabelle = [["Toleranzklasse","Nennmaß", "Oberes Abmaß", "Unteres Abmaß", "Mindestmaß", "Höchstmaß", "Toleranz"],
               [f"{toleranzklasse}",f"{nennmass} mm", f"{oberes_abmass} μm", f"{unteres_abmass} μm", f"Ø{formatiertes_hoechstmass}",
                f"Ø{formatiertes_mindestmass}", f"{toleranz} μm"]]
    print()
    print("===================================ERGEBNIS===================================")

    print("Grenzabmaße in μm für Nennmaße in mm (nach DIN ISO 286)")
    print(tabulate(tabelle, headers="firstrow", tablefmt="fancy_grid"))

# Die Methode *masse_und_toleranz_berechnen* berechnet die Maße(oberes Abmaß & unteres Abmaß, Höchstmaß, Mindestmaß) sowie die Toleranz.
def masse_und_toleranz_berechnen(nennmass, toleranzklasse):
    oberes_abmass = unteres_abmass = 0

    # Toleranzklasse 1 entspricht H6
    if toleranzklasse == 1:
        if nennmass >= 1 and nennmass <= 3:
            oberes_abmass = +6
        elif nennmass >= 4 and nennmass <= 6:
            oberes_abmass = +8
        elif nennmass >= 7 and nennmass <= 10:
            oberes_abmass = +9
        elif nennmass >= 11 and nennmass <= 18:
            oberes_abmass = +11
        elif nennmass >= 19 and nennmass <= 30:
            oberes_abmass = +13

    # Toleranzklasse 2 entspricht H8
    elif toleranzklasse == 2:
        if nennmass >= 1 and nennmass <= 3:
            oberes_abmass = +14
        elif nennmass >= 4 and nennmass <= 6:
            oberes_abmass = +18
        elif nennmass >= 7 and nennmass <= 10:
            oberes_abmass = +22
        elif nennmass >= 11 and nennmass <= 18:
            oberes_abmass = +27
        elif nennmass >= 19 and nennmass <= 30:
            oberes_abmass = +33

    # Toleranzklasse 3 entspricht g6
    elif toleranzklasse == 3:
        if nennmass >= 1 and nennmass <= 3:
            oberes_abmass, unteres_abmass = -2, -8
        elif nennmass >= 4 and nennmass <= 6:
            oberes_abmass, unteres_abmass = -4, -12
        elif nennmass >= 7 and nennmass <= 10:
            oberes_abmass, unteres_abmass = -5, -14
        elif nennmass >= 11 and nennmass <= 18:
            oberes_abmass, unteres_abmass = -6, -17
        elif nennmass >= 19 and nennmass <= 30:
            oberes_abmass, unteres_abmass = -7, -20

    # Toleranzklasse 4 entspricht r6
    elif toleranzklasse == 4:
        if nennmass >= 1 and nennmass <= 3:
            oberes_abmass, unteres_abmass = +16, +10
        elif nennmass >= 4 and nennmass <= 6:
            oberes_abmass, unteres_abmass = +23, +15
        elif nennmass >= 7 and nennmass <= 10:
            oberes_abmass, unteres_abmass = +28, +19
        elif nennmass >= 11 and nennmass <= 18:
            oberes_abmass, unteres_abmass = +34, +23
        elif nennmass >= 19 and nennmass <= 30:
            oberes_abmass, unteres_abmass = +41, +28

    # Berechnung & Formatierung von Maßen
    # Damit das Mindestmaß und Höchstmaß mit 3 Nachkommastellen angezeigt werden, werden die Maßen formatiert.
    mindestmass = nennmass + unteres_abmass
    hoechstmass = nennmass + oberes_abmass
    formatiertes_mindestmass = format(mindestmass, ".3f")
    formatiertes_hoechstmass = format(hoechstmass, ".3f")
    # Berechnung der Toleranz
    toleranz = hoechstmass - mindestmass
    # Aufruf der Methode fuer die Ausgabe in Tabellenformat
    tabelle_anzeigen(toleranzklasse, nennmass, oberes_abmass, unteres_abmass, formatiertes_hoechstmass,
                     formatiertes_mindestmass, toleranz)

def main():
    while True:
        try:
            haupt_menu_anzeigen()
            user_input = int(input("Ihre Auswahl (1-2): "))

            if user_input == 1:
                toleranz_menu_anzeigen()
                klasse_input = int(input("Ihre Auswahl (1-5): "))

                if klasse_input in [1, 2, 3, 4]:
                    nennmass_input = float(input("Geben Sie bitte das Nennmaß (1-30) ein: \n"))
                    validiertes_nennmass = nennmass_ueberpruefen(nennmass_input)
                    if validiertes_nennmass is not None:
                        masse_und_toleranz_berechnen(validiertes_nennmass,klasse_input)
                elif klasse_input == 5:
                    continue
                    # print("Auf Wiedersehen \U0001F642")
                    # break
                else:
                    print("Ungültige Auswahl! Wählen Sie bitte eine Nummer von 1 bis 5.")

            elif user_input == 2:
                print("Auf Wiedersehen \U0001F642")
                break
            else:
                print("Ungültige Eingabe! Wählen Sie bitte entweder 1 oder 2.")
                print()

        except ValueError:
            print("Geben Sie bitte nur Zahlen ein. Versuchen Sie es nochmal.")
            print()
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            print()

if __name__ == "__main__":
    main()