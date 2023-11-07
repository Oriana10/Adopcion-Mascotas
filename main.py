class Animal:
    def __init__(self, nombre, raza, edad, estado="No adoptado"):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.estado = estado

    def __str__(self):
        return f"Nombre: {self.nombre}, Raza: {self.raza}, Edad: {self.edad}, Estado: {self.estado}"

    def adoptar(self):
        self.estado = "Adoptado"


class Perro(Animal):
    def __init__(self, nombre, raza, edad, tamaño, estado="No adoptado"):
        super().__init__(nombre, raza, edad, estado)
        self.tamaño = tamaño


class Gato(Animal):
    def __init__(self, nombre, raza, edad, estado="No adoptado"):
        super().__init__(nombre, raza, edad, estado)


class Persona:
    def __init__(self, nombre, apellido, edad, documento):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.documento = documento
        self.mascota = None

    def __str__(self):
        mascota_nombre = self.mascota.nombre if self.mascota else 'Ninguno'
        mascota_tipo = type(self.mascota).__name__ if self.mascota else 'Ninguno'
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Documento: {self.documento}, Mascota: {mascota_nombre} ({mascota_tipo})"

    def adoptar_mascota(self, animal):
        if not self.tiene_mascota():
            self.mascota = animal

    def tiene_mascota(self):
        return self.mascota is not None


def adoptarMascota(persona, mascota):
    if not persona.tiene_mascota() and mascota.estado == "No adoptado":
        persona.adoptar_mascota(mascota)
        mascota.adoptar()
        print(f"{persona.nombre} ha adoptado a {mascota.nombre} ({type(mascota).__name__}).")
    else:
        print("La persona ya tiene una mascota o la mascota ya ha sido adoptada.")

def mostrarAnimalesDisponibles(animales):
    print("Lista de animales disponibles para adopción:")
    for animal in animales:
        print(f"{animal.nombre} - Estado: {'Adoptado' if animal.estado == 'Adoptado' else 'Disponible'}")

def mostrarPersonasConMascotas(personas):
    print("Personas con sus mascotas adoptadas:")
    for persona in personas:
        if persona.tiene_mascota():
            print(f"{persona.nombre} tiene a {persona.mascota.nombre} ({type(persona.mascota).__name__}).")

def mostrarPersonas(personas):
    for persona in personas:
      print(f"{persona.nombre}")

def buscarPersonaPorNombre(personas, nombre):
  for persona in personas:
    if persona.nombre == nombre:
      return persona
  return None

def buscarMascotaorNombre(animales, nombre):
  for animal in animales:
    if animal.nombre == nombre:
      return animal
  return None

def main():
    perro1 = Perro("Pupi", "Labrador", 3, "grande")
    perro2 = Perro("Tomi", "Golden Retriever", 2, "grande")
    perro3 = Perro("Paloma", "Galgo", 3, "grande")
    gato1 = Gato("Michi", "Siamés", 2)
    gato2 = Gato("Maxi", "Persa", 4)
    persona1 = Persona("Juan", "Pérez", 30, "12345678")
    persona2 = Persona("María", "Gómez", 25, "87654321")

    personas = [persona1, persona2]
    animales = [perro1, perro2, perro3, gato1, gato2]

    print("Adopcion")

    while True:
        print("1. Mostrar animales disponibles para adopción")
        print("2. Mostrar personas con sus mascotas adoptadas")
        print("3. Adoptar una mascota")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            mostrarAnimalesDisponibles(animales)
        elif opcion == '2':
            if any(personas):
              print("La lista de personas con mascotas está vacía")
            else:
              mostrarPersonasConMascotas(personas)
        elif opcion == '3':
            mostrarPersonas(personas)
            nombre_persona = input("Ingrese el nombre de la persona que quiere adoptar una mascota: ")
            persona = buscarPersonaPorNombre(personas, nombre_persona)
            if persona:
                mostrarAnimalesDisponibles(animales)
                nombre_mascota = input("Ingrese el nombre de la mascota que desea adoptar: ")
                mascota = buscarMascotaorNombre(animales, nombre_mascota)
                if mascota:
                    adoptarMascota(persona, mascota)
                else:
                    print("La mascota no se encontró en la lista.")
            else:
                print("La persona no se encontró en la lista.")
        elif opcion == '4':
            break

main()
