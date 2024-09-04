import React, { useState } from 'react';

function AddSpace() {
  const [spaceId, setSpaceId] = useState('');
  const [state, setState] = useState('Libre');
  const [disabled, setDisabled] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log({ spaceId, state, disabled });
  };

  return (
    <div>
      <h1>Añadir Espacio de Estacionamiento</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="space_id">ID del Espacio:</label>
        <input 
          type="text" 
          id="space_id" 
          value={spaceId} 
          onChange={(e) => setSpaceId(e.target.value)} 
          required 
        />
        <br />
        <label htmlFor="state">Estado:</label>
        <select 
          id="state" 
          value={state} 
          onChange={(e) => setState(e.target.value)}>
          <option value="Libre">Libre</option>
          <option value="Ocupado">Ocupado</option>
        </select>
        <br />
        <label htmlFor="disabled">Espacio para Discapacitados:</label>
        <input 
          type="checkbox" 
          id="disabled" 
          checked={disabled} 
          onChange={(e) => setDisabled(e.target.checked)} 
        />
        <br />
        <button type="submit">Añadir Espacio</button>
      </form>
    </div>
  );
}

export default AddSpace;
