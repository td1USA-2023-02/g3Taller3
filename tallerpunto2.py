import pulp

# Crear el problema
problema = pulp.LpProblem("Dieta", pulp.LpMinimize)

# Variables de decisión
x1 = pulp.LpVariable("Manzanas", 0, 6, pulp.LpInteger)
x2 = pulp.LpVariable("Plátanos", 0, 4, pulp.LpInteger)
x3 = pulp.LpVariable("Yogur", 0, 2, pulp.LpInteger)

# Función objetivo
problema += 0.5 * x1 + 0.4 * x2 + 1.2 * x3

# Restricciones de calorías
problema += 50 * x1 + 89 * x2 + 150 * x3 >= 2000, "Calorías"

# Restricciones de proteínas
problema += 1.2 * x1 + 1.1 * x2 + 3.4 * x3 >= 80, "Proteínas"

# Resolver el problema
problema.solve()
print("Estado:", pulp.LpStatus[problema.status])
print("Cantidad óptima de manzanas:", x1.varValue)
print("Cantidad óptima de plátanos:", x2.varValue)
print("Cantidad óptima de yogur:", x3.varValue)
print("Costo total mínimo:", pulp.value(problema.objective))

#El resultado obtenido muestra que el problema de optimización es infactible, lo que significa que no es 
#posible encontrar una solución que cumpla con todas las restricciones del problema. Sin embargo, los valores que 
#se muestran para "Cantidad óptima de manzanas," "Cantidad óptima de plátanos," "Cantidad óptima de yogur" y 
#"Costo total mínimo" no son relevantes en este contexto, ya que el problema es infactible y estos valores no tienen
#un significado realista. Esos valores no son útiles en este caso, ya que no cumplen con las restricciones 
# del problema, y no deberían ser interpretados como una solución válida en la práctica.
#Para resolver el problema de infactibilidad, es necesario revisar y ajustar las restricciones del problema, 
#los requisitos nutricionales o los límites máximos de consumo de alimentos para que sean factibles y representen 
# una situación realista.