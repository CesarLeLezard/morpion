# -*- coding: utf-8 -*-
"""
Created on Wed May  5 10:33:29 2021

@author: Antoine
"""
import numpy as np


class Morpion:
	def __init__(self,tab=None):
		if (tab ==None)or tab.shape!=(12,12):
			self.tab= np.full((12,12),None)
		else:
			self.tab = tab

	def __str__(self):
		msg = ""
		for i in range(self.tab.shape[0]):
			for j in range(self.tab.shape[1]):
	 			if self.tab[i][j] == None:
					 msg += " _ "
	 			else:
					 msg += " "+str(self.tab[i][j])+" "
			msg += "\n"
		return msg

	def __repr__(self):
		return str(self)

def Action(s):
	l = []
	for i in range(s.shape[0]):
		for j in range(s.shape[1]):
			if s[i][j] == None:
				l.append([i,j])
	return l

def Result(s,a):
	sbis = np.copy(s)
	sbis[a[0]][a[1]]=a[2]
	return sbis

def Terminal_Test(s):
	flag = True
	for i in range(s.shape[0]):
		for j in range(s.shape[1]):
			if s[i][j] == None:
				flag = False
	if not flag:
		for j in range(s.shape[1]):
			#colonnes
			for i in range(s.shape[0]-3):
				flagTemp = True
				if ((s[i][j]!=s[i+1][j])or(s[i+1][j]!=s[i+2][j])or(s[i+2][j]!=s[i+3][j]))or(s[i][j]==None):
					flagTemp = False
				flag = flag	or flagTemp
		if not flag :
			for i in range(s.shape[0]):
				#lignes
# 				flagTemp = True
				for j in range(s.shape[1]-3):
					flagTemp = True
					if ((s[i][j]!=s[i][j+1])or(s[i][j+1]!=s[i][j+2])or(s[i][j+2]!=s[i][j+3]))or(s[i][j]==None):
						flagTemp = False
					flag = flag or flagTemp
			if not flag :
				flagTemp = True
				for ligne in range(s.shape[0]-3):
# 					print("ligne",ligne)
					for i in range(min(s.shape[0]-3-ligne,s.shape[1]-3-ligne)):
# 						print(i)
						flagTemp = True
						if ((s[ligne+i][i]!=s[ligne+i+1][i+1])or(s[ligne+i+1][i+1]!=s[ligne+i+2][i+2])or(s[ligne+i+2][i+2]!=s[ligne+i+3][i+3]))or(s[ligne+i][i]==None):
							flagTemp = False
						flag = flag or flagTemp
				if not flag:
					flagTemp = True
					stemp = np.rot90(s)
					for ligne in range(stemp.shape[0]-3):
						for i in range(min(stemp.shape[0]-3-ligne,stemp.shape[1]-3-ligne)):
							flagTemp = True
							if ((stemp[ligne+i][i]!=stemp[ligne+i+1][i+1])or(stemp[ligne+i+1][i+1]!=stemp[ligne+i+2][i+2])or(stemp[ligne+i+2][i+2]!=stemp[ligne+i+3][i+3]))or(stemp[ligne+i][i]==None):
								flagTemp = False
							flag = flag or flagTemp
	return flag

def Voisins(s,x,y):
	res = 0
	val = s[x][y]
	if x+1<12:
		if s[x+1][y]==val:
			res+=1
		s[x+1][y] = 'null'
	if y+1<12:
		if s[x][y+1]==val:
			res +=1
		s[x][y+1] = 'null'
	if x+1<12 and y+1<12:
		if s[x+1][y+1]==val:
			res +=1
		s[x+1][y+1]= 'null'
	if x-1>=0:
		if s[x-1][y]==val:
			res+=1
		s[x-1][y]='null'
	if y-1>=0:
		if s[x][y-1]==val:
			res +=1
		s[x][y-1]='null'
	if x-1>=0 and y-1>=0:
		if s[x-1][y-1]==val:
			res +=1
		s[x-1][y-1]='null'
	return res

def Utility(s,symbole ="X",symbloleAdversaire="O"):
	res = 0
	flag = False
	for j in range(s.shape[1]):
			#colonnes
			for i in range(s.shape[0]-3):
				flagTemp = True
				if ((s[i][j]!=s[i+1][j])or(s[i+1][j]!=s[i+2][j])or(s[i+2][j]!=s[i+3][j]))or(s[i][j]==None):
					flagTemp = False
				if flagTemp :
					if s[i][j] == symbole:
						res = 1
					else:
						res = -1
				flag = flag	or flagTemp
	if not flag:
		for i in range(s.shape[0]):
				#lignes
