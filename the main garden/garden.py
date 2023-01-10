import spacy

nlp = spacy.load("en_core_web_sm")

gardenpath_sentences = [
    "I know the words to that song about the queen don’t rhyme.",
    "She told me a little white lie will come back to haunt me.",
    "The dog that I had really loved bones.",
    "That Jill is never here hurts.",
    "The man who whistles tunes pianos.",
]

for sentence in gardenpath_sentences:
    doc = nlp(sentence)
    print("Sentence:", sentence)
    print("Tokens:", [token.text for token in doc])
    print("Entities:", [(ent.text, ent.label_) for ent in doc.ents])
    print()


# Two unusual entities that spaCy identified were "old man" and "wound" in the
# first and fifth sentences, respectively. I did not expect spaCy to recognize
# these as entities because they are not proper nouns or named entities.
# However, spaCy was able to identify them as entities by using its contextual
# understanding of language and its knowledge of common nouns and verb phrases.
