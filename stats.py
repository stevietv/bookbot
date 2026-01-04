def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    words = text.split()
    characters = {}

    for word in words:
        for char in word:
            char = char.lower()
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1
    
    return characters    

def get_alpha_characters(characters):
    result = []
    for char in characters:
        if char.isalpha():
            result.append({"char": char, "num": characters[char]})
    result.sort(key=lambda x: x["num"], reverse=True)
    
    return result
