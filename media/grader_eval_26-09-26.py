import random
import math


def grade(exercice, reponse):
    if exercice == "exo1":
        return _grade_qcm(reponse)

    elif exercice == "exo2":
        return _grade_exo2(reponse)

    elif exercice == "exo3":
        return _grade_exo3(reponse)

    elif exercice == "exo4":
        return _grade_exo4(reponse)

    else:
        print(f"Exercice inconnu : {exercice}")


# ============================================================
# QCM
# ============================================================

def _grade_qcm(reponses):
    bonnes_reponses = [3, 2, 3, 4, 3, 1]

    if not isinstance(reponses, list):
        print("Les réponses doivent être données sous forme de liste.")
        return False

    if len(reponses) != 6:
        print("Il faut donner exactement 6 réponses.")
        return False

    score = sum(
        reponse == bonne
        for reponse, bonne in zip(reponses, bonnes_reponses)
    )

    print(f"Score : {score}/6")

    return score == 6


# ============================================================
# EXERCICE 2 — FACTORIELLE
# ============================================================

def _grade_exo2(fonction):
    if not callable(fonction):
        print("La réponse doit être une fonction.")
        return False

    # Tests classiques + quelques valeurs aléatoires
    tests = [
        0,
        1,
        2,
        3,
        5,
        6,
        10,
        20,
        50,
        67,
    ]

    # Quelques tests aléatoires supplémentaires
    random.seed(42)
    tests += [random.randint(2, 30) for _ in range(5)]

    for n in tests:
        attendu = math.factorial(n)

        try:
            resultat = fonction(n)
        except Exception as e:
            print(f"Ta fonction provoque une erreur avec n = {n}.")
            print(f"Erreur : {type(e).__name__}: {e}")
            print("Vérifie notamment ta boucle et les valeurs utilisées dans le calcul.")
            return False

        if resultat != attendu:
            print(f"Le résultat est incorrect pour n = {n}.")
            print(f"Ta fonction renvoie : {resultat}")
            print(f"Il fallait : {attendu}")
            print("Vérifie que tu multiplies bien tous les nombres de 1 à n.")
            return False

    print("BRAVO!!!")
    return True


# ============================================================
# EXERCICE 3 — LISTE DE COURSE
# ============================================================

def _grade_exo3(fonction):
    if not callable(fonction):
        print("La réponse doit être une fonction.")
        return False

    tests = [
        [
            {"nom": "moquette", "prix": 6, "quantite": 7},
            {"nom": "led", "prix": 4, "quantite": 3},
            {"nom": "eleve serieux", "prix": 6767, "quantite": 4},
        ],

        [
            {"nom": "pomme", "prix": 2, "quantite": 5},
        ],

        [
            {"nom": "bloc", "prix": 10, "quantite": 10},
            {"nom": "torche", "prix": 3, "quantite": 20},
        ],

        [],

        [
            {"nom": "objet", "prix": 0, "quantite": 50},
            {"nom": "objet2", "prix": 12, "quantite": 0},
        ],
    ]

    # Tests aléatoires
    random.seed(123)

    for _ in range(5):
        course = []

        for i in range(random.randint(1, 6)):
            course.append({
                "nom": f"objet{i}",
                "prix": random.randint(0, 100),
                "quantite": random.randint(0, 20),
            })

        tests.append(course)

    for liste_course in tests:

        attendu = sum(
            article["prix"] * article["quantite"]
            for article in liste_course
        )

        # Copie pour vérifier qu'on donne bien une liste normale
        liste_test = [
            article.copy()
            for article in liste_course
        ]

        try:
            resultat = fonction(liste_test)
        except Exception as e:
            print("Ta fonction provoque une erreur avec une liste de course.")
            print(f"Erreur : {type(e).__name__}: {e}")
            print("Vérifie notamment comment tu parcours la liste et comment tu accèdes aux dictionnaires.")
            return False

        if resultat != attendu:
            print("Le prix total est incorrect.")
            print(f"Liste testée : {liste_course}")
            print(f"Ta fonction renvoie : {resultat}")
            print(f"Il fallait : {attendu}")
            print("Pour chaque article, il faut prendre son prix et le multiplier par sa quantité.")
            return False

    print("BRAVO!!!")
    return True


# ============================================================
# EXERCICE 4 — CLASSE PLAYER
# ============================================================

