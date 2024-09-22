import random

# Word lists
adjectives = ["silly", "wacky", "purple", "gigantic", "tiny", "smelly", "brave", "lazy", "mysterious", "loud"]
nouns = ["elephant", "pizza", "banana", "guitar", "snowman", "astronaut", "pickle", "unicorn", "volcano", "sock"]
verbs = ["danced", "exploded", "laughed", "sang", "flew", "snored", "juggled", "teleported", "whispered", "surfed"]
adverbs = ["quickly", "sneakily", "happily", "loudly", "awkwardly", "gracefully", "clumsily", "eagerly", "suddenly", "silently"]
names = ["Bob", "Zorg", "Captain Noodle", "Lady Gaga", "Pickle Rick", "Fluffy", "Dr. Giggles", "Sparkles", "Groot", "Ziggy"]

def get_word(word_type):
    if word_type == "adjective":
        return random.choice(adjectives)
    elif word_type == "noun":
        return random.choice(nouns)
    elif word_type == "verb":
        return random.choice(verbs)
    elif word_type == "adverb":
        return random.choice(adverbs)
    elif word_type == "name":
        return random.choice(names)
    elif word_type == "plural noun":
        return random.choice(nouns) + "s"
    else:
        return input(f"Enter a {word_type}: ")

def generate_madlib():
    templates = [
        "The {adjective} {noun} {verb} over the {adjective} {noun}.",
        "Once upon a time, a {adjective} {noun} decided to {verb} a {noun}.",
        "{name} loves to {verb} {adverb} while wearing {adjective} {plural noun}.",
        "In a world where {plural noun} can {verb}, one {adjective} {noun} stands alone.",
        "The {adjective} chef cooked {plural noun} with a side of {noun}."
    ]
    
    template = random.choice(templates)
    words = {}
    
    for word_type in set(word for word in template.split() if word.startswith("{") and word.endswith("}")):
        clean_word_type = word_type.strip("{}").replace("_", " ")
        words[word_type] = get_word(clean_word_type)
    
    return template.format(**words)

print("Welcome to the Silly Mad Libs Generator!")
print(generate_madlib())
print("Thanks for playing!")
