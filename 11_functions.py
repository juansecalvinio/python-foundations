def hello_world():
    print("Hello, world!")

# -------------------------
# parameters with default values
# -------------------------


def hello(greet="Hello", name="World"):
    print(f"{greet}, {name}!")


# no args
hello_world()
hello()

# args
hello("Hello", "John")
hello("Hola", "Juan")

# kwargs
hello(name="Eberechi", greet="Hey")

# -------------------------
# args and kwargs
# -------------------------


def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return kwargs


print(big_function(1, 2, 3, 4, 5, name="John", age=33))
