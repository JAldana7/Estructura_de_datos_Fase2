from views.loginview import LoginView
from controllers.login_controller import LoginController

def main():
    # 1. Instanciar la vista de Login
    app_login = LoginView()
    
    # 2. Instanciar el controlador y asociarle la vista
    controller = LoginController(app_login)
    
    # 3. Iniciar el bucle de la aplicación
    app_login.mainloop()

if __name__ == "__main__":
    main()