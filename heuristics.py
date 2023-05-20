import collections
import string


def compute_perm_letter_freq(filename, known_letter_freqs):
    """ for each permutation, compute the frequencies of each letter on our deciphered output text,
        and compare that frequency to the known frequency of the letter, which is in the given file "Letter_Freq".
    """
    # Initialize a counter with keys copied from known_letter_freqs
    letter_counter = collections.Counter(dict.fromkeys(known_letter_freqs.keys(), 0))
    with open(filename, 'r') as f:
        decrypted_file = f.read().lower()
    # Count occurrences of each letter in the decrypted_file
    for letter in decrypted_file:
        if letter in letter_counter:
            letter_counter[letter] += 1
    # Calculate total number of letters
    total_letters = sum(letter_counter.values())
    # Calculate frequencies and store them in dict
    perm_letter_freqs = {letter: count / total_letters for letter, count in letter_counter.items()}

    return perm_letter_freqs


# compare current perm frequencies with the known frequencies
def compare_freqs(perm_letter_freqs, known_letter_freqs):
    total_difference = 0
    for letter in string.ascii_lowercase:
        # Get the frequency of the letter in perm_letter_freqs
        perm_freq = perm_letter_freqs[letter]
        # Get the frequency of the letter in known_letter_freqs
        known_freq = known_letter_freqs[letter]
        # Add the absolute difference between the frequencies to the total difference
        total_difference += abs(perm_freq - known_freq)

    return total_difference


def compute_letter_pairs_freq(filename, known_letter_pairs_freqs):
    """ for each permutation, compute the frequencies of each letter pair on our deciphered output text,
        and compare that frequency to the known frequency of the pair, which is in the given file "Letter_Freq2".
    """
    # Copy the keys from known_letter_pairs_freqs and initialize pair_counter with them
    pair_counter = collections.Counter(dict.fromkeys(known_letter_pairs_freqs.keys(), 0))
    with open(filename, 'r') as f:
        decrypted_file = f.read().lower()
    # Run through all pairs in the file and count their occurrences
    for i in range(len(decrypted_file) - 1):
        pair = decrypted_file[i:i + 2]
        if pair in pair_counter:
            pair_counter[pair] += 1

    # Calculate total number of pairs
    total_pairs = sum(pair_counter.values())
    # Calculate frequencies and store them in a dictionary
    pair_freqs = {pair: count / total_pairs for pair, count in pair_counter.items()}

    return pair_freqs


def compare_pairs_freqs(pair_freqs, known_letter_pairs_freqs):
    total_difference = 0
    # Iterate over each pair in known_letter_pairs_freqs
    for pair in known_letter_pairs_freqs.keys():
        # Get the frequency of the pair in pair_freqs
        perm_pairs_freq = pair_freqs[pair]
        # Get the frequency of the pair in known_letter_pairs_freqs
        known_pairs_freq = known_letter_pairs_freqs[pair]
        # Add the absolute difference between the frequencies to the total difference
        total_difference += abs(perm_pairs_freq - known_pairs_freq)

    return total_difference


def search_common_words(perm_deciphered_file, common_words):
    # TODO: should iterate over words in output file, and search for words that appear in common_words
    # TODO: test score for words match - not necessarily be 1.
    file_score = 0
    important_words = {"i", "a"}
    with open("output.txt", "r") as f:
        for line in perm_deciphered_file:
            words = line.split()
            for word in words:
                if word.isalpha():
                    # TODO: normalize score points
                    if word.lower() in common_words:
                        file_score += 1
                    elif word.lower in important_words:
                        file_score += 5
    return file_score


# if __name__ == '__main__':
#     global common_words, known_letter_freqs, known_letter_pairs_freqs
#
#     perm_letter_freqs = compute_perm_letter_freq('output.txt', known_letter_freqs)
#     # for letter, freq in sorted(perm_letter_freqs.items()):
#     #     print(f'{letter}: {freq:.4f}')
#
#     difference = compare_freqs(perm_letter_freqs, known_letter_freqs)
#     print(f'letters freq Total difference: {difference:.4f}')
#
#     pair_freqs = compute_letter_pairs_freq('output.txt', known_letter_pairs_freqs)
#     # for pair, freq in sorted(pair_freqs.items()):
#     #     print(f'{pair}: {freq:.4f}')
#
#     difference = compare_pairs_freqs(pair_freqs, known_letter_pairs_freqs)
#     print(f'pairs freq Total difference: {difference:.4f}')
#