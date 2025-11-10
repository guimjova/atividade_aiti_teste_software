def IMC(peso, altura):
    if altura <= 0 or peso <= 0:
        return "Altura e peso devem ser maiores que zero!"
    return round(peso/(altura)**2)

def class_imc(imc):
    if imc <= 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc < 25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    elif imc >= 30 and imc < 25:
        return "Obesidade grau I"
    elif imc >= 35 and imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"