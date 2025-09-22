name = 'alice' #string
age = 30 #integer
temperature = 36.6 #float

print(name)
print('name:', name) 
print('age:', age)
print('temperature:', temperature)

_mein_alter = 25
print(_mein_alter)
# ehrfachzuweisung 
x, y, z = 1, 2.5, 'hallo'
print(x, y, z)
print(x)    
print(y)
print(z)

anzahl = 10.0
print('anzahl:', type(anzahl)) #type() gibt den Datentyp zurück, nicht den Wert

name = input("was ist dein Name?   ")
print('hallo', name)    
age_str = input("wie alt bist du?   ")
age_str = int(age_str) #umwandlung von string zu integer

print('du bist', age_str, 'jahre alt')

note = float(input("wie ist deine note?   ")) #umwandlung von string zu float
print('deine note ist: ', note)