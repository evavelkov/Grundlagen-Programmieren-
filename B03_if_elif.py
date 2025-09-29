#elif = else if 
#verienfacht die eingabe von if und else 
#damit sich das programm nicht wie eine pyramide nach recht bewegt

punkte = float(input("Erreichte Punktzahlt: "))

if punkte >= 90:
    note = "Sehr gut"
elif punkte >= 80:
    note = "Gut"
elif punkte >= 70:
    note = "Genügend"

print(f"Ihre Note: {note}")


