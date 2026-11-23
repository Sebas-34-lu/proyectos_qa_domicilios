def calcular_envio(distancia):
    if distancia < 0:
        return "Distancia inválida"
    elif distancia <= 5:
        return 5000
    elif distancia <= 10:
        return 8000
    else:
        return "Fuera de rango"