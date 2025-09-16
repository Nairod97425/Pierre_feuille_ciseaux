import random

def init():
    
    # Liste des choix possibles
    liste = ["pierre", "feuille", "ciseaux"]

    # Fonction pour que le joueur choisisse son coup
    def choix_joueur():
        while True:
            user = input("pierre✊, feuille✋ ou ciseaux✌️ : ").lower()
            if user in liste:
                print(f"Vous avez choisi : {user}")
                return user
            else: 
                print("Mauvais choix. Essaie encore !")

    # Fonction pour que l'IA choisisse son coup    
    def choix_ia():
        ia = random.choice(liste)
        print(f"L'IA a choisi : {ia}")
        return ia

    # Fonction pour déterminer le gagnant
    def gagnant(user, ia):
        if user == ia:
            return "egalite"
        elif (user == "ciseaux" and ia == "feuille") or \
            (user == "feuille" and ia == "pierre") or \
            (user == "pierre" and ia == "ciseaux"):
            return "user"
        else:
            return "ia"

    # Fonction principale du jeu
    def jeu():    
        while True:
            score_user = 0
            score_ia = 0
            egalite = 0

            # Demande combien de parties
            while True:
                try:
                    nbre_partie = int(input("Nombre de parties : "))
                    if nbre_partie > 0:
                        break
                    else:
                        print("Entre un nombre supérieur à 0.")
                except ValueError:
                    print("Merci d’entrer un nombre valide.")

            for _ in range(nbre_partie):
                user = choix_joueur()
                ia = choix_ia()

                resultat = gagnant(user, ia)

                if resultat == "egalite":
                    egalite += 1
                    print("Égalité ! 🤝")
                elif resultat == "user":
                    score_user += 1
                    print("Tu gagnes cette manche ! 🎉")
                else:
                    score_ia += 1
                    print("L'IA gagne cette manche ! 💻")

            # Résultat final
            print("\n=== Résultats finaux 🏆 ===")
            if score_user > score_ia:
                print("Bravo, tu gagnes la partie ! 🎆")
            elif score_ia > score_user:
                print("L'IA remporte la partie ! 😈")
            else:
                print("Match nul ! ⚖️")

            # Score
            print("\n=== Score 📊 ===")
            print(f"Nombre de parties : {nbre_partie}")
            print(f"Score utilisateur : {score_user}")
            print(f"Score IA : {score_ia}")
            print(f"Égalités : {egalite}")

            # Rejouer ?
            try_again = input("\nVeux-tu rejouer ? (o/n) : ").lower()
            if try_again != "o":
                print("Merci d'avoir joué ! À bientôt ! 🤗")
                break

    # Lancer le jeu
    jeu()
