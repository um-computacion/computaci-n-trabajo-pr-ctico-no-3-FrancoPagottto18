from src.exceptions import NumeroDebeSerPositivo

def Ingrese_Numero():
    numero = input("Ingresa un número positivo: ")
    try:
    
        numero = int(numero)
        if numero < 0:
            raise NumeroDebeSerPositivo("El número debe ser positivo.")
        return numero
    except ValueError:
       

        print("Eso no es un número válido.") 
        raise ValueError("Eso no es un número válido.")
    except NumeroDebeSerPositivo as e:
        print(e)  

if __name__ == "__main__":
    try:
        numero = Ingrese_Numero()
        print(f"Número válido: {numero}")
    except Exception as e:
        print(f"Error: {e}")
