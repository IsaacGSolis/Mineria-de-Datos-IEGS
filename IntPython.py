#Ejercicio 1
numero = int(input("Ingresa un numero: "))
if numero%2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
#Ejercicio 2
numero1 = int(input("Ingresa un numero: "))
if numero1 > 0:
    print("El numero es positivo")
elif numero1 < 0:
    print("El numero es negativo")
#Ejercicio 3
edad = int(input("Ingresa una edad: "))
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")
#Ejercicio 4
calif = int(input("Ingresa una calificacion (escala 0-100): "))
if  calif >= 60:
    print("Aprobado")
else: 
    print("Reprobado")
#Ejercicio 5
calif1 = int(input("Ingresa una calificacion (escala 0-100): "))
if calif1>=90:
    print("A")
elif calif1>=80 and calif1<90:
    print("B")
elif calif1>=70 and calif1<80:
    print("C")
elif calif1>=60 and calif1<70:
    print("D")
else:
    print("F")
#Ejercicio 6
temp = int(input("Ingresa la temperatura en grados Celsius: "))
if temp < 0:
    print("Sólido")
elif temp >= 0 and temp < 100:
    print("Líquido")
else:
    print("Vapor")