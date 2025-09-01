# decorators
# es una forma elegante de modificar el comportamiento de una funcion
# sin modificar su codigo fuente

def require_auth(func):
    def wrapper(user: str):
        if user.lower() == "admin":
            return func(user)
        else:
            return "Acceso denegado"

    return wrapper


@require_auth
def admin_dashboard(user):
    return f"Bienvenido al panel de administrador, {user}"


print(admin_dashboard("Admin"))
print(admin_dashboard("Guest"))
