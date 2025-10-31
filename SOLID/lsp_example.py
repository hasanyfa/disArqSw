"""
PRINCIPIO L - LISKOV SUBSTITUTION PRINCIPLE (SUSTITUCIÓN DE LISKOV)

Las clases hijas deben poder reemplazar a sus clases padre sin alterar 
el correcto funcionamiento del programa.

Analogía: Vehículos intercambiables - si alquilas un "auto" y te entregan 
una bicicleta, se rompe la expectativa del comportamiento.
"""

from abc import ABC, abstractmethod

# ❌ VIOLACIÓN DEL PRINCIPIO LSP
# No todos los pájaros pueden volar, por lo que Penguin viola LSP

class BadBird(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def fly(self):
        """❌ Método que no todos los pájaros pueden cumplir"""
        pass
    
    def eat(self):
        print(f"{self.name} está comiendo")


class BadEagle(BadBird):
    def __init__(self):
        super().__init__("Águila")
    
    def fly(self):
        print(f"{self.name} vuela majestuosamente")


class BadPenguin(BadBird):
    def __init__(self):
        super().__init__("Pingüino")
    
    def fly(self):
        # ❌ Viola LSP: Un pingüino no puede volar pero debe implementar el método
        raise NotImplementedError("Los pingüinos no pueden volar!")


# ✅ APLICACIÓN CORRECTA DEL PRINCIPIO LSP
# Jerarquía bien diseñada que respeta el comportamiento esperado

class Bird(ABC):
    """Clase base para todos los pájaros"""
    
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} está comiendo")
    
    def sleep(self):
        print(f"{self.name} está durmiendo")
    
    @abstractmethod
    def make_sound(self):
        pass


# Interfaces específicas para comportamientos especializados
class Flyable(ABC):
    """Interfaz para pájaros que pueden volar"""
    
    @abstractmethod
    def fly(self):
        pass
    
    @abstractmethod
    def get_flight_speed(self):
        pass


class Swimmable(ABC):
    """Interfaz para pájaros que pueden nadar"""
    
    @abstractmethod
    def swim(self):
        pass
    
    @abstractmethod
    def get_swim_speed(self):
        pass


class RunningBird(ABC):
    """Interfaz para pájaros que corren"""
    
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def get_running_speed(self):
        pass


# Implementaciones específicas que respetan LSP
class Eagle(Bird, Flyable):
    def __init__(self):
        super().__init__("Águila")
    
    def make_sound(self):
        print(f"{self.name} hace: ¡Grito agudo!")
    
    def fly(self):
        print(f"{self.name} vuela alto en el cielo")
    
    def get_flight_speed(self):
        return 80  # km/h


class Penguin(Bird, Swimmable, RunningBird):
    def __init__(self):
        super().__init__("Pingüino")
    
    def make_sound(self):
        print(f"{self.name} hace: ¡Graznido!")
    
    def swim(self):
        print(f"{self.name} nada graciosamente bajo el agua")
    
    def get_swim_speed(self):
        return 35  # km/h
    
    def run(self):
        print(f"{self.name} corre torpemente en tierra")
    
    def get_running_speed(self):
        return 5  # km/h


class Duck(Bird, Flyable, Swimmable):
    def __init__(self):
        super().__init__("Pato")
    
    def make_sound(self):
        print(f"{self.name} hace: ¡Cuac cuac!")
    
    def fly(self):
        print(f"{self.name} vuela sobre el lago")
    
    def get_flight_speed(self):
        return 65  # km/h
    
    def swim(self):
        print(f"{self.name} nada en el estanque")
    
    def get_swim_speed(self):
        return 8  # km/h


class Ostrich(Bird, RunningBird):
    def __init__(self):
        super().__init__("Avestruz")
    
    def make_sound(self):
        print(f"{self.name} hace: ¡Rugido grave!")
    
    def run(self):
        print(f"{self.name} corre muy rápido por la sabana")
    
    def get_running_speed(self):
        return 70  # km/h


# Ejemplo adicional: Formas geométricas con LSP
class Shape(ABC):
    """Clase base para formas geométricas"""
    
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    def get_color(self):
        return self.color


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)
        self._width = width
        self._height = height
    
    def calculate_area(self):
        return self._width * self._height
    
    def calculate_perimeter(self):
        return 2 * (self._width + self._height)
    
    def set_width(self, width):
        self._width = width
    
    def set_height(self, height):
        self._height = height
    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height


# ✅ Square extiende Rectangle respetando LSP
class Square(Rectangle):
    def __init__(self, color, side):
        super().__init__(color, side, side)
    
    def set_width(self, width):
        # Mantiene la forma cuadrada
        self._width = width
        self._height = width
    
    def set_height(self, height):
        # Mantiene la forma cuadrada
        self._height = height
        self._width = height


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def calculate_area(self):
        import math
        return math.pi * self.radius ** 2
    
    def calculate_perimeter(self):
        import math
        return 2 * math.pi * self.radius


# Ejemplo de violación LSP con vehículos
class BadVehicle:
    """❌ Clase que viola LSP"""
    
    def __init__(self, brand):
        self.brand = brand
    
    def start_engine(self):
        print(f"{self.brand} motor encendido")
    
    def accelerate(self):
        print(f"{self.brand} acelerando")


