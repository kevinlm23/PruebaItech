# PruebaItech
Proyecto desarrollado como prueba para Itech en Django 1.9 - Python 2.7

A continuación se describen aspectos a tener en cuenta para la ejecución de la prueba:
- La página principal para usuario se ejecuta apartir de la siguiente dirección luego de ejecutar el servidor: http://localhost:8000/accounts/login/
- El usuario Super Administrador se creo con las siguientes credenciales:
    usuario: admin
    password: admin123 --> *No se dejo como admin unicamente debido a que django pedia por lo menos 8 caracteres

- Credenciales de otros usuarios para realizar pruebas rápidas en la página de usuarios:

    1. usuario: juan           * Permisos asignados desde el usuario super administrador: Solo puede añadir registros.
        password: prueba123

    2. usuario: maria          * Permisos asignados desde el usuario super administrador: Solo puede añadir y actualizar registros.
        password: prueba123

    NOTA: si el usuario intenta acceder a una función de la cual no tenga concedido el permiso este sera deslogueado