if __name__ == '__main__':
    print("Ingrese el numero de caracteres: "),
    n = int(raw_input())
    a,b = 0,1
    for i in range(n):
        a, b = b, a + b
        print(b),
