import json
import os


def afficher_menu():
    print("""===== STUDENT GRADE MANAGER =====
    1. Inscrire un étudiant
    2. Afficher tous les étudiants
    3. Rechercher un étudiant
    4. Modifier un étudiant
    5. Supprimer un étudiant
    6. Quitter""")


def calculer_moyenne(notes):
    if not notes:
        return None

    return sum(notes) / len(notes)


def afficher_etudiants(etudiants):
    print("##### Voici la liste actuelle #####")
    for nom, notes in etudiants.items():
        avg = calculer_moyenne(notes)
        if avg is None:
            print("L'étudiant n'as pas de note")
        else:
            print("-", nom, "Moyenne : ", avg)


def rechercher_etudiant(etudiants):
    print("##### Voici la liste actuelle #####")
    for nom in etudiants:
        print("-", nom)

    choix = input("Quelle élèves cherchez vous ? : ")
    choix_format = choix.strip().capitalize()

    if choix_format in etudiants:
        notes = etudiants.get(choix_format)
        avg = calculer_moyenne(notes)
        print(f"Les notes de : {choix} sont : {notes} et il/elle a {avg} de moyenne")
    else:
        print("Ce étudant n'existe pas ou est mal orthographié")


def modifier_notes(etudiants):
    print("##### Voici la liste actuelle #####")
    for nom in etudiants:
        print("-", nom)
    choix = input("Quelle étudiants cherchez vous ? : ")
    choix_format = choix.strip().capitalize()

    if choix_format in etudiants:
        note = input(
            "Entrer les notes de l'étudiant séparées par une virgule : ")
        note_separe = note.strip().split(",")

        notes_temp = []
        notes_valides = True

        for x in note_separe:
            try:
                x = float(x.strip())
                if x < 0 or x > 20:
                    print("Note hors de l'intervalle 0-20")
                    notes_valides = False
                else:
                    notes_temp.append(x)

            except ValueError:
                print("Une valeur saisie est incorrecte")
                notes_valides = False

        if notes_valides:
            etudiants[choix_format] = notes_temp.copy()
            print("Notes modifiées avec succès")
        else:
            print("Modification annulée : les anciennes notes sont conservées")
    else:
        print("L'etudiant n'existe pas ou est mal orthographié")


def supprimer_etudiant(etudiants):
    print("##### Voici la liste actuelle #####")
    for nom in etudiants:
        print("-", nom)
    choix = input("Quelle étudiants voulez vous supprimer ? : ")
    choix_format = choix.strip().capitalize()

    if choix_format in etudiants:
        del etudiants[choix_format]
        print("L'étudiants a bien été supprimé")
    else:
        print("Ce étudants n'existe pas ou est mal orthographié")


def inscrire_etudiant(etudiants):
    nom = input("Entrer le nom d'un étudiant : ").strip().capitalize()
    if not nom:
        print("Erreur nom non pris en compte")
        return
    else:
        if nom in etudiants:
            print("L'étudiant existe déja")
        else:
            note = input(
                "Entrer les notes de l'étudiant séparées par une virgule : ")
            note_separe = note.strip().split(",")

            notes_temp = []
            notes_valides = True

            for x in note_separe:
                try:
                    x = float(x.strip())

                    if x < 0 or x > 20:
                        print("Note hors de l'intervalle 0-20")
                        notes_valides = False
                    else:
                        notes_temp.append(x)

                except ValueError:
                    print("Une valeur saisie est incorrecte")
                    notes_valides = False

            if not notes_valides:
                print("Etudiant non enregistré")
            else:
                etudiants[nom] = notes_temp.copy()


def sauvegarder_etudiants(etudiants):
    with open("etudiants.json", "w", encoding="utf-8") as fichier:
        json.dump(etudiants, fichier, indent=4)


def charger_etudiants():
    chemin_json = "etudiants.json"
    if not os.path.exists(chemin_json):
        print("Aucune sauvegarde trouvée. Démarrage avec une liste vide.")
        donnees = {}
    else:
        try:
            with open(chemin_json, "r", encoding="utf-8") as fichier:
                donnees = json.load(fichier)
                print("Fichier chargé avec succès !")
        except json.JSONDecodeError:
            print(
                f"Erreur : Le fichier '{chemin_json}' est vide ou le format JSON est invalide.")
            donnees = {}
        except PermissionError:
            print(
                f"Erreur : Accès refusé au fichier '{chemin_json}'.")
            donnees = {}
    return donnees


etudiants = charger_etudiants()
while True:
    afficher_menu()
    try:
        choix = int(input("Votre choix ? : "))
        if choix == 1:
            inscrire_etudiant(etudiants)
            sauvegarder_etudiants(etudiants)
        elif choix == 2:
            afficher_etudiants(etudiants)
        elif choix == 3:
            rechercher_etudiant(etudiants)
        elif choix == 4:
            modifier_notes(etudiants)
            sauvegarder_etudiants(etudiants)
        elif choix == 5:
            supprimer_etudiant(etudiants)
            sauvegarder_etudiants(etudiants)
        elif choix == 6:
            break
        else:
            print("Valeur incorrecte : choisissez entre 1 et 6.")
    except ValueError:
        print("Entrer une valeur correcte")
