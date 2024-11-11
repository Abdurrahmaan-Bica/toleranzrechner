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
