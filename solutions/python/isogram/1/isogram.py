def is_isogram(phrase):
    phrase = phrase.lower()
    letters = [char for char in phrase if char.isalpha()]
    return len(set(letters)) == len(letters)
