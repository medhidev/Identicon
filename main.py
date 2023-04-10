# Projet Identicon
# v1.0 - Test

# import du module aléatoire
import random

def creeCube(n, m):
    matrice = [[ random.randint(0, 1) for x in range(m)] for y in range(n)]
    return matrice

# Pour les test
# def printCube(matrice):
#     n = len(matrice)
#     m = len(matrice[0])

#     for i in range(n):
#         for j in range(m):
#             print(matrice[i][j],end=" ")

#         #saut de ligne
#         print(" ")

def coloration(matrice):
    n = len(matrice)
    m = len(matrice[0])

    for i in range(n):
        for j in range(m):
            if (j < m//2):
                print('\u25a1', end=" ")
            else:
                if matrice[i][j] == 1:
                    # ■
                    print('\u25a0', end=" ")
                else:
                    # □
                    print('\u25a1', end=" ")

        print("")


def symetrieCube(matrice):
    n = len(matrice)
    midsize = len(matrice[0])//2

    for i in range(n):
        for j in range(midsize):
            print('\u25a1', end=" ")
        print("")


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
        size = input('dimension du cube (avec L;l paire): ')
        for i in (size):
            if (i == ';'):
                changeur += 1
            elif (changeur == 1):
                largeur += i
            else:
                longueur += i

        # if(int(longueur + largeur)%2 != 0):
        #     print('Erreur, les dimension ne sont pas paire')
        #     size = ''

        # if(int(longueur) != int(largeur)):
        #     size = ''
        #     print('Erreur, les dimensions doivent être les mêmes')
        
        # print(f'L={longueur}; l={largeur}')

    cube = creeCube(int(longueur), int(largeur))
    # printCube(cube)
    coloration(cube)
    # symetrieCube(cube)

main()