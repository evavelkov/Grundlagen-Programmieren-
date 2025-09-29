passwort = input("geben sie ihre passwort ein: ")

if passwort.lower() == "geheim":
    #das lower() wandelt die eigegebenen Buchstaben in kleinbuchstaben um. 
    print(passwort.lower())
    print("Zugang genehmigt!")
else:
    print("Zugang verweigert")

print ("Programm beendet.")
