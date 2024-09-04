import React, { useState, useEffect } from 'react';


function AddVehicle() {
  const [ownerName, setOwnerName] = useState('');
  const [vehiclePlate, setVehiclePlate] = useState('');
  const [parkingSpace, setParkingSpace] = useState('');
  const [spaces, setSpaces] = useState([]);

  useEffect(() => {
    // Aquí puedes hacer una petición al backend para obtener los espacios disponibles
    // Usando datos simulados por ahora
    setSpaces([
      { id: 'A1', estado: 'Libre' },
      { id: 'B1', estado: 'Libre' }
    ]);
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    // Aquí deberías hacer la petición al backend para añadir el vehículo
    console.log({ ownerName, vehiclePlate, parkingSpace });
  };

  return (
    <div>
      <h1>Añadir Vehículo</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="owner_name">Nombre del Propietario:</label>
        <input 
          type="text" 
          id="owner_name" 
          value={ownerName} 
          onChange={(e) => setOwnerName(e.target.value)} 
          required 
        />
        <br />
        <label htmlFor="vehicle_plate">Patente del Vehículo:</label>
        <input 
          type="text" 
          id="vehicle_plate" 
          value={vehiclePlate} 
          onChange={(e) => setVehiclePlate(e.target.value)} 
          required 
        />
        <br />
        <label htmlFor="parking_space">Espacio de Estacionamiento:</label>
        <select 
          id="parking_space" 
          value={parkingSpace} 
          onChange={(e) => setParkingSpace(e.target.value)}>
          {spaces.map(space => (
            <option key={space.id} value={space.id}>{space.id}</option>
          ))}
        </select>
        <br />
        <button type="submit">Añadir Vehículo</button>
      </form>
    </div>
  );
}

export default AddVehicle;
