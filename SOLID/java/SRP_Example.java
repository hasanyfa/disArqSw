package java;
/**
 * PRINCIPIO S - SINGLE RESPONSIBILITY PRINCIPLE (RESPONSABILIDAD ÚNICA)
 * 
 * Una clase debe tener una sola razón para cambiar, es decir, una sola responsabilidad.
 * 
 * Analogía: El chef del restaurante - cada persona tiene su rol específico.
 */

// ❌ VIOLACIÓN DEL PRINCIPIO SRP
// Esta clase tiene múltiples responsabilidades: generar, formatear, imprimir y guardar reportes
class BadReport {
    private String data;
    
    public BadReport(String data) {
        this.data = data;
    }
    
    // Responsabilidad 1: Generar contenido del reporte
    public String generateContent() {
        return "Reporte generado con datos: " + data;
    }
    
    // Responsabilidad 2: Formatear el reporte
    public String formatToHTML() {
        return "<html><body>" + generateContent() + "</body></html>";
    }
    
    // Responsabilidad 3: Imprimir el reporte
    public void printReport() {
        System.out.println("Imprimiendo: " + formatToHTML());
    }
    
    // Responsabilidad 4: Guardar el reporte en archivo
    public void saveToFile(String filename) {
        System.out.println("Guardando reporte en archivo: " + filename);
        // Lógica para guardar archivo...
    }
}

// ✅ APLICACIÓN CORRECTA DEL PRINCIPIO SRP
// Cada clase tiene una sola responsabilidad

// Responsabilidad única: Generar contenido del reporte
class ReportGenerator {
    public String generateContent(String data) {
        return "Reporte generado con datos: " + data;
    }
}

// Responsabilidad única: Formatear reportes
class ReportFormatter {
    public String formatToHTML(String content) {
        return "<html><body>" + content + "</body></html>";
    }
    
    public String formatToPDF(String content) {
        return "PDF: " + content;
    }
}

// Responsabilidad única: Imprimir reportes
class ReportPrinter {
    public void print(String formattedReport) {
        System.out.println("Imprimiendo: " + formattedReport);
    }
}

// Responsabilidad única: Guardar reportes
class ReportSaver {
    public void saveToFile(String content, String filename) {
        System.out.println("Guardando reporte en archivo: " + filename);
        // Lógica para guardar archivo...
    }
}

// Clase coordinadora que utiliza las otras clases
class ReportService {
    private ReportGenerator generator;
    private ReportFormatter formatter;
    private ReportPrinter printer;
    private ReportSaver saver;
    
    public ReportService() {
        this.generator = new ReportGenerator();
        this.formatter = new ReportFormatter();
        this.printer = new ReportPrinter();
        this.saver = new ReportSaver();
    }
    
    public void processReport(String data, String filename) {
        String content = generator.generateContent(data);
        String formatted = formatter.formatToHTML(content);
        printer.print(formatted);
        saver.saveToFile(formatted, filename);
    }
}

// Ejemplo de uso
public class SRP_Example {
    public static void main(String[] args) {
        System.out.println("=== EJEMPLO SRP - PRINCIPIO DE RESPONSABILIDAD ÚNICA ===\n");
        
        // Uso de la implementación correcta
        ReportService reportService = new ReportService();
        reportService.processReport("Datos de ventas Q4", "reporte_ventas.html");
        
        System.out.println("\n✅ Ventajas del SRP:");
        System.out.println("- Cada clase tiene una sola razón para cambiar");
        System.out.println("- Fácil mantenimiento y testing");
        System.out.println("- Mayor reutilización de código");
        System.out.println("- Reducción de acoplamiento");
    }
}