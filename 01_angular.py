# Clase para representar puntos
class Punto:
  def __init__(self, x, y):
    self.x = x
    self.y = y

# Función para encontrar el ángulo polar de un punto
def angulo_polar(punto, origen):
  return math.atan2(punto.y - origen.y, punto.x - origen.x)

# Función para calcular el casco convexo
def casco_convexo_barrido_angular(puntos):
  # Ordenar puntos por ángulo polar
  puntos.sort(key=lambda punto: angulo_polar(punto, puntos[0]))

  # Inicializar casco convexo
  casco = [puntos[0], puntos[1]]

  # Recorrer los puntos restantes
  for punto in puntos[2:]:
    # Eliminar puntos que no forman parte de la frontera convexa
    while len(casco) >= 2 and angulo_polar(punto, casco[-2]) <= angulo_polar(casco[-1], casco[-2]):
      casco.pop()

    # Agregar punto a la frontera convexa
    casco.append(punto)

  return casco

# Ejemplo de uso
puntos = [Punto(1, 4), Punto(3, 2), Punto(5, 1), Punto(4, 6), Punto(2, 3)]
casco = casco_convexo_barrido_angular(puntos)
print("Casco convexo:", casco)
