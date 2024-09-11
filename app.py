from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# Diccionario con los espacios de estacionamiento (ejemplo)
espacios_estacionamiento = {
    'A1': {'estado': 'Libre', 'discapacitado': False},
    'A2': {'estado': 'Ocupado', 'discapacitado': False},
    'B1': {'estado': 'Libre', 'discapacitado': True},
    'B2': {'estado': 'Ocupado', 'discapacitado': False}
}

# Lista para almacenar los vehículos registrados
vehiculos = []

# Ruta principal que muestra la página de gestión de estacionamiento
@app.route('/')
def inicio():
    # Renderiza la plantilla `index.html` con la lista de espacios y vehículos
    return render_template('index', espacios=espacios_estacionamiento, vehiculos=vehiculos)

# Ruta para añadir un nuevo espacio de estacionamiento
@app.route('/anadir_espacio', methods=['GET', 'POST'])
def anadir_espacio():
    if request.method == 'POST':
        # Captura los datos del formulario
        id_espacio = request.form['id_espacio']
        estado = request.form['estado']
        discapacitado = 'discapacitado' in request.form
        # Añade el nuevo espacio si no existe
        if id_espacio not in espacios_estacionamiento:
            espacios_estacionamiento[id_espacio] = {'estado': estado, 'discapacitado': discapacitado}
        # Redirige a la página principal
        return redirect(url_for('inicio'))
    # Renderiza la plantilla para añadir espacios
    return render_template('anadir_espacio')

# Ruta para añadir un vehículo al registro
@app.route('/anadir_vehiculo', methods=['GET', 'POST'])
def anadir_vehiculo():
    if request.method == 'POST':
        # Captura los datos del formulario
        nombre_propietario = request.form['nombre_propietario']
        patente_vehiculo = request.form['patente_vehiculo']
        espacio_estacionamiento = request.form['espacio_estacionamiento']
        # Verifica si el espacio está libre y lo asigna al vehículo
        if espacio_estacionamiento in espacios_estacionamiento and espacios_estacionamiento[espacio_estacionamiento]['estado'] == 'Libre':
            vehiculos.append({
                'nombre_propietario': nombre_propietario,
                'patente_vehiculo': patente_vehiculo,
                'espacio_estacionamiento': espacio_estacionamiento
            })
            # Cambia el estado del espacio a 'Ocupado'
            espacios_estacionamiento[espacio_estacionamiento]['estado'] = 'Ocupado'
        # Redirige a la página principal
        return redirect(url_for('inicio'))
    # Renderiza la plantilla para añadir vehículos
    return render_template('anadir_vehiculo.html')

# Ruta para liberar un espacio de estacionamiento
@app.route('/liberar/<id_espacio>', methods=['POST'])
def liberar(id_espacio):
    # Verifica si el espacio está ocupado
    if id_espacio in espacios_estacionamiento and espacios_estacionamiento[id_espacio]['estado'] == 'Ocupado':
        # Cambia el estado a 'Libre'
        espacios_estacionamiento[id_espacio]['estado'] = 'Libre'
        # Elimina el vehículo asociado al espacio liberado
        global vehiculos
        vehiculos = [v for v in vehiculos if v['espacio_estacionamiento'] != id_espacio]
    # Redirige a la página principal
    return redirect(url_for('inicio'))

# Inicia la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
