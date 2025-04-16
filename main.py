import pandas as pd 

path='D:\\Documents\\VSCode\\Revue de perfo métro\\1_raw_data_metrologie.xlsx'
raw_data=pd.read_excel(path) 
clean_data=raw_data.copy()

clean_data.info()

clean_data.to_pickle("clean_data.pkl") #enregistre le df nettoyé dans un fichier pickle
