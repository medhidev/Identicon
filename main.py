# Projet Identicon
# v1.1 - Test
# Ne marche que sur les terminale qui inclu les caractère ANSI

# import du module aléatoire
from PIL import Image, ImageDraw
import random

def creeCube(n, m):
    matrice = [[ random.randint(0, 1) for x in range(m)] for y in range(n)]
    return matrice

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
    longeur = len(symetrique) # longeur
    largeur = len(symetrique[0]) # largeur
    image = Image.new("RGB", (longeur, largeur), "white")
    draw = ImageDraw.Draw(image)

    # couleur possible; Vert; Jaune; Bleu; Magenta; Cyan
    color = random.randint(31, 36)

    carre = '██'
    rempli = f"\033[{color}m{carre}\033[37m"
    result = ''

    for i in range(longeur):
        if(i < longeur):
            result += '\n'
        for j in range(largeur):
            if symetrique[i][j] == 1:
                # carré colorie
                result += rempli
            else:
                # carré blanc
                result += carre

    return image


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
    resultat = coloration(cube)
    print(resultat)

    fichier = open("data.txt", "a")
    fichier.write(resultat)
    fichier.close()

main()