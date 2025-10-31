"""
PRINCIPIO I - INTERFACE SEGREGATION PRINCIPLE (SEGREGACIÓN DE INTERFACES)

Las clases no deben estar obligadas a implementar métodos que no usan.
Es mejor tener varias interfaces pequeñas que una enorme.

Analogía: Controles remotos específicos - el control de la TV no debería 
tener botones para abrir el refrigerador.
"""

from abc import ABC, abstractmethod

# ❌ VIOLACIÓN DEL PRINCIPIO ISP
# Interfaz monolítica que obliga a implementar métodos no utilizados

class BadMultiFunctionDevice(ABC):
    """❌ Interfaz que viola ISP - demasiadas responsabilidades"""
    
    # Funciones de impresora
    @abstractmethod
    def print_document(self, document):
        pass
    
    @abstractmethod
    def print_color(self, document):
        pass
    
    # Funciones de scanner
    @abstractmethod
    def scan_document(self):
        pass
    
    @abstractmethod
    def scan_to_email(self, email):
        pass
    
    # Funciones de fax
    @abstractmethod
    def send_fax(self, document, number):
        pass
    
    @abstractmethod
    def receive_fax(self):
        pass
    
    # Funciones de copiadora
    @abstractmethod
    def copy_document(self, document):
        pass
    
    @abstractmethod
    def copy_color(self, document):
        pass


# ❌ Una impresora simple se ve obligada a implementar funciones que no tiene
class BadSimplePrinter(BadMultiFunctionDevice):
    def print_document(self, document):
        print(f"Imprimiendo: {document}")
    
    def print_color(self, document):
        # ❌ Esta impresora no imprime a color
        raise NotImplementedError("Esta impresora no soporta color")
    
    def scan_document(self):
        # ❌ Esta impresora no puede escanear
        raise NotImplementedError("Esta impresora no puede escanear")
    
    def scan_to_email(self, email):
        raise NotImplementedError("Esta impresora no puede escanear")
    
    def send_fax(self, document, number):
        # ❌ Esta impresora no puede enviar fax
        raise NotImplementedError("Esta impresora no puede enviar fax")
    
    def receive_fax(self):
        raise NotImplementedError("Esta impresora no puede recibir fax")
    
    def copy_document(self, document):
        # ❌ Esta impresora no puede copiar
        raise NotImplementedError("Esta impresora no puede copiar")
    
    def copy_color(self, document):
        raise NotImplementedError("Esta impresora no puede copiar")


# ✅ APLICACIÓN CORRECTA DEL PRINCIPIO ISP
# Interfaces segregadas y específicas

class Printer(ABC):
    """Interfaz específica para impresión"""
    
    @abstractmethod
    def print_document(self, document):
        pass


class ColorPrinter(Printer):
    """Interfaz específica para impresión a color"""
    
    @abstractmethod
    def print_color(self, document):
        pass


class Scanner(ABC):
    """Interfaz específica para escaneo"""
    
    @abstractmethod
    def scan_document(self):
        pass
    
    @abstractmethod
    def scan_to_email(self, email):
        pass


class FaxMachine(ABC):
    """Interfaz específica para fax"""
    
    @abstractmethod
    def send_fax(self, document, number):
        pass
    
    @abstractmethod
    def receive_fax(self):
        pass


class Copier(ABC):
    """Interfaz específica para copiado"""
    
    @abstractmethod
    def copy_document(self, document):
        pass


class ColorCopier(Copier):
    """Interfaz específica para copiado a color"""
    
    @abstractmethod
    def copy_color(self, document):
        pass


# ✅ Implementaciones específicas que solo implementan lo que necesitan

class SimplePrinter(Printer):
    """Impresora simple que solo imprime en blanco y negro"""
    
    def __init__(self, model):
        self.model = model
    
    def print_document(self, document):
        print(f"[{self.model}] Imprimiendo: {document}")


class LaserPrinter(ColorPrinter):
    """Impresora láser con capacidad de color"""
    
    def __init__(self, model):
        self.model = model
    
    def print_document(self, document):
        print(f"[{self.model}] Imprimiendo en blanco y negro: {document}")
    
    def print_color(self, document):
        print(f"[{self.model}] Imprimiendo a color: {document}")


class DocumentScanner(Scanner):
    """Escáner de documentos"""
    
    def __init__(self, model):
        self.model = model
    
    def scan_document(self):
        scanned_content = f"Documento escaneado por {self.model}"
        print(f"[{self.model}] Escaneando documento...")
        return scanned_content
    
    def scan_to_email(self, email):
        content = self.scan_document()
        print(f"[{self.model}] Enviando escaneo a: {email}")
        return content