# 				flagTemp = True
				for j in range(s.shape[1]-3):
					flagTemp = True
					if ((s[i][j]!=s[i][j+1])or(s[i][j+1]!=s[i][j+2])or(s[i][j+2]!=s[i][j+3]))or(s[i][j]==None):
						flagTemp = False
					if flagTemp:
						if s[i][j]==symbole:
							res = 1
						else:
							res = -1
					flag = flag or flagTemp
		if not flag:
			flagTemp = True
			for ligne in range(s.shape[0]-3):
# 					print("ligne",ligne)
				for i in range(min(s.shape[0]-3-ligne,s.shape[1]-3-ligne)):
# 						print(i)
					flagTemp = True
					if ((s[ligne+i][i]!=s[ligne+i+1][i+1])or(s[ligne+i+1][i+1]!=s[ligne+i+2][i+2])or(s[ligne+i+2][i+2]!=s[ligne+i+3][i+3]))or(s[ligne+i][i]==None):
						flagTemp = False
					if flagTemp:
						if s[ligne+i][i]==symbole:
							res = 1
						else:
							res = -1
					flag = flag or flagTemp
			if not flag:
				flagTemp = True
				stemp = np.rot90(s)
				for ligne in range(stemp.shape[0]-3):
					for i in range(min(stemp.shape[0]-3-ligne,stemp.shape[1]-3-ligne)):
						flagTemp = True
						if ((stemp[ligne+i][i]!=stemp[ligne+i+1][i+1])or(stemp[ligne+i+1][i+1]!=stemp[ligne+i+2][i+2])or(stemp[ligne+i+2][i+2]!=stemp[ligne+i+3][i+3]))or(stemp[ligne+i][i]==None):
							flagTemp = False
						if flagTemp:
							if stemp[ligne+i][i]==symbole:
								res = 1
							else:
								res = -1
						flag = flag or flagTemp
	if res == 0:
		for i in Action(s):
			if Utility(Result(s, i+[symbole]),symbole)==1:
				res = 0.99
			if Utility(Result(s,i+[symbloleAdversaire]),symbloleAdversaire)==-1:
				res = -0.99
# 		if res == 0:

	return res

def MinMax(s,listedecoup = list([]),symbole="X",symboleAdversaire="O"):
	if Terminal_Test(s):
			return Utility(s,symbole),listedecoup
	elif (np.count_nonzero(s == symbole))<=(np.count_nonzero(s == symboleAdversaire)):
		sbis = np.copy(s)
		print(sbis,Action(sbis)[0])
		coup = Action(sbis)[0]+[symbole]
		extr = MinMax(Result(sbis,coup),listedecoup+coup)
		print(extr)
		for i in Action(s):
			sbis = np.copy(s)
			coup = i+[symbole]
			if MinMax(Result(sbis,coup),listedecoup+(coup))[0]>extr[0]:
				extr = MinMax(Result(s,i+[symbole]),listedecoup+i+[symbole])
		return extr
	else :
		extr = MinMax(Result(s,Action(s)[0]+[symboleAdversaire]),listedecoup+Action(s)[0]+[symboleAdversaire])
		for i in Action(s):
			if MinMax(Result(s,i+[symboleAdversaire]),listedecoup+(i+[symboleAdversaire]))[0]<extr[0]:
				extr = MinMax(Result(s,i+[symboleAdversaire]),listedecoup+(i+[symboleAdversaire]))
		return extr

