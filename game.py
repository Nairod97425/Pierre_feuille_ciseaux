import random

liste = ["pierre", "feuille", "ciseaux"]
score_user = 0
score_IA = 0
egalite = 0
nbre_partie = int(input("nombre de partie : "))

for n in range(nbre_partie):
    user_1 = input("pierre, feuille ou ciseaux : ")
    IA = random.choice(liste)
    if user_1 == IA :
        print("egalite")
        egalite += 1
    elif (user_1 == "ciseaux" and IA == "feuille") or \
        (user_1 == "feuille" and IA == "pierre") or \
        (user_1 == "pierre" and IA == "ciseaux"):
        print("user win")
        score_user += 1
    else:
        print("IA win")
        score_IA += 1
if score_user > score_IA :
    print("the user win")
elif score_IA > score_user:
    print("the IA win")
else:
    print("égalité")
print(f"score user : {score_user}, score IA:{score_IA}, egalite : {egalite}")
