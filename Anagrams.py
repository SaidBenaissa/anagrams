# Format/read txt file to dictionary
f = open('ordbok-utf8-2.txt', 'r', errors='ignore')
dictionary = f.read()
# print(dictionary)

# Return the hash value for the given object.
# Two objects that compare equal must also have the same hash value,
# but the reverse is not necessarily true.


def make_hash(v):
    hashed = sum((hash(x) for x in list(v)))
    return hashed


# Select all words from txt file, remove punctuation symbols, remove stop words, remove duplicate words
processed_words = []


def cleanup(file_contents):
    # Process String Data into Lists
    # print(file_contents)
    processed_file_contents = file_contents.split()
    # print(processed_file_contents)

    frequency_processed_words = {}
    # Iterate over each word
    for word in processed_file_contents:
        # print(word)
        # Iterate over each alphabet of every VALID word
        clean_word = ""
        letters = word.split()
        # print(letters)

        for letter in letters:
            # print(letter)
            # Return True if all characters in letter are alphabetic and there is at least one character in letter, False otherwise.
            if letter.isalpha():
                clean_word += letter
                # print(clean_word)
                processed_words.append("".join(clean_word))
                # print(processed_words)

    for word in processed_words:
        # print(word)
        if word not in frequency_processed_words.keys():
            # print(word)
            frequency_processed_words[word] = 1
        else:
            frequency_processed_words[word] += 1

    # Return unique, clean, uppercase words, with frequencies
    # print(frequency_processed_words)
    return frequency_processed_words


# clean_file_contents -> clean_words
clean_words = cleanup(dictionary)
# Number of Words
# print("Number of Words in book = {}".format(len(clean_words)))


def anagram_analyzer(clean_words):
    # Pairing Anagrams by Hash value

    global hash_register
    hash_register = {}

    for i in processed_words:
        if make_hash(i) not in hash_register.keys():
            hash_register[make_hash(i)] = [i]
        elif i in hash_register[make_hash(i)]:
            pass
        else:
            hash_register[make_hash(i)].extend([i])

    # Clean hash register, only contains 2 or more values

    global anagram_hash_register
    anagram_hash_register = {}

    for k, v in hash_register.items():
        if len(v) > 1:
            anagram_hash_register[k] = v

    # Creates Hash values for all keys in clean_word

    global hash_word
    hash_word = {}

    for k, v in clean_words.items():
        if make_hash(k) not in hash_word:
            hash_word[make_hash(k)] = v
        else:
            hash_word[make_hash(k)] += v

    # # Match Clean register with frequency

    global anagram_frequency_table
    anagram_frequency_table = {}

    for k, v in anagram_hash_register.items():
        if k in hash_word:
            anagram_frequency_table['{}'.format(v)] = hash_word[k]

    return anagram_frequency_table


if __name__ == '__main__':
    anagrams = anagram_analyzer(clean_words)
    print(anagrams)
