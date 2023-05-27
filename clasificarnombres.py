nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pelé", "Juánes"]

magos = [] 
cientificos = []
otros = []

def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El Gran " + magos[i]
    return magos    

 
def imprimir_nombres():
    for nombre in nombres:
        print(nombre)

   

for nombre in nombres:
    if nombre in ["Harry Houdini", "David Blaine", "Teller"]:
        magos.append(nombre)
    elif nombre in ["Newton", "Hawking", "Einstein"]:
        cientificos.append(nombre)
    else:
        otros.append(nombre)


print("Lista completa de nombres:")
imprimir_nombres()

print("\nMagos grandiosos:", hacer_grandioso(magos))


print("\nCientíficos:", cientificos)

print("\nOtros:", otros)
