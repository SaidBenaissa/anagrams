# Return the hash value for the given object. Two objects that compare equal must also have the same hash value,
def make_hash(v):
    hashed = sum((hash(x) for x in list(v)))
    return hashed

# Select all words from txt file, remove empty space
processed_words = []
def cleanup(contents):
    splited_contents = contents.split()
    # ############### splited_contents ###############################################################
    # ['akte', 'aldri', 'alle', 'aller', 'allfarveien', 'allting', 'alt', 'altfor', 'andre',......]
    for word in splited_contents:
        # ############ word ##########################################################################
        # dratt
        # dreper
        # drev
        # drikke
        # drikker
        letters = word.split()
        # ############ letters ######################################################################
        # ['dratt']
        # ['dreper']
        # ['drev']
        # ['drikke']
        # ['drikker']

        clean_word = ""
        for letter in letters:
            # Return True if all characters in letter are alphabetic and there is at least one character in letter
            if letter.isalpha():
                clean_word += letter
                processed_words.append("".join(clean_word))
                # ############ processed_words #################################################################
                # [ler', 'talte', 'tar', 'taska', 'tatt', 'tau', 'tauet', 'tenk', 'tenke', 'tenker', 'tenkte'

    processed_words_frequency = {}
    for word in processed_words:
        if word in processed_words_frequency.keys():
            processed_words_frequency[word] += 1
        else:
            processed_words_frequency[word] = 1

    # ############ processed_words_frequency #############################################################
    # {'akte': 1, 'aldri': 1, 'alle': 1, 'aller': 1, 'allfarveien': 1, 'allting': 1, 'alt': 1, 'altfor': 1, 
    # ...}
    return processed_words_frequency


# Read txt file to dictionary
f = open('ordbok-utf8-2.txt', 'r', errors='ignore')
input_data = f.read()
clean_words = cleanup(input_data)
print("Number of Words in txt input file = {}".format(len(clean_words)))

# clean_words ###############################################################################################
# {'akte': 1, 'aldri': 1, 'alle': 1, 'aller': 1, 'allfarveien': 1, 'allting': 1, 'alt': 1, 'altfor': 1, 
# 'andre': 1, 'annen': 1, 'annet': 1,
# ...}

def find_anagrams(clean_words):
    # Pairing Anagrams by Hash value
    clean_words_hash_table = {}

    for word in clean_words:
        if make_hash(word) not in clean_words_hash_table.keys():
            clean_words_hash_table[make_hash(word)] = [word]
            # print(clean_words_hash_table)
        elif word in clean_words_hash_table[make_hash(word)]:
            pass
        else:
            clean_words_hash_table[make_hash(word)].extend([word])

    # clean_words_hash_table ############################################################
    # {10537339097141344516: ['akte'], 28998290657399899697: ['aldri'], 16787045441859543998: ['alle'], 

    # Clean clean_words_hash_table, only contains 2 letter or more values can be anagrams
    anagram_hash_table = {}
    for k, v in clean_words_hash_table.items():
        if len(v) > 1:
            anagram_hash_table[k] = v
    # anagram_hash_table ##########################################################
    # {10939202460068486256: ['at', 'ta'], 17281837970771535480: ['bar', 'bra'], 
    # 12315734925037834454: ['bry', 'byr'], 

    # Creates Hash values for all keys in clean_word
    hash_word = {}
    for k, v in clean_words.items():
        if make_hash(k) not in hash_word:
            hash_word[make_hash(k)] = v
        else:
            hash_word[make_hash(k)] += v
    # hash_word ##########################################################
    # {18850452034543600945: 1, -17207395831741420928: 1, 6644983032283399904: 1, 2580367764680674904: 1,
    # ...}

    # Match hash_word frequency
    anagram_frequency_table = {}
    for k, v in anagram_hash_table.items():
        if k in hash_word:
            anagram_frequency_table['{}'.format(v)] = hash_word[k]

    # print(anagram_frequency_table)
    for item in anagram_frequency_table:
        print(item, "\n")
    return anagram_frequency_table

if __name__ == '__main__':
    anagrams = find_anagrams(clean_words)