def NbCMin(password):
    return sum(1 for char in password if char.islower())

def NbCMaj(password):
    return sum(1 for char in password if char.isupper())

def NbCAlpha(password):
    return sum(1 for char in password if not char.isalpha())

def LongMaj(password):
    max_length = 0
    current_length = 0

    for char in password:
        if char.isupper():
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0

    return max_length

def LongMin(password):
    max_length = 0
    current_length = 0

    for char in password:
        if char.islower():
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 0

    return max_length

def score(password):
    total_chars = len(password)
    bonus = total_chars + (total_chars - NbCMaj(password)) * 2 + (total_chars - NbCMin(password)) * 3 + NbCAlpha(password) * 5
    malus = LongMaj(password) * 2 + LongMin(password) * 2
    final_score = bonus - malus

    if final_score < 20:
        return "Très faible"
    elif 20 <= final_score < 40:
        return "Faible"
    elif 40 <= final_score < 80:
        return "Fort"
    else:
        return "Très fort"

mot_de_passe = input("enter your password")
print("Score du mot de passe:", score(mot_de_passe))
