def encode(plain_text):
    clean_text = "".join(ch for ch in plain_text.lower() if ch.isalnum())
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")
    encoded = clean_text.translate(table)
    return " ".join("".join(encoded[i:i+5]) for i in range(0, len(encoded), 5))
    

def decode(ciphered_text):
    text = ciphered_text.replace(" ","")
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba")
    decoded = text.translate(table)
    return decoded
