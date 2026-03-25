import numpy as np
import scipy.stats as stats
import pandas as pd
#Ejercicio 1
print("Ejercicio 1")
#Datos del problema
mu_0=10#Hipotesis nula
n=49#Tamaño de la muestra
x_bar=9.7#Media muestral
s=0.5#Desviación estándar muestral
alpha=0.1#Nivel de significancia
#Calculamos el estadístico de prueba Z
z=(x_bar-mu_0)/(s/np.sqrt(n))
#Valor crítico para la prueba
z_critical=stats.norm.ppf(1-alpha)
#Comparacion de los valores
if z > z_critical:
    print("Rechazamos la hipótesis nula")
else:
    print("No rechazamos la hipótesis nula")
#Crear un Dataframe con los datos
df=pd.DataFrame({
    'parametros':['Media teorica','Media muestral','Desviación estándar','Tamaño de la muestra','Z-Calculado','Z-Crítico','Conclusión'],
    'valores':[mu_0,x_bar,s,n,z,z_critical,'Rechazar la hipótesis nula' if z > z_critical else 'No rechazar la hipótesis nula']
})
print(df)
#Ejercicio 2
print("Ejercicio 2")
#Datos del problema
mu_0=20#Hipotesis nula
n=30#Tamaño de la muestra
x_bar=18.5#Media muestral
s=2.5#Desviación estándar muestral
alpha=0.5#Nivel de significancia
#Calculamos el estadístico de prueba Z
z=(x_bar-mu_0)/(s/np.sqrt(n))
#Valor crítico para la prueba
z_critical=stats.norm.ppf(1-alpha)
#Comparacion de los valores
if z > z_critical:
    print("Rechazamos la hipótesis nula")
else:
    print("No rechazamos la hipótesis nula")
#Crear un Dataframe con los datos
df=pd.DataFrame({
    'parametros':['Media teorica','Media muestral','Desviación estándar','Tamaño de la muestra','Z-Calculado','Z-Crítico','Conclusión'],
    'valores':[mu_0,x_bar,s,n,z,z_critical,'Rechazar la hipótesis nula' if z > z_critical else 'No rechazar la hipótesis nula']
})
print(df)
#Ejercicio 3
print("Ejercicio 3")
#Datos del problema
mu_0=1000#Hipotesis nula
n=40#Tamaño de la muestra
x_bar=990#Media muestral
s=12#Desviación estándar muestral
alpha=0.2#Nivel de significancia
#Calculamos el estadístico de prueba Z
z=(x_bar-mu_0)/(s/np.sqrt(n))
#Valor crítico para la prueba
z_critical=stats.norm.ppf(1-alpha)
#Comparacion de los valores
if z > z_critical:
    print("Rechazamos la hipótesis nula")
else:
    print("No rechazamos la hipótesis nula")
#Crear un Dataframe con los datos
df=pd.DataFrame({
    'parametros':['Media teorica','Media muestral','Desviación estándar','Tamaño de la muestra','Z-Calculado','Z-Crítico','Conclusión'],
    'valores':[mu_0,x_bar,s,n,z,z_critical,'Rechazar la hipótesis nula' if z > z_critical else 'No rechazar la hipótesis nula']
})
print(df)