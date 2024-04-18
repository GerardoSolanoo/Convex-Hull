# Clase para representar puntos
class Punto:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Función para encontrar la orientación de tres puntos
def orientacion(p, q, r):
  val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
  if val == 0:
    return 0  # colineales
  elif val > 0:
    return 1  # sentido de las agujas del reloj
  else:
    return 2  # sentido contrario a las agujas del reloj

# Función para comparar puntos por ángulo polar
def comparar_por_angulo(p1, p2, origen):
  angulo_p1 = angulo_polar(p1, origen)
  angulo_p2 = angulo_polar(p2, origen)
  if angulo_p1 == angulo_p2:
    return dist(origen, p1) - dist(origen, p2)  # Comparar por distancia a origen si tienen el mismo ángulo
  else:
    return angulo_p1 - angulo_p2

# Función para calcular el casco convexo
def casco_convexo_graham(puntos):
  # Encontrar el punto con la coordenada y mínima
  minimo_y = min(puntos, key=lambda punto: punto.y)

  # Ordenar puntos por ángulo polar con respecto al punto con coordenada y mínima
  puntos.sort(key=lambda punto: comparar_por_angulo(punto, minimo_y, origen))

  # Inicializar pila de puntos
  pila = []
  pila.append(minimo_y)
  pila.append(puntos[1])  # Agregar el siguiente punto con mayor ángulo polar

  # Recorrer los puntos restantes
  for punto in puntos[2:]:
    # Eliminar puntos que no forman parte de la frontera convexa
    while len(pila) >= 2 and orientacion(pila[-2], pila[-1], punto) != 2:
      pila.pop()

    # Agregar punto a la pila
    pila.append(punto)

  # Invertir la pila para obtener el orden correcto del casco convexo
  casco = pila[::-1]

  return casco

# Ejemplo de uso
puntos = [Punto(1, 4), Punto(3, 2), Punto(5, 1), Punto(4, 6), Punto(2, 3)]
casco = casco_convexo_graham(puntos)
print("Casco convexo:", casco)
