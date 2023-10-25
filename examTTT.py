#1. Écrire la fonction permettant d’afficher la grille de jeu.
#Elle prend un tableau en entrée, et affiche la grille grâce aux données du tableau.

#colonne: 
#==> un espace de n//3
#==> un |
#==> un espace de n//3
#==> un |
n=5 
def ligne(n):
    for i in range(n):
        print("*", end = " ")
    print()
    
def colonne(n):
        for i in range (n//3):
            print("|", end=" ")
            print()

def tableau(n):
    for i in range(n):
        ligne(n)
        colonne(n)
#Pas la peine de tester, cela ne fonctionne pas. 
   
#2. Écrire la fonction permettant de jouer un O ou un X.
#Elle prend un tableau en entrée, et le modifie afin d’ajouter un O ou un X à l’endroit souhaité
#par le joueur courant.
def swap(tableau,index1,index2):
    stock = tableau[index1]
    tableau[index1] = tableau[index2]
    tableau[index2] = stock

grille=[1,2,3,4,5,6,7,8,9]
emplacement=0
#étant donné que je n'ai pas réussi à réaliser visuellement mon tableau, j'ai essayé textuellement.
PremierJoueur="X"
casechoisie=int(input("Quelle est la case choisie? "))
#le joueur choisit une case parmis les 6 cases dans le tableau, ensuite je pense qu'on pourrait mettre des if suivant les cases choisies.
for j in range(len(grille)):
    if casechoisie==grille[0]:
        swap(grille,PremierJoueur,emplacement)
        emplacement=0
        grille.pop(emplacement)
print(grille)
#Ici, ça ne fonctionne pas en partie car je n'ai pas inclu le X du joueur. 
#Je voulais que si la case choisie correspondait à la case 0, (ou plus généralement à la case j mais il voulait encore moins fonctionner),le X prenait 
#la place de la case choisie/l'emplacement correspondant au tableau.


#3. Écrire les fonctions vérifiant si oui ou non l’un des joueurs a réussi à aligner 3
#symboles sur une ligne verticale, horizontale, diagonale.

#Pas le temps.  

#6. Qu’aura-t-on besoin de faire, si on souhaite désormais programmer un jeu de Puissance 4 ?
'''Au lieu d'avoir un tableau de 3 par 3, on aurait un tableau de x par x. Au lieu de vérifier si le joueur a aligné 3 jetons/croix/ronds verticalement,
horizontalement, en diagonale, on vérifierait si le joueur en a aligné 4. '''