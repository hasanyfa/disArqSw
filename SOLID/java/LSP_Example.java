package java;
/**
 * PRINCIPIO L - LISKOV SUBSTITUTION PRINCIPLE (SUSTITUCIÓN DE LISKOV)
 * 
 * Las clases hijas deben poder reemplazar a sus clases padre sin alterar 
 * el correcto funcionamiento del programa.
 * 
 * Analogía: Vehículos intercambiables - si alquilas un "auto" y te entregan 
 * una bicicleta, se rompe la expectativa del comportamiento.
 */

// ❌ VIOLACIÓN DEL PRINCIPIO LSP
// No todos los pájaros pueden volar, por lo que Penguin viola LSP

abstract class BadBird {
    protected String name;
    
    public BadBird(String name) {
        this.name = name;
    }
    
    // ❌ Método que no todos los pájaros pueden cumplir
    public abstract void fly();
    
    public void eat() {
        System.out.println(name + " está comiendo");
    }
}

class BadEagle extends BadBird {
    public BadEagle() {
        super("Águila");
    }
    
    @Override
    public void fly() {
        System.out.println(name + " vuela majestuosamente");
    }
}

class BadPenguin extends BadBird {
    public BadPenguin() {
        super("Pingüino");
    }
    
    @Override
    public void fly() {
        // ❌ Viola LSP: Un pingüino no puede volar pero debe implementar el método
        throw new UnsupportedOperationException("Los pingüinos no pueden volar!");
    }
}

// ✅ APLICACIÓN CORRECTA DEL PRINCIPIO LSP
// Jerarquía bien diseñada que respeta el comportamiento esperado

abstract class Bird {
    protected String name;
    
    public Bird(String name) {
        this.name = name;
    }
    
    public void eat() {
        System.out.println(name + " está comiendo");
    }
    
    public void sleep() {
        System.out.println(name + " está durmiendo");
    }
    
    public String getName() {
        return name;
    }
}

// Interfaz específica para pájaros que pueden volar
interface Flyable {
    void fly();
    int getFlightSpeed();
}

// Interfaz específica para pájaros que pueden nadar
interface Swimmable {
    void swim();
    int getSwimSpeed();
}

class Eagle extends Bird implements Flyable {
    public Eagle() {
        super("Águila");
    }
    
    @Override
    public void fly() {
        System.out.println(name + " vuela alto en el cielo");
    }
    
    @Override
    public int getFlightSpeed() {
        return 80; // km/h
    }
}

class Penguin extends Bird implements Swimmable {
    public Penguin() {
        super("Pingüino");
    }
    
    @Override
    public void swim() {
        System.out.println(name + " nada graciosamente bajo el agua");
    }
    
    @Override
    public int getSwimSpeed() {
        return 35; // km/h
    }
}

class Duck extends Bird implements Flyable, Swimmable {
    public Duck() {
        super("Pato");
    }
    
    @Override
    public void fly() {
        System.out.println(name + " vuela sobre el lago");
    }
    
    @Override
    public int getFlightSpeed() {
        return 65; // km/h
    }
    
    @Override
    public void swim() {
        System.out.println(name + " nada en el estanque");
    }
    
    @Override
    public int getSwimSpeed() {
        return 8; // km/h
    }
}

// Ejemplo adicional: Formas geométricas con área
abstract class Shape {
    protected String color;
    
    public Shape(String color) {
        this.color = color;
    }
    
    public abstract double calculateArea();
    public abstract double calculatePerimeter();
    
    public String getColor() {
        return color;
    }
}

class GoodRectangle extends Shape {
    private double width;
    private double height;
    
    public GoodRectangle(String color, double width, double height) {
        super(color);
        this.width = width;
        this.height = height;
    }
    
    @Override
    public double calculateArea() {
        return width * height;
    }
    
    @Override
    public double calculatePerimeter() {
        return 2 * (width + height);
    }
    
    public void setWidth(double width) {
        this.width = width;
    }
    
    public void setHeight(double height) {
        this.height = height;
    }
    
    public double getWidth() { return width; }
    public double getHeight() { return height; }
}

