def rotate(text, key):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    rotated = ''

    for char in text:
        if char.lower() in alpha:
            old_idx = alpha.index(char.lower())
            new_char = alpha[(old_idx + key) % 26]
            rotated += new_char if char.islower() else new_char.upper()
        else:
            rotated += char
    return rotated