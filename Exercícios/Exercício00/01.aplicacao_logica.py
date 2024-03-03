import math

ponto_a = (1, 3)
ponto_b = (5, 6)

x1, y1 = ponto_a
x2, y2 = ponto_b

dx = x2 - x1
dy = y2 - y1

distancia = math.sqrt(dx**2 + dy**2)

print(f"A distância entre os pontos A e B é de {distancia}")