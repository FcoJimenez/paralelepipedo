# Define función para eliminar vocales de palabra paralelepípedo
def remove_vowels():
    counter = 0
    
    word = "paralelepípedo"
    vowels = ["a", "á", "e", "é", "i", "í", "o", "ó" "u", "ú"]

    for letter in word:
        counter += 1
        if letter in vowels:
            continue
        print(letter, counter)


# Añade convención
if __name__ == "__main__":
    remove_vowels()