class FaxDevice(FaxMachine):
    """Dispositivo de fax"""
    
    def __init__(self, model):
        self.model = model
    
    def send_fax(self, document, number):
        print(f"[{self.model}] Enviando fax a {number}: {document}")
    
    def receive_fax(self):
        print(f"[{self.model}] Recibiendo fax...")
        return "Fax recibido"


# ✅ Dispositivo multifuncional que implementa múltiples interfaces según sus capacidades
class MultiFunctionPrinter(ColorPrinter, Scanner, Copier, ColorCopier):
    """Impresora multifuncional con todas las capacidades"""
    
    def __init__(self, model):
        self.model = model
    
    def print_document(self, document):
        print(f"[{self.model}] Imprimiendo: {document}")
    
    def print_color(self, document):
        print(f"[{self.model}] Imprimiendo a color: {document}")
    
    def scan_document(self):
        print(f"[{self.model}] Escaneando...")
        return f"Documento escaneado por {self.model}"
    
    def scan_to_email(self, email):
        content = self.scan_document()
        print(f"[{self.model}] Enviando escaneo a: {email}")
        return content
    
    def copy_document(self, document):
        print(f"[{self.model}] Copiando: {document}")
    
    def copy_color(self, document):
        print(f"[{self.model}] Copiando a color: {document}")


# Ejemplo adicional: Trabajadores con diferentes habilidades
class Worker(ABC):
    """Interfaz básica para trabajadores"""
    
    @abstractmethod
    def work(self):
        pass


class Eater(ABC):
    """Interfaz para entidades que pueden comer"""
    
    @abstractmethod
    def eat(self):
        pass


class Sleeper(ABC):
    """Interfaz para entidades que pueden dormir"""
    
    @abstractmethod
    def sleep(self):
        pass


class Communicator(ABC):
    """Interfaz para entidades que pueden comunicarse"""
    
    @abstractmethod
    def communicate(self, message):
        pass


# ❌ Interfaz que viola ISP
class BadWorker(ABC):
    """❌ Interfaz monolítica que viola ISP"""
    
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass


# ✅ Implementaciones segregadas
class HumanWorker(Worker, Eater, Sleeper, Communicator):
    """Trabajador humano con todas las capacidades humanas"""
    
    def __init__(self, name):
        self.name = name
    
    def work(self):
        print(f"{self.name} está trabajando")
    
    def eat(self):
        print(f"{self.name} está comiendo")
    
    def sleep(self):
        print(f"{self.name} está durmiendo")
    
    def communicate(self, message):
        print(f"{self.name} dice: {message}")


class RobotWorker(Worker, Communicator):
    """Robot trabajador que no necesita comer ni dormir"""
    
    def __init__(self, model):
        self.model = model
    
    def work(self):
        print(f"Robot {self.model} está trabajando 24/7")
    
    def communicate(self, message):
        print(f"Robot {self.model} transmite: {message}")
    
    # ✅ El robot no implementa Eater ni Sleeper porque no las necesita


class AIAssistant(Communicator):
    """Asistente de IA que solo puede comunicarse"""
    
    def __init__(self, name):
        self.name = name
    
    def communicate(self, message):
        print(f"IA {self.name} responde: Procesando '{message}'...")


# Ejemplo adicional: Animales con diferentes capacidades
class Animal(ABC):
    """Interfaz base para animales"""
    
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        pass


class Swimmer(ABC):
    """Interfaz para animales que nadan"""
    
    @abstractmethod
    def swim(self):
        pass


class Flyer(ABC):
    """Interfaz para animales que vuelan"""
    
    @abstractmethod
    def fly(self):
        pass


class Runner(ABC):
    """Interfaz para animales que corren"""
    
    @abstractmethod
    def run(self):
        pass


class Dog(Animal, Runner, Swimmer):
    """Perro que puede correr y nadar"""
    
    def make_sound(self):
        print(f"{self.name} hace: ¡Guau!")
    
    def run(self):
        print(f"{self.name} está corriendo")
    
    def swim(self):
        print(f"{self.name} está nadando")


class Bird(Animal, Flyer):
    """Pájaro que puede volar"""
    
    def make_sound(self):
        print(f"{self.name} hace: ¡Pío pío!")
    
    def fly(self):
        print(f"{self.name} está volando")


class Fish(Animal, Swimmer):
    """Pez que solo puede nadar"""
    
    def make_sound(self):
        print(f"{self.name} hace: ¡Glub glub!")
    
    def swim(self):
        print(f"{self.name} está nadando")


