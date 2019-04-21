def shiftCharacter(c, k):
    if 'A' <= c and c <= 'Z':
        new_ord = ord(c) + ord(k) - ord('a')
        if new_ord > ord('Z'):
            new_ord -= 26
        return chr(new_ord)
    if 'a' <= c and c <= 'z':
        new_ord = ord(c) + ord(k) - ord('a')
        if new_ord > ord('z'):
            new_ord -= 26
        return chr(new_ord)
    raise Exception()

def caesarCipher(text, key):
    encrypted = ""
    for c in text:
        if 'A' <= c and c <= 'z':
            encrypted += shiftCharacter(c, key)
        else:
            encrypted += c
    return encrypted

if __name__ == "__main__":
    print(caesarCipher(input(), input()))
