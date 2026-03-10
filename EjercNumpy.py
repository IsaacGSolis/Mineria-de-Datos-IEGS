import numpy as np
#Ejercicio 1
a1=np.random.randint(0,100,10)
print(a1)
#Ejercicio 2
a2=np.random.rand(5)
print(a2)
#Ejercicio 3
a=np.random.randint(0,50,5)
b=np.random.randint(50,100,5)
ab=np.concatenate((a,b))
print(ab)
#Ejercicio 4
a3=np.random.randint(0,100,10)
a4=np.split(a3,2)
print(a3)
print(a4)
#Ejercicio 5
a5=np.random.rand(3,3)
print(a5)
#Ejercicio 6
a6=np.random.randint(0,100,10)
a7=np.random.choice(a6,3,replace=False)
print(a6)
print("3 elementos al azar: ",a7)
#Ejercicio 7
a8=np.random.randint(0,100,10)
media=np.mean(a8)
print("Array: ",a8)
print("Media:", media)