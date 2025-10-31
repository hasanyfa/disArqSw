"""
PRINCIPIO D - DEPENDENCY INVERSION PRINCIPLE (INVERSIÓN DE DEPENDENCIAS)

Las clases de alto nivel no deben depender de clases concretas, sino de abstracciones.
Los detalles deben depender de las abstracciones, no al revés.

Analogía: Cargadores universales - tu celular no depende de un cargador específico,
sino de un estándar (USB). Así puedes conectar distintos cargadores sin cambiar el teléfono.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List

# ❌ VIOLACIÓN DEL PRINCIPIO DIP
# La clase de alto nivel depende directamente de implementaciones concretas

class BadEmailService:
    """Servicio concreto de email"""
    
    def send_email(self, message, recipient):
        print(f"Enviando email a {recipient}: {message}")


class BadSMSService:
    """Servicio concreto de SMS"""
    
    def send_sms(self, message, phone_number):
        print(f"Enviando SMS a {phone_number}: {message}")


# ❌ NotificationService depende de implementaciones concretas
class BadNotificationService:
    """❌ Clase que viola DIP - depende de implementaciones concretas"""
    
    def __init__(self):
        # ❌ Violación DIP: creamos dependencias concretas
        self.email_service = BadEmailService()
        self.sms_service = BadSMSService()
    
    def send_notification(self, message, contact, notification_type):
        if notification_type == "email":
            self.email_service.send_email(message, contact)
        elif notification_type == "sms":
            self.sms_service.send_sms(message, contact)
        # ❌ Para agregar WhatsApp, debemos modificar esta clase


# ✅ APLICACIÓN CORRECTA DEL PRINCIPIO DIP
# Definimos abstracciones y dependemos de ellas

class MessageSender(ABC):
    """Abstracción de alto nivel para envío de mensajes"""
    
    @abstractmethod
    def send_message(self, message: str, recipient: str) -> bool:
        pass
    
    @abstractmethod
    def get_sender_type(self) -> str:
        pass


# Implementaciones concretas que dependen de la abstracción
class EmailService(MessageSender):
    """Servicio de email que implementa la abstracción"""
    
    def __init__(self, smtp_server: str):
        self.smtp_server = smtp_server
    
    def send_message(self, message: str, recipient: str) -> bool:
        print(f"[Email via {self.smtp_server}] To: {recipient}")
        print(f"Message: {message}")
        return True
    
    def get_sender_type(self) -> str:
        return "Email"


class SMSService(MessageSender):
    """Servicio de SMS que implementa la abstracción"""
    
    def __init__(self, provider: str):
        self.provider = provider
    
    def send_message(self, message: str, recipient: str) -> bool:
        print(f"[SMS via {self.provider}] To: {recipient}")
        print(f"Message: {message}")
        return True
    
    def get_sender_type(self) -> str:
        return "SMS"


# ✅ Nueva implementación sin modificar código existente
class WhatsAppService(MessageSender):
    """Servicio de WhatsApp que implementa la abstracción"""
    
    def send_message(self, message: str, recipient: str) -> bool:
        print(f"[WhatsApp] To: {recipient}")
        print(f"Message: {message}")
        return True
    
    def get_sender_type(self) -> str:
        return "WhatsApp"


class PushNotificationService(MessageSender):
    """Servicio de notificaciones push que implementa la abstracción"""
    
    def __init__(self, platform: str):
        self.platform = platform
    
    def send_message(self, message: str, recipient: str) -> bool:
        print(f"[Push {self.platform}] To device: {recipient}")
        print(f"Notification: {message}")
        return True
    
    def get_sender_type(self) -> str:
        return "Push Notification"


# ✅ Clase de alto nivel que depende de abstracciones
class NotificationService:
    """Servicio de notificaciones que depende de abstracciones"""
    
    def __init__(self, message_sender: MessageSender):
        # ✅ Inversión de dependencias: recibimos la abstracción por inyección
        self.message_sender = message_sender
    
    def send_notification(self, message: str, recipient: str) -> bool:
        print(f"Preparando notificación via {self.message_sender.get_sender_type()}")
        success = self.message_sender.send_message(message, recipient)
        
        if success:
            print("✅ Notificación enviada exitosamente\n")
        else:
            print("❌ Error al enviar notificación\n")
        
        return success


# Ejemplo adicional: Sistema de persistencia
class DataRepository(ABC):
    """Abstracción para repositorio de datos"""
    
    @abstractmethod
    def save(self, data: Dict[str, Any]) -> bool:
        pass
    
    @abstractmethod
    def load(self, id: str) -> Dict[str, Any]:
        pass
    
    @abstractmethod
    def delete(self, id: str) -> bool:
        pass
    
    @abstractmethod
    def get_repository_type(self) -> str:
        pass


# Implementaciones concretas
class DatabaseRepository(DataRepository):
    """Repositorio de base de datos"""
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.data_store = {}  # Simulación de BD
    
    def save(self, data: Dict[str, Any]) -> bool:
        data_id = data.get('id', 'unknown')
        self.data_store[data_id] = data
        print(f"[Database {self.connection_string}] Guardando: {data}")
        return True
    
    def load(self, id: str) -> Dict[str, Any]:
        print(f"[Database] Cargando ID: {id}")
        return self.data_store.get(id, {"id": id, "data": "Data from database"})
    
    def delete(self, id: str) -> bool:
        print(f"[Database] Eliminando ID: {id}")
        if id in self.data_store:
            del self.data_store[id]
        return True
    
    def get_repository_type(self) -> str:
        return "Database"


class FileRepository(DataRepository):
    """Repositorio de archivos"""
    
    def __init__(self, base_path: str):
        self.base_path = base_path
        self.files = {}  # Simulación de sistema de archivos
    
    def save(self, data: Dict[str, Any]) -> bool:
        data_id = data.get('id', 'unknown')
        filename = f"{self.base_path}/{data_id}.json"
        self.files[filename] = data
        print(f"[File System {self.base_path}] Guardando: {data}")
        return True
    
    def load(self, id: str) -> Dict[str, Any]:
        filename = f"{self.base_path}/{id}.json"
        print(f"[File System] Cargando archivo: {filename}")
        return self.files.get(filename, {"id": id, "data": "Data from file"})
    
    def delete(self, id: str) -> bool:
        filename = f"{self.base_path}/{id}.json"
        print(f"[File System] Eliminando archivo: {filename}")
        if filename in self.files:
            del self.files[filename]
        return True
    
    def get_repository_type(self) -> str:
        return "File System"


class CloudRepository(DataRepository):
    """Repositorio en la nube"""
    
    def __init__(self, cloud_provider: str):
        self.cloud_provider = cloud_provider
        self.cloud_storage = {}  # Simulación de almacenamiento en nube
    
    def save(self, data: Dict[str, Any]) -> bool:
        data_id = data.get('id', 'unknown')
        self.cloud_storage[data_id] = data
        print(f"[Cloud {self.cloud_provider}] Subiendo: {data}")
        return True
    
    def load(self, id: str) -> Dict[str, Any]:
        print(f"[Cloud] Descargando ID: {id}")
        return self.cloud_storage.get(id, {"id": id, "data": "Data from cloud"})
    
    def delete(self, id: str) -> bool:
        print(f"[Cloud] Eliminando ID: {id}")
        if id in self.cloud_storage:
            del self.cloud_storage[id]
        return True
    
    def get_repository_type(self) -> str:
        return f"Cloud ({self.cloud_provider})"


# ✅ Servicio de alto nivel que depende de abstracción
class DataService:
    """Servicio de datos que depende de abstracciones"""
    
    def __init__(self, repository: DataRepository):
        self.repository = repository
    
    def process_data(self, data: Dict[str, Any]) -> bool:
        print(f"Procesando datos con {self.repository.get_repository_type()}...")
        success = self.repository.save(data)
        
        if success:
            loaded_data = self.repository.load(data['id'])
            print(f"Datos verificados: {loaded_data}")
        
        return success
    
    def cleanup_data(self, id: str) -> bool:
        print(f"Limpiando datos con {self.repository.get_repository_type()}...")
        return self.repository.delete(id)


# Ejemplo adicional: Sistema de logging
class Logger(ABC):
    """Abstracción para logging"""
    
    @abstractmethod
    def log(self, level: str, message: str) -> None:
        pass


class ConsoleLogger(Logger):
    """Logger que imprime en consola"""
    
    def log(self, level: str, message: str) -> None:
        print(f"[CONSOLE {level}] {message}")


class FileLogger(Logger):
    """Logger que escribe a archivo"""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.logs = []  # Simulación de archivo
    
    def log(self, level: str, message: str) -> None:
        log_entry = f"[FILE {level}] {message}"
        self.logs.append(log_entry)
        print(f"Escribiendo a {self.filename}: {log_entry}")


class Application:
    """Aplicación que depende de abstracciones"""
    
    def __init__(self, logger: Logger, data_service: DataService, notification_service: NotificationService):
        self.logger = logger
        self.data_service = data_service
        self.notification_service = notification_service
    
    def run(self):
        self.logger.log("INFO", "Aplicación iniciada")
        
        # Procesar algunos datos
        user_data = {"id": "user_001", "name": "Ana García", "email": "ana@ejemplo.com"}
        success = self.data_service.process_data(user_data)
        
        if success:
            self.logger.log("INFO", "Datos procesados exitosamente")
            self.notification_service.send_notification(
                "Tu cuenta ha sido creada exitosamente", 
                user_data["email"]
            )
        else:
            self.logger.log("ERROR", "Error al procesar datos")
        
        self.logger.log("INFO", "Aplicación finalizada")


# Factory para crear diferentes configuraciones
class ServiceFactory:
    """Factory para crear servicios con diferentes implementaciones"""
    
    @staticmethod
    def create_email_notification_service(smtp_server: str) -> NotificationService:
        email_sender = EmailService(smtp_server)
        return NotificationService(email_sender)
    
    @staticmethod
    def create_sms_notification_service(provider: str) -> NotificationService:
        sms_sender = SMSService(provider)
        return NotificationService(sms_sender)
    
    @staticmethod
    def create_database_data_service(connection_string: str) -> DataService:
        db_repo = DatabaseRepository(connection_string)
        return DataService(db_repo)
    
    @staticmethod
    def create_file_data_service(base_path: str) -> DataService:
        file_repo = FileRepository(base_path)
        return DataService(file_repo)
    
    @staticmethod
    def create_cloud_data_service(provider: str) -> DataService:
        cloud_repo = CloudRepository(provider)
        return DataService(cloud_repo)


def main():
    print("=== EJEMPLO DIP - PRINCIPIO DE INVERSIÓN DE DEPENDENCIAS ===\n")
    
    # Ejemplo con notificaciones
    print("📧 Sistema de notificaciones:")
    
    # ✅ Inyectamos diferentes implementaciones sin cambiar NotificationService
    message = "¡Bienvenido a nuestro sistema!"
    
    # Crear diferentes servicios de notificación
    email_service = ServiceFactory.create_email_notification_service("smtp.gmail.com")
    sms_service = ServiceFactory.create_sms_notification_service("Telcel")
    whatsapp_service = NotificationService(WhatsAppService())
    push_service = NotificationService(PushNotificationService("iOS"))
    
    # Usar los servicios polimórficamente
    services_and_recipients = [
        (email_service, "usuario@ejemplo.com"),
        (sms_service, "+52123456789"),
        (whatsapp_service, "+52123456789"),
        (push_service, "device_token_123")
    ]
    
    for service, recipient in services_and_recipients:
        service.send_notification(message, recipient)
    
    # Ejemplo con persistencia de datos
    print("💾 Sistema de persistencia:")
    
    # ✅ Diferentes repositorios sin cambiar DataService
    data_services = [
        ServiceFactory.create_database_data_service("jdbc:mysql://localhost:3306/mydb"),
        ServiceFactory.create_file_data_service("/data/files"),
        ServiceFactory.create_cloud_data_service("AWS S3")
    ]
    
    test_data = {"id": "product_001", "name": "Laptop", "price": 999.99}
    
    for i, data_service in enumerate(data_services, 1):
        print(f"\n--- Configuración {i} ---")
        data_service.process_data(test_data)
    
    # Ejemplo con aplicación completa
    print("\n🚀 Aplicación completa con DIP:")
    
    # Configuración 1: Desarrollo
    console_logger = ConsoleLogger()
    file_data_service = ServiceFactory.create_file_data_service("/tmp/dev")
    email_notification = ServiceFactory.create_email_notification_service("localhost")
    
    dev_app = Application(console_logger, file_data_service, email_notification)
    
    print("\n--- Configuración de Desarrollo ---")
    dev_app.run()
    
    # Configuración 2: Producción
    file_logger = FileLogger("app.log")
    cloud_data_service = ServiceFactory.create_cloud_data_service("Azure Blob")
    sms_notification = ServiceFactory.create_sms_notification_service("Twilio")
    
    prod_app = Application(file_logger, cloud_data_service, sms_notification)
    
    print("\n--- Configuración de Producción ---")
    prod_app.run()
    
    print("\n✅ Ventajas del DIP:")
    print("- Bajo acoplamiento entre módulos")
    print("- Fácil testing con mocks y stubs")
    print("- Flexibilidad para cambiar implementaciones")
    print("- Código más mantenible y extensible")
    print("- Principio de inversión de control (IoC)")
    print("- Facilita la inyección de dependencias")


if __name__ == "__main__":
    main()