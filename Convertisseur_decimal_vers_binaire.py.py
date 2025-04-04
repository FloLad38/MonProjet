#Fonctions de conversion

def decimal_vers_binaire(n):
    if n == 0:
        return "0"
    resultat = ""
    while n > 0:
        resultat = str(n % 2) + resultat
        n = n // 2
    return resultat

def binaire_vers_decimal(b):
    total = 0
    longueur = len(b) - 1
    for chiffre in b:
        if chiffre == '1':
            total += 2 ** longueur
        longueur -= 1
    return total

# Programme principal
while True:
    print("\n--- Convertisseur Décimal/Binaire ---")
    print("1. Décimal → Binaire")
    print("2. Binaire → Décimal")
    print("3. Quitter")
    
    choix = input("Votre choix (1-3) : ")
    
    if choix == "1":
        nombre = int(input("Entrez un nombre décimal : "))
        print(f"Résultat en binaire : {decimal_vers_binaire(nombre)}")
    elif choix == "2":
        binaire = input("Entrez un nombre binaire : ")
        if all(c in "01" for c in binaire):
            print(f"Résultat en décimal : {binaire_vers_decimal(binaire)}")
        else:
            print("Erreur : Entrez uniquement des 0 et 1")
    elif choix == "3":
        print("Au revoir !")
        break
    else:
        print("Choix invalide")

