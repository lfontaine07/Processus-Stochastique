import numpy as np

def markov_chain(initial_state, transition_matrix, num_steps):
    current_state = initial_state
    chain = [current_state]

    for _ in range(num_steps):
        # Trouver les probabilités de transition pour l'état actuel
        transition_probabilities = transition_matrix[current_state]

        # Choisir le prochain état en fonction des probabilités de transition
        next_state = np.random.choice(range(len(transition_probabilities)), p=transition_probabilities)

        # Ajouter le prochain état à la chaîne
        chain.append(next_state)
        current_state = next_state

    return chain

def simulation(n_jours, initial_state, transition_matrix):
    jours = list(range(n_jours))

    etat_intitial = initial_state

    chain = markov_chain(etat_intitial, transition_matrix, n_jours)

    # Convertir les états en chaîne de caractères
    etats = ['Soleil', 'Pluie', 'Nuageux']

    etats_simules = [etats[state] for state in chain]

    # Afficher la chaîne simulée
    print(' '.join(etats_simules))

# Matrice de transition
matrice_transition = np.array([[0.7, 0.2, 0.1],
                                [0.5, 0.3, 0.2],
                                [0.4, 0.3, 0.3]])

# État initial (soleil)
initial_state = 0

# Nombre de jours à simuler
n_jours = 10

# Simulation de la chaîne de Markov
simulation(n_jours, initial_state, matrice_transition)