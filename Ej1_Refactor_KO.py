# Sistema de venta de billetes de avión

class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha, hora_salida, hora_llegada, precio):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha = fecha
        self.hora_salida = hora_salida
        self.hora_llegada = hora_llegada
        self.precio = precio

    def __str__(self):
        return (f"Número de vuelo: {self.numero_vuelo}, Origen: {self.origen}, Destino: {self.destino}, "
                f"Fecha: {self.fecha}, Hora de salida: {self.salida}, Hora de llegada: {self.llegada}, "
                f"Precio: {self.precio}")


class Pasajero:
    def __init__(self, nombre, apellido, edad, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.correo = correo

class Informacion:
    def __init__(self, vuelo, pasajero, asientos):
        self.vuelo = vuelo
        self.pasajero = pasajero
        self.asientos = asientos

def mostrar_vuelos_disponibles(vuelos):
    print("Vuelos disponibles:")
    for vuelo in vuelos:
        print(vuelo)

def validar_numero_asientos():
    numero = input("Ingrese el número de vuelo que desea reservar: ")
    cantidad = int(input("Ingrese la cantidad de asientos que desea reservar (máximo 10): "))
    if cantidad > 10:
        print("No puedes hacer una reserva mayor a 10 asientos")
    elif cantidad < 1:
        print("Esa cantidad no es válida")
    else:
        print("La cantidad de asientos es válida")
    

def reservar_vuelo(lista, numero_vuelo, pasajero, cantidad):
    for v in lista:
        if v.numero_vuelo == numero_vuelo:
            if cantidad <= 0:
                print("La cantidad de asientos debe ser mayor que cero.")
                return
            elif cantidad > 10:
                print("Lo sentimos, no se pueden reservar más de 10 asientos por reserva.")
                return
            elif cantidad > 0 and cantidad <= 10:
                reserva = Informacion(v, pasajero, cantidad)
                print(f"¡Reserva exitosa para el vuelo {v.numero_vuelo}!")
                print(f"Nombre del pasajero: {pasajero.nombre} {pasajero.apellido}, Asientos reservados: {cantidad}")
                return
    print("No se encontró ningún vuelo con el número especificado.")

def obtener_datos_reserva():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = int(input("Ingrese su edad: "))
    telefono = input("Ingrese su número de teléfono: ")
    correo = input("Ingrese su correo electrónico: ")

    pasajero = Pasajero(nombre, apellido, edad, telefono, correo)


def main():
    vuelos = [
        Vuelo("AA123", "Nueva York", "Los Angeles", "2024-05-15", "08:00", "11:00", 250.00),
        Vuelo("AA456", "Los Angeles", "Chicago", "2024-05-20", "10:00", "13:00", 200.00),
        Vuelo("AA789", "Chicago", "Miami", "2024-05-25", "12:00", "15:00", 300.00)
    ]

    print("Bienvenido al sistema de venta de billetes de avión.")
    opcion = input("Seleccione una opción:\n1. Ver vuelos disponibles\n2. Reservar vuelo\nIngrese su opción: ")

    if opcion == '1':
        mostrar_vuelos_disponibles(vuelos)
    elif opcion == '2':
        obtener_datos_reserva()
        validar_numero_asientos()
        reservar_vuelo(vuelos, numero, pasajero, cantidad)
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
