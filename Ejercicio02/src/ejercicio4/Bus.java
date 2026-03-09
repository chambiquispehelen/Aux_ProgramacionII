package ejercicio4;

public class Bus {

    private int capacidad;
    private int pasajeros;
    private double costoPasaje;

    public Bus(int capacidad) {
        this.capacidad = capacidad;
        this.pasajeros = 0;
        this.costoPasaje = 1.50;
    }

    // a) Subir pasajeros
    public void subirPasajeros(int cantidad) {
        if (pasajeros + cantidad <= capacidad) {
            pasajeros += cantidad;
            System.out.println("Subieron " + cantidad + " pasajeros.");
        } else {
            System.out.println("No hay suficientes asientos disponibles.");
        }
    }

    // b) Cobrar pasaje
    public double cobrarPasaje() {
        return pasajeros * costoPasaje;
    }

    // c) Mostrar asientos disponibles
    public int asientosDisponibles() {
        return capacidad - pasajeros;
    }

    public void mostrarDatos() {
        System.out.println("Capacidad: " + capacidad);
        System.out.println("Pasajeros: " + pasajeros);
        System.out.println("Asientos disponibles: " + asientosDisponibles());
    }
}
