"""  1. Gestión de Clientes y Mascotas:
  
  * Crear clientes con atributos como nombre, contacto y dirección.
  * Asociar una o más mascotas a cada cliente. Cada mascota debe tener
  atributos como nombre, especie, raza, edad y un historial de citas."""

class Persona ():
    def __init__(self, nombre, contacto, direccion):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion

class Cliente(Persona):
    def __init__(self, nombre, contacto, direccion):
        super().__init__(nombre, contacto, direccion)
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
    
class Mascota:
    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.citas = []

class Veterinaria:
    def __init__(self):
        self.clientes = []
    
    def registrar_cliente(self, nombre, contacto, direccion):
        cliente = Cliente(nombre, contacto, direccion)
        self.clientes.append(cliente)
        return cliente
    
    def registrar_mascota(self, cliente, nombre, especie, raza, edad):
        mascota = Mascota(nombre, especie, raza, edad)
        cliente.agregar_mascota(mascota)
        return mascota
    
    def mostrar_clientes(self):
        for cliente in self.clientes:
            print(f"Cliente: {cliente.nombre}, Contacto: {cliente.contacto}, Dirección: {cliente.direccion}")
            for mascota in cliente.mascotas:
                print(f" - Mascota: {mascota.nombre}, Especie: {mascota.especie}, Raza: {mascota.raza}, Edad: {mascota.edad}")
                
if __name__ == "__main__":
    vet = Veterinaria()
    cliente1 = vet.registrar_cliente("Ana Pérez", "3123456789", "Calle 123")
    mascota1 = vet.registrar_mascota(cliente1, "Firulais", "Perro", "Labrador", 3)
    mascota2 = vet.registrar_mascota(cliente1, "Fifi", "Gato", "Siames", 8)
    vet.mostrar_clientes()