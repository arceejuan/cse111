# Exceeds requirements
# In this output, I fulfilled the other requirement to earn the remaining 7% of points. I made a function names get_adjetive and get_adverb and call it to my make_sentence function.

import random

def get_determiner(quantity):
    """Return a randomly chosen determiner."""
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["some", "many", "the"]

    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun."""
    if quantity == 1:
        nouns = ["bird", "boy", "car", "cat", "child", "dog", "girl", "man", "rabbit", "woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "rabbits", "women"]

    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb."""
    past_verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    present_verbs_singular = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    present_verbs_plural = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    if tense == "past":
        verbs = past_verbs
    elif tense == "present" and quantity == 1:
        verbs = present_verbs_singular
    elif tense == "present" and quantity != 1:
        verbs = present_verbs_plural
    elif tense == "future":
        verbs = future_verbs

    verb = random.choice(verbs)
    return verb

def get_preposition():
    """Return a randomly chosen preposition."""
    prepositions = ["about", "above", "across", "after", "along", "around", "at", "before", "behind", "below",
                    "beyond", "by", "despite", "except", "for", "from", "in", "into", "near", "of",
                    "off", "on", "onto", "out", "over", "past", "to", "under", "with", "without"]

    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)

    prepositional_phrase = f"{preposition} {determiner} {noun}"
    return prepositional_phrase

def get_adjective():
    """Return a randomly chosen adjective."""
    adjectives = ["happy", "sad", "big", "small", "colorful", "quiet", "loud", "fast", "slow", "bright"]
    adjective = random.choice(adjectives)
    return adjective

def get_adverb():
    """Return a randomly chosen adverb."""
    adverbs = ["quickly", "slowly", "loudly", "softly", "happily", "sadly", "eagerly", "calmly", "gracefully", "awkwardly"]
    adverb = random.choice(adverbs)
    return adverb

def make_sentence(quantity, tense):
    """Build and return a sentence with two prepositional phrases, an adjective, and an adverb."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase_1 = get_prepositional_phrase(quantity)
    prepositional_phrase_2 = get_prepositional_phrase(quantity)
    adjective = get_adjective()
    adverb = get_adverb()

    sentence = f"{determiner.capitalize()} {adjective} {noun} {verb} {prepositional_phrase_1} and {prepositional_phrase_2} {adverb}."
    return sentence

def main():
    # Print six sentences with different characteristics
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

if __name__ == "__main__":
    main()
