from vidamais import *

def test_IMC():
    assert IMC(50, 1.69) == 18
    assert IMC(0, -1) == "Altura e peso devem ser maiores que zero!"


def test_classimc():
    assert class_imc(IMC(50, 1.69)) == "Abaixo do peso"
    assert class_imc(IMC(100, 1.69)) == "Obesidade grau II"