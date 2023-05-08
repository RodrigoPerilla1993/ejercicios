ejercicios = int(input("entre al numero que desea ejecutar"))
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













