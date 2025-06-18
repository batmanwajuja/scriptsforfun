import os

# Constants for uppercase alphabet
A = ord('A')
Z = ord('Z')
ALPHABET_SIZE = Z - A + 1

def caesar(text, shift):
    result = ''

    for ch in text.upper():
        if ch.isalpha():
            shifted = ord(ch) + shift

            if shifted > Z:
                shifted -= ALPHABET_SIZE
            elif shifted < A:
                shifted += ALPHABET_SIZE

            result += chr(shifted)
        else:
            result += ch

    return result

def get_input():
    choice = input("Input from (1) keyboard or (2) file? ").strip()

    if choice == '1':
        return input("Enter your message: ")
    
    elif choice == '2':
        path = input("Enter file path: ").strip()
        if not os.path.exists(path):
            print("File not found.")
            exit(1)
        with open(path, 'r') as f:
            return f.read()
    
    else:
        print("Invalid input option.")
        exit(1)

def output_result(text):
    choice = input("Output to (1) screen or (2) file? ").strip()

    if choice == '1':
        print("\n=== Result ===")
        print(text)
    
    elif choice == '2':
        path = input("Enter output file name: ").strip()
        with open(path, 'w') as f:
            f.write(text)
        print(f"Result written to '{path}'")
    
    else:
        print("Invalid output option.")
        exit(1)

def main():
    print("Caesar Cipher")
    mode = input("Choose mode - (E)ncrypt or (D)ecrypt: ").strip().lower()

    if mode not in ['e', 'd']:
        print("Invalid mode. Use 'E' or 'D'.")
        exit(1)

    try:
        key = int(input("Enter shift key (integer): "))
    except ValueError:
        print("Shift key must be an integer.")
        exit(1)

    if mode == 'd':
        key = -key

    message = get_input()
    result = caesar(message, key)
    output_result(result)

if __name__ == '__main__':
    main()
