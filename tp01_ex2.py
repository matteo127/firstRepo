"""
Programme simulant un distributeur de snacks
 Données : - Un montant entré par l'utilisateur
           - Un numéro d'article entré par l'utilisateur
 Indications :
           Le distributeur comporte :
           - Sandwich au poulet à 4.90
           - Chips paprika à 2.50
           - Barre chocolat à 2.00
           - Bonbons à 3.30
           - Ice Tea à 2.20
           - Limonade à 1.90
 Résultats : - Un message confirmant ou annulant la transaction
             - Un message indiquant la monnaie rendue si existante
             - Un message indiquant le produit vendu et souhaitant un bon appétit/santé
"""

### Déclaration des variables
monnaie: float
produit: int
reste: float

sandwichAuPoulet: int
chipsPaprika: int
barreChocolat: int
bonbons: int
iceTea: int
limonade: int

prixSandwichAuPoulet: float
prixChipsPaprika: float
prixBarreChocolat: float
prixBonbons: float
prixIceTea: float
prixLimonade: float

###Initialisation des variables
sandwichAuPoulet = 1
chipsPaprika = 2
barreChocolat = 3
bonbons = 4
iceTea = 5
limonade = 6

prixSandwichAuPoulet = 4.90
prixChipsPaprika = 2.50
prixBarreChocolat = 2.00
prixBonbons = 3.30
prixIceTea = 2.20
prixLimonade = 1.90

### Séquence d'opération

print("Bienvenue ! Voici notre sélection de produit :")
print("----------------------------------------------")
print("1. Sandwich au poulet")
print("2. Chips Paprika")
print("3. Barre chocolatée")
print("4. Bonbons")
print("5. Ice Tea")
print("6. Limonade")

monnaie = float(input("Veuillez introduire votre monnaie :"))
produit = int(input("Veuillez selectionner un produit :"))

if produit == 1:
    if monnaie > prixSandwichAuPoulet:
        reste = monnaie - prixSandwichAuPoulet
        if reste > 0:
            print("Monaie à rendre :", round(reste,2))
        print("Sandwich au poulet servie ! Bon appétit !")
    else:
        print("Transaction annulée")
elif produit == 2:
    if monnaie > prixChipsPaprika:
        reste = monnaie - prixChipsPaprika
        if reste > 0:
            print("Monaie à rendre :", round(reste,2))
        print("Chips Paprika servies ! Bon appétit !")
    else:
        print("Transaction annulée")
elif produit == 3:
    if monnaie > prixBarreChocolat:
        reste = monnaie - prixBarreChocolat
        if reste > 0:
            print("Monaie à rendre :", round(reste,2))
        print("Barre chocolatée servie ! Bon appétit !")
    else:
        print("Transaction annulée")
elif produit == 4:
    if monnaie > prixBonbons:
        reste = monnaie - prixBonbons
        if reste > 0:
            print("Monaie à rendre :", round(reste,2))
        print("Bonbons servie ! Bon appétit !")
    else:
        print("Transaction annulée")
elif produit == 5:
    if monnaie > prixIceTea:
        reste = monnaie - prixIceTea
        if reste > 0:
            print("Monaie à rendre :", round(reste,2))
        print("Ice Tea servie ! Santé !")
    else:
        print("Transaction annulée")
elif produit == 6:
    if monnaie > prixLimonade:
        reste = monnaie - prixLimonade
        if reste > 0:
            print("Monaie à rendre :", round(reste,2))
        print("Limonade servie ! Santé !")
    else:
        print("Transaction annulée")
else:
    print("Veuillez entrer un numéro entre 1 et 6")
