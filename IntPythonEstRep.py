#Ejercicio 1
suma=0
N=int(input("Ingresa un numero: "))
for i in range(1,N+1):
    suma=suma+i
print("El total es:",suma)
#Ejercicio 2
fact=1
num=int(input("Ingresa un numero positivo: "))
for i in range(1,num+1):
    fact=fact*i
print("El factorial es:",fact)
#Ejercicio 3
num1=int(input("Ingresa el numero de la tabla de multiplicar: "))
for i in range(1,11):
    print(num1,"x",i,"=",num1*i)
#Ejercicio 4
sum=0
cont=0
nota=float(input("Ingresa una nota (negativa para terminar): "))
while nota>=0:
    sum+=nota
    cont+=1
    nota = float(input("Ingresa otra nota (negativa para terminar): "))
if cont>0:
    promedio=sum/cont
    print("El promedio es:", promedio)
else:
    print("No hay notas ingresadas.")
#Ejercicio 5
base=int(input("Ingresa el valor de la base: "))
exp=int(input("Ingresa el valor del exponente: "))
result=1
for i in range(exp):
    result=result*base
print(base,"elevado a",exp,"es:",result)
#Ejercicio 6
a=int(input("Ingresa el valor A: "))
b=int(input("Ingresa el valor B: "))
suma1=0
for i in range(a,b+1):
    if i%2==0:
        suma1+=i
print("La suma de los números pares entre",a,"y",b,"es:",suma1)