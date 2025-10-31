"""
PRINCIPIO O - OPEN/CLOSED PRINCIPLE (ABIERTO/CERRADO)

El código debe estar abierto a la extensión, pero cerrado a la modificación.
Podemos agregar nuevas funcionalidades sin cambiar las clases existentes.

Analogía: Enchufes y adaptadores - el enchufe no cambia, pero puedes conectar distintos aparatos.
"""

from abc import ABC, abstractmethod
import math

# ❌ VIOLACIÓN DEL PRINCIPIO OCP
# Esta clase debe modificarse cada vez que se agrega una nueva forma geométrica
class BadAreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return math.pi * shape.radius ** 2
        # ❌ Si queremos agregar Triangle, debemos MODIFICAR esta clase
        # elif isinstance(shape, Triangle):
        #     return (shape.base * shape.height) / 2
        else:
            return 0


# Clases auxiliares para el ejemplo incorrecto
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


# ✅ APLICACIÓN CORRECTA DEL PRINCIPIO OCP
# Definimos una interfaz que está cerrada a modificación pero abierta a extensión

class Shape(ABC):
    """Interfaz abstracta para formas geométricas"""
    
    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def get_shape_type(self):
        pass


# Implementaciones específicas - EXTENSIÓN sin modificación
class GoodRectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_area(self):
        return self.width * self.height
    
    def get_shape_type(self):
        return "Rectángulo"


class GoodCircle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_area(self):
        return math.pi * self.radius ** 2
    
    def get_shape_type(self):
        return "Círculo"


# ✅ Nueva forma agregada SIN MODIFICAR código existente
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return (self.base * self.height) / 2
    
    def get_shape_type(self):
        return "Triángulo"


class Pentagon(Shape):
    def __init__(self, side, apothem):
        self.side = side
        self.apothem = apothem
    
    def calculate_area(self):
        perimeter = 5 * self.side
        return (perimeter * self.apothem) / 2
    
    def get_shape_type(self):
        return "Pentágono"


# Esta clase NUNCA necesita modificarse cuando agregamos nuevas formas
class GoodAreaCalculator:
    def calculate_area(self, shape: Shape):
        return shape.calculate_area()
    
    def print_shape_info(self, shape: Shape):
        print(f"{shape.get_shape_type()} - Área: {shape.calculate_area():.2f}")
    
    def calculate_total_area(self, shapes):
        total = sum(shape.calculate_area() for shape in shapes)
        return total


# Ejemplo adicional: Sistema de descuentos extensible
class DiscountStrategy(ABC):
    """Estrategia abstracta para descuentos"""
    
    @abstractmethod
    def apply_discount(self, amount):
        pass
    
    @abstractmethod
    def get_discount_type(self):
        pass


class RegularCustomerDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.95  # 5% descuento
    
    def get_discount_type(self):
        return "Cliente Regular (5%)"


class VIPCustomerDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.85  # 15% descuento
    
    def get_discount_type(self):
        return "Cliente VIP (15%)"


class StudentDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.80  # 20% descuento
    
    def get_discount_type(self):
        return "Descuento Estudiante (20%)"


# ✅ Nueva estrategia agregada SIN MODIFICAR código existente
class SeniorDiscount(DiscountStrategy):
    def apply_discount(self, amount):
        return amount * 0.75  # 25% descuento
    
    def get_discount_type(self):
        return "Descuento Adulto Mayor (25%)"


class HolidayDiscount(DiscountStrategy):
    def __init__(self, holiday_name, discount_percentage):
        self.holiday_name = holiday_name
        self.discount_percentage = discount_percentage
    
    def apply_discount(self, amount):
        multiplier = 1 - (self.discount_percentage / 100)
        return amount * multiplier
    
    def get_discount_type(self):
        return f"Descuento {self.holiday_name} ({self.discount_percentage}%)"


class PriceCalculator:
    def calculate_final_price(self, original_price, discount_strategy: DiscountStrategy):
        return discount_strategy.apply_discount(original_price)
    
    def show_price_breakdown(self, original_price, discount_strategy: DiscountStrategy):
        final_price = self.calculate_final_price(original_price, discount_strategy)
        discount_amount = original_price - final_price
        
        print(f"Precio original: ${original_price:.2f}")
        print(f"Descuento ({discount_strategy.get_discount_type()}): -${discount_amount:.2f}")
        print(f"Precio final: ${final_price:.2f}")


