#Ejercicio 5
import numpy as np
from scipy import stats
print("Ejercicio 5")
# 1) Datos: pesos de los sacos
pesos=np.array([495, 498, 502, 490, 497, 499, 501, 493, 496, 498, 492, 495, 500, 494, 496])
# 2) Valor hipotético bajo H0
mu0=500
# 3) Prueba t de una muestra
res=stats.ttest_1samp(pesos, mu0)
# 4) Extraer resultados
t_stat=res.statistic
p_value=res.pvalue
# 5) Nivel de significancia
alpha=0.05
# 6) Resultados
print("t =", t_stat)
print("p-value =", p_value)
if p_value<alpha:
    print("Rechazo H0; el peso promedio es diferente de 500 gramos.")
else:
    print("No rechazo H0; no hay evidencia suficiente para decir que el peso difiere de 500 gramos.")
#Ejercicio 6
print("Ejercicio 6")
# 1) Datos
gasolina_A=np.array([12.5, 13.2, 12.8, 14.0, 13.5, 12.9, 13.1])
gasolina_B=np.array([14.2, 15.0, 14.8, 13.9, 15.5, 14.7, 15.1])
# 2) Prueba t de dos muestras independientes
res=stats.ttest_ind(gasolina_A, gasolina_B, equal_var=False)
# 3) Resultados
t_stat=res.statistic
p_value=res.pvalue
# 4) Nivel de significancia
alpha=0.05
# 5) Imprimir resultados
print(f"t = {t_stat:.4f}")
print(f"p-value = {p_value:.4f}")
if p_value<alpha:
    print("Rechazo H0; existe diferencia significativa en el rendimiento.")
else:
    print("No rechazo H0; no hay evidencia suficiente de diferencia.")
#Ejercicio 7
print("Ejercicio 7")
# 1) Datos antes del fertilizante
antes=np.array([15.2, 16.0, 14.8, 15.5, 17.1, 16.4, 15.9, 16.2, 15.0, 15.7])
# 2) Datos después del fertilizante
despues=np.array([15.4, 16.1, 14.9, 15.6, 17.0, 16.5, 16.0, 16.3, 15.2, 15.8])
# 3) Prueba t pareada
res=stats.ttest_rel(antes, despues)
# 4) Resultados
t_stat=res.statistic
p_value=res.pvalue
# 5) Nivel de significancia
alpha=0.05
# 6) Mostrar resultados
print(f"t = {t_stat:.4f}")
print(f"p-value = {p_value:.4f}")
# 7) Decisión
if p_value<alpha:
    print("Rechazo H0; el fertilizante produjo un cambio significativo.")
else:
    print("No rechazo H0; no hay evidencia suficiente de cambio significativo.")