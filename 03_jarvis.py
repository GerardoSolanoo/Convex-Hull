# Clase para representar puntos
class Punto:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Función para encontrar la distancia entre dos puntos
def distancia(p1, p2):
  return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

# Función para encontrar el ángulo polar de un punto
def angulo_polar(punto, origen):
  return math.atan2(punto.y - origen.y, punto.x - origen.x)

# Función para comparar puntos por ángulo polar y distancia al origen
def comparar_por_angulo_distancia(p1, p2, origen):
  angulo_p1 = angulo_polar(p1, origen)
  angulo_p2 = angulo_polar(p2, origen)
  if angulo_p1 == angulo_p2:
    return distancia(origen, p1) - distancia(origen, p2)  # Comparar por distancia si tienen el mismo ángulo
  else:
    return angulo_p1 - angulo_p2

# Función para calcular el casco convexo
def casco_convexo_jarvis(puntos):
  # Encontrar el punto con la coordenada x mínima
  minimo_x = min(puntos, key=lambda punto: punto.x)

  # Ordenar puntos por ángulo polar y distancia al origen con respecto al punto con coordenada x mínima
  puntos.sort(key=lambda punto: comparar_por_angulo_distancia(punto, minimo_x, origen))

  # Inicializar lista de puntos del casco convexo
  casco = []

  # Agregar el punto inicial al casco
  casco.append(minimo_x)

  # Recorrer los puntos restantes
  for punto in puntos[1:]:
    # Eliminar puntos que no forman parte de la frontera convexa
    while len(casco) >= 2 and orientacion(casco[-2], casco[-1], punto) != 2:
      casco.pop()

    # Agregar punto al casco
    casco.append(punto)

  return casco

# Ejemplo de uso
puntos = [Punto(1, 4), Punto(3, 2), Punto(5, 1), Punto(4, 6), Punto(2, 3)]
casco = casco_convexo_jarvis(puntos)
print("Casco convexo:", casco)
