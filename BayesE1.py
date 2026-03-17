from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
data={
    'resena':[
        "el producto funciona excelente",
        "muy buena calidad",
        "el producto llego dañado",
        "muy mala calidad",
        "excelente producto y calidad",
        "producto de mala calidad"
    ],
    'clacificacion':[
        "satisfecho",
        "satisfecho",
        "insatisfecho",
        "insatisfecho",
        "satisfecho",
        "insatisfecho"
    ]
}
df=pd.DataFrame(data)
vectorizador=CountVectorizer()
X=vectorizador.fit_transform(df['resena'])
y=df['clacificacion']
modelo=MultinomialNB()
modelo.fit(X,y)
#Probar modelo
nueva_resena=["producto mala calidad"]
X_nueva=vectorizador.transform(nueva_resena)
prediccion=modelo.predict(X_nueva)
print(prediccion)