from services.temperatura import celsius_para_fahrenheit


def test_conversao_basica():
    assert celsius_para_fahrenheit(0) == 32


def test_conversao_positiva():
    assert celsius_para_fahrenheit(25) == 77


def test_conversao_negativa():
    assert celsius_para_fahrenheit(-10) == 14