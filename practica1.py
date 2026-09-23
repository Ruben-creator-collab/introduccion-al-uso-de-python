def main():
    lista = ["Manzana", "Pera", "Melocotón"]
    lista_2 = ["Kiwi", "Sandía", "Melón"]
    lista.extend(lista_2)
    print("Último elemento de la lista: ", lista[-1])

    numeros = (3,5,7)
    print("Primer elemento de la tupla: ", numeros[0])

    inicio = int(input("Introduce el inicio: "))
    fin = int(input("Introduce el fin: "))
    salto = int(input("Introduce el salto: "))

    rango = range(inicio, fin, salto)

    print("Rango: ", list(rango))


if __name__ == "__main__":
    main()
    