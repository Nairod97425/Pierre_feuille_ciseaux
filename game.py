import random

def init_game():
    # Variiables
    liste = ["pierre", "feuille", "ciseaux"]

    while True:
        score_user = 0
        score_IA = 0
        egalite = 0

        # Demande combien de parties et vérifie la valeur entré (boucle)
        while True:
            try:
                nbre_partie = int(input("Nombre de parties : "))
                if nbre_partie > 0:
                    break
                else:
                    print("Entre un nombre supérieur à 0.")
            except ValueError:
                print("Merci d’entrer un nombre valide.")

        for n in range(nbre_partie):
            # Valide l'entré utilisateur(boucle)
            while True:
                user_1 = input("pierre✊, feuille✋ ou ciseaux✌️ : ").lower()
                if user_1 in liste:
                    print(f"Vous avez choisi : {user_1}")
                    break
                else: 
                    print("Mauvais choix. Essaie encore !")

            # Choix de l'IA
            IA = random.choice(liste)
            print(f"L'IA a choisie : {IA}")

            # Les conditions a vérifier 
            if user_1 == IA :
                print("Égalité ! ⚖️")
                egalite += 1
            elif (user_1 == "ciseaux" and IA == "feuille") or \
                (user_1 == "feuille" and IA == "pierre") or \
                (user_1 == "pierre" and IA == "ciseaux"):
                print("Vous remporter la manche !🎉")
                score_user += 1
            else:
                print("L'IA gange la manche !")
                score_IA += 1

        # Résultat
        print("\n=== Résultats finaux 🏆 ===")
        if score_user > score_IA :
            print("Bravo, tu gane la partie ! 🎆")
        elif score_IA > score_user:
            print("L'IA remporte la partie !")
        else:
            print("Égalité ⚖️")
        
        # Score
        print("\n=== Score 🏆 ===")
        print(f"Nombre de partie : {nbre_partie}, Score utilisateur : {score_user}, Score IA:{score_IA}, Égalités : {egalite}")

        # Rejouer
        try_again = input("\nVeux tu rejouer ? (o/n) ").lower()
        if try_again != "o":
            print("Merci d'avoir jouer ! À bientôt ! 🤗")
            break