def Jeu(mp,symboleOrdi="X",symboleAdversaire="O",ordinateurcommence =True):
	print("\nLe jeu commence ! \(^ヮ^)/\n~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print(mp)
	while not Terminal_Test(mp.tab):
		if ordinateurcommence:
			sbis = np.copy(mp.tab)
			coup = MinMax(sbis,[],symboleOrdi,symboleAdversaire)[1][0:3]
			print("\nMon coup (⌐■_■) :",coup,"\n")
			Result(mp.tab,coup)
			print(mp)
			ordinateurcommence = not ordinateurcommence
		else:
			print("\nA toi de jouer ヽ(♡‿♡)ノ \n")
			x = int(input("Ta ligne stp (つ✧ω✧)つ :"))
			y = int(input("Ta colonne maintenant (⌒_⌒;) :"))
			if mp.tab[x,y]==None:
				mp.tab = Result(mp.tab, [x,y] + [symboleAdversaire])
				print('\n',mp)
				ordinateurcommence = not ordinateurcommence
			else:
				print("\nTu n'as pas le droit tricheur ((╬◣﹏◢)) rejoue!")
	if Utility(mp.tab)==1:
		print("\nJ'ai gagné !!! 	＼(٥⁀▽⁀ )／ ")
	if Utility(mp.tab)==-1:
		print("\nTu as gagné 	(╯︵╰,)")



#%% Test de la fonction Terminal_test

mp = Morpion()
"""
mp.tab = Result(mp.tab,[1,2,'X'])
mp.tab = np.full((12,12),'X')
# mp.tab = Result(mp.tab,[2,3,None])
# mp.tab[2,3] = None
# print(mp.tab)
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = np.array([[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]])
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = (np.array([['X',None,None,None,None,None,None,None,None,None,None,None],['X',None,None,None,None,None,None,None,None,None,None,None],['X',None,None,None,None,None,None,None,None,None,None,None],['X',None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = (np.array([['O',None,None,None,None,None,None,None,None,None,None,None],['O',None,None,None,None,None,None,None,None,None,None,None],['O',None,None,None,None,None,None,None,None,None,None,None],['O',None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = (np.array([['X',None,None,None,None,None,None,None,None,None,None,None],['O',None,None,None,None,None,None,None,None,None,None,None],['X',None,None,None,None,None,None,None,None,None,None,None],['X',None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = (np.array([[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,'X'],[None,None,None,None,None,None,None,None,None,None,None,'X'],[None,None,None,None,None,None,None,None,None,None,None,'X'],[None,None,None,None,None,None,None,None,None,None,None,'X']]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = (np.array([[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,'X'],[None,None,None,None,None,None,None,None,None,None,None,'X'],[None,None,None,None,None,None,None,None,None,None,None,'X'],[None,None,None,None,None,None,None,None,None,None,None,'O']]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = (np.array([['X','X','X','X',None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
mp.tab = (np.array([['X','X','O','X',None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = (np.array([[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,'X','X','X','X']]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = (np.array([[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,'O','X','X','X']]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = (np.array([['X',None,None,None,None,None,None,None,None,None,None,None],[None,'X',None,None,None,None,None,None,None,None,None,None],[None,None,'X',None,None,None,None,None,None,None,None,None],[None,None,None,'X',None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = (np.array([['X',None,None,None,None,None,None,None,None,None,None,None],[None,'O',None,None,None,None,None,None,None,None,None,None],[None,None,'X',None,None,None,None,None,None,None,None,None],[None,None,None,'X',None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = (np.array([[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],['X',None,None,None,None,None,None,None,None,None,None,None],[None,'X',None,None,None,None,None,None,None,None,None,None],[None,None,'X',None,None,None,None,None,None,None,None,None],[None,None,None,'X',None,None,None,None,None,None,None,None]]))
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = np.array([[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,'X',None,None,None,None,None,None,None,None],[None,None,'X',None,None,None,None,None,None,None,None,None],[None,'X',None,None,None,None,None,None,None,None,None,None],['X',None,None,None,None,None,None,None,None,None,None,None]])
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = np.array([[None,None,None,'X',None,None,None,None,None,None,None,None],[None,None,'X',None,None,None,None,None,None,None,None,None],[None,'X',None,None,None,None,None,None,None,None,None,None],['X',None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]])
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
mp.tab = np.array([[None,None,None,'O',None,None,None,None,None,None,None,None],[None,None,'O',None,None,None,None,None,None,None,None,None],[None,'O',None,None,None,None,None,None,None,None,None,None],['O',None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]])
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
"""
#%% Finale
"""
mp.tab = np.array([[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]])
Jeu(mp)
"""
#%% Test basique 1
mp.tab = np.array([["X","X","X",None,None,None,None,None,None,None,None,None],["O","O","O",None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]])
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
#%% Test basique 2
"""
mp.tab = np.array([["O","O","O",None,None,None,None,None,None,None,None,None],["X","X","X",None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None],[None,None,None,None,None,None,None,None,None,None,None,None]])
print(mp)
print(Terminal_Test(mp.tab))
print(Utility(mp.tab))
print(MinMax(mp.tab))
"""