from pyfiglet import Figlet
from tabulate import tabulate

willkommens_text = Figlet()
print(willkommens_text.renderText("Python Toleranzrechner"))
print("======================================================================")
print("Willkommen zum Toleranzrechner!")
print("Hinweis: Dieser Rechner wurde getestet, aber die Genauigkeit der Ergebnisse kann nicht garantiert werden.")
print("======================================================================")

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
    print("Grenzabmaße in μm für Nennmaße in mm (nach DIN ISO 286)")
    print(tabulate(tabelle, headers="firstrow", tablefmt="fancy_grid"))
