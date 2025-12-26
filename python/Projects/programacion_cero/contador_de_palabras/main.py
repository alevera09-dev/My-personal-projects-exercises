# pedir texto hasta que el usuario desee

def main():
    # imports
    from time import sleep
    
    # variables globales main
    text: str = None
    opc: str = None
    cont_words: int = 0
    palabras_frecuentes: dict[str:int] = {}
    
    # bucle main
    while True:
        text = input("Digita lo que sea: ")
        opc = input("Quieres continuar?[y/n]: ").lower()
        
        # Exception of close option 
        while opc != 'y' and opc != 'n':
            opc = input("Quieres continuar?[y/n]: ").lower()
        
        text = text.split(" ")
        for word in text:
            if word in ['!', '?', '¡', '¡']:
                continue
            
            if word in palabras_frecuentes.keys():
                palabras_frecuentes[word] +=  1
            else:
                palabras_frecuentes[word] = 1
            
            cont_words += 1
        
        match opc:
            case 'y':
                continue
            case 'n':
                break
            case _:
                print("Imposible llegar aqui.")
                
    print("\n-Cantidad de palabras:", cont_words)
    
    print("\n---Palabras mas frecuentes---")
    i: int = 0
    for key, value in palabras_frecuentes.items():
        print(f"{key}: {value}.")
        i += 1
        if i == 4:
            break
                
if __name__ == "__main__":
    main()