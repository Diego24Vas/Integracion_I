
from datetime import datetime

class Dueño:
    def __init__(self, nombre, apellido, rut, edad, sexo, status):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.edad = edad
        self.sexo = sexo
        self.status = status

    
    def __str__(self):
        return f"Nombre del dueño es: {self.nombre} {self.apellido}\n rut: {self.rut}\n edad: {self.edad}\n sexo: {self.sexo}\n status: {self.status}"
    


class Vehiculo:
    def __init__(self, patente, marca, modelo, color, idDueño):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.idDueño = idDueño


    def __str__(self):
        return f"{self.patente}; {self.marca}; {self.modelo}; {self.color}; {self.idDueño}"



class Registro:
    def __init__(self, idRegistro, vehiculo):
        self.idRegistro = idRegistro
        self.fechaEntrada = None
        self.fechaSalida = None
        self.vehiculo = vehiculo


    def registrar_entrada(self):
        self.fechaEntrada = datetime.now()    
        print(f"El Vehículo con patente {self.vehiculo.patente} se registró su entrada a las {self.fechaEntrada}.")


    def registrar_salida(self):
        if self.fechaEntrada is None:
            print("El vehículo aún no se registra.")


        self.fechaSalida = datetime.now()
        print(f"El vehículo con patente {self.vehiculo.patente} se registró su salida a las {self.fechaSalida}")


    def tiempo_estacionado(self):
        if self.fechaEntrada is None or self.fechaSalida is None:
            print("No se a registrado una Entrada o Salida")
            return None
            
        return f"Su tiempo estacionado es: {self.fechaSalida - self.fechaEntrada}"



class Estacionamiento:
    def __init__(self, idEstac, estacDisp):
        self.idEstac = idEstac
        self.estacDisp = estacDisp
        self.totalEstac = []


    def actualizar_disp(self, vehiculo):  #Básicamente es un 'añadir vehiculo'
        if self.estacDisp > 0:
            self.totalEstac.append(vehiculo)
            self.estacDisp -=1
            print(f"El vehículo {vehiculo.patente} se registró correctamente. Estacionamientos disponibles: {self.estacDisp}")

        else:
            print("No hay espacios disponibles")


    def eliminar_vehiculo(self, vehiculo):
        if vehiculo in self.totalEstac:
            self.totalEstac.remove(vehiculo)
            self.estacDisp +=1
            print("Vehículo eliminado del estacionamiento correctamente")
        

class Encargado:
    def __init__(self, idEncargado, nombre, apellido, edad, sexo):
        self.idEncargado = idEncargado
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
        self.list_dueños = []


    def consultar_disp(self, estacionamiento):
        if estacionamiento.estacDisp > 0:
            print(f"El {estacionamiento.idEstac} se encuentra disponible para uso")
        else:
            print(f"El Estacionamiento {estacionamiento.idEstac} está ocupado")




    def agregar_dueño(self, dueño):
        self.list_dueños.append(dueño)

    
    def lista_dueños(self):
       for dueño in self.list_dueños:
           print(dueño)