def _grade_exo4(classe):
    if not isinstance(classe, type):
        print("La réponse doit être une classe.")
        return False

    # --------------------------------------------------------
    # 1. estVivant
    # --------------------------------------------------------

    try:
        joueur = classe("Test", 0, 0, 0)
    except Exception as e:
        print("Impossible de créer un Player.")
        print(f"Erreur : {type(e).__name__}: {e}")
        print("Vérifie le constructeur __init__ et les paramètres demandés.")
        return False

    try:
        if joueur.estVivant() is not True:
            print("La méthode estVivant() ne renvoie pas True pour un joueur avec 20 HP.")
            print("Un joueur est vivant lorsque ses points de vie sont strictement supérieurs à 0.")
            return False
    except Exception as e:
        print("La méthode estVivant() provoque une erreur.")
        print(f"Erreur : {type(e).__name__}: {e}")
        print("Vérifie que tu utilises bien les points de vie du joueur.")
        return False

    # Test avec 0 HP
    try:
        joueur.hp = 0

        if joueur.estVivant() is not False:
            print("La méthode estVivant() est incorrecte lorsque les HP valent 0.")
            print("Un joueur avec 0 point de vie doit être considéré comme mort.")
            return False

    except Exception as e:
        print("La méthode estVivant() provoque une erreur avec 0 HP.")
        print(f"Erreur : {type(e).__name__}: {e}")
        return False

    # Test avec des HP négatifs
    try:
        joueur.hp = -10

        if joueur.estVivant() is not False:
            print("La méthode estVivant() est incorrecte avec des HP négatifs.")
            print("Il faut vérifier que les HP sont strictement supérieurs à 0.")
            return False

    except Exception as e:
        print("La méthode estVivant() provoque une erreur avec des HP négatifs.")
        print(f"Erreur : {type(e).__name__}: {e}")
        return False

    # --------------------------------------------------------
    # 2. avanceX
    # --------------------------------------------------------

    try:
        joueur = classe("Test", 10, 20, 30)

        joueur.avanceX(5)

        if joueur.x != 15:
            print("La méthode avanceX() est incorrecte.")
            print("Elle doit ajouter la distance donnée à la coordonnée X.")
            print(f"Après avanceX(5), X devrait être 15, mais vaut {joueur.x}.")
            return False

        joueur.avanceX(-3)

        if joueur.x != 12:
            print("La méthode avanceX() ne gère pas correctement une valeur négative.")
            print("Elle doit simplement ajouter n à X.")
            return False

    except Exception as e:
        print("La méthode avanceX() provoque une erreur.")
        print(f"Erreur : {type(e).__name__}: {e}")
        print("Vérifie notamment le paramètre n et la modification de self.x.")
        return False

    # --------------------------------------------------------
    # 3. avanceY
    # --------------------------------------------------------

    try:
        joueur = classe("Test", 10, 20, 30)

        joueur.avanceY(7)

        if joueur.y != 27:
            print("La méthode avanceY() est incorrecte.")
            print("Elle doit ajouter la distance donnée à la coordonnée Y.")
            print(f"Après avanceY(7), Y devrait être 27, mais vaut {joueur.y}.")
            return False

        joueur.avanceY(-5)

        if joueur.y != 22:
            print("La méthode avanceY() ne gère pas correctement une valeur négative.")
            print("Elle doit simplement ajouter n à Y.")
            return False

    except Exception as e:
        print("La méthode avanceY() provoque une erreur.")
        print(f"Erreur : {type(e).__name__}: {e}")
        print("Vérifie notamment le paramètre n et la modification de self.y.")
        return False

    # --------------------------------------------------------
    # 4. avanceZ
    # --------------------------------------------------------

    try:
        joueur = classe("Test", 10, 20, 30)

        joueur.avanceZ(8)

        if joueur.z != 38:
            print("La méthode avanceZ() est incorrecte.")
            print("Elle doit ajouter la distance donnée à la coordonnée Z.")
            print(f"Après avanceZ(8), Z devrait être 38, mais vaut {joueur.z}.")
            return False

        joueur.avanceZ(-6)

        if joueur.z != 32:
            print("La méthode avanceZ() ne gère pas correctement une valeur négative.")
            print("Elle doit simplement ajouter n à Z.")
            return False

    except Exception as e:
        print("La méthode avanceZ() provoque une erreur.")
        print(f"Erreur : {type(e).__name__}: {e}")
        print("Vérifie notamment le paramètre n et la modification de self.z.")
        return False

    # --------------------------------------------------------
    # 5. attaque
    # --------------------------------------------------------

    # Cas 1 : joueurs trop éloignés
    try:
        attaquant = classe("Attaquant", 0, 0, 0, 5, 20)
        adversaire = classe("Adversaire", 10, 0, 0, 3, 20)

        hp_avant = adversaire.hp

        resultat = attaquant.attaque(adversaire)

        if resultat is not False:
            print("La méthode attaque() est incorrecte lorsque les joueurs sont trop éloignés.")
            print("Elle doit renvoyer False si l'attaque ne peut pas être effectuée.")
            return False

        if adversaire.hp != hp_avant:
            print("La méthode attaque() enlève des HP alors que les joueurs sont trop éloignés.")
            print("Les dégâts ne doivent être infligés que si la distance est inférieure ou égale à 3 mètres.")
            return False

    except Exception as e:
        print("La méthode attaque() provoque une erreur avec deux joueurs éloignés.")
        print(f"Erreur : {type(e).__name__}: {e}")
        print("Vérifie notamment le calcul de la distance entre les deux joueurs.")
        return False

    # Cas 2 : joueurs à exactement 3 mètres
    try:
        attaquant = classe("Attaquant", 0, 0, 0, 5, 20)
        adversaire = classe("Adversaire", 3, 0, 0, 20, 20)

        resultat = attaquant.attaque(adversaire)

        if resultat is not True:
            print("La méthode attaque() est incorrecte à exactement 3 mètres.")
            print("La condition demandée est « à moins de 3 mètres ».")
            return False

        if adversaire.hp != 15:
            print("Les dégâts infligés par attaque() sont incorrects.")
            print("L'adversaire devait perdre exactement les dégâts de l'attaquant.")
            return False

    except Exception as e:
        print("La méthode attaque() provoque une erreur à 3 mètres.")
        print(f"Erreur : {type(e).__name__}: {e}")
        return False

    # Cas 3 : adversaire mort
    try:
        attaquant = classe("Attaquant", 0, 0, 0, 5, 20)
        adversaire = classe("Adversaire", 1, 0, 0, 3, 0)

        resultat = attaquant.attaque(adversaire)

        if resultat is not False:
            print("La méthode attaque() permet d'attaquer un joueur déjà mort.")
            print("Les dégâts ne doivent être infligés que si les deux joueurs sont vivants.")
            return False

    except Exception as e:
        print("La méthode attaque() provoque une erreur avec un adversaire mort.")
        print(f"Erreur : {type(e).__name__}: {e}")
        return False

    # Cas 4 : attaquant mort
    try:
        attaquant = classe("Attaquant", 0, 0, 0, 5, 0)
        adversaire = classe("Adversaire", 1, 0, 0, 3, 20)

        resultat = attaquant.attaque(adversaire)

        if resultat is not False:
            print("La méthode attaque() permet à un joueur mort d'attaquer.")
            print("Les dégâts ne doivent être infligés que si les deux joueurs sont vivants.")
            return False

    except Exception as e:
        print("La méthode attaque() provoque une erreur avec un attaquant mort.")
        print(f"Erreur : {type(e).__name__}: {e}")
        return False

    # Cas 5 : vraie attaque avec distance dans l'espace
    try:
        attaquant = classe("Attaquant", 0, 0, 0, 7, 20)

        # Distance = sqrt(1² + 2² + 2²) = 3
        adversaire = classe("Adversaire", 1, 2, 2, 3, 20)

        hp_avant = adversaire.hp

        resultat = attaquant.attaque(adversaire)

        if resultat is not True:
            print("La méthode attaque() ne permet pas correctement une attaque valide.")
            print("Les deux joueurs sont vivants et la distance est de 3 mètres.")
            return False

        if adversaire.hp != hp_avant - attaquant.degats:
            print("La méthode attaque() retire un mauvais nombre de points de vie.")
            print("L'adversaire doit perdre exactement self.degats.")
            return False

    except Exception as e:
        print("La méthode attaque() provoque une erreur lors d'une attaque valide.")
        print(f"Erreur : {type(e).__name__}: {e}")
        print("Vérifie le calcul de distance et la modification des HP.")
        return False

    # Cas 6 : vérifier qu'un joueur peut être tué
    try:
        attaquant = classe("Attaquant", 0, 0, 0, 10, 20)
        adversaire = classe("Adversaire", 0, 0, 2, 5, 5)

        resultat = attaquant.attaque(adversaire)

        if resultat is not True:
            print("La méthode attaque() devrait réussir lorsque l'adversaire est à portée.")
            return False

        if adversaire.hp != -5:
            print("Les dégâts ne sont pas correctement retirés aux HP.")
            return False

        if adversaire.estVivant() is not False:
            print("Le joueur devrait être mort après être tombé à 0 HP ou moins.")
            return False

    except Exception as e:
        print("Erreur lors du test d'une attaque qui tue l'adversaire.")
        print(f"Erreur : {type(e).__name__}: {e}")
        return False

    print("BRAVO!!!")
    return True
