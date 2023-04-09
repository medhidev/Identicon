# Projet Identicon
# v1.0 - Test

# import du module aléatoire
import random

def creeCube(n, m):
    matrice = [[ random.randint(0, 1) for x in range(m)] for y in range(n)]
    return matrice

def printCube(matrice):
    n = len(matrice)
    m = len(matrice[0])

    for i in range(n):
        for j in range(m):
            print(matrice[i][j],end=" ")

        #saut de ligne
        print(" ")

def coloration(matrice):
    n = len(matrice)
    m = len(matrice[0])

    for i in range(n):
        for j in range(m):
            if matrice[i][j] == 1:
                print('\u25a0', end=" ")
            else:
                print('\u25a1', end=" ")
        print("")


# def symetrieCube():
#     # Système de symétrie
#     return 


def main():
    '''
    Gestion de la taille (plus tard)
    '''
    # default value
    largeur = ''
    longueur = ''
    changeur = 0
    size = ''

    while(size == ''):
        size = input('dimension du cube (avec Longeur;largeur): ')
        for i in (size):
            if (i == ';'):
                changeur += 1
            elif (changeur == 1):
                largeur += i
            else:
                longueur += i

    cube = creeCube(int(longueur), int(largeur))
    # printCube(cube)
    coloration(cube)

main()