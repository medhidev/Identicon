# Projet Identicon
# v1.0 - Test

def creeCube(n, m):
    matrice = [[0 for x in range(m)]
        for y in range(n)]
    return matrice

def printCube(matrice):
    """
    Entree: Prend T un tableau précréer
    Sortie: Renvoie les valeur du tableau T
    Role: Permet de mieux visualiser le contenu d'une matrice O
    """
    n = len(matrice)
    m = len(matrice[0])
    
    # espace les matrices entre elles
    print("\n")
    for i in range(n):
        for j in range(m):
            print(matrice[i][j],end=" ")
            
        #saut de ligne
        print(" ")



def main():

    '''
    Gestion de la taille (plus tard)
    '''
    # default value
    # largeur = ''
    # longueur = ''
    # changeur = 0
    # size = ''

    # while(size == ''):
    #     size = input('dimension du cube (avec Longeur;largeur): ')
    #     for i in (size):
    #         if (i == ';'):
    #             changeur += 1
    #         elif (changeur == 1):
    #             largeur += i
    #         else:
    #             longueur += i

        # if (isinstance(int(longueur), str) and isinstance(int(largeur), str)):
        #     print('Erreur, mauvaise dimension')
        #     size = ''

    cube = creeCube(5, 5)
    printCube(cube)

main()