/**
 * PRINCIPIO D - DEPENDENCY INVERSION PRINCIPLE (INVERSIÓN DE DEPENDENCIAS)
 * 
 * Las clases de alto nivel no deben depender de clases concretas, sino de abstracciones.
 * Los detalles deben depender de las abstracciones, no al revés.
 * 
 * Analogía: Cargadores universales - tu celular no depende de un cargador específico,
 * sino de un estándar (USB). Así puedes conectar distintos cargadores sin cambiar el teléfono.
 */

// ❌ VIOLACIÓN DEL PRINCIPIO DIP
// La clase de alto nivel depende directamente de implementaciones concretas

class BadEmailService {
    public void sendEmail(String message, String recipient) {
        System.out.println("Enviando email a " + recipient + ": " + message);
    }
}

class BadSMSService {
    public void sendSMS(String message, String phoneNumber) {
        System.out.println("Enviando SMS a " + phoneNumber + ": " + message);
    }
}

// ❌ NotificationService depende de implementaciones concretas
class BadNotificationService {
    private BadEmailService emailService; // Dependencia concreta
    private BadSMSService smsService;     // Dependencia concreta
    
    public BadNotificationService() {
        // ❌ Violación DIP: creamos dependencias concretas
        this.emailService = new BadEmailService();
        this.smsService = new BadSMSService();
    }
    
    public void sendNotification(String message, String contact, String type) {
        if ("email".equals(type)) {
            emailService.sendEmail(message, contact);
        } else if ("sms".equals(type)) {
            smsService.sendSMS(message, contact);
        }
        // ❌ Para agregar WhatsApp, debemos modificar esta clase
    }
}

// ✅ APLICACIÓN CORRECTA DEL PRINCIPIO DIP
// Definimos abstracciones y dependemos de ellas

// Abstracción de alto nivel
interface MessageSender {
    void sendMessage(String message, String recipient);
    String getSenderType();
}

// Implementaciones concretas que dependen de la abstracción
class EmailService implements MessageSender {
    private String smtpServer;
    
    public EmailService(String smtpServer) {
        this.smtpServer = smtpServer;
    }
    
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println("[Email via " + smtpServer + "] To: " + recipient);
        System.out.println("Message: " + message);
    }
    
    @Override
    public String getSenderType() {
        return "Email";
    }
}

class SMSService implements MessageSender {
    private String provider;
    
    public SMSService(String provider) {
        this.provider = provider;
    }
    
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println("[SMS via " + provider + "] To: " + recipient);
        System.out.println("Message: " + message);
    }
    
    @Override
    public String getSenderType() {
        return "SMS";
    }
}

// ✅ Nueva implementación sin modificar código existente
class WhatsAppService implements MessageSender {
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println("[WhatsApp] To: " + recipient);
        System.out.println("Message: " + message);
    }
    
    @Override
    public String getSenderType() {
        return "WhatsApp";
    }
}

class PushNotificationService implements MessageSender {
    private String platform;
    
    public PushNotificationService(String platform) {
        this.platform = platform;
    }
    
    @Override
    public void sendMessage(String message, String recipient) {
        System.out.println("[Push " + platform + "] To device: " + recipient);
        System.out.println("Notification: " + message);
    }
    
    @Override
    public String getSenderType() {
        return "Push Notification";
    }
}

// ✅ Clase de alto nivel que depende de abstracciones
class NotificationService {
    private final MessageSender messageSender;
    
    // ✅ Inversión de dependencias: recibimos la abstracción por inyección
    public NotificationService(MessageSender messageSender) {
        this.messageSender = messageSender;
    }
    
    public void sendNotification(String message, String recipient) {
        System.out.println("Preparando notificación via " + messageSender.getSenderType());
        messageSender.sendMessage(message, recipient);
        System.out.println("Notificación enviada exitosamente\n");
    }
}

// Ejemplo adicional: Sistema de persistencia
interface DataRepository {
    void save(String data);
    String load(String id);
    void delete(String id);
}

// Implementaciones concretas
class DatabaseRepository implements DataRepository {
    private String connectionString;
    
    public DatabaseRepository(String connectionString) {
        this.connectionString = connectionString;
    }
    
    @Override
    public void save(String data) {
        System.out.println("[Database " + connectionString + "] Guardando: " + data);
    }
    
    @Override
    public String load(String id) {
        System.out.println("[Database] Cargando ID: " + id);
        return "Data from database for ID: " + id;
    }
    
    @Override
    public void delete(String id) {
        System.out.println("[Database] Eliminando ID: " + id);
    }
}

class FileRepository implements DataRepository {
    private String basePath;
    
    public FileRepository(String basePath) {
        this.basePath = basePath;
    }
    
    @Override
    public void save(String data) {
        System.out.println("[File System " + basePath + "] Guardando: " + data);
    }
    
