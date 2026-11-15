def find_anagrams(word, candidates):
    answer = []
    word_letters = {}
    for char in word.lower():
        word_letters[char] = word_letters.get(char, 0) + 1
        
    for candidate in candidates:
        if len(candidate)!=len(word):
            continue
        if candidate.lower()==word.lower():
            continue
        candidate_letters = {}
        for char in candidate.lower():
            candidate_letters[char] = candidate_letters.get(char, 0) + 1
        if candidate_letters==word_letters:
            answer.append(candidate)

    return answer
            
