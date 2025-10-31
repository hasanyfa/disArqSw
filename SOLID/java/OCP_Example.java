package java;
/**
 * PRINCIPIO O - OPEN/CLOSED PRINCIPLE (ABIERTO/CERRADO)
 * 
 * El código debe estar abierto a la extensión, pero cerrado a la modificación.
 * Podemos agregar nuevas funcionalidades sin cambiar las clases existentes.
 * 
 * Analogía: Enchufes y adaptadores - el enchufe no cambia, pero puedes conectar distintos aparatos.
 */

// ❌ VIOLACIÓN DEL PRINCIPIO OCP
// Esta clase debe modificarse cada vez que se agrega una nueva forma geométrica
class BadAreaCalculator {
    public double calculateArea(Object shape) {
        if (shape instanceof Rectangle) {
            Rectangle rectangle = (Rectangle) shape;
            return rectangle.width * rectangle.height;
        } else if (shape instanceof Circle) {
            Circle circle = (Circle) shape;
            return Math.PI * circle.radius * circle.radius;
        }
        // ❌ Si queremos agregar Triangle, debemos MODIFICAR esta clase
        // else if (shape instanceof Triangle) { ... }
        
        return 0;
    }
}

// Clases auxiliares para el ejemplo incorrecto
class Rectangle {
    public double width;
    public double height;
    
    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
}

class Circle {
    public double radius;
    
    public Circle(double radius) {
        this.radius = radius;
    }
}

// ✅ APLICACIÓN CORRECTA DEL PRINCIPIO OCP
// Definimos una interfaz que está cerrada a modificación pero abierta a extensión

interface Shape {
    double calculateArea();
    String getShapeType();
}

// Implementaciones específicas - EXTENSIÓN sin modificación
class GoodRectangle implements Shape {
    private double width;
    private double height;
    
    public GoodRectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }
    
    @Override
    public double calculateArea() {
        return width * height;
    }
    
    @Override
    public String getShapeType() {
        return "Rectángulo";
    }
}

class GoodCircle implements Shape {
    private double radius;
    
    public GoodCircle(double radius) {
        this.radius = radius;
    }
    
    @Override
    public double calculateArea() {
        return Math.PI * radius * radius;
    }
    
    @Override
    public String getShapeType() {
        return "Círculo";
    }
}

// ✅ Nueva forma agregada SIN MODIFICAR código existente
class Triangle implements Shape {
    private double base;
    private double height;
    
    public Triangle(double base, double height) {
        this.base = base;
        this.height = height;
    }
    
    @Override
    public double calculateArea() {
        return (base * height) / 2;
    }
    
    @Override
    public String getShapeType() {
        return "Triángulo";
    }
}

// Esta clase NUNCA necesita modificarse cuando agregamos nuevas formas
class GoodAreaCalculator {
    public double calculateArea(Shape shape) {
        return shape.calculateArea();
    }
    
    public void printShapeInfo(Shape shape) {
        System.out.printf("%s - Área: %.2f%n", 
            shape.getShapeType(), 
            shape.calculateArea());
    }
}

// Ejemplo adicional: Sistema de descuentos extensible
interface DiscountStrategy {
    double applyDiscount(double amount);
    String getDiscountType();
}

class RegularCustomerDiscount implements DiscountStrategy {
    @Override
    public double applyDiscount(double amount) {
        return amount * 0.95; // 5% descuento
    }
    
    @Override
    public String getDiscountType() {
        return "Cliente Regular (5%)";
    }
}

class VIPCustomerDiscount implements DiscountStrategy {
    @Override
    public double applyDiscount(double amount) {
        return amount * 0.85; // 15% descuento
    }
    
    @Override
    public String getDiscountType() {
        return "Cliente VIP (15%)";
    }
}

// ✅ Nueva estrategia agregada SIN MODIFICAR código existente
class StudentDiscount implements DiscountStrategy {
    @Override
    public double applyDiscount(double amount) {
        return amount * 0.80; // 20% descuento
    }
    
    @Override
    public String getDiscountType() {
        return "Descuento Estudiante (20%)";
    }
}

class PriceCalculator {
    public double calculateFinalPrice(double originalPrice, DiscountStrategy discount) {
        return discount.applyDiscount(originalPrice);
    }
}

// Ejemplo de uso
public class OCP_Example {
    public static void main(String[] args) {
        System.out.println("=== EJEMPLO OCP - PRINCIPIO ABIERTO/CERRADO ===\n");
        
        // Ejemplo con formas geométricas
        GoodAreaCalculator calculator = new GoodAreaCalculator();
        
        Shape rectangle = new GoodRectangle(5, 3);
        Shape circle = new GoodCircle(4);
        Shape triangle = new Triangle(6, 8);
        
        System.out.println("📐 Cálculo de áreas:");
        calculator.printShapeInfo(rectangle);
        calculator.printShapeInfo(circle);
        calculator.printShapeInfo(triangle);
        
        // Ejemplo con descuentos
        System.out.println("\n💰 Sistema de descuentos:");
        PriceCalculator priceCalc = new PriceCalculator();
        double originalPrice = 100.0;
        
        DiscountStrategy[] strategies = {
            new RegularCustomerDiscount(),
            new VIPCustomerDiscount(),
            new StudentDiscount()
        };
        
        for (DiscountStrategy strategy : strategies) {
            double finalPrice = priceCalc.calculateFinalPrice(originalPrice, strategy);
            System.out.printf("%s: $%.2f → $%.2f%n", 
                strategy.getDiscountType(), 
                originalPrice, 
                finalPrice);
        }
        
        System.out.println("\n✅ Ventajas del OCP:");
        System.out.println("- Extensión sin modificación del código existente");
        System.out.println("- Reduce el riesgo de introducir bugs");
        System.out.println("- Facilita el mantenimiento y testing");
        System.out.println("- Permite polimorfismo efectivo");
    }
}