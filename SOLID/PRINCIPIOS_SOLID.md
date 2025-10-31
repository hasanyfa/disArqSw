# 🧠 Principios SOLID

Los **principios SOLID** son un conjunto de buenas prácticas de diseño de software orientado a objetos.  
Fueron definidos por **Robert C. Martin (Uncle Bob)** y ayudan a crear sistemas más **mantenibles, escalables y fáciles de entender**.

---

## 🧩 S – Single Responsibility Principle (Responsabilidad Única)

### 💬 Definición

Cada clase o módulo debe tener **una sola razón para cambiar**, es decir, una sola responsabilidad.

### 💻 Ejemplo técnico

Una clase `Report` que genera, imprime y guarda reportes tiene demasiadas tareas.  
✅ Mejor dividirla en:

-  `ReportGenerator`
-  `ReportPrinter`
-  `ReportSaver`

Así cada clase se encarga de una sola cosa.

### 🎯 Analogía

**El chef del restaurante.**  
El chef cocina, el mesero sirve, el cajero cobra.  
Si una sola persona hiciera todo, sería ineficiente y propensa a errores.  
Cada uno tiene su rol, igual que las clases deben tener una sola responsabilidad.

---

## 🔄 O – Open/Closed Principle (Abierto/Cerrado)

### 💬 Definición

El código debe estar **abierto a la extensión, pero cerrado a la modificación**.  
Podemos agregar nuevas funcionalidades sin cambiar las clases existentes.

### 💻 Ejemplo técnico

En lugar de modificar una clase `Shape` cada vez que agregas una nueva figura:  
✅ Define una interfaz `Shape` con el método `area()` y crea subclases (`Circle`, `Square`, `Triangle`).

### 🔌 Analogía

**Enchufes y adaptadores.**  
El enchufe de la pared (la interfaz) no cambia, pero puedes conectar distintos aparatos (implementaciones) usando adaptadores.  
El sistema se extiende sin romper el código original.

---

## 🧬 L – Liskov Substitution Principle (Sustitución de Liskov)

### 💬 Definición

Las clases hijas deben poder **reemplazar a sus clases padre** sin alterar el correcto funcionamiento del programa.

### 💻 Ejemplo técnico

Si tienes una clase `Bird` con el método `fly()`, una subclase `Penguin` no debería heredar ese método, porque no vuela.  
✅ Mejor crear jerarquías como `FlyingBird` y `NonFlyingBird`.

### 🚗 Analogía

**Vehículos intercambiables.**  
Si alquilas un “auto” y te entregan una bicicleta, se rompe la expectativa.  
Ambos son medios de transporte, pero no pueden sustituirse sin cambiar el comportamiento esperado.

---

## 🔌 I – Interface Segregation Principle (Segregación de Interfaces)

### 💬 Definición

Las clases no deben estar obligadas a implementar **métodos que no usan**.  
Es mejor tener varias interfaces pequeñas que una enorme.

### 💻 Ejemplo técnico

❌ Una interfaz `IMachine` con métodos `print()`, `scan()` y `fax()` obliga a una impresora simple a implementar funciones que no necesita.  
✅ Separar en:

-  `IPrinter`
-  `IScanner`
-  `IFax`

### 📺 Analogía

**Controles remotos específicos.**  
El control de la TV no debería tener botones para abrir el refrigerador.  
Cada aparato necesita su propio conjunto de botones.  
Así se evita la confusión y el desperdicio.

---

## 🧱 D – Dependency Inversion Principle (Inversión de Dependencias)

### 💬 Definición

Las clases de alto nivel no deben depender de clases concretas, sino de **abstracciones (interfaces)**.  
Los detalles deben depender de las abstracciones, no al revés.

### 💻 Ejemplo técnico

❌ `NotificationService` usa directamente `EmailClient`.  
✅ `NotificationService` depende de una interfaz `IMessenger`, y luego `EmailClient` o `SMSClient` implementan esa interfaz.

### 🔋 Analogía

**Cargadores universales.**  
Tu celular no depende de un cargador específico, sino de un estándar (USB o USB-C).  
Así puedes conectar distintos cargadores sin cambiar el teléfono.  
El “teléfono” depende de una **abstracción**, no de una implementación.

---

## 📘 Resumen visual con analogías

| Principio | Nombre                    | Idea técnica                                   | Analogía cotidiana                                |
| --------- | ------------------------- | ---------------------------------------------- | ------------------------------------------------- |
| **S**     | Responsabilidad Única     | Una clase, una función                         | 👨‍🍳 Cada persona con su rol (chef, mesero, cajero) |
| **O**     | Abierto/Cerrado           | Extiende sin modificar                         | 🔌 Enchufes y adaptadores                         |
| **L**     | Sustitución de Liskov     | Subclases deben comportarse como su padre      | 🚗 Autos intercambiables                          |
| **I**     | Segregación de Interfaces | Interfaces pequeñas y específicas              | 📺 Control remoto con solo los botones necesarios |
| **D**     | Inversión de Dependencias | Depender de abstracciones, no implementaciones | 🔋 Cargadores universales                         |

---

✨ **Conclusión:**  
Aplicar SOLID no solo mejora el código, sino también la **colaboración, escalabilidad y mantenibilidad** de los proyectos.  
Cada principio busca que el software sea **modular, limpio y adaptable** a los cambios futuros.
