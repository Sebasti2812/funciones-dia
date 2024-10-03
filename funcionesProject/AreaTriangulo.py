#ejemplo para calcular el are del triangulo


#from main import my_function

#variables de entrada
#base =int(input("ingrese la base:  "))
#altura =int(input("ingrese la altura:  "))


#proceso
#def calcularAreaTriangulo(b,a):
    #area = (b*a)/2
    #return  area

#resultado = calcularAreaTriangulo(base,altura)
#print(f"el area del triangulo cuya base {base}y altura {altura} es:  {resultado}")#



#funcion con argumento predeterminado

def my_function(country = "colombia"):
    print("i am from "+country)

my_function()
my_function("sweden")


#argumento args

def mostrarEstudiantes(*args):
    print("el estudiant: "+args[0])

#invocar la funcion
mostrarEstudiantes("Emil","tobias","linus")


#argumento palabra  clave valor
def mostrarCarros (carro1, carro2, carro3):
    print("el carro es:  " + carro2)

mostrarCarros(carro1= "BMW", carro3= "FERRARI", carro2= "Ford")


#argumento arbritario kwargs
def mostrarCliente(**kwargs):
    print("su apellido es: " + kwargs["nombre"])

mostrarCliente(nombre = "tobias", apellido= "refsnes")

#declaracion de paso
def mifuncion():
    pass