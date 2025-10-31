"""
PRINCIPIO S - SINGLE RESPONSIBILITY PRINCIPLE (RESPONSABILIDAD ÚNICA)

Una clase debe tener una sola razón para cambiar, es decir, una sola responsabilidad.

Analogía: El chef del restaurante - cada persona tiene su rol específico.
"""

# ❌ VIOLACIÓN DEL PRINCIPIO SRP
# Esta clase tiene múltiples responsabilidades: generar, formatear, imprimir y guardar reportes
class BadReport:
    def __init__(self, data):
        self.data = data
    
    # Responsabilidad 1: Generar contenido del reporte
    def generate_content(self):
        return f"Reporte generado con datos: {self.data}"
    
    # Responsabilidad 2: Formatear el reporte
    def format_to_html(self):
        content = self.generate_content()
        return f"<html><body>{content}</body></html>"
    
    # Responsabilidad 3: Imprimir el reporte
    def print_report(self):
        formatted = self.format_to_html()
        print(f"Imprimiendo: {formatted}")
    
    # Responsabilidad 4: Guardar el reporte en archivo
    def save_to_file(self, filename):
        formatted = self.format_to_html()
        print(f"Guardando reporte en archivo: {filename}")
        # Lógica para guardar archivo...


# ✅ APLICACIÓN CORRECTA DEL PRINCIPIO SRP
# Cada clase tiene una sola responsabilidad

class ReportGenerator:
    """Responsabilidad única: Generar contenido del reporte"""
    
    def generate_content(self, data):
        return f"Reporte generado con datos: {data}"


class ReportFormatter:
    """Responsabilidad única: Formatear reportes"""
    
    def format_to_html(self, content):
        return f"<html><body>{content}</body></html>"
    
    def format_to_pdf(self, content):
        return f"PDF: {content}"
    
    def format_to_json(self, content):
        import json
        return json.dumps({"report": content}, indent=2)


class ReportPrinter:
    """Responsabilidad única: Imprimir reportes"""
    
    def print_report(self, formatted_report):
        print(f"Imprimiendo: {formatted_report}")


class ReportSaver:
    """Responsabilidad única: Guardar reportes"""
    
    def save_to_file(self, content, filename):
        print(f"Guardando reporte en archivo: {filename}")
        try:
            with open(filename, 'w') as file:
                file.write(content)
            print(f"✅ Archivo guardado exitosamente: {filename}")
        except Exception as e:
            print(f"❌ Error al guardar archivo: {e}")


class ReportService:
    """Clase coordinadora que utiliza las otras clases"""
    
    def __init__(self):
        self.generator = ReportGenerator()
        self.formatter = ReportFormatter()
        self.printer = ReportPrinter()
        self.saver = ReportSaver()
    
    def process_report(self, data, filename, format_type="html"):
        # Generar contenido
        content = self.generator.generate_content(data)
        
        # Formatear según el tipo
        if format_type == "html":
            formatted = self.formatter.format_to_html(content)
        elif format_type == "pdf":
            formatted = self.formatter.format_to_pdf(content)
        elif format_type == "json":
            formatted = self.formatter.format_to_json(content)
        else:
            formatted = content
        
        # Imprimir y guardar
        self.printer.print_report(formatted)
        self.saver.save_to_file(formatted, filename)
        
        return formatted


# Ejemplo adicional: Sistema de usuarios
class BadUser:
    """❌ Clase que viola SRP - tiene múltiples responsabilidades"""
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    # Responsabilidad 1: Validar datos
    def validate_email(self):
        return "@" in self.email and "." in self.email
    
    # Responsabilidad 2: Encriptar contraseña
    def encrypt_password(self):
        return f"encrypted_{self.password}"
    
    # Responsabilidad 3: Guardar en base de datos
    def save_to_database(self):
        print(f"Guardando usuario {self.username} en la base de datos")
    
    # Responsabilidad 4: Enviar email de bienvenida
    def send_welcome_email(self):
        print(f"Enviando email de bienvenida a {self.email}")


