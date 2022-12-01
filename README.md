# Unscrambler

* Sample code to test python packaging.
* Python tool to find words from scrambled letters, mostly cos I wanted to solve scramble in Deccan Chronicle.
* Returns a list of words that can be formed using all the letters in the scrambled word.
* Uses Wordnet to get complete vocabulary.

## Installation

pip install unscramble-dc

## Usage

* from unscramble_dc import unscramble
* unscramble('letters', 'word_length')
* Use word_length == -1 to get list of all words
