from services.fatorial import calcular_fatorial


def test_fatorial_5():
    assert calcular_fatorial(5) == 120


def test_fatorial_0():
    assert calcular_fatorial(0) == 1