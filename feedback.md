
---

## 📄 `FEEDBACK.md`

```markdown
# Feedback – Projet Pierre–Feuille–Ciseaux

---

## ✅ Points positifs

- **Structure claire** : Le code est bien organisé avec plusieurs fonctions (`choix_joueur`, `choix_ia`, `gagnant`, `jeu`) séparant les responsabilités.

- **Lisibilité** : Variables bien nommées, commentaires clairs, logique facile à suivre.

- **Fonctionnalité complète** : Score, égalités, choix aléatoire de l'IA, et rejouabilité sont bien implémentés.

- **Bonne gestion des erreurs** : Validation de l'entrée utilisateur pour éviter les plantages.

- **Respect du cahier des charges** : Plusieurs manches, interaction utilisateur, fichier `main.py`, venv, etc.

---

## ⚠️ Points d'amélioration

- **Validation d'entrée répétée** : La saisie utilisateur est doublée dans la fonction `jeu()` et `choix_joueur()`. Le code peut être unifié.

- **Refactorisation possible** : La logique de score pourrait être extraite dans une fonction dédiée pour plus de clarté.

- **Affichage IA manquant au départ** : L'IA choisit son coup, mais il n’est pas toujours affiché (corrigé dans la dernière version).

- **Peu de modularité** : Tout est dans un seul fichier `main.py`. On pourrait découper davantage (ex: `utils.py`, `game.py`).

---

## 💡 Suggestions bonus (extensions possibles)

- **Mode difficile** : L’IA pourrait analyser les anciens choix du joueur pour adapter sa stratégie.

- **Interface graphique (Tkinter ou PyQt)** : Rendre le jeu plus visuel et attractif.

- **Système de scores persistants** : Enregistrer les scores dans un fichier `.json` ou `.csv`.

- **Tests unitaires** : Ajouter des tests pour valider la logique (ex : fonction `gagnant`).

- **Multijoueur local** : Permettre à deux joueurs de s’affronter sur la même machine.

---

