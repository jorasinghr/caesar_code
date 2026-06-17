nor_upper = "abcdefghijklmnopqrstuvwxyzæøå"
nor_lower = "ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ"
size = 29

def caesar_crypt(text, shift, c):
    result = []
    if c not in ('e', 'd'):
        raise ValueError("please provide 'd' for decrypt or 'e' for encrypt")
    if c == 'd':
        shift=-shift

    for char in text:
        if char in nor_upper:
            idx = nor_upper.index(char)
            result.append(nor_upper[(idx + shift) % size])
        elif char in nor_lower:
            idx = nor_lower.index(char)
            result.append(nor_lower[(idx + shift) % size])
        else:
            # mellomrom etc.
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    filetype = int(input("skriv 1 for tekstfil eller 0 for tekst: "))
    if filetype==1:
        path = input("skriv inn path til tekstfil: ")
        with open(path, "r", encoding="utf-8") as f:
            message = f.read()
    elif filetype==0:
        message = input("Skriv inn melding: ")
    else:
        ValueError('skriv 1 eller 0')

    shift = int(input("Skriv inn skift (1-28): "))
    crypt = input("Skriv 'd' for 'dekrypter', 'e' for 'krypter': ").lower()
    
    crypted = caesar_crypt(message, shift, crypt)
 
    print(f"\nOriginal:\n{message}")
    if crypt=='d':
        print(f"Kryptert:\n{crypted}")
    if crypt=='e':
        print(f"Dekryptert:\n{crypted}")