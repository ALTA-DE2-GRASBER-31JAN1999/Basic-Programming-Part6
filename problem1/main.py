def compare(a, b):
    pattern = ""
    for char_a, char_b in zip(a, b):
        if char_a == char_b:
            pattern += char_a
        else:
            break
    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI")) # AKA
    print(compare("KANGOORO", "KANG")) # KANG
    print(compare("KI", "KIJANG")) # KI
    print(compare("KUPU-KUPU", "KUPU")) # KUPU
    print(compare("ILALANG", "ILA")) # ILA