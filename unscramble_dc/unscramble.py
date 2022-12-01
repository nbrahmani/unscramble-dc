import pickle
from nltk.corpus import wordnet
from pathlib import Path


def get_words_from_wordnet(outfile):
    words = list(wordnet.words())

    with open(outfile, 'wb') as fp:
        pickle.dump(words, fp)

    print(f'Words stored in {outfile}')


def unscramble(scrambled, word_length):
    filename = f'{str(Path(__file__).absolute().parent)}/all_words.pkl'
    path = Path(filename)

    if not path.is_file():
        get_words_from_wordnet(filename)

    with open(filename, 'rb') as fp:
        words = pickle.load(fp)

    unscrambled = []
    orig_letters = {x for x in scrambled}
    for word in words:
        letters = {x for x in word}

        if orig_letters == letters:
            unscrambled.append(word)

    if word_length != -1:
        unscrambled = [x for x in unscrambled
                       if len(x) == word_length]

    return unscrambled


if __name__ == "__main__":
    unscrambled = unscramble('air', 3)
    print(unscrambled)
