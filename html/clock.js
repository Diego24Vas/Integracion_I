function updateClock() {
    const now = new Date();
    const hours = now.getHours().toString().padStart(2, '0');
    const minutes = now.getMinutes().toString().padStart(2, '0');
    const seconds = now.getSeconds().toString().padStart(2, '0');
    const currentTime = `${hours}:${minutes}:${seconds}`;
    document.getElementById('clock').textContent = currentTime;
}

// Actualizar el reloj cada segundo
setInterval(updateClock, 1000);

// Mostrar la hora al cargar la página
updateClock();
