#!/usr/bin/env python3
def main():
    msg = input("Messaggio da decifrare: ")
    for k, testo in brute_force(msg):
        print(f"Messaggio decifrato con chiave {k}: {testo}")


def brute_force(ciphertext: str) -> list[tuple[int, str]]:
    msg_list = []

    for k in range(26):
        result = ""
        for char in ciphertext:
            if char.islower():
                result += chr((ord(char) - 97 - k) % 26 + 97)
            elif char.isupper():
                result += chr((ord(char) - 65 - k) % 26 + 65)
            else:
                result += char

        msg_list.append((k, result))

    return msg_list

if __name__ == "__main__":
    main()
