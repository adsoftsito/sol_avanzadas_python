import pandas as pd

datos = pd.read_csv('datos.csv')
print(datos)

wine_reviews = pd.read_csv("winemag-data-130k-v2.csv", index_col=0)
print('wines_reviews...')
print (wine_reviews.shape)
print (wine_reviews.head())

