
from create import create_user
from read import read_users
from update import update_user
from delete import delete_user

def main():
    while True:
        print("\nMenu de Usuario")
        print("1. Crear usuario")
        print("2. Leer usuarios")
        print("3. Actualizar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "1":
            nom = input("Nombre: ")
            cognom = input("Apellido: ")
            edat = int(input("Edad: "))
            email = input("Email: ")
            create_user(nom, cognom, edat, email)

        elif opcion == "2":
            read_users()

        elif opcion == "3":
            user_id = int(input("ID del usuario a actualizar: "))
            nom = input("Nombre (dejar vacío si no deseas cambiarlo): ") or None
            cognom = input("Apellido (dejar vacío si no deseas cambiarlo): ") or None
            edat = input("Edad (dejar vacío si no deseas cambiarlo): ")
            edat = int(edat) if edat else None
            email = input("Email (dejar vacío si no deseas cambiarlo): ") or None
            update_user(user_id, nom, cognom, edat, email)

        elif opcion == "4":
            user_id = int(input("ID del usuario a eliminar: "))
            delete_user(user_id)

        elif opcion == "5":
            print("Saliendo del programa...")
            break

        else:
            print("Opcion no valida, por favor selecciona una opcion valida.")

if __name__ == "__main__":
    main()
