import numpy as np


#matrice de transition
matrice_transistion= np.array([[0.7, 0.2, 0.1], [0.5, 0.3, 0.2], [0.4, 0.3, 0.3]])
#etat initial ensoleilée 
etat_intitial_soleil= np.array([[1], [0], [0]])
#matrice de transition pour avoir l'état dans deux jours
matrice_carré = matrice_transistion.dot(matrice_transistion)

#etat dans deux jours
etat_apr_2j= np.transpose(etat_intitial_soleil).dot(matrice_carré)



def chaine_markow(etat_initial, matrice_de_transition, n_jours) : 

    etat_actuel = etat_initial
    chaine = [etat_actuel]
    for _ in range (n_jours) : 

        proba = matrice_de_transition[etat_actuel]

        etat_suivant = np.random.choice(range(len(proba)), p=proba)
        chaine.append(etat_suivant)
        etat_actuel = etat_suivant

    return chaine


def simulation (etat_initial,n_jours,matrice_de_transition) : 

    #les état initiaux possible


    etats = ["Soleil" , "Pluie" , "Nuageux"]


    matrice_transistion= np.array([[0.7, 0.2, 0.1], [0.5, 0.3, 0.2], [0.4, 0.3, 0.3]])

    #python a besoin de bouger mais pas sur un entier
    jours = list(range(n_jours))

    index_etat = etats.index(etat_initial)

    chaine = chaine_markow(index_etat, matrice_de_transition, n_jours)

    simul_etat = [etats[state] for state in chaine]

    print(' '.join(simul_etat))

    #verifie les état initiales afin d'appliquer la chaine de markow a celle ci



etat_intitial_soleil= np.array([[1], [0], [0]])
etat_intitial_nuageux= np.array([[0], [1], [0]])
etat_intitial_pluvieux= np.array([[0], [0], [1]])



etat_initial = input( "Choisissez l'état initial entre Soleil/Pluie/Nuegeux : ").capitalize()
n_jours = int(input("Combien de jours voulez-vous simuler ? "))

if etat_initial not in ["Soleil", "Pluie", "Nuageux"] :

    print("Choix d'état invalide. ")

else : 

    matrice_transition= np.array([[0.7, 0.2, 0.1], [0.5, 0.3, 0.2], [0.4, 0.3, 0.3]])
    simulation(etat_initial, n_jours, matrice_transition)


