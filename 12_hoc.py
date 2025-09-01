# higher order functions
# funciones de order superior:
# funciones que reciben funciones como argumentos
# o retornan una funcion, como en JavaScript

def require_auth(func):
    def wrapper(user: str):
        if user.lower() == "admin":
            return func(user)
        else:
            return "Acceso denegado"

    return wrapper


def admin_dashboard(user):
    return f"Bienvenido al panel de administrador, {user}"


auth_view_dashboard = require_auth(admin_dashboard)
print(auth_view_dashboard("Admin"))
print(auth_view_dashboard("Guest"))
