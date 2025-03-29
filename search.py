#!/bin/python3

import subprocess

def lire_mots_utilisateur():
    print("Entrez les mots à rechercher, un par ligne. Appuyez sur Entrée après chaque mot. Laissez une ligne vide pour terminer :")

    mots = []
    while True:
        mot = input()
        if mot == "":
            break
        mots.append(mot)

    return mots

def rechercher_fichiers_avec_mots(mots):
    for mot in mots:
        print(f"Recherche de fichiers contenant '{mot}' :")

        # Construire et exécuter la commande find
        commande = ['find', '.', '-name', f'*{mot}*']
        resultat = subprocess.run(commande, capture_output=True, text=True)

        # Vérifier si la commande a réussi
        if resultat.returncode == 0:
            # Afficher les résultats
            print(resultat.stdout)
        elif resultat.stdout == "":
                print('Auncune correspondance')
        else:
            # Afficher l'erreur
            print("Erreur lors de la recherche :")
            print(resultat.stderr)

# Exemple d'utilisation
mots = lire_mots_utilisateur()
rechercher_fichiers_avec_mots(mots)

