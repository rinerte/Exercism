def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sentence=sentence.lower()
    for i in alphabet:
        if i not in sentence:
            return False
    return True
