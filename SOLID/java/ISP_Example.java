package java;
/**
 * PRINCIPIO I - INTERFACE SEGREGATION PRINCIPLE (SEGREGACIÓN DE INTERFACES)
 * 
 * Las clases no deben estar obligadas a implementar métodos que no usan.
 * Es mejor tener varias interfaces pequeñas que una enorme.
 * 
 * Analogía: Controles remotos específicos - el control de la TV no debería 
 * tener botones para abrir el refrigerador.
 */

// ❌ VIOLACIÓN DEL PRINCIPIO ISP
// Interfaz monolítica que obliga a implementar métodos no utilizados

interface BadMultiFunctionDevice {
    // Funciones de impresora
    void print(String document);
    void printColor(String document);
    
    // Funciones de scanner
    String scan();
    String scanToEmail(String email);
    
    // Funciones de fax
    void sendFax(String document, String number);
    void receiveFax();
    
    // Funciones de copiadora
    void copy(String document);
    void copyColor(String document);
}

// ❌ Una impresora simple se ve obligada a implementar funciones que no tiene
class BadSimplePrinter implements BadMultiFunctionDevice {
    @Override
    public void print(String document) {
        System.out.println("Imprimiendo: " + document);
    }
    
    @Override
    public void printColor(String document) {
        // ❌ Esta impresora no imprime a color
        throw new UnsupportedOperationException("Esta impresora no soporta color");
    }
    
    @Override
    public String scan() {
        // ❌ Esta impresora no puede escanear
        throw new UnsupportedOperationException("Esta impresora no puede escanear");
    }
    
    @Override
    public String scanToEmail(String email) {
        throw new UnsupportedOperationException("Esta impresora no puede escanear");
    }
    
    @Override
    public void sendFax(String document, String number) {
        // ❌ Esta impresora no puede enviar fax
        throw new UnsupportedOperationException("Esta impresora no puede enviar fax");
    }
    
    @Override
    public void receiveFax() {
        throw new UnsupportedOperationException("Esta impresora no puede recibir fax");
    }
    
    @Override
    public void copy(String document) {
        // ❌ Esta impresora no puede copiar
        throw new UnsupportedOperationException("Esta impresora no puede copiar");
    }
    
    @Override
    public void copyColor(String document) {
        throw new UnsupportedOperationException("Esta impresora no puede copiar");
    }
}

// ✅ APLICACIÓN CORRECTA DEL PRINCIPIO ISP
// Interfaces segregadas y específicas

interface Printer {
    void print(String document);
}

interface ColorPrinter extends Printer {
    void printColor(String document);
}

interface Scanner {
    String scan();
    String scanToEmail(String email);
}

interface FaxMachine {
    void sendFax(String document, String number);
    void receiveFax();
}

interface Copier {
    void copy(String document);
}

interface ColorCopier extends Copier {
    void copyColor(String document);
}

// ✅ Implementaciones específicas que solo implementan lo que necesitan

class SimplePrinter implements Printer {
    private String model;
    
    public SimplePrinter(String model) {
        this.model = model;
    }
    
    @Override
    public void print(String document) {
        System.out.println("[" + model + "] Imprimiendo: " + document);
    }
}

class LaserPrinter implements ColorPrinter {
    private String model;
    
    public LaserPrinter(String model) {
        this.model = model;
    }
    
    @Override
    public void print(String document) {
        System.out.println("[" + model + "] Imprimiendo en blanco y negro: " + document);
    }
    
    @Override
    public void printColor(String document) {
        System.out.println("[" + model + "] Imprimiendo a color: " + document);
    }
}

class DocumentScanner implements Scanner {
    private String model;
    
    public DocumentScanner(String model) {
        this.model = model;
    }
    
    @Override
    public String scan() {
        String scannedContent = "Documento escaneado por " + model;
        System.out.println("[" + model + "] Escaneando documento...");
        return scannedContent;
    }
    
    @Override
    public String scanToEmail(String email) {
        String content = scan();
        System.out.println("[" + model + "] Enviando escaneo a: " + email);
        return content;
    }
}

class FaxDevice implements FaxMachine {
    private String model;
    
    public FaxDevice(String model) {
        this.model = model;
    }
    
    @Override
    public void sendFax(String document, String number) {
        System.out.println("[" + model + "] Enviando fax a " + number + ": " + document);
    }
    
    @Override
    public void receiveFax() {
        System.out.println("[" + model + "] Recibiendo fax...");
    }
}

// ✅ Dispositivo multifuncional que implementa múltiples interfaces según sus capacidades
class MultiFunctionPrinter implements ColorPrinter, Scanner, Copier, ColorCopier {
    private String model;
    
    public MultiFunctionPrinter(String model) {
        this.model = model;
    }
    
