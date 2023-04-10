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

# def coloration(matrice):
#     n = len(matrice)
#     m = len(matrice[0])

#     for i in range(n):
#         for j in range(m):
            
#             if (j > m//2):
#                 # k -= 1
#                 if (matrice[n-1][j] == 1):
#                     print('\u25a1', end=" ")
#             else:
#                 if matrice[i][j] == 1:
#                     # ■
#                     print('\u25a0', end=" ")
#                     matrice[n-1][j] = 1
#                 else:
#                     # □
#                     print('\u25a1', end=" ")

#         print("")


# def symetrieCube(matrice):
#     n = len(matrice)
#     midsize = len(matrice[0])//2

#     for i in range(n):
#         for j in range(midsize):
#             print('\u25a1', end=" ")
#         print("")

def symetrie(matrice):
    n = len(matrice)
    m = len(matrice[0])

    symetrie = [[0 for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if (j >= m//2):
                symetrie[i][j] = matrice[i][m-j-1]
            else:
                symetrie[i][j] = matrice[i][j]

    return symetrie

def coloration(matrice):
    symetrique = symetrie(matrice)
    n = len(symetrique)
    m = len(symetrique[0])

    # couleur possible; Vert; Jaune; Bleu; Magenta; Cyan
    color = random.randint(31, 36)

    vide = '■'
    rempli = f"\033[{color}m■\033[37m"

    for i in range(n):
        for j in range(m):
            if symetrique[i][j] == 1:
                # carré noir
                print(rempli, end=" ")
            else:
                # carré blanc
                print(vide, end=" ")
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

    cube = creeCube(int(longueur), int(largeur))
    coloration(cube)


main()