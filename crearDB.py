import sqlite3
#crear conexion con base de datos
conexion = sqlite3.connect('estacionamientosCJP2.db')
#crear cursor
cursor = conexion.cursor()
#crear tabla dueño con sus respectivas columnas
cursor.execute('''
CREATE TABLE Dueño (
    Rut VARCHAR(10) PRIMARY KEY,
    nombre CHAR(10), 
    apellido CHAR(10),
    edad INT(2),
    sexo CHAR(1),
    estatus CHAR(15)
);
''')
#crear tabla encargado con sus respectivas columnas
cursor.execute('''
CREATE TABLE Encargado (
    IdEncargado INT(4) PRIMARY KEY,
    nombre CHAR(10),
    apellido CHAR(10),
    edad INT(2),
    sexo CHAR(1)
);
''')
#crear tabla vehiculo con sus respectivas columnas
cursor.execute('''
CREATE TABLE Vehiculo (
    patente VARCHAR(6) PRIMARY KEY,
    marca CHAR(15),
    modelo CHAR(10),
    color CHAR(10),
    Rut VARCHAR(10),
    FOREIGN KEY (Rut) REFERENCES Dueño(Rut)
);
''')
#crear tabla estacionamiento con sus respectivas columnas
cursor.execute('''
CREATE TABLE Estacionamiento (
    IdEstacionamiento VARCHAR(4) PRIMARY KEY,
    ubicacion CHAR(7),
    preferenciales CHAR(10),
    disponibilidad CHAR(10),
    patente VARCHAR(6),
    FOREIGN KEY (patente) REFERENCES Vehiculo(patente)
);
''')
#crear tabla registro con sus respectivas columnas
cursor.execute('''
CREATE TABLE Registro (
    Id_Registro INT PRIMARY KEY,
    dateEntrada DATETIME,
    dateSalida DATETIME,
    IdEncargado INT(4),
    IdEstacionamiento VARCHAR(4),
    FOREIGN KEY (IdEncargado) REFERENCES Encargado(IdEncargado),
    FOREIGN KEY (IdEstacionamiento) REFERENCES Estacionamiento(IdEstacionamiento)
);
''')
#guardar los cambios
conexion.commit()
#cerrar la conexion con la base de datos
conexion.close()
