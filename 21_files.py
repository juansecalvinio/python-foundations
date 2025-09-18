try:
    # Escribir en un archivo
    with open('test.txt', mode='w') as my_file:
        text = my_file.write(":)")
    # Leer el archivo
    with open('test.txt', mode='r') as my_file:
        print(my_file.readlines())
    # Leer y escribir en un archivo
    with open('test.txt', mode='r+') as my_file:
        print(my_file.readlines())
        text = my_file.write("Hola mundo\n")
    # Agregar texto al final del archivo
    with open('test.txt', mode='a') as my_file:
        text = my_file.write("123")
        print(text)

except FileNotFoundError:
    print(f"El archivo no existe.")
except Exception as error:
    print(f"Ocurrió un error: {error}")
