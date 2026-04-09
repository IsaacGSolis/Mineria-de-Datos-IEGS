import numpy as np
from scipy import stats
#Ejercicio 1
print("Ejercicio 1")
print("H0: El contenido promedio de las botellas es 500 ml")
print("H1: El contenido promedio de las botellas es diferente de 500 ml")
muestra_agua=np.array([498, 501, 499, 502, 500, 497, 503, 499, 501, 500])
mu0=500
res=stats.ttest_1samp(muestra_agua, mu0)
t_stat=res.statistic
p_value=res.pvalue
alpha=0.05
print(f"t = {t_stat:.4f}")
print(f"p-value = {p_value:.4f}")
if p_value<alpha:
    print("Rechazo H0; el contenido de las botellas difiere de 500 ml.")
else:
    print("No rechazo H0; no hay evidencia suficiente para decir que el contenido difiere de 500 ml.")
#Ejercicio 2
print("Ejercicio 2")
print("H0: No existe diferencia en las calificaciones promedio entre los grupos")
print("H1: Existe diferencia en las calificaciones promedio entre los grupos")
grupo_musica=np.array([65, 70, 68, 72, 66, 69, 71, 67, 70, 68])
grupo_silencio=np.array([85, 88, 90, 87, 92, 86, 89, 91, 88, 90])
res=stats.ttest_ind(grupo_musica, grupo_silencio, equal_var=False)
t_stat=res.statistic
p_value=res.pvalue
alpha=0.01
print(f"t = {t_stat:.4f}")
print(f"p-value = {p_value:.4f}")
if p_value<alpha:
    print("Rechazo H0; existe diferencia significativa en las calificaciones.")
else:
    print("No rechazo H0; no hay evidencia suficiente de diferencia en las calificaciones.")
#Ejercicio 3
print("Ejercicio 3")
print("H0: La distribución de estudiantes por carrera es igual a la histórica")
print("H1: La distribución de estudiantes por carrera es diferente a la histórica")
observadas=np.array([200, 120, 80])
p=np.array([0.40,0.35,0.25])
n=observadas.sum()
esperadas=n*p
res=stats.chisquare(f_obs=observadas,f_exp=esperadas)
chi2=res.statistic
p_value=res.pvalue
gl=len(observadas)-1
print(f"Frecuencias observadas: {observadas}")
print(f"Frecuencias esperadas: {esperadas}")
print(f"Chi-cuadrado={chi2:.4f}")
print(f"Grados de libertad={gl}")
print(f"p-value={p_value:.4f}")
alpha=0.05
if p_value < alpha:
    print("Rechazo H0; la distribución de estudiantes por carrera difiere de la histórica.")
else:
    print("No rechazo H0; la distribución de estudiantes por carrera no difiere de la histórica.")