def caesar(offset, input_str):
    result = ""
    for char in input_str:
        if char.isalpha():  # Check if character is a letter
            ascii_code = ord(char.lower())  # Convert to lowercase ASCII code
            shifted_code = (ascii_code - 97 + offset) % 26 + 97
            result += chr(shifted_code)
        else:
            result += char  # Preserve non-alphabetic characters
    return result
if __name__ == '__main__':
    print(caesar(3, "abc")) # def
    print(caesar(2, "alta")) # cnvc
    print(caesar(10, "alterraacademy")) # kvdobbkkmknowi
    print(caesar(1, "abcdefghijklmnopqrstuvwxyz")) # bcdefghijklmnopqrstuvwxyza
    print(caesar(1000, "abcdefghijklmnopqrstuvwxyz")) # mnopqrstuvwxyzabcdefghijkl