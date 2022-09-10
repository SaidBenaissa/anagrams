
def make_hash(v):
    hashed = sum((hash(x) for x in list(v)))
    return hashed

# Select all words from txt file, remove empty space
processed_words = []


def cleanup(contents):
    splited_contents = contents.split()
    for word in splited_contents:

        letters = word.split()

        clean_word = ""
        for letter in letters:
            # Return True if all characters in letter are alphabetic and there is at least one character in letter
            if letter.isalpha():
                clean_word += letter
                processed_words.append("".join(clean_word))

    processed_words_frequency = {}
    for word in processed_words:
        if word in processed_words_frequency.keys():
            processed_words_frequency[word] += 1
        else:
            processed_words_frequency[word] = 1
    
    return processed_words_frequency

# Read txt file to dictionary
f = open('ordbok-utf8-2.txt', 'r', errors='ignore')
input_data = f.read()
clean_words = cleanup(input_data)

def find_anagrams(clean_words):
    # Pairing Anagrams by Hash value [hash_key: value]
    clean_words_hash_table = {}
    for word in clean_words:
        # print(word)
        if make_hash(word) not in clean_words_hash_table.keys():
            clean_words_hash_table[make_hash(word)] = [word]
            # print(clean_words_hash_table)
        elif word in clean_words_hash_table[make_hash(word)]:
            pass
        else:
            clean_words_hash_table[make_hash(word)].extend([word])

    # Detect anagrams and Clean clean_words_hash_table, only contains 2 letter or more values can be anagrams
    anagram_hash_table = {}
    # ANAGRAMS WILL HAVE SAME make_hash() value ###########################
    for k, v in clean_words_hash_table.items():
        if len(v) > 1:
            anagram_hash_table[k] = v

    hash_word = {}
    for k, v in clean_words.items():
        if make_hash(k) not in hash_word:
            hash_word[make_hash(k)] = v
        else:
            hash_word[make_hash(k)] += v

    # Match hash_word frequency
    anagram_frequency_table = {}
    for k, v in anagram_hash_table.items():
        if k in hash_word:
            anagram_frequency_table['{}'.format(v)] = hash_word[k]
            # anagram_frequency_table[str(v)] = hash_word[k]
    # print(anagram_frequency_table)
    for k,v in anagram_frequency_table.items():
        # print(''.join(item), "\n")
        # print(k," - Are - ",v,"anagrams", "\n")
        print(k[1:-1], "\n")

    return anagram_frequency_table


if __name__ == '__main__':
    anagrams = find_anagrams(clean_words)
