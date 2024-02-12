import joblib
import numpy as np


# Carica il modello addestrato
modello_random_forest = joblib.load('random_forest_model3.joblib')

# Prepara i dati di input (assumiamo che siano già codificati)
nuovi_dati_codificati = np.array([[2, 3, 1, 0, 2, 3, 3, 1]])  # Assicurati che le caratteristiche corrispondano all'one-hot encoding

# Fai previsioni utilizzando il modello
previsioni = modello_random_forest.predict(nuovi_dati_codificati)

# Stampa le previsioni
print("Previsioni:", previsioni)