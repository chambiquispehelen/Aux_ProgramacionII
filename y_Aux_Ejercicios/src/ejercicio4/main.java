package ejercicio4;

public class main {

	public static void main(String[] args) {
		Bus bus1 = new Bus(20);

        bus1.subirPasajeros(10);

        bus1.mostrarDatos();

        double total = bus1.cobrarPasaje();
        System.out.println("Total recaudado: " + total + " Bs");
    }

	}


