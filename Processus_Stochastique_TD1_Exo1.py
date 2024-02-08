import numpy as np


#matrice de transition
matrice_transistion= np.array([[0.7, 0.2, 0.1], [0.5, 0.3, 0.2], [0.4, 0.3, 0.3]])
#etat initial ensoleilée 
etat_intitial= np.array([[1], [0], [0]])
#matrice de transition pour avoir l'état dans deux jours
matrice_carré = matrice_transistion.dot(matrice_transistion)

#etat dans deux jours
etat_apr_2j= np.transpose(etat_intitial).dot(matrice_carré)

print(etat_apr_2j)