# Ejemplo adicional: Sistema de procesamiento de pagos
class PaymentProcessor(ABC):
    """Procesador abstracto de pagos"""
    
    @abstractmethod
    def process_payment(self, amount, payment_details):
        pass
    
    @abstractmethod
    def get_processor_name(self):
        pass


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount, payment_details):
        card_number = payment_details.get('card_number', 'XXXX')
        print(f"Procesando pago de ${amount:.2f} con tarjeta de crédito {card_number[-4:]}")
        return {"status": "success", "transaction_id": f"CC_{hash(card_number) % 10000}"}
    
    def get_processor_name(self):
        return "Tarjeta de Crédito"


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount, payment_details):
        email = payment_details.get('email', 'usuario@ejemplo.com')
        print(f"Procesando pago de ${amount:.2f} con PayPal para {email}")
        return {"status": "success", "transaction_id": f"PP_{hash(email) % 10000}"}
    
    def get_processor_name(self):
        return "PayPal"


# ✅ Nuevos procesadores agregados SIN MODIFICAR código existente
class BitcoinProcessor(PaymentProcessor):
    def process_payment(self, amount, payment_details):
        wallet = payment_details.get('wallet_address', 'XXXX')
        print(f"Procesando pago de ${amount:.2f} con Bitcoin a wallet {wallet[:6]}...")
        return {"status": "success", "transaction_id": f"BTC_{hash(wallet) % 10000}"}
    
    def get_processor_name(self):
        return "Bitcoin"


class BankTransferProcessor(PaymentProcessor):
    def process_payment(self, amount, payment_details):
        account = payment_details.get('account_number', 'XXXX')
        print(f"Procesando transferencia de ${amount:.2f} a cuenta {account[-4:]}")
        return {"status": "success", "transaction_id": f"BT_{hash(account) % 10000}"}
    
    def get_processor_name(self):
        return "Transferencia Bancaria"


class PaymentService:
    """Servicio que nunca necesita modificarse"""
    
    def process_order_payment(self, amount, processor: PaymentProcessor, payment_details):
        print(f"\n💰 Procesando pago con {processor.get_processor_name()}")
        result = processor.process_payment(amount, payment_details)
        
        if result["status"] == "success":
            print(f"✅ Pago exitoso. ID de transacción: {result['transaction_id']}")
        else:
            print(f"❌ Error en el pago: {result.get('error', 'Error desconocido')}")
        
        return result


def main():
    print("=== EJEMPLO OCP - PRINCIPIO ABIERTO/CERRADO ===\n")
    
    # Ejemplo con formas geométricas
    print("📐 Cálculo de áreas:")
    calculator = GoodAreaCalculator()
    
    shapes = [
        GoodRectangle(5, 3),
        GoodCircle(4),
        Triangle(6, 8),
        Pentagon(4, 2.75)
    ]
    
    for shape in shapes:
        calculator.print_shape_info(shape)
    
    total_area = calculator.calculate_total_area(shapes)
    print(f"\nÁrea total de todas las formas: {total_area:.2f}")
    
    # Ejemplo con descuentos
    print("\n💰 Sistema de descuentos:")
    price_calc = PriceCalculator()
    original_price = 100.0
    
    discount_strategies = [
        RegularCustomerDiscount(),
        VIPCustomerDiscount(),
        StudentDiscount(),
        SeniorDiscount(),
        HolidayDiscount("Black Friday", 30)
    ]
    
    for strategy in discount_strategies:
        print(f"\n--- {strategy.get_discount_type()} ---")
        price_calc.show_price_breakdown(original_price, strategy)
    
    # Ejemplo con procesamiento de pagos
    print("\n💳 Sistema de procesamiento de pagos:")
    payment_service = PaymentService()
    amount = 250.0
    
    # Diferentes procesadores de pago
    processors_and_details = [
        (CreditCardProcessor(), {"card_number": "1234567890123456"}),
        (PayPalProcessor(), {"email": "usuario@ejemplo.com"}),
        (BitcoinProcessor(), {"wallet_address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa"}),
        (BankTransferProcessor(), {"account_number": "123456789012"})
    ]
    
    for processor, details in processors_and_details:
        payment_service.process_order_payment(amount, processor, details)
    
    print("\n✅ Ventajas del OCP:")
    print("- Extensión sin modificación del código existente")
    print("- Reduce el riesgo de introducir bugs")
    print("- Facilita el mantenimiento y testing")
    print("- Permite polimorfismo efectivo")
    print("- Código más flexible y escalable")


if __name__ == "__main__":
    main()