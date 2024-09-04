import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import ParkingManagement from './components/ParkingManagement';
import AddSpace from './components/AddSpace';
import AddVehicle from './components/AddVehicle';
import './App.css';

function App() {
    const [spaces, setSpaces] = useState({});
    const [vehicles, setVehicles] = useState([]);

    useEffect(() => {
        // Simulación de carga de datos
        // Aquí puedes realizar llamadas a API para obtener los datos
        setSpaces({
            'A1': { estado: 'Libre' },
            'A2': { estado: 'Ocupado' },
        });
        setVehicles([
            { owner_name: 'Juan Pérez', vehicle_plate: 'ABC123', parking_space: 'A1' }
        ]);
    }, []);

    return (
        <Router>
            <Routes>
                <Route path="/" element={<ParkingManagement spaces={spaces} vehicles={vehicles} />} />
                <Route path="/add-space" element={<AddSpace />} />
                <Route path="/add-vehicle" element={<AddVehicle />} />
            </Routes>
        </Router>
    );
}

export default App;
