package ejercicio5;

public class main {

	  public static void main(String[] args) {

	        Minecraft m = new Minecraft();

	        m.agregarJugador("Steve", 120);
	        m.agregarJugador("Alex", 65);
	        m.agregarJugador("Juan", 200);

	        m.mostrarStacks();
	        m.jugadorMasDiamantes();
	        m.totalDiamantes();
	    }
}
