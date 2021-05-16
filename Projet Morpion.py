# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:33:29 2021

@author: Antoine
"""
import numpy as np
import time

compteur = 0
jeton = None


class Morpion:
    def __init__(self, x=12, y=12, grille=None):
        if (grille is None) or grille.shape != (x, y):
            self.grille = np.full((x, y), None)
        else:
            self.grille = grille

    def __str__(self):
        msg = ""
        for i in range(self.grille.shape[0]):
            for j in range(self.grille.shape[1]):
                if self.grille[i][j] is None:
                    msg += " _ "
                else:
                    msg += " " + str(self.grille[i][j]) + " "
            msg += "\n"
        return msg

    def __repr__(self):
        return str(self)


def cases_jouables(grille):
    cases = []
    for i in range(grille.shape[0]):
        for j in range(grille.shape[1]):
            if grille[i][j] is None:
                cases.append([i, j])
    return cases


def applique_coup(grille, coup, modifier=False):
    if modifier:
        grille[coup[0]][coup[1]] = coup[2]
    copie_grille = np.copy(grille)
    copie_grille[coup[0]][coup[1]] = coup[2]
    return copie_grille


def grille_remplie(grille):
    for i in range(grille.shape[0]):
        for j in range(grille.shape[1]):
            if grille[i][j] is None:
                return False
    return True


def test_colonne(grille):
    global jeton
    for j in range(grille.shape[1]):
        for i in range(grille.shape[0] - 3):
            if grille[i][j] is not None and grille[i][j] == grille[i + 1][j] and grille[i][j] == grille[i + 2][j] \
                    and grille[i][j] == grille[i + 3][j]:
                jeton = grille[i][j]
                return True
    return False


def test_ligne(grille):
    global jeton
    for i in range(grille.shape[0]):
        for j in range(grille.shape[1] - 3):
            if grille[i][j] is not None and grille[i][j] == grille[i][j + 1] and grille[i][j] == grille[i][j + 2] \
                    and grille[i][j] == grille[i][j + 3]:
                jeton = grille[i][j]
                return True
    return False


def test_diagonale(grille):
    global jeton
    for i in range(grille.shape[0] - 3):
        for j in range(grille.shape[1] - 3):
            if grille[i][j] is not None and grille[i][j] == grille[i + 1][j + 1] \
                    and grille[i][j] == grille[i + 2][j + 2] and grille[i][j] == grille[i + 3][j + 3]:
                jeton = grille[i][j]
                return True
    return False


def partie_terminee(grille):
    return grille_remplie(grille) or test_ligne(grille) or test_colonne(grille) or test_diagonale(grille) \
           or test_diagonale(np.rot90(grille))


def voisins_identiques(grille, x, y):
    res = 0
    val = grille[x][y]
    if x + 1 < taille:
        if grille[x + 1][y] == val or grille[x + 1][y] is None:
            res += 1
    if y + 1 < taille:
        if grille[x][y + 1] == val or grille[x][y + 1] is None:
            res += 1
    if x + 1 < taille and y + 1 < taille:
        if grille[x + 1][y + 1] == val or grille[x + 1][y + 1] is None:
            res += 1
    if x - 1 >= 0:
        if grille[x - 1][y] == val or grille[x - 1][y] is None:
            res += 1
    if y - 1 >= 0:
        if grille[x][y - 1] == val or grille[x][y - 1] is None:
            res += 1
    if x - 1 >= 0 and y - 1 >= 0:
        if grille[x - 1][y - 1] == val or grille[x - 1][y - 1] is None:
            res += 1
    if x - 1 >= 0 and y + 1 < taille:
        if grille[x - 1][y + 1] == val or grille[x - 1][y + 1] is None:
            res += 1
    if y - 1 >= 0 and x + 1 < taille:
        if grille[x + 1][y - 1] == val or grille[x + 1][y - 1] is None:
            res += 1
    return res


def nombre_voisins(grille, x, y):
    res = 0
    if x + 1 < taille:
        if grille[x + 1][y] == symbole_joueur or grille[x + 1][y] == symbole_ordinateur:
            res += 1
    if y + 1 < taille:
        if grille[x][y + 1] == symbole_joueur or grille[x][y + 1] == symbole_ordinateur:
            res += 1
    if x + 1 < taille and y + 1 < taille:
        if grille[x + 1][y + 1] == symbole_joueur or grille[x + 1][y + 1] == symbole_ordinateur:
            res += 1
    if x - 1 >= 0:
        if grille[x - 1][y] == symbole_joueur or grille[x - 1][y] == symbole_ordinateur:
            res += 1
    if y - 1 >= 0:
        if grille[x][y - 1] == symbole_joueur or grille[x][y - 1] == symbole_ordinateur:
            res += 1
    if x - 1 >= 0 and y - 1 >= 0:
        if grille[x - 1][y - 1] == symbole_joueur or grille[x - 1][y - 1] == symbole_ordinateur:
            res += 1
    if x - 1 >= 0 and y + 1 < taille:
        if grille[x - 1][y + 1] == symbole_joueur or grille[x - 1][y + 1] == symbole_ordinateur:
            res += 1
    if y - 1 >= 0 and x + 1 < taille:
        if grille[x + 1][y - 1] == symbole_joueur or grille[x + 1][y - 1] == symbole_ordinateur:
            res += 1
    return res


def cases_jouables_interessantes(grille):
    tableau = cases_jouables(grille)
    res = []
    for coup in tableau:
        if nombre_voisins(grille, coup[0], coup[1]) > 0:
            res.append(coup)
    return res


def evaluation_grille(grille):
    if jeton is not None:
        return notation[jeton]
    cases_interessantes = cases_jouables_interessantes(grille)
    nb_coup_critique = 0
    for case in cases_interessantes:
        grille2 = applique_coup(grille, case + [symbole_ordinateur])
        if test_ligne(grille2) or test_colonne(grille2) or test_diagonale(grille2) or test_diagonale(np.rot90(grille2)):
            nb_coup_critique += 1
    if nb_coup_critique > 0:
        if nb_coup_critique >= 2:
            return 0.99
        else:
            return 0.80
    for case in cases_interessantes:
        grille2 = applique_coup(grille, case + [symbole_joueur])
        if test_ligne(grille2) or test_colonne(grille2) or test_diagonale(grille2) or test_diagonale(np.rot90(grille2)):
            nb_coup_critique += 1
    if nb_coup_critique > 0:
        if nb_coup_critique >= 2:
            return -0.99
        else:
            return -0.80
    compteur_joueur = 0
    compteur_ordinateur = 0
    for i in range(grille.shape[0]):
        for j in range(grille.shape[1]):
            if grille[i, j] is not None:
                voisins_identiques_ou_nuls = voisins_identiques(grille, i, j)
                if grille[i, j] == symbole_ordinateur:
                    compteur_ordinateur += voisins_identiques_ou_nuls
                else:
                    compteur_joueur += voisins_identiques_ou_nuls
    return (compteur_ordinateur - compteur_joueur) / (grille.shape[0] * grille.shape[1] * 8)


def minimax(grille, ordinateur, alpha, beta, profondeur):
    global compteur
    global jeton
    jeton = None
    compteur += 1
    # print(compteur)
    if partie_terminee(grille) or profondeur < 1:
        return evaluation_grille(grille)
    elif ordinateur:
        max_evaluation = - np.Inf
        for coup in cases_jouables_interessantes(grille):
            coup.append(symbole_ordinateur)
            evaluation = minimax(applique_coup(grille, coup), False, alpha, beta, profondeur - 1)
            alpha = max(alpha, evaluation)
            max_evaluation = max(max_evaluation, evaluation)
            if beta <= alpha:
                break
        return max_evaluation
    else:
        min_evaluation = np.Inf
        for coup in cases_jouables_interessantes(grille):
            coup.append(symbole_joueur)
            evaluation = minimax(applique_coup(grille, coup), True, alpha, beta, profondeur - 1)
            min_evaluation = min(min_evaluation, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_evaluation


# commence la partie
def jeu(mp, tour_ordinateur=True):
    print("\nLe jeu commence ! \\(^ヮ^)/\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(mp)
    while not partie_terminee(mp.grille):
        if tour_ordinateur:
            t = time.time()
            coup = []
            if len(cases_jouables(mp.grille)) == taille * taille:
                coup = [taille // 2, taille // 2]
            else:
                valeur = - np.Inf
                print("Nombres de cases_jouables intéressantes : ", len(cases_jouables_interessantes(mp.grille)))
                for i in cases_jouables_interessantes(mp.grille):
                    minimax_valeur = minimax(applique_coup(mp.grille, i + [symbole_ordinateur]), False,
                                             - np.Inf, np.Inf, profondeur_minimax)
                    if valeur <= minimax_valeur:
                        print("minimax : ", minimax_valeur, i)
                        valeur = minimax_valeur
                        coup = i
            print("\nMon coup (⌐■_■) :", coup, "\n")
            applique_coup(mp.grille, coup + [symbole_ordinateur], True)
            print(mp)
            tour_ordinateur = not tour_ordinateur
            print("Temps de réflexion : ", time.time() - t)
        else:
            print("\nA toi de jouer ヽ(♡‿♡)ノ \n")
            x = int(input("Ta ligne stp (つ✧ω✧)つ :"))
            y = int(input("Ta colonne maintenant (⌒_⌒;) :"))
            if mp.grille[x, y] is None:
                mp.grille = applique_coup(mp.grille, [x, y, symbole_joueur])
                print('\n')
                print(mp)
                tour_ordinateur = not tour_ordinateur
            else:
                print("\nTu n'as pas le droit tricheur ((╬◣﹏◢)) rejoue!")
    if evaluation_grille(mp.grille) == 1:
        print("\nJ'ai gagné !!! 	＼(٥⁀▽⁀ )／ ")
    if evaluation_grille(mp.grille) == -1:
        print("\nTu as gagné 	(╯︵╰,)")


if __name__ == '__main__':
    symbole_joueur = "O"
    symbole_ordinateur = "X"
    notation = {symbole_ordinateur: 1, symbole_joueur: -1}
    taille = 12
    profondeur_minimax = 0
    morpion = Morpion(x=taille, y=taille)
    jeu(morpion)
