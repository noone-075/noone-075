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
        return

    if len(reponses) != 6:
        print("Il faut donner exactement 6 réponses.")
        return

    score = sum(
        reponse == bonne
        for reponse, bonne in zip(reponses, bonnes_reponses)
    )

    print(f"Score : {score}/6")

    return score==6

def _grade_exo2(fonction):
  pass

def _grade_exo3(fonction):
  pass

def _grade_exo4(classe):
  pass
