
import pytest
from envios import calcular_envio


@pytest.mark.parametrize("distancia, esperado", [
    (3, 5000),
    (5, 5000),
    (7, 8000),
    (10, 8000),
    (-2, "Distancia no válida"),
    (12, "Fuera de cobertura")
])


def test_calcular_envio(distancia, esperado):
    resultado = calcular_envio(distancia)

    assert resultado == esperado
