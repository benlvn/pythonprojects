from caesar import caesarCipher

def avg_diff(data1, data2):
    total_diff = 0.0
    n = 0
    for key in data1:
        # Assuming the two have the same exact keys
        total_diff += abs(data1[key] - data2[key])
        n += 1.0
    return total_diff / n

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    return [chr(c) for c in range(ord(c1), ord(c2) + 1)]    

def count_letter_freq(text):
    total_letters = 0
    letter_freqs = {}
    for c in char_range('a','z'):
        letter_freqs[c] = 0.0
    for c in text:
        if 'a' <= c and c <= 'z':
            letter_freqs[c] += 1
            total_letters += 1
        if 'A' <= c and c <= 'Z':
            letter_freqs[chr(ord(c) + 32)] += 1
            total_letters += 1
    for l in letter_freqs:
        letter_freqs[l] /= float(total_letters)
        letter_freqs[l] *= 100
    return letter_freqs

ENGLISH_FREQS = {
    'e': 12.02, 't': 9.10, 'a': 8.12, 'o': 7.68,
    'i': 7.31, 'n': 6.95, 's': 6.28, 'r': 6.02,
    'h': 5.92, 'd': 4.32, 'l': 3.98, 'u': 2.88,
    'c': 2.71, 'm': 2.61, 'f': 2.30, 'y': 2.11,
    'w': 2.09, 'g': 2.03, 'p': 1.82, 'b': 1.49,
    'v': 1.11, 'k': 0.69, 'x': 0.17, 'q': 0.11,
    'j': 0.10, 'z': 0.07
}

def decipher(text):
    best_key = None
    best_score = None
    for c in char_range('a','z'):
        ciphert = caesarCipher(text, c)
        score = avg_diff(count_letter_freq(ciphert), ENGLISH_FREQS)
        if best_key == None or score < best_score:
            best_score = score
            best_key = c
    return caesarCipher(text, best_key)

if __name__ == "__main__":
    print(decipher(input()))
