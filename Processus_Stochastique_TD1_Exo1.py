import numpy as np


#matrice de transition
matrice_transistion= np.array([[0.7, 0.2, 0.1], [0.5, 0.3, 0.2], [0.4, 0.3, 0.3]])
#etat initial ensoleilée 
etat_intitial_soleil= np.array([[1], [0], [0]])
#matrice de transition pour avoir l'état dans deux jours
matrice_carré = matrice_transistion.dot(matrice_transistion)

#etat dans deux jours
etat_apr_2j= np.transpose(etat_intitial_soleil).dot(matrice_carré)


def simulation (n_jours) : 

    #les état initiaux possible
    etat_intitial_soleil= np.array([[1], [0], [0]])
    etat_intitial_nuageux= np.array([[0], [1], [0]])
    etat_intitial_pluvieux= np.array([[0], [0], [1]])

    matrice_transistion= np.array([[0.7, 0.2, 0.1], [0.5, 0.3, 0.2], [0.4, 0.3, 0.3]])

    jours = list(range(n_jours))

    etat_intitial = etat_intitial_soleil

    if np.all(etat_intitial == etat_intitial_soleil) : 

        for i in jours :

            #etat aprres n jours
            etat_apr_n_jours = np.transpose(etat_intitial).dot(np.linalg.matrix_power(matrice_transistion, i))
            print("Matrice  : ", etat_apr_n_jours)

    if np.all(etat_intitial == etat_intitial_nuageux) :

        for i in jours :

            #etat aprres n jours
            etat_apr_n_jours = np.transpose(etat_intitial).dot(np.linalg.matrix_power(matrice_transistion, i))
            print("Matrice  : ", etat_apr_n_jours)

    if np.all(etat_intitial == etat_intitial_pluvieux):  

        for i in jours :

            #etat aprres n jours
            etat_apr_n_jours = np.transpose(etat_intitial).dot(np.linalg.matrix_power(matrice_transistion, i))
            print("Matrice  : ", etat_apr_n_jours)



simulation(20)


