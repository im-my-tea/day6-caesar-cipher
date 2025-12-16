import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = int(input("Type '1' to encrypt, type '2' to decrypt:"))
text = input("Type your cipher text:").lower()
shift = int(input("Type the shift number:"))


def caesar(text, shift):
    cipher_text = ""
    for i in text:
        position = alphabet.index(i)
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded/decoded text is {cipher_text}")

if direction == 1:
    caesar(text, shift)
elif direction == 2:
    caesar(text, shift * -1)
else:
    print("Invalid input")