// ✅ Square extiende Rectangle respetando LSP
class Square extends GoodRectangle {
    public Square(String color, double side) {
        super(color, side, side);
    }
    
    @Override
    public void setWidth(double width) {
        super.setWidth(width);
        super.setHeight(width); // Mantiene la forma cuadrada
    }
    
    @Override
    public void setHeight(double height) {
        super.setHeight(height);
        super.setWidth(height); // Mantiene la forma cuadrada
    }
}

class GoodCircle extends Shape {
    private double radius;
    
    public GoodCircle(String color, double radius) {
        super(color);
        this.radius = radius;
    }
    
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
    
    @Override
    public double calculatePerimeter() {
        return 2 * Math.PI * radius;
    }
    
    public double getRadius() { return radius; }
}

// Clases que trabajan con las abstracciones
class BirdCare {
    public void feedBird(Bird bird) {
        System.out.println("Alimentando a " + bird.getName());
        bird.eat();
    }
    
    public void exerciseFlyingBird(Flyable flyingBird) {
        System.out.println("Ejercitando pájaro volador");
        flyingBird.fly();
        System.out.println("Velocidad de vuelo: " + flyingBird.getFlightSpeed() + " km/h");
    }
    
    public void exerciseSwimmingBird(Swimmable swimmingBird) {
        System.out.println("Ejercitando pájaro nadador");
        swimmingBird.swim();
        System.out.println("Velocidad de nado: " + swimmingBird.getSwimSpeed() + " km/h");
    }
}

class ShapeCalculator {
    public void printShapeInfo(Shape shape) {
        System.out.printf("Forma %s - Área: %.2f, Perímetro: %.2f%n",
            shape.getColor(),
            shape.calculateArea(),
            shape.calculatePerimeter());
    }
    
    public double getTotalArea(Shape[] shapes) {
        double total = 0;
        for (Shape shape : shapes) {
            total += shape.calculateArea();
        }
        return total;
    }
}

// Ejemplo de uso
public class LSP_Example {
    public static void main(String[] args) {
        System.out.println("=== EJEMPLO LSP - PRINCIPIO DE SUSTITUCIÓN DE LISKOV ===\n");
        
        // Ejemplo con pájaros
        System.out.println("🐦 Manejo de pájaros:");
        BirdCare birdCare = new BirdCare();
        
        Bird[] birds = {
            new Eagle(),
            new Penguin(),
            new Duck()
        };
        
        // ✅ Todos los pájaros pueden ser alimentados (comportamiento común)
        for (Bird bird : birds) {
            birdCare.feedBird(bird);
        }
        
        System.out.println("\n🛩️ Ejercitando pájaros voladores:");
        Eagle eagle = new Eagle();
        Duck duck = new Duck();
        
        birdCare.exerciseFlyingBird(eagle);
        birdCare.exerciseFlyingBird(duck);
        
        System.out.println("\n🏊 Ejercitando pájaros nadadores:");
        Penguin penguin = new Penguin();
        birdCare.exerciseSwimmingBird(penguin);
        birdCare.exerciseSwimmingBird(duck);
        
        // Ejemplo con formas geométricas
        System.out.println("\n📐 Manejo de formas geométricas:");
        ShapeCalculator calculator = new ShapeCalculator();
        
        Shape[] shapes = {
            new GoodRectangle("Rojo", 5, 3),
            new Square("Azul", 4),
            new GoodCircle("Verde", 3)
        };
        
        // ✅ Todas las formas pueden ser sustituidas sin problemas
        for (Shape shape : shapes) {
            calculator.printShapeInfo(shape);
        }
        
        System.out.printf("\nÁrea total de todas las formas: %.2f%n", 
            calculator.getTotalArea(shapes));
        
        System.out.println("\n✅ Ventajas del LSP:");
        System.out.println("- Las subclases pueden reemplazar a sus superclases");
        System.out.println("- Comportamiento predecible y consistente");
        System.out.println("- Polimorfismo seguro y confiable");
        System.out.println("- Facilita el testing y mantenimiento");
    }
}