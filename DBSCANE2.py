from matplotlib import colors
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
df=pd.read_csv("C:\\Users\\isaac\\Downloads\\ejercicio_2_sensores_ambientales.csv")
df=df.rename(columns={"Temperatura_C": "Temperatura", "Humedad_pct": "Humedad"})
print(df.head())
datos=df[["Temperatura", "Humedad"]].values
datos_normalized=StandardScaler().fit_transform(datos)
k=2
nn=NearestNeighbors(n_neighbors=k)
nn.fit(datos_normalized)
distancias, _=nn.kneighbors(datos_normalized)
distancias_k=np.sort(distancias[:, -1])[::-1]
plt.figure(figsize=(9, 5))
plt.plot(range(1, len(distancias_k) + 1), distancias_k,
         color="royalblue", linewidth=2, marker="o", markersize=5)
plt.title("Gráfico k-Distancia para Selección de eps\n(k=2, min_samples=3)", fontsize=14)
plt.xlabel("Puntos ordenados (mayor a menor distancia)", fontsize=12)
plt.ylabel(f"Distancia al vecino {k}°", fontsize=12)
plt.legend(fontsize=11)
plt.grid(True)
plt.show()
dbscan=DBSCAN(eps=0.8, min_samples=3)
clusters=dbscan.fit_predict(datos_normalized)
df["Cluster"] = clusters
print(df)
colores = {-1: "red",0: "blue",1: "green",2: "orange"}
for cluster, grupo in df.groupby("Cluster"):
    plt.scatter(
        grupo["Temperatura"], grupo["Humedad"],
        color=colores[cluster],
        label=f"Cluster {cluster}" if cluster != -1 else "Ruido",
        s=150,
        alpha=0.75
   )
plt.title("Segmentación de Sensores — DBSCAN (eps=0.8, min_samples=3)", fontsize=14)
plt.xlabel("Temperatura (°C)", fontsize=12)
plt.ylabel("Humedad (%)", fontsize=12)
plt.legend(fontsize=10)
plt.grid(True)
plt.show()
#¿K-Means hubiera detectado las anomalías? ¿Por qué sí o no?
#No, ya que K-Means es sensible a los puntos atípicos y los asignaría a un cluster,
#mientras que DBSCAN los clasifica como ruido (Cluster -1).