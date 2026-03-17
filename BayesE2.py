from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
data={
    'titular':[
        "equipo gana campeonato",
        "nuevo telefono inteligente",
        "jugador anota gol decisivo",
        "empresa lanza nueva computadora",
        "equipo gana torneo"
    ],
    'categoria':[
        "deportes",
        "tecnologia",
        "deportes",
        "tecnologia",
        "deportes"
    ]
}
df=pd.DataFrame(data)
vectorizador=CountVectorizer()
X=vectorizador.fit_transform(df['titular'])
y=df['categoria']
modelo=MultinomialNB()
modelo.fit(X,y)
#Probar modelo
nueva_resena=["nuevo equipo gana"]
X_nueva=vectorizador.transform(nueva_resena)
prediccion=modelo.predict(X_nueva)
print(prediccion)