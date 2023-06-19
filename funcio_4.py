class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def obtener_datos(self):
        return f"Nombre: {self.nombre}, Salario: {self.salario}"

    def calcular_pago(self):
        return self.salario


class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre, salario_mensual)

    def calcular_pago(self):
        return self.salario

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, salario_hora, horas_trabajadas):
        super().__init__(nombre, salario_hora)
        self.horas_trabajadas = horas_trabajadas

    def obtener_datos(self):
        return super().obtener_datos() + f", Horas trabajadas: {self.horas_trabajadas}"

    def calcular_pago(self):
        return self.salario * self.horas_trabajadas

# Ejemplo de uso
empleado1 = EmpleadoTiempoCompleto("Juan", 4000)
empleado2 = EmpleadoPorHoras("Ana", 20, 80)

print(empleado1.obtener_datos())
print("Pago:", empleado1.calcular_pago())

print(empleado2.obtener_datos())
print("Pago:", empleado2.calcular_pago())
