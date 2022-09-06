* Task - Et anagram:

    Et anagram er et ord eller et uttrykk som er satt sammen ved å stokke om bokstavene i et annet ord eller uttrykk (<http://no.wikipedia.org/wiki/Anagram>)

    Oppgaven består i å lage et program som finner alle ord i lista som har ett eller flere anagrammer andre steder i lista.

    Den vedlagte filen er en ordliste med ett ord pr linje.

    Disse skal så listes opp sammen med det opprinnelige ordet. Ikke alle ordene har et anagram, og du skal kun finne ettordsanagrammer.

    Hver linje i resultatet skal inneholde de ordene som er anagrammer av
    hverandre.

    For eksempel slik

   ```txt
    akte teak kate
    aldri arild
    aller ralle
    alt tal
    andre rande denar ander
    .
    .
    .
    ```

    Med denne oppgaven ønsker vi å se hvordan du løser programmeringsutfordringer, samt å teste Programmeringskunnskapene dine. I intervj

* Solution:

  * Input:  `ordbok-utf8-2.txt` input data file
  
  * Output: Expected result

    ```scripte
    {"['at', 'ta']": 2, "['bar', 'bra']": 2, "['bry', 'byr']": 2, "['dem', 'med']": 2, "['den', 'ned']": 2, "['denne', 'enden']": 2, "['dra', 'rad']": 2, "['dro', 'ord', 'rod']": 3, "['ende', 'nede']": 2, "['engang', 'gangen']": 2, "['ens', 'sen']": 2, "['etter', 'rette']": 2, "['glinset', 'glinste']": 2, "['hellestein', 'steinhelle']": 2, "['kisten', 'skinte']": 2, "['kristent', 'kristnet']": 2, "['krok', 'rokk']": 2, "['lovt', 'tolv']": 2, "['lysnet', 'lysten']": 2, "['løst', 'støl']": 2, "['mor', 'rom']": 2, "['navn', 'vann']": 2, "['niste', 'stien']": 2, "['ordet', 'torde']": 2, "['ristet', 'sitter']": 2, "['rå', 'år']": 2, "['stuen', 'suten']": 2, "['søsteren', 'søstrene']": 2, "['truet', 'turte']": 2}
    ```

    * `def make_hash(v)` method

        ```python
        def make_hash(v):
        hashed = sum((hash(x) for x in list(v)))
        return hashed
        ```

    * `def cleanup(clean_words)` method, that select all words from txt file, remove punctuation symbols, remove stop words, remove duplicate words

    ```python
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
    ```

    * `def find_anagrams(clean_words)` methode, that select all words from txt file, remove punctuation symbols, remove stop words, remove duplicate words

    ```python

    def find_anagrams(clean_words):
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
    ```