# ✅ Versión corregida con SRP
class User:
    """Responsabilidad única: Representar un usuario"""
    
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    def __str__(self):
        return f"User(username={self.username}, email={self.email})"


class EmailValidator:
    """Responsabilidad única: Validar emails"""
    
    @staticmethod
    def is_valid(email):
        return "@" in email and "." in email and len(email) > 5
    
    @staticmethod
    def validate_format(email):
        if not EmailValidator.is_valid(email):
            raise ValueError(f"Email inválido: {email}")


class PasswordEncryptor:
    """Responsabilidad única: Encriptar contraseñas"""
    
    @staticmethod
    def encrypt(password):
        # Simulación de encriptación
        import hashlib
        return hashlib.md5(password.encode()).hexdigest()
    
    @staticmethod
    def verify(password, encrypted):
        return PasswordEncryptor.encrypt(password) == encrypted


class UserRepository:
    """Responsabilidad única: Gestionar persistencia de usuarios"""
    
    def __init__(self):
        self.users = []
    
    def save(self, user):
        self.users.append(user)
        print(f"✅ Usuario {user.username} guardado en la base de datos")
    
    def find_by_username(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None
    
    def get_all(self):
        return self.users.copy()


class EmailService:
    """Responsabilidad única: Enviar emails"""
    
    def send_welcome_email(self, user):
        print(f"📧 Enviando email de bienvenida a {user.email}")
        print(f"   Asunto: ¡Bienvenido {user.username}!")
        print(f"   Mensaje: Gracias por registrarte en nuestro sistema.")
    
    def send_notification(self, user, subject, message):
        print(f"📧 Enviando notificación a {user.email}")
        print(f"   Asunto: {subject}")
        print(f"   Mensaje: {message}")


class UserService:
    """Servicio que coordina la creación de usuarios"""
    
    def __init__(self):
        self.repository = UserRepository()
        self.email_service = EmailService()
        self.validator = EmailValidator()
        self.encryptor = PasswordEncryptor()
    
    def register_user(self, username, email, password):
        try:
            # Validar email
            self.validator.validate_format(email)
            
            # Encriptar contraseña
            encrypted_password = self.encryptor.encrypt(password)
            
            # Crear usuario
            user = User(username, email, encrypted_password)
            
            # Guardar en repository
            self.repository.save(user)
            
            # Enviar email de bienvenida
            self.email_service.send_welcome_email(user)
            
            print(f"✅ Usuario {username} registrado exitosamente")
            return user
            
        except ValueError as e:
            print(f"❌ Error al registrar usuario: {e}")
            return None


def main():
    print("=== EJEMPLO SRP - PRINCIPIO DE RESPONSABILIDAD ÚNICA ===\n")
    
    # Ejemplo con reportes
    print("📊 Sistema de reportes:")
    report_service = ReportService()
    
    # Generar diferentes tipos de reportes
    data = "Datos de ventas Q4 2024"
    
    print("\n--- Reporte HTML ---")
    report_service.process_report(data, "reporte_ventas.html", "html")
    
    print("\n--- Reporte JSON ---")
    report_service.process_report(data, "reporte_ventas.json", "json")
    
    # Ejemplo con usuarios
    print("\n👤 Sistema de usuarios:")
    user_service = UserService()
    
    # Registrar usuarios
    print("\n--- Registrando usuarios ---")
    user1 = user_service.register_user("ana_garcia", "ana@ejemplo.com", "password123")
    user2 = user_service.register_user("juan_perez", "juan@ejemplo.com", "secreto456")
    user3 = user_service.register_user("maria", "email_invalido", "123")  # Email inválido
    
    # Mostrar usuarios registrados
    print("\n--- Usuarios en el sistema ---")
    all_users = user_service.repository.get_all()
    for user in all_users:
        print(f"  {user}")
    
    print("\n✅ Ventajas del SRP:")
    print("- Cada clase tiene una sola razón para cambiar")
    print("- Fácil mantenimiento y testing")
    print("- Mayor reutilización de código")
    print("- Reducción de acoplamiento")
    print("- Código más limpio y comprensible")


if __name__ == "__main__":
    main()