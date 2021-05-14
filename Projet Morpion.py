# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:33:29 2021

@author: Antoine
"""
import numpy as np
import time

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


def applique_coup(grille, coup,modifier = False):
    if modifier:
        grille[coup[0]][coup[1]] = coup[2]
    copie_grille = np.copy(grille)
    copie_grille[coup[0]][coup[1]] = coup[2]
    return copie_grille


# vérifie si la partie est terminée
def partie_terminee(s):
    flag = True
    for i in range(s.shape[0]):
        for j in range(s.shape[1]):
            if s[i][j] is None:
                flag = False
    if not flag:
        for j in range(s.shape[1]):
            # colonnes
            for i in range(s.shape[0] - 3):
                flag_temp = True
                if ((s[i][j] != s[i + 1][j]) or (s[i + 1][j] != s[i + 2][j]) or (s[i + 2][j] != s[i + 3][j])) or (
                        s[i][j] is None):
                    flag_temp = False
                flag = flag or flag_temp
        if not flag:
            for i in range(s.shape[0]):
                # lignes
                for j in range(s.shape[1] - 3):
                    flag_temp = True
                    if ((s[i][j] != s[i][j + 1]) or (s[i][j + 1] != s[i][j + 2]) or (s[i][j + 2] != s[i][j + 3])) or (
                            s[i][j] is None):
                        flag_temp = False
                    flag = flag or flag_temp
            if not flag:
                for ligne in range(s.shape[0] - 3):
                    # print("ligne",ligne)
                    for i in range(min(s.shape[0] - 3 - ligne, s.shape[1] - 3 - ligne)):
                        # print(i)
                        flag_temp = True
                        if ((s[ligne + i][i] != s[ligne + i + 1][i + 1]) or (
                                s[ligne + i + 1][i + 1] != s[ligne + i + 2][i + 2]) or (
                                    s[ligne + i + 2][i + 2] != s[ligne + i + 3][i + 3])) or (s[ligne + i][i] == None):
                            flag_temp = False
                        flag = flag or flag_temp
                if not flag:
                    stemp = np.rot90(s)
                    for ligne in range(stemp.shape[0] - 3):
                        for i in range(min(stemp.shape[0] - 3 - ligne, stemp.shape[1] - 3 - ligne)):
                            flag_temp = True
                            if ((stemp[ligne + i][i] != stemp[ligne + i + 1][i + 1]) or (
                                    stemp[ligne + i + 1][i + 1] != stemp[ligne + i + 2][i + 2]) or (
                                        stemp[ligne + i + 2][i + 2] != stemp[ligne + i + 3][i + 3])) or (
                                    stemp[ligne + i][i] is None):
                                flag_temp = False
                            flag = flag or flag_temp
    # print(flag)
    return flag


def voisins(grille, x, y):
    res = 0
    val = grille[x][y]
    if x + 1 < taille:
        if grille[x + 1][y] == val:
            res += 1
    if y + 1 < taille:
        if grille[x][y + 1] == val:
            res += 1
    if x + 1 < taille and y + 1 < taille:
        if grille[x + 1][y + 1] == val:
            res += 1
    if x - 1 >= 0:
        if grille[x - 1][y] == val:
            res += 1
    if y - 1 >= 0:
        if grille[x][y - 1] == val:
            res += 1
    if x - 1 >= 0 and y - 1 >= 0:
        if grille[x - 1][y - 1] == val:
            res += 1
    if x - 1 >= 0 and y + 1 < taille:
        if grille[x - 1][y + 1] == val:
            res += 1
    if y - 1 >= 0 and x + 1 < taille:
        if grille[x + 1][y - 1] == val:
            res += 1
    return res

def absence_voisins(grille, x, y):
    res = 0
    if x + 1 < taille:
        if grille[x + 1][y] == symbole_joueur or grille[x + 1][y]==symbole_ordinateur:
            res += 1
    if y + 1 < taille:
        if grille[x][y + 1] == symbole_joueur or grille[x][y + 1]==symbole_ordinateur:
            res += 1
    if x + 1 < taille and y + 1 < taille:
        if grille[x + 1][y + 1] == symbole_joueur or grille[x + 1][y + 1]==symbole_ordinateur:
            res += 1
    if x - 1 >= 0:
        if grille[x - 1][y] == symbole_joueur or grille[x - 1][y]==symbole_ordinateur:
            res += 1
    if y - 1 >= 0:
        if grille[x][y - 1] == symbole_joueur or grille[x][y - 1]==symbole_ordinateur:
            res += 1
    if x - 1 >= 0 and y - 1 >= 0:
        if grille[x - 1][y - 1] == symbole_joueur or grille[x - 1][y - 1]==symbole_ordinateur:
            res += 1
    if x - 1 >= 0 and y + 1 < taille:
        if grille[x - 1][y + 1] == symbole_joueur or grille[x - 1][y + 1]==symbole_ordinateur:
            res += 1
    if y - 1 >= 0 and x + 1 < taille:
        if grille[x + 1][y - 1] == symbole_joueur or grille[x + 1][y - 1]==symbole_ordinateur:
            res += 1
    return res

def cases_jouables_interessantes(grille):
    tableau = cases_jouables(grille)
    res = []
    for coup in tableau:
        if absence_voisins(grille, coup[0],coup[1]) >0:
            res.append(coup)
    return res

def evaluation_grille(grille):
    res = 0
    flag = False
    if len(cases_jouables(grille)) == taille * taille:
        flag = True
    for j in range(grille.shape[1]):
        # colonnes
        for i in range(grille.shape[0] - 3):
            flagTemp = True
            if ((grille[i][j] != grille[i + 1][j]) or (grille[i + 1][j] != grille[i + 2][j]) or (grille[i + 2][j] != grille[i + 3][j])) or (
                    grille[i][j] == None):
                flagTemp = False
            if flagTemp:
                if grille[i][j] == symbole_ordinateur:
                    res = 1
                else:
                    res = -1
            flag = flag or flagTemp
    if not flag:
        for i in range(grille.shape[0]):
            # lignes
            # flagTemp = True
            for j in range(grille.shape[1] - 3):
                flagTemp = True
                if ((grille[i][j] != grille[i][j + 1]) or (grille[i][j + 1] != grille[i][j + 2]) or (grille[i][j + 2] != grille[i][j + 3])) or (
                        grille[i][j] == None):
                    flagTemp = False
                if flagTemp:
                    if grille[i][j] == symbole_ordinateur:
                        res = 1
                    else:
                        res = -1
                flag = flag or flagTemp
        if not flag:
            for ligne in range(grille.shape[0] - 3):
                # print("ligne",ligne)
                for i in range(min(grille.shape[0] - 3 - ligne, grille.shape[1] - 3 - ligne)):
                    # print(i)
                    flagTemp = True
                    if ((grille[ligne + i][i] != grille[ligne + i + 1][i + 1]) or (
                            grille[ligne + i + 1][i + 1] != grille[ligne + i + 2][i + 2]) or (
                                grille[ligne + i + 2][i + 2] != grille[ligne + i + 3][i + 3])) or (grille[ligne + i][i] == None):
                        flagTemp = False
                    if flagTemp:
                        if grille[ligne + i][i] == symbole_ordinateur:
                            res = 1
                        else:
                            res = -1
                    flag = flag or flagTemp
            if not flag:
                stemp = np.rot90(grille)
                for ligne in range(stemp.shape[0] - 3):
                    for i in range(min(stemp.shape[0] - 3 - ligne, stemp.shape[1] - 3 - ligne)):
                        flagTemp = True
                        if ((stemp[ligne + i][i] != stemp[ligne + i + 1][i + 1]) or (
                                stemp[ligne + i + 1][i + 1] != stemp[ligne + i + 2][i + 2]) or (
                                    stemp[ligne + i + 2][i + 2] != stemp[ligne + i + 3][i + 3])) or (
                                stemp[ligne + i][i] == None):
                            flagTemp = False
                        if flagTemp:
                            if stemp[ligne + i][i] == symbole_ordinateur:
                                res = 1
                            else:
                                res = -1
                        flag = flag or flagTemp
    if res == 0 and not flag:
        for i in cases_jouables(grille):
            if partie_terminee(applique_coup(grille, i + [symbole_ordinateur])):
                if evaluation_grille(applique_coup(grille, i + [symbole_ordinateur])) == 1:
                    res = 0.99
                elif evaluation_grille(applique_coup(grille, i + [symbole_joueur])) == -1:
                    res = -0.99
        if res == 0:
            nbv = 0

            for i in range(taille):
                for j in range(taille):
                    # print(i,j)
                    if grille[i][j] is not None:
                        nbv += voisins(grille, i, j)
            res = nbv / ((taille * taille - len(cases_jouables(grille))) * 100)
    return res


def minimax(grille, ordinateur, alpha, beta,profondeur):
    # print(Morpion(x=12, y=12, grille=grille))
    if partie_terminee(grille) or profondeur<1:
        # print(evaluation_grille(grille))
        return evaluation_grille(grille)
    elif ordinateur:
        max_evaluation = - np.Inf
        for coup in cases_jouables_interessantes(grille):
            copie_grille = np.copy(grille)
            coup.append(symbole_ordinateur)
            evaluation = minimax(applique_coup(copie_grille, coup), False, alpha, beta,profondeur-1)
            alpha = max(alpha, evaluation)
            max_evaluation = max(max_evaluation,evaluation)
            if beta <= alpha:
                break
        return max_evaluation
    else:
        min_evaluation = np.Inf
        for coup in cases_jouables_interessantes(grille):
            copie_grille = np.copy(grille)
            coup.append(symbole_joueur)
            evaluation = minimax(applique_coup(copie_grille, coup), True, alpha, beta,profondeur-1)
            min_evaluation = min(min_evaluation,evaluation)
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
            if len(cases_jouables(mp.grille))== taille*taille:
                coup = [5,5]
            else:
                copie_grille = np.copy(mp.grille)
                valeure=-1000
                for i in cases_jouables_interessantes(copie_grille):
                    minimax_valeure = minimax(copie_grille, True, - np.Inf, np.Inf,3)
                    if valeure <= minimax_valeure:
                        valeure = minimax_valeure
                        coup = i
            print("\nMon coup (⌐■_■) :", coup, "\n")
            applique_coup(mp.grille, coup+[symbole_ordinateur],True)
            print(mp)
            tour_ordinateur = not tour_ordinateur
            print("Temps de réfléxion: ",time.time()-t)
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
    taille = 12
    morpion = Morpion(x=taille, y=taille)
    # morpion.grille = (np.array([['X','X','O','X',None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]]))
    # print(len(cases_jouables(morpion.grille)))
    # print((cases_jouables_interessantes(morpion.grille)))
    jeu(morpion)
