import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
df=pd.read_csv("C:\\Users\\isaac\\Downloads\\ejercicio_1_zonas_entrega.csv")
print(df.head())
plt.figure(figsize=(8, 6))
plt.scatter(df["X"], df["Y"], color="steelblue", s=100, alpha=0.8, edgecolors="black")
plt.title("Puntos de Entrega (Sin Clasificar)", fontsize=14)
plt.xlabel("Coordenada X", fontsize=12)
plt.ylabel("Coordenada Y", fontsize=12)
plt.grid(True)
plt.tight_layout()
plt.show()
coords=df[["X", "Y"]].values
coords_normalized=StandardScaler().fit_transform(coords)
dbscan=DBSCAN(eps=0.8, min_samples=3)
clusters=dbscan.fit_predict(coords_normalized)
df["Cluster"] = clusters
print(df)
plt.figure(figsize=(10, 7))
colors = {-1: "red",0: "blue",1: "green",2: "orange"}
for cluster, grupo in df.groupby("Cluster"):
    plt.scatter(
        grupo["X"], grupo["Y"],
        color=colors[cluster],
        label=f"Cluster {cluster}" if cluster != -1 else "Ruido",
        s=150,
        alpha=0.7
    )
plt.title("Zonas de Entrega con DBSCAN (eps=0.8, min_samples=3)", fontsize=14)
plt.xlabel("Coordenada X", fontsize=12)
plt.ylabel("Coordenada Y", fontsize=12)
plt.legend()
plt.grid(True)
plt.show()
#¿Cuántas zonas de entrega identificó el algoritmo?
#El algoritmo identificó 3 zonas de entrega (Cluster 0, Cluster 1 y Cluster 2)
#y clasificó algunos puntos como ruido (Cluster -1). 
