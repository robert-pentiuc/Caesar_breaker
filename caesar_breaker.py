#!/usr/bin/env python3
def main():
    msg = input("Messaggio da decifrare: ")
    for k, testo in brute_force(msg):
        print(f"Messaggio decifrato con chiave {k}: {testo}")

    msg = brute_force(msg)
    prob_text_key, prob_text = search_prob_text(msg)
    print(f"\nIl testo con più probabilità è quello con  Chiave : {prob_text_key} , {prob_text}")


def brute_force(ciphertext: str) -> list[tuple[int, str]]:
    msg_list = []

    for k in range(26):
        result = ""
        for char in ciphertext:
            if 'a' <= char <= 'z':
                result += chr((ord(char) - 97 + k) % 26 + 97)
            elif 'A' <= char <= 'Z':
                result += chr((ord(char) - 65 + k) % 26 + 65)
            else:
                result += char

        msg_list.append((k, result))

    return msg_list

def count_matches(text: str) -> tuple[int, str]:
    COMMON_ITALIAN = ["di", "il", "che", "è", "e", "la", "a", "per", "in", "un", "ciao"]
    COMMON_ENGLISH = ["the", "and", "of", "to", "a", "in", "is", "it", "you", "that", "hello"]

    words = text.lower().split()
    ita_matches = 0
    eng_matches = 0

    for word in COMMON_ITALIAN:
        if word in words:
            ita_matches += 1

    for word in COMMON_ENGLISH:
        if word in words:
            eng_matches += 1

    if ita_matches > eng_matches:
        return ita_matches, "it"
    else:
        return eng_matches, "en"




def search_prob_text(msglist: list[tuple[int, str]]) -> tuple[int, str]:

    prob_msg = ""
    prob_key = 0
    best_prob_ita = 0
    best_prob_en = 0

    for k, msg in msglist:
        prob=count_matches(msg)
        if prob[1] == "it":
            if prob[0] > best_prob_ita:
                best_prob_ita = prob[0]
                prob_msg_ita = msg
                prob_key_ita = k

        if prob[1] == "en":
            if prob[0] > best_prob_en:
                best_prob_en = prob[0]
                prob_msg_en = msg
                prob_key_en = k


    if best_prob_ita > best_prob_en:
        return prob_key_ita, prob_msg_ita
    else:
        return prob_key_en, prob_msg_en





if __name__ == "__main__":
    main()