# Clases que manejan las interfaces segregadas
class OfficeManager:
    """Gestor de oficina que maneja diferentes dispositivos"""
    
    def manage_printing(self, printer: Printer, document):
        print("📄 Gestionando impresión...")
        printer.print_document(document)
    
    def manage_color_printing(self, color_printer: ColorPrinter, document):
        print("🌈 Gestionando impresión a color...")
        color_printer.print_color(document)
    
    def manage_scanning(self, scanner: Scanner):
        print("📷 Gestionando escaneo...")
        return scanner.scan_document()
    
    def manage_copying(self, copier: Copier, document):
        print("📋 Gestionando copiado...")
        copier.copy_document(document)


class WorkManager:
    """Gestor de trabajo que maneja diferentes tipos de trabajadores"""
    
    def assign_work(self, worker: Worker):
        print("💼 Asignando trabajo...")
        worker.work()
    
    def schedule_break(self, eater: Eater):
        print("☕ Programando descanso...")
        eater.eat()
    
    def schedule_rest(self, sleeper: Sleeper):
        print("😴 Programando descanso...")
        sleeper.sleep()
    
    def send_message(self, communicator: Communicator, message):
        print("💬 Enviando mensaje...")
        communicator.communicate(message)


def main():
    print("=== EJEMPLO ISP - PRINCIPIO DE SEGREGACIÓN DE INTERFACES ===\n")
    
    # Ejemplo con dispositivos de oficina
    print("🖨️ Dispositivos de oficina:")
    manager = OfficeManager()
    
    # Cada dispositivo implementa solo las interfaces que necesita
    simple = SimplePrinter("HP LaserJet Basic")
    laser = LaserPrinter("Canon Color Laser")
    scanner = DocumentScanner("Epson Scanner Pro")
    mfp = MultiFunctionPrinter("Brother MFC-9000")
    
    # Uso específico según las capacidades
    print("\n--- Impresión simple ---")
    manager.manage_printing(simple, "Documento simple")
    manager.manage_printing(laser, "Documento profesional")
    
    print("\n--- Impresión a color ---")
    manager.manage_color_printing(laser, "Presentación colorida")
    manager.manage_color_printing(mfp, "Gráficos coloridos")
    
    print("\n--- Escaneo ---")
    manager.manage_scanning(scanner)
    manager.manage_scanning(mfp)
    
    print("\n--- Copiado ---")
    manager.manage_copying(mfp, "Documento importante")
    
    # Ejemplo con trabajadores
    print("\n👷 Gestión de trabajadores:")
    work_manager = WorkManager()
    
    human = HumanWorker("Ana")
    robot = RobotWorker("R2D2")
    ai = AIAssistant("Copilot")
    
    print("\n--- Asignando trabajo ---")
    work_manager.assign_work(human)
    work_manager.assign_work(robot)
    
    print("\n--- Comunicación ---")
    work_manager.send_message(human, "¿Cómo está el proyecto?")
    work_manager.send_message(robot, "Ejecutar protocolo de limpieza")
    work_manager.send_message(ai, "¿Cuál es el clima de hoy?")
    
    print("\n--- Descansos (solo humanos) ---")
    work_manager.schedule_break(human)
    work_manager.schedule_rest(human)
    
    # Ejemplo con animales
    print("\n🐾 Animales y sus capacidades:")
    dog = Dog("Rex")
    bird = Bird("Canario")
    fish = Fish("Nemo")
    
    animals = [dog, bird, fish]
    
    print("\n--- Sonidos de animales ---")
    for animal in animals:
        animal.make_sound()
    
    print("\n--- Actividades específicas ---")
    # Solo los que pueden nadar
    swimmers = [animal for animal in animals if isinstance(animal, Swimmer)]
    for swimmer in swimmers:
        swimmer.swim()
    
    # Solo los que pueden volar
    flyers = [animal for animal in animals if isinstance(animal, Flyer)]
    for flyer in flyers:
        flyer.fly()
    
    # Solo los que pueden correr
    runners = [animal for animal in animals if isinstance(animal, Runner)]
    for runner in runners:
        runner.run()
    
    print("\n✅ Ventajas del ISP:")
    print("- Las clases solo implementan métodos que realmente usan")
    print("- Interfaces pequeñas y cohesivas")
    print("- Menor acoplamiento entre componentes")
    print("- Facilita el testing y la extensibilidad")
    print("- Reduce la complejidad del código")
    print("- Mayor flexibilidad en el diseño")


if __name__ == "__main__":
    main()