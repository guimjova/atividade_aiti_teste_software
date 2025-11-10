from eficiencia_motor import *

def test_calcular_eficiencia():
    assert calcular_eficiencia(400,20) == 2000.0
    assert calcular_eficiencia(10,0) == "Potência de entrada deve ser maior que zero."

def test_classificar_eficiencia():
    assert classificar_eficiencia(2000.0) == "IE3 - Alta eficiência"

def analise_motor():
    assert analise_motor(400, 20) == {
        "potencia_saida": 400,
        "potencia_entrada": 20,
        "eficiencia": 2000.0,
        'classificacao': "IE3 - Alta eficiência"
    }