class BadBicycle(BadVehicle):
    def __init__(self, brand):
        super().__init__(brand)
    
    def start_engine(self):
        # ❌ Viola LSP: Las bicicletas no tienen motor
        raise NotImplementedError("Las bicicletas no tienen motor!")


# ✅ Versión corregida que respeta LSP
class Vehicle(ABC):
    """Clase base abstracta para vehículos"""
    
    def __init__(self, brand):
        self.brand = brand
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass


class MotorVehicle(Vehicle):
    """Vehículos con motor"""
    
    @abstractmethod
    def start_engine(self):
        pass
    
    @abstractmethod
    def stop_engine(self):
        pass


class ManualVehicle(Vehicle):
    """Vehículos manuales"""
    
    @abstractmethod
    def pedal(self):
        pass


class Car(MotorVehicle):
    def move(self):
        print(f"{self.brand} avanzando en carretera")
    
    def stop(self):
        print(f"{self.brand} frenando")
    
    def start_engine(self):
        print(f"{self.brand} motor encendido")
    
    def stop_engine(self):
        print(f"{self.brand} motor apagado")


class Bicycle(ManualVehicle):
    def move(self):
        print(f"{self.brand} pedaleando")
    
    def stop(self):
        print(f"{self.brand} frenando con las manos")
    
    def pedal(self):
        print(f"{self.brand} pedaleando más fuerte")


# Clases que trabajan con las abstracciones
class BirdCare:
    """Cuidado de pájaros que respeta LSP"""
    
    def feed_bird(self, bird: Bird):
        print(f"Alimentando a {bird.name}")
        bird.eat()
    
    def put_bird_to_sleep(self, bird: Bird):
        print(f"Poniendo a dormir a {bird.name}")
        bird.sleep()
    
    def exercise_flying_bird(self, flying_bird: Flyable):
        print("Ejercitando pájaro volador")
        flying_bird.fly()
        print(f"Velocidad de vuelo: {flying_bird.get_flight_speed()} km/h")
    
    def exercise_swimming_bird(self, swimming_bird: Swimmable):
        print("Ejercitando pájaro nadador")
        swimming_bird.swim()
        print(f"Velocidad de nado: {swimming_bird.get_swim_speed()} km/h")


class ShapeCalculator:
    """Calculadora que trabaja con formas respetando LSP"""
    
    def print_shape_info(self, shape: Shape):
        print(f"Forma {shape.get_color()} - Área: {shape.calculate_area():.2f}, "
              f"Perímetro: {shape.calculate_perimeter():.2f}")
    
    def get_total_area(self, shapes):
        total = 0
        for shape in shapes:
            total += shape.calculate_area()
        return total
    
    def resize_rectangle(self, rectangle: Rectangle, new_width, new_height):
        """Función que funciona con Rectangle y sus subclases"""
        print(f"Redimensionando {rectangle.get_color()} rectangle:")
        print(f"  Área original: {rectangle.calculate_area():.2f}")
        
        rectangle.set_width(new_width)
        rectangle.set_height(new_height)
        
        print(f"  Área nueva: {rectangle.calculate_area():.2f}")


def main():
    print("=== EJEMPLO LSP - PRINCIPIO DE SUSTITUCIÓN DE LISKOV ===\n")
    
    # Ejemplo con pájaros
    print("🐦 Manejo de pájaros:")
    bird_care = BirdCare()
    
    birds = [Eagle(), Penguin(), Duck(), Ostrich()]
    
    # ✅ Todos los pájaros pueden ser alimentados (comportamiento común)
    print("--- Alimentando pájaros ---")
    for bird in birds:
        bird_care.feed_bird(bird)
        bird.make_sound()
    
    print("\n--- Ejercitando pájaros por habilidad ---")
    # Solo ejercitamos pájaros según sus habilidades específicas
    for bird in birds:
        if isinstance(bird, Flyable):
            bird_care.exercise_flying_bird(bird)
        if isinstance(bird, Swimmable):
            bird_care.exercise_swimming_bird(bird)
    
    # Ejemplo con formas geométricas
    print("\n📐 Manejo de formas geométricas:")
    calculator = ShapeCalculator()
    
    shapes = [
        Rectangle("Rojo", 5, 3),
        Square("Azul", 4),
        Circle("Verde", 3)
    ]
    
    # ✅ Todas las formas pueden ser procesadas igual
    for shape in shapes:
        calculator.print_shape_info(shape)
    
    print(f"\nÁrea total de todas las formas: {calculator.get_total_area(shapes):.2f}")
    
    # Demostración de LSP con Rectangle y Square
    print("\n--- Demostrando LSP con Rectangle y Square ---")
    rectangle = Rectangle("Naranja", 6, 4)
    square = Square("Morado", 5)
    
    # ✅ Square puede sustituir a Rectangle sin problemas
    calculator.resize_rectangle(rectangle, 8, 6)
    calculator.resize_rectangle(square, 7, 7)  # Square mantiene su invariante
    
    print("\n✅ Ventajas del LSP:")
    print("- Las subclases pueden reemplazar a sus superclases")
    print("- Comportamiento predecible y consistente")
    print("- Polimorfismo seguro y confiable")
    print("- Facilita el testing y mantenimiento")
    print("- Reduce bugs por comportamientos inesperados")


if __name__ == "__main__":
    main()