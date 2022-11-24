menu = """Bienvenido a las tablas de multiplicar en matematicas, aqui aprenderas todas las tablas de multiplicar que hay del 1 al 10:
Porfavor elige la opcion del 1 al 10 para que te muestre la tabla que quieras aprender hoy:
1.- Tabla del 1
2.- Tabla del 2
3.- Tabla del 3
4.- Tabla del 4
5.- Tabla del 5
6.- Tabla del 6
7.- Tabla del 7
8.- Tabla del 8
9.- Tabla del 9
10.- Tabla del 10: """
opcion = int(input(menu))
if opcion == 1:
 for i in range(1, 11):
  print("1 x {} = {}".format(i, i * 1))
elif opcion == 2:
 for i in range(1, 11):
  print("2 x {} = {}".format(i, i * 2))
elif opcion == 3:
 for i in range(1, 11):
  print("3 x {} = {}".format(i, i * 3))
elif opcion == 4:
 for i in range(1, 11):
  print("4 x {} = {}".format(i, i * 4))
elif opcion == 5:
 for i in range(1, 11):
  print("5 x {} = {}".format(i, i * 5))
elif opcion == 6:
 for i in range(1, 11):
  print("6 x {} = {}".format(i, i * 6))
elif opcion == 7:
 for i in range(1, 11):
  print("7 x {} = {}".format(i, i * 7))
elif opcion == 8:
 for i in range(1, 11):
  print("8 x {} = {}".format(i, i * 8))
elif opcion == 9:
 for i in range(1, 11):
  print("9 x {} = {}".format(i, i * 9))
elif opcion == 10:
 for i in range(1, 11):
  print("10 x {} = {}".format(i, i * 10))
else:
 print("¡Lo siento solo puedes elegir las tablas de multiplicar del 1 a 10!")