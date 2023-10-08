def calculate_bmi(weight, height):
    return float(weight) / float(height)**2

def get_weight_group(bmi):
    if bmi < 16.5:
        return "těžká podvýživa"
    elif bmi >= 16.5 and bmi < 18.5:
        return "podváha"
    elif bmi >= 18.5 and bmi < 25:
        return "ideální váha"
    elif bmi >= 25 and bmi < 30:
        return "nadváha"
    elif bmi >= 30:
        return "obezita"