    @Override
    public void print(String document) {
        System.out.println("[" + model + "] Imprimiendo: " + document);
    }
    
    @Override
    public void printColor(String document) {
        System.out.println("[" + model + "] Imprimiendo a color: " + document);
    }
    
    @Override
    public String scan() {
        System.out.println("[" + model + "] Escaneando...");
        return "Documento escaneado por " + model;
    }
    
    @Override
    public String scanToEmail(String email) {
        String content = scan();
        System.out.println("[" + model + "] Enviando escaneo a: " + email);
        return content;
    }
    
    @Override
    public void copy(String document) {
        System.out.println("[" + model + "] Copiando: " + document);
    }
    
    @Override
    public void copyColor(String document) {
        System.out.println("[" + model + "] Copiando a color: " + document);
    }
}

// Ejemplo adicional: Trabajadores con diferentes habilidades
interface Worker {
    void work();
}

interface Eater {
    void eat();
}

interface Sleeper {
    void sleep();
}

// ❌ Interfaz que viola ISP
interface BadWorker {
    void work();
    void eat();
    void sleep();
}

// ✅ Implementaciones segregadas
class HumanWorker implements Worker, Eater, Sleeper {
    private String name;
    
    public HumanWorker(String name) {
        this.name = name;
    }
    
    @Override
    public void work() {
        System.out.println(name + " está trabajando");
    }
    
    @Override
    public void eat() {
        System.out.println(name + " está comiendo");
    }
    
    @Override
    public void sleep() {
        System.out.println(name + " está durmiendo");
    }
}

class RobotWorker implements Worker {
    private String model;
    
    public RobotWorker(String model) {
        this.model = model;
    }
    
    @Override
    public void work() {
        System.out.println("Robot " + model + " está trabajando 24/7");
    }
    
    // ✅ El robot no necesita comer ni dormir, así que no implementa esas interfaces
}

// Clases que manejan las interfaces segregadas
class OfficeManager {
    public void managePrinting(Printer printer, String document) {
        printer.print(document);
    }
    
    public void manageColorPrinting(ColorPrinter printer, String document) {
        printer.printColor(document);
    }
    
    public void manageScanning(Scanner scanner) {
        scanner.scan();
    }
    
    public void manageCopying(Copier copier, String document) {
        copier.copy(document);
    }
}

class WorkManager {
    public void assignWork(Worker worker) {
        worker.work();
    }
    
    public void scheduleBreak(Eater eater) {
        eater.eat();
    }
    
    public void scheduleRest(Sleeper sleeper) {
        sleeper.sleep();
    }
}

// Ejemplo de uso
public class ISP_Example {
    public static void main(String[] args) {
        System.out.println("=== EJEMPLO ISP - PRINCIPIO DE SEGREGACIÓN DE INTERFACES ===\n");
        
        // Ejemplo con dispositivos de oficina
        System.out.println("🖨️ Dispositivos de oficina:");
        OfficeManager manager = new OfficeManager();
        
        // Cada dispositivo implementa solo las interfaces que necesita
        SimplePrinter simple = new SimplePrinter("HP LaserJet Basic");
        LaserPrinter laser = new LaserPrinter("Canon Color Laser");
        DocumentScanner scanner = new DocumentScanner("Epson Scanner Pro");
        MultiFunctionPrinter mfp = new MultiFunctionPrinter("Brother MFC-9000");
        
        // Uso específico según las capacidades
        manager.managePrinting(simple, "Documento simple");
        manager.managePrinting(laser, "Documento profesional");
        manager.manageColorPrinting(laser, "Presentación colorida");
        manager.manageScanning(scanner);
        manager.manageScanning(mfp);
        manager.manageCopying(mfp, "Documento importante");
        
        // Ejemplo con trabajadores
        System.out.println("\n👷 Gestión de trabajadores:");
        WorkManager workManager = new WorkManager();
        
        HumanWorker human = new HumanWorker("Ana");
        RobotWorker robot = new RobotWorker("R2D2");
        
        // Asignar trabajo a todos
        workManager.assignWork(human);
        workManager.assignWork(robot);
        
        // Solo los humanos necesitan descansos
        workManager.scheduleBreak(human);
        workManager.scheduleRest(human);
        
        // ✅ No podemos llamar scheduleBreak(robot) porque Robot no implementa Eater
        
        System.out.println("\n✅ Ventajas del ISP:");
        System.out.println("- Las clases solo implementan métodos que realmente usan");
        System.out.println("- Interfaces pequeñas y cohesivas");
        System.out.println("- Menor acoplamiento entre componentes");
        System.out.println("- Facilita el testing y la extensibilidad");
        System.out.println("- Reduce la complejidad del código");
    }
}