import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
df=pd.read_csv("C:\\Users\\isaac\\Downloads\\ejercicio_3_fraude_bancario.csv")
print(df.head())
datos = df[["Monto", "Hora"]].values
datos_normalized=StandardScaler().fit_transform(datos)
k=2
nn=NearestNeighbors(n_neighbors=k)
nn.fit(datos_normalized)
distancias, _=nn.kneighbors(datos_normalized)
distancias_k=np.sort(distancias[:, -1])[::-1]
plt.figure(figsize=(9, 5))
plt.plot(range(1, len(distancias_k) + 1), distancias_k,color="steelblue", linewidth=2, marker="o", markersize=6)
plt.title("Gráfico k-Distancia para Selección de eps\n(k=2, min_samples=3)", fontsize=14)
plt.xlabel("Transacciones ordenadas (mayor a menor distancia)", fontsize=12)
plt.ylabel(f"Distancia al vecino {k}°", fontsize=12)
plt.legend(fontsize=11)
plt.grid(True)
plt.show()
dbscan=DBSCAN(eps=0.9, min_samples=3)
clusters=dbscan.fit_predict(datos_normalized)
df["Cluster"]=clusters
df["Etiqueta"]=df["Cluster"].apply(lambda c: "Sospechosa" if c == -1 else "Normal")
print(df)
plt.figure(figsize=(11, 7))
colores = {-1: "red", 0: "blue",1:"green"}
for cluster, grupo in df.groupby("Cluster"):
    plt.scatter(
        grupo["Monto"], grupo["Hora"],
        color=colores[cluster],
        label=f"Cluster {cluster}" if cluster != -1 else "Sospechosa",
        s=150,
        alpha=0.75
    )
plt.title("Detección de Fraude Bancario — DBSCAN (eps=0.9, min_samples=2)", fontsize=14)
plt.xlabel("Hora del Día (0–23 h)", fontsize=12)
plt.ylabel("Monto de la Transacción ($)", fontsize=12)
plt.xticks(range(0, 24))
plt.legend(fontsize=10)
plt.grid(True)
plt.show()
#¿Qué ventaja tiene DBSCAN sobre K-Means para detectar fraude?
#DBScan puede identificar transacciones atipicas como ruido, en cambio,
#K-Means, al ser mas sensible a los atipicos, los clasificaria en un Cluster.