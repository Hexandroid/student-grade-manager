# Student Grade Manager 🎓

Application en ligne de commande (CLI) développée en **Python** pour gérer des étudiants et leurs notes, calculer leurs moyennes et conserver les données d'une session à l'autre grâce à un fichier JSON.

> **Contexte d'apprentissage :** projet pratique de consolidation des bases Python. Ce README sert également de journal de progression pour reprendre facilement le travail après une pause.

## Fonctionnalités réalisées

- **Inscrire un étudiant** à la fois, sans limite fixe du nombre d'étudiants.
- **Afficher les étudiants** et calculer leur moyenne.
- **Rechercher un étudiant** par son nom.
- **Modifier les notes** d'un étudiant, sans écraser les anciennes notes si la saisie est invalide.
- **Supprimer un étudiant**.
- **Sauvegarder les données** dans `etudiants.json` après les opérations de modification.
- **Charger les données** lors du lancement du programme.
- Gérer plusieurs erreurs de saisie et de lecture du fichier JSON.

## Technologies et notions pratiquées

- Python 3
- Dictionnaires (`{nom: [notes]}`), listes et boucles
- Fonctions, paramètres, valeurs de retour
- Chaînes : `strip()`, `capitalize()`, `split()`
- Conversion et validation : `float()`, `try` / `except ValueError`
- Manipulation de fichiers : `with open(...)`
- Sérialisation JSON : `json.dump()` et `json.load()`
- Vérification de l'existence d'un fichier : `os.path.exists()`
- Gestion d'exceptions : `json.JSONDecodeError`, `PermissionError`

## Exemple de données

Les étudiants sont représentés dans un dictionnaire Python, puis enregistrés en JSON :

```json
{
    "Alice": [15.0, 12.0, 17.0],
    "Bob": [10.0, 14.0, 13.0]
}
```

La moyenne est calculée avec `sum(notes) / len(notes)` ; lorsqu'une liste est vide, `calculer_moyenne()` renvoie `None`.

## Démarrage

### Prérequis

- Python 3 installé
- Aucune bibliothèque externe nécessaire (`json` et `os` font partie de la bibliothèque standard)

### Exécution

1. Placer le fichier Python principal dans un dossier de projet.
2. Ouvrir un terminal dans ce dossier.
3. Exécuter, **en remplaçant `main.py` par le nom réel du fichier** :

```bash
python main.py
```

Sous Windows, si nécessaire :

```bash
py main.py
```

Au premier lancement, aucun fichier de sauvegarde n'est nécessaire : le programme démarre avec une liste vide. Un fichier `etudiants.json` est créé lors d'une sauvegarde.

## Menu de l'application

```text
===== STUDENT GRADE MANAGER =====
1. Inscrire un étudiant
2. Afficher tous les étudiants
3. Rechercher un étudiant
4. Modifier un étudiant
5. Supprimer un étudiant
6. Quitter
```

## Organisation du code actuel

Le programme est pour l'instant regroupé dans **un seul fichier Python** :

| Fonction | Rôle |
| --- | --- |
| `afficher_menu()` | Affiche les choix disponibles |
| `calculer_moyenne(notes)` | Retourne la moyenne ou `None` si aucune note |
| `afficher_etudiants(etudiants)` | Liste les étudiants et leurs moyennes |
| `rechercher_etudiant(etudiants)` | Cherche un étudiant par nom |
| `inscrire_etudiant(etudiants)` | Ajoute un étudiant et vérifie les notes |
| `modifier_notes(etudiants)` | Remplace les notes uniquement si elles sont valides |
| `supprimer_etudiant(etudiants)` | Supprime l'étudiant choisi |
| `sauvegarder_etudiants(etudiants)` | Écrit le dictionnaire dans `etudiants.json` |
| `charger_etudiants()` | Lit le JSON ou initialise un dictionnaire vide |

La boucle principale charge les données au démarrage, affiche le menu et déclenche les différentes fonctions.

## Tests réalisés

Les scénarios habituels ont été testés manuellement et fonctionnent :

- Ajout, recherche, affichage, modification et suppression d'étudiants.
- Rejet des notes hors de l'intervalle **0 à 20** et des saisies non convertibles en nombre.
- Conservation des anciennes notes lors d'une modification invalide.
- Sauvegarde, fermeture du programme, redémarrage puis vérification des données rechargées.

**Remarque :** les tests sont manuels ; il n'existe pas encore de suite de tests automatisés.

## Points à revoir à la reprise

1. **Fiabiliser les cas limites :** nom vide, saisies vides, valeurs numériques spéciales (`nan`, `inf`) et structure inattendue du JSON. Certaines corrections ont pu être essayées localement, mais restent à vérifier dans la version publiée.
2. **Gérer le succès des opérations :** faire retourner `True` / `False` par les fonctions qui modifient les données, afin de ne sauvegarder qu'en cas de changement réel.
3. **Protéger le fichier existant :** si le chargement JSON échoue, éviter qu'une sauvegarde remplace silencieusement les données corrompues ou inaccessibles.
4. **Éviter les répétitions :** extraire la logique commune de validation des notes utilisée à l'inscription et à la modification.
5. **Améliorer la structure :** séparer progressivement les responsabilités (interface CLI, opérations de gestion, stockage), puis envisager des tests automatisés.

## Conseil pour GitHub

Le fichier `etudiants.json` peut contenir des noms et des notes. **Ne pas publier de données personnelles réelles.** Il est conseillé d'ajouter `etudiants.json` à `.gitignore` et, si nécessaire, de fournir un fichier d'exemple avec des données fictives.

## État du projet

**Version CLI fonctionnelle — pause dans l'apprentissage Python.**

À la reprise, commencer par relire ce README et vérifier la dernière version du fichier Python, puis reprendre la liste « Points à revoir à la reprise ».
