package ejercicio5;


import java.util.ArrayList;

public class Minecraft {

    // ATRIBUTOS
    ArrayList<String> jugadores = new ArrayList();
    ArrayList<Integer> diamantes = new ArrayList();

    // CONSTRUCTOR
    public Minecraft() {
    }

    // a) agregar jugador
    public void agregarJugador(String nombre, int d) {
        jugadores.add(nombre);
        diamantes.add(d);
    }

    // b) mostrar stacks de diamantes
    public void mostrarStacks() {

        for (int i = 0; i < jugadores.size(); i++) {

            int stacks = diamantes.get(i) / 64;

            System.out.println(jugadores.get(i) + 
            " tiene " + stacks + " stacks de diamantes");
        }
    }

    // c) jugador con más diamantes
    public void jugadorMasDiamantes() {

        int mayor = diamantes.get(0);
        String jugadorMayor = jugadores.get(0);

        for (int i = 0; i < diamantes.size(); i++) {

            if (diamantes.get(i) > mayor) {
                mayor = diamantes.get(i);
                jugadorMayor = jugadores.get(i);
            }
        }

        System.out.println("Jugador con más diamantes: " + jugadorMayor);
    }

    // d) total de diamantes
    public void totalDiamantes() {

        int suma = 0;

        for (int i = 0; i < diamantes.size(); i++) {
            suma += diamantes.get(i);
        }

        System.out.println("Total de diamantes: " + suma);
    }

  
}