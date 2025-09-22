print(5-2)
print(5*2)
print(5/2)  #immer ein float Division
print(2**3) #hoch 3
print(5//2) #ganzzahlige Division (integer Division) 
print(5%2)  #Modulo, Rest der Division

arbeitsstunden = float(input("wie viele stunden hast du gearbeitet?:  "  ))
stundenlohn = float(input("wie hoch ist dein stundenlohn?: "))
gehalt = arbeitsstunden * stundenlohn   
print(f"dein gehalt beträgt: {gehalt:.2f} CHF") #f-string, ohne das f würde "{gehalt}" einfach so ausgegeben werden 




