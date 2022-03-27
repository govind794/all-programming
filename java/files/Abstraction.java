abstract class Abstraction{

    int tyre;

    abstract void start();
}

class Car extends Abstraction{

    void start(){
        System.out.println("Car start with key");
    }
}

class Bike extends Abstraction{

    void start(){
        System.out.println("Bike start with kick");
    }

    public static void main(String[] args){
        // Abstraction a = new Abstraction();
        Car c = new Car();
        c.start();

        Bike b = new Bike();
        b.start();
    }
}