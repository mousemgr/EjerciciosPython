import pandas as pd

# DataFrame. Creación de tablas en Pandas
df = pd.DataFrame({'columna1':[1,2,3,4,5],
                   'columna2':['a','e','i','o','u']})
print(df)

url = 'http://apmonitor.com/che263/uploads/Main/tclab.txt'
y = pd.read_csv(url) #Lee e importa bases de datos en formato csv
# print(y)
print(y.head()) #Primeros 5 renglones

x = pd.read_csv('Calificaciones.csv')
print(x)