    @Override
    public String load(String id) {
        System.out.println("[File System] Cargando archivo: " + id);
        return "Data from file: " + id;
    }
    
    @Override
    public void delete(String id) {
        System.out.println("[File System] Eliminando archivo: " + id);
    }
}

class CloudRepository implements DataRepository {
    private String cloudProvider;
    
    public CloudRepository(String cloudProvider) {
        this.cloudProvider = cloudProvider;
    }
    
    @Override
    public void save(String data) {
        System.out.println("[Cloud " + cloudProvider + "] Subiendo: " + data);
    }
    
    @Override
    public String load(String id) {
        System.out.println("[Cloud] Descargando ID: " + id);
        return "Data from cloud for ID: " + id;
    }
    
    @Override
    public void delete(String id) {
        System.out.println("[Cloud] Eliminando ID: " + id);
    }
}

// ✅ Servicio de alto nivel que depende de abstracción
class DataService {
    private final DataRepository repository;
    
    public DataService(DataRepository repository) {
        this.repository = repository;
    }
    
    public void processData(String data, String id) {
        System.out.println("Procesando datos...");
        repository.save(data);
        
        String loadedData = repository.load(id);
        System.out.println("Datos cargados: " + loadedData);
    }
    
    public void cleanupData(String id) {
        System.out.println("Limpiando datos...");
        repository.delete(id);
    }
}

// Factory para crear diferentes tipos de servicios
class NotificationFactory {
    public static MessageSender createEmailSender(String smtpServer) {
        return new EmailService(smtpServer);
    }
    
    public static MessageSender createSMSSender(String provider) {
        return new SMSService(provider);
    }
    
    public static MessageSender createWhatsAppSender() {
        return new WhatsAppService();
    }
    
    public static MessageSender createPushSender(String platform) {
        return new PushNotificationService(platform);
    }
}

class RepositoryFactory {
    public static DataRepository createDatabaseRepository(String connectionString) {
        return new DatabaseRepository(connectionString);
    }
    
    public static DataRepository createFileRepository(String basePath) {
        return new FileRepository(basePath);
    }
    
    public static DataRepository createCloudRepository(String provider) {
        return new CloudRepository(provider);
    }
}

// Ejemplo de uso
public class DIP_Example {
    public static void main(String[] args) {
        System.out.println("=== EJEMPLO DIP - PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS ===\n");
        
        // Ejemplo con notificaciones
        System.out.println("📧 Sistema de notificaciones:");
        
        // ✅ Inyectamos diferentes implementaciones sin cambiar NotificationService
        MessageSender emailSender = NotificationFactory.createEmailSender("smtp.gmail.com");
        MessageSender smsSender = NotificationFactory.createSMSSender("Telcel");
        MessageSender whatsappSender = NotificationFactory.createWhatsAppSender();
        MessageSender pushSender = NotificationFactory.createPushSender("iOS");
        
        NotificationService emailNotifier = new NotificationService(emailSender);
        NotificationService smsNotifier = new NotificationService(smsSender);
        NotificationService whatsappNotifier = new NotificationService(whatsappSender);
        NotificationService pushNotifier = new NotificationService(pushSender);
        
        String message = "¡Bienvenido a nuestro sistema!";
        String recipient = "usuario@ejemplo.com";
        
        emailNotifier.sendNotification(message, recipient);
        smsNotifier.sendNotification(message, "+52123456789");
        whatsappNotifier.sendNotification(message, "+52123456789");
        pushNotifier.sendNotification(message, "device_token_123");
        
        // Ejemplo con persistencia de datos
        System.out.println("💾 Sistema de persistencia:");
        
        // ✅ Diferentes repositorios sin cambiar DataService
        DataRepository dbRepo = RepositoryFactory.createDatabaseRepository("jdbc:mysql://localhost:3306/mydb");
        DataRepository fileRepo = RepositoryFactory.createFileRepository("/data/files");
        DataRepository cloudRepo = RepositoryFactory.createCloudRepository("AWS S3");
        
        DataService dbService = new DataService(dbRepo);
        DataService fileService = new DataService(fileRepo);
        DataService cloudService = new DataService(cloudRepo);
        
        String testData = "Información importante del usuario";
        String dataId = "user_001";
        
        System.out.println("\n--- Usando Base de Datos ---");
        dbService.processData(testData, dataId);
        
        System.out.println("\n--- Usando Sistema de Archivos ---");
        fileService.processData(testData, dataId);
        
        System.out.println("\n--- Usando Almacenamiento en la Nube ---");
        cloudService.processData(testData, dataId);
        
        System.out.println("\n✅ Ventajas del DIP:");
        System.out.println("- Bajo acoplamiento entre módulos");
        System.out.println("- Fácil testing con mocks");
        System.out.println("- Flexibilidad para cambiar implementaciones");
        System.out.println("- Código más mantenible y extensible");
        System.out.println("- Principio de inversión de control (IoC)");
    }
}