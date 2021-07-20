"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words = text_string.split()
    # print(words)
    words.append(None)

    for i in range(len(words)-2):
        # print(words[i], words[i+1], words[j+2])
        if (words[i], words[i+1]) in chains:
            chains[(words[i], words[i+1])].append(words[i+2])
        else:
            chains[(words[i], words[i+1])] = [words[i+2]]

    return chains
    # print(chains)


def make_text(chains):
    """Return text from chains."""

    # words.append(choice(chains[('Would', 'you')]))
    # words.append(choice(chains[('you', words[0])]))
    # words.append(choice(chains[(words[0], words[1])]))
    # words.append(choice(chains[(words[1], words[2])]))
    # words.append(choice(chains[(words[2], words[3])]))
    # words.append(choice(chains[(words[3], words[4])]))
    # words.append(choice(chains[(words[4], words[5])]))
    # words.append(choice(chains[(words[5], words[6])]))
    # words.append(choice(chains[(words[6], words[7])]))
    # words.append(choice(chains[(words[7], words[8])]))
    # words.append(choice(chains[(words[8], words[9])]))
    # words.append(choice(chains[(words[9], words[10])]))
    # print(words)

    key = choice(list(chains))
    words = [key[0], key[1]]
    ran_word = choice(chains[key])

    while ran_word is not None:
        key = (key[1], ran_word)
        words.append(ran_word)
        ran_word = choice(chains[key])

    return ' '.join(words)


input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
