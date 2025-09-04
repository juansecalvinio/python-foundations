def divide_numbers():
    try:
        a = int(input("Ingresa el numerador: "))  # numero de arriba
        b = int(input("Ingresa el demoninador: "))  # numero de abajo
        result = a / b
    except ZeroDivisionError:
        print("ERROR: No se puede dividir por cero")
    except ValueError:
        print("ERROR: Debes ingresar números válidos")
    except Exception as error:
        print(type(error))
    else:
        print("---------------------------")
        print("Resultado:", result)
        print("---------------------------")

        return result
    finally:
        print("Gracias por usar nuestro programa.")


divide_numbers()
