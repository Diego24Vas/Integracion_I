import React from 'react';
import '../App.css';
import { Link } from 'react-router-dom';

const ParkingManagement = ({ spaces = {}, vehicles = [] }) => {
    return (
        <div>
            <h1>Gestión de Estacionamiento</h1>
            <Link to="/add-space" className="btn btn-add">Añadir Espacio</Link>
            <Link to="/add-vehicle" className="btn btn-add">Añadir Vehículo</Link>
            <table>
                <thead>
                    <tr>
                        <th>Espacio</th>
                        <th>Estado</th>
                        <th>Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {Object.keys(spaces).map((spaceId) => (
                        <tr key={spaceId}>
                            <td>{spaceId}</td>
                            <td>{spaces[spaceId].estado}</td>
                            <td>
                                {spaces[spaceId].estado === 'Ocupado' ? (
                                    <button className="btn btn-release">Liberar</button>
                                ) : (
                                    <button className="btn btn-reserve">Reservar</button>
                                )}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <h2>Vehículos Registrados</h2>
            <table>
                <thead>
                    <tr>
                        <th>Propietario</th>
                        <th>Patente</th>
                        <th>Espacio</th>
                    </tr>
                </thead>
                <tbody>
                    {vehicles.length > 0 ? (
                        vehicles.map((vehicle, index) => (
                            <tr key={index}>
                                <td>{vehicle.owner_name}</td>
                                <td>{vehicle.vehicle_plate}</td>
                                <td>{vehicle.parking_space}</td>
                            </tr>
                        ))
                    ) : (
                        <tr>
                            <td colSpan="3">No hay vehículos registrados.</td>
                        </tr>
                    )}
                </tbody>
            </table>
        </div>
    );
};

export default ParkingManagement;
