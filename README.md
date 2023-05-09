# EJERCICIOS DE OPERADORES
ejercicios = int(input("entre al numero que desea ejecutar"))
("
if ejercicios == 1:
  base = int(input("ingrese la base del triangulo: "))
  altura = int(input("ingrese la altura del triangulo: "))
  area = (base*altura) /2
  print("el area del triangulo es: ", area)

if ejercicios == 2:
  n1 = int(input("numero 1: "))
  n2 = int(input("numero 2: "))
  x = (n1+n2)
  print("la suma:", x)

if ejercicios == 3:
  n1 = int(input("numero 1: "))
  n2 = int(input("numero 2: "))
  x = (n1**n2)
  print("el numero al cuadrado es:", x)

if ejercicios == 4:
  a = 1234
  b = 532
  c = (a+b)
  print("la suma de 1234+532 es de", c)
if ejercicios == 5:
  a = 1234
  b = 532
  c = (a-b)
  print("la resta de 1234 y 532 es:", c)

if ejercicios == 6:
  a = 1234
  b = 532
  c = (a*b)
  print("la multiplicacion de 1234 y 532 es", c)

if ejercicios == 7:
  a = 1234
  b = 532
  c = (a/b)
  print("la division de 1234 y 532 es", c)

if ejercicios == 8:
  a = 1234
  b = 532 
  c = (a%b)
  print("el modulo de 1234 y 532 es:", c)

if ejercicios == 9:
  euros = float(input("Ingrese la cantidad en euros: "))
  dolar = 1.12  

  dolares = euros * dolar

  print("La cantidad en dólares es:", dolares)

if ejercicios == 10:
  base = float(input("Ingrese la base del rectángulo: "))
  altura = float(input("Ingrese la altura del rectángulo: "))
  area = (base*altura)
  print("El área del rectángulo es:", area)

if ejercicios == 11:
  lado = float(input("Ingrese el valor del lado del cuadrado: "))
  area = lado ** 2
  perimetro = lado * 4  
  print("El área del cuadrado es:", area)
  print("El perímetro del cuadrado es:", perimetro)

if ejercicios == 12:
  radio = float(input("Ingrese el radio del cilindro: "))
  altura = float(input("Ingrese la altura del cilindro: "))

  area_1 = 3.14159 * radio**2
  area_2 = 2 * 3.14159 * radio * altura
  area_total = 2 * area_1 + area_2

  volumen = area_1 * altura

  print("El área del cilindro es:", area_total)
  print("El volumen del cilindro es:", volumen)
  

if ejercicios == 13:
  radio = float(input("Ingrese el radio de la circunferencia:     "))

  longitud = 2 * 3.14159 * radio
  print("La longitud de la circunferencia es:", longitud)

  area = 3.14159 * (radio**2)
  print("El área del círculo es:", area)

if ejercicios == 14:
  n1 = float(input("ingrese un numero"))
  n2 = float(input("ingrese un segundo numero"))
  n3 = float(input("ingrese un tercer numero"))
  promedio = (n1+n2+n3)/3
  print("el promedio es:", promedio)

#EJERICICIOS CONDICIONALES 
ejercicios = int(input("ingrese el ejercicio que desea ejecutar"))

if ejercicios == 1:
  print ("codigo para saber si un codigo es positivo o           negativo")
  number1 = int(input("ingrese un numero: "))

  if number1 > 0:
    print ("el numero", number1 ,"es positivo")
  elif number1 < 0:
    print("el numero", number1 , "es negativo")
  else:
    print(number1 , "se considera un numero neutro")

elif ejercicios == 2:
  number1 = int(input("ingresa un numero: "))
  number2 = int(input("ingresa un numero: "))
  if number1 > number2:
    print (number1,"es mayor", number2)
  elif number1 < number2:
    print (number1,"es menor", number2)
  if number2 > number1:
    print (number2,"es mayor", number1)
  elif number2 < number1:
    print (number2,"es menor", number1)
 



elif ejercicios == 3:

  number1 = int(input("Ingrese el primer número: "))
  number2 = int(input("Ingrese el segundo número: "))
  number3 = int(input("Ingrese el tercer número: "))

  if number1 >= number2 and number1 >= number3:
   mayor = number1
  elif number2 >= number1 and number2 >= number3:
    mayor = number2
  else:
    mayor = number3

  
  if number1 <= number2 and number1 <= number3:
    menor = number1
  elif number2 <= number1 and number2 <= number3:
    menor = number2
  else:
    menor = number3

  print("El número mayor es:", mayor)
  print("El número menor es:", menor)

  
elif ejercicios == 4: 
  nombre_empleado = input("Ingrese el nombre del empleado: ")
  horas_normales = float(input("Ingrese las horas normales trabajadas: "))
  horas_extras = float(input("Ingrese las horas extras trabajadas: "))

  valor_hora = 4.0 

  sueldo_normal = horas_normales * valor_hora
  sueldo_extra = horas_extras * valor_hora_extra

  sueldo_total = sueldo_normal + sueldo_extra

  print("Nombre del empleado:", nombre_empleado)
  print("Sueldo normal:", sueldo_normal)
  print("Sueldo extra:", sueldo_extra)
  print("Sueldo total:", sueldo_total)
  
elif ejercicios == 5: 
    A = int(input("Enter the value of A: "))
    B = int(input("Enter the value of B: "))
    if A < B:
      C = A + B
    else:
      C = A - B
      print("The resultado es:", C)  
  
elif ejercicios == 6:
    def calcular_cociente(A, B):
      if B == 0:
        return "La división no es posible, B es igual a cero."
      else:
        cociente = A / B
        return cociente
      A = 10
      B = 2
      resultado = calcular_cociente(A, B)
      print("El cociente entre A y B es:", resultado)

elif  ejercicios == 7:
    numDia = int(input("ingrese un numero para ver en el dia       de la semana que corresponde"))
    if numDia == 1:
      print(("lunes"))
    elif numDia == 2:
      print("martes")
    elif numDia == 3:
      print("miercoles")
    elif numDia == 4:
      print("jueves")
    elif numDia == 5:
      print("viernes")
    elif numDia == 6:
      print("sabado")
    elif numDia == 7:
      print("domingo")
    else:
      print("Error ingrese un numero del 1 al 7")

if ejercicios == 8:
  lado1 = 5
  lado2 = 5
  lado3 = 5

  if lado1 == lado2 and lado2 == lado3:
    print("El triángulo es equilátero")
  else:
    print("El triángulo no es equilátero")
  if ejercicios ==9:
     
    A = int(input("Ingrese el valor de A: "))
    B = int(input("Ingrese el valor de B: "))
  if A < 0 or B < 0:
    
   resultado = A + B
  else:
    
   resultado = A * B


   print("El resultado es: ", resultado)

if ejercicios == 10: 
  dia = int(input("Ingresa el día de nacimiento: "))
  mes = int(input("Ingresa el mes de nacimiento: "))

  if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
    signo = "Acuario"
  elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
    signo = "Piscis"
  elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
    signo = "Aries"
  elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "Tauro"
  elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
    signo = "Géminis"
  elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
    signo = "Cáncer"
  elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
    signo = "Leo"
  elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
    signo = "Virgo"
  elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
    signo = "Libra"
  elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
    signo = "Escorpio"
  elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
    signo = "Sagitario"
  else:
    signo = "Capricornio"

  print("Tu signo zodiacal es:", signo)  

if ejercicios == 11:
  base = int(input("Ingresa la base del cuadrilátero: "))
  altura = int(input("Ingresa la altura del cuadrilátero: "))

  if base == altura:
    tipo = "cuadrado"
    perimetro = 4 * base
    area = base * altura
  else:
    tipo = "rectángulo"
    perimetro = 2 * (base + altura)
    area = base * altura

  print("El cuadrilátero es un", tipo)
  print("Perímetro:", perimetro)
  print("Superficie:", area)

if ejercicios == 12:
  precio_venta = int(input("Ingresa el precio de venta: "))

  if precio_venta < 100:
    descuento_porcentaje = 5
  elif precio_venta < 200:
    descuento_porcentaje = 10
  else:
    descuento_porcentaje = 15

  descuento = precio_venta * (descuento_porcentaje / 100)
  precio_final = precio_venta - descuento

  print("Descuento realizado: $", descuento)
  print("Precio final con descuento: $", precio_final)

if ejercicios == 13:
  total_varones = 0
  total_mujeres = 0
  total_general = 0

  cantidad_nacimientos = int(input("Ingrese la cantidad de nacimientos a registrar: "))

if ejercicios == 14:
    for _ in range(cantidad_nacimientos):
      dia = int(input("Ingrese el día de nacimiento: "))
      mes = int(input("Ingrese el mes de nacimiento: "))
      año = int(input("Ingrese el año de nacimiento: "))
      sexo = int(input("Ingrese el sexo (1 para femenino, 2          para     masculino): "))

    if sexo == 1:
        total_mujeres += 1
    elif sexo == 2:
        total_varones += 1

    total_general += 1

    print("Total de varones:", total_varones)
    print("Total de mujeres:", total_mujeres)
    print("Total general:", total_general)
