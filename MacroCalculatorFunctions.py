def calories(choice, gender, weight, height, age, activity):
    if choice == 1:
        if activity == 1:
            cals = bmr(gender, weight, height, age) * 1.2
            return cals - 500
        elif activity == 2:
            cals = bmr(gender, weight, height, age) * 1.375
            return cals - 500
        elif activity == 3:
            cals = bmr(gender, weight, height, age) * 1.55
            return cals - 500
        else:
            cals = bmr(gender, weight, height, age) * 1.725
            return cals - 500
    elif choice == 2:
        if activity == 1:
            cals = bmr(gender, weight, height, age) * 1.2
            return cals
        elif activity == 2:
            cals = bmr(gender, weight, height, age) * 1.375
            return cals
        elif activity == 3:
            cals = bmr(gender, weight, height, age) * 1.55
            return cals
        else:
            cals = bmr(gender, weight, height, age) * 1.725
            return cals
    elif choice == 3:
        if activity == 1:
            cals = bmr(gender, weight, height, age) * 1.2
            return cals + 500
        elif activity == 2:
            cals = bmr(gender, weight, height, age) * 1.375
            return cals + 500
        elif activity == 3:
            cals = bmr(gender, weight, height, age) * 1.55
            return cals + 500
        else:
            cals = bmr(gender, weight, height, age) * 1.725
            return cals + 500


def bmr(gender, weight, height, age):
    if gender == 1:
        a = abs(float(weight) * 6.23)
        b = abs(float(height) * 12.7)
        c = abs(float(age) * 6.8)
        return a + b - c + 66
    else:
        a = abs(float(weight) * 4.35)
        b = abs(float(height) * 4.7)
        c = abs(float(age) * 4.7)
        return a + b - c + 655


def protein(weight):
    weight = float(weight)
    return abs(weight * 0.9)


def fat(choice, gender, weight, height, age, activity):
    return abs((calories(choice, gender, weight, height, age, activity) * 0.15) / 9)


def carbs(choice, gender, weight, height, age, activity):
    return abs((calories(choice, gender, weight, height, age, activity) -
                ((protein(weight) * 4) +
                (fat(choice, gender, weight, height, age, activity) * 9))) / 4)
