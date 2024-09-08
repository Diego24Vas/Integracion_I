from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__, template_folder='../templates')

# Carpeta de imágenes estáticas
app.config['UPLOAD_FOLDER'] = 'recursos'

# Datos de ejemplo
parking_spaces = {
    'A1': {'estado': 'Libre', 'discapacitado': False, 'sector': 'A'},
    'A2': {'estado': 'Ocupado', 'discapacitado': False, 'sector': 'A'},
    'B1': {'estado': 'Libre', 'discapacitado': True, 'sector': 'B'},
    'B2': {'estado': 'Ocupado', 'discapacitado': False, 'sector': 'B'}
}

# Datos de vehículos
vehicles = []

# URLs de imágenes de los sectores
sector_images = {
    'A': 'sector_a.jpg',
    'B': 'sector_b.jpg'
}

@app.route('/')
def index():
    return render_template('index.html', spaces=parking_spaces, vehicles=vehicles)

@app.route('/add_space.html', methods=['GET', 'POST'])
def add_space():
    if request.method == 'POST':
        space_id = request.form['space_id']
        state = request.form['state']
        disabled = 'disabled' in request.form
        sector = request.form['sector']
        if space_id not in parking_spaces:
            parking_spaces[space_id] = {'estado': state, 'discapacitado': disabled, 'sector': sector}
        return redirect(url_for('index'))
    return render_template('add_space.html')

@app.route('/add_vehicle.html', methods=['GET', 'POST'])
def add_vehicle():
    if request.method == 'POST':
        owner_name = request.form['owner_name']
        vehicle_plate = request.form['vehicle_plate']
        parking_space = request.form['parking_space']
        if parking_space in parking_spaces and parking_spaces[parking_space]['estado'] == 'Libre':
            vehicles.append({
                'owner_name': owner_name,
                'vehicle_plate': vehicle_plate,
                'parking_space': parking_space
            })
            parking_spaces[parking_space]['estado'] = 'Ocupado'
        return redirect(url_for('index'))
    return render_template('add_vehicle.html')

@app.route('/release/<space_id>', methods=['POST'])
def release(space_id):
    if space_id in parking_spaces and parking_spaces[space_id]['estado'] == 'Ocupado':
        parking_spaces[space_id]['estado'] = 'Libre'
        global vehicles
        vehicles = [v for v in vehicles if v['parking_space'] != space_id]
    return redirect(url_for('index'))

@app.route('/get_location', methods=['GET'])
def get_location():
    sector = request.args.get('sector')
    image_filename = sector_images.get(sector)
    image_url = url_for('static_files', filename=image_filename) if image_filename else None
    return render_template('add_space.html', image_url=image_url)
@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
