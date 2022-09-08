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

    * `def make_hash(v)` method is hash function selcted in order to have the same hash code for anagrams

        ```python
        def make_hash(v):
        hashed = sum((hash(x) for x in list(v)))
        return hashed
        ```

    * `def cleanup(clean_words)` method, that select all words from txt file, remove punctuation symbols, remove stop words, remove duplicate words

    ```python
    processed_words = []
    def cleanup(contents):
        splited_contents = contents.split()
        # print(splited_contents)
        # ############### splited_contents ###############################################################
        # ['akte', 'aldri', 'alle', 'aller', 'allfarveien', 'allting', 'alt', 'altfor', 'andre',......]
        # ################################################################################################

        for word in splited_contents:
            # print(word)#################################################################################
            # ############ word ##########################################################################
            # dratt
            # dreper
            # drev
            # drikke
            # drikker
            # drive
            # dro
            # drog
            # ###########################################################################################
            letters = word.split()
            # print(letters)#############################################################################
            # ############ letters ######################################################################
            # ['dram']
            # ['dratt']
            # ['dreper']
            # ['drev']
            # ['drikke']
            # ['drikker']
            # ['drive']
            # ['dro']
            # ['drog']
            # ['dronning']
            # ['dronningen']
            # ['drukket'
            # #############################################################################################

            clean_word = ""
            for letter in letters:
                # Return True if all characters in letter are alphabetic and there is at least one character in letter.
                if letter.isalpha():
                    # print(letter)
                    clean_word += letter
                    processed_words.append("".join(clean_word))

        # print(processed_words)
        processed_words_frequency = {}
        for word in processed_words:
            # print(word)
            if word not in processed_words_frequency.keys():
                # print(word)
                processed_words_frequency[word] = 1
            else:
                processed_words_frequency[word] += 1
        ##################################################################################################################################################
        # print(processed_words_frequency) ###############################################################################################################
        # ##################################################################################################################################################
        # {'akte': 1, 'aldri': 1, 'alle': 1, 'aller': 1, 'allfarveien': 1, 'allting': 1, 'alt': 1, 'altfor': 1, 'andre': 1, 'annen': 1, 'annet': 1,
        #  'arbeid': 1, 'arbeide': 1, 'arbeidet': 1, 'arving': 1, 'at': 1, 'attpå': 1, 'av': 1, 'avdaler': 1, 'avdrukket': 1, 'avsted': 1, 'avtalen': 1,
        # 'ba': 1, 'bak': 1, 'bakfjerdingen': 1, 'bakom': 1, 'bakst': 1, 'bakstefløy': 1, 'bakte': 1, 'bar': 1, 'bare': 1, 'barn': 1, 'bedre': 1,
        # 'begge': 1, 'bein': 1, 'bende': 1, 'benker': 1, 'berge': 1, 'berget': 1, 'bergtrollene': 1, 'best': 1, 'beste': 1, 'bjørn': 1, 'bjørnen': 1,
        # 'blankskurt': 1, 'ble': 1, 'blei': 1, 'bleien': 1, 'bli': 1, 'blir': 1, 'blod': 1, 'blomster': 1, 'blå': 1, 'blåne': 1, 'blåse': 1, 'blåser': 1,
        # 'blåst': 1, 'blåste': 1, 'bodde': 1, 'bordet': 1, 'bordskuff': 1, 'bort': 1, 'borte': 1, 'bortenfor': 1, 'bortetter': 1, 'bortigjennom': 1, 'bra':
        # ...}
        # ####################################################################################################################################################
        return processed_words_frequency

    ```

    * `def find_anagrams(clean_words)` method responsible for finding anagrams, that select all words from txt file, remove punctuation symbols, remove stop words, remove duplicate words

    ```python
    # clean_words ##################################################################################################################################################
    # {'akte': 1, 'aldri': 1, 'alle': 1, 'aller': 1, 'allfarveien': 1, 'allting': 1, 'alt': 1, 'altfor': 1, 'andre': 1, 'annen': 1, 'annet': 1,
    #  'arbeid': 1, 'arbeide': 1, 'arbeidet': 1, 'arving': 1, 'at': 1, 'attpå': 1, 'av': 1, 'avdaler': 1, 'avdrukket': 1, 'avsted': 1, 'avtalen': 1,
    # 'ba': 1, 'bak': 1, 'bakfjerdingen': 1, 'bakom': 1, 'bakst': 1, 'bakstefløy': 1, 'bakte': 1, 'bar': 1, 'bare': 1, 'barn': 1, 'bedre': 1,
    # 'begge': 1, 'bein': 1, 'bende': 1, 'benker': 1, 'berge': 1, 'berget': 1, 'bergtrollene': 1, 'best': 1, 'beste': 1, 'bjørn': 1, 'bjørnen': 1,
    # 'blankskurt': 1, 'ble': 1, 'blei': 1, 'bleien': 1, 'bli': 1, 'blir': 1, 'blod': 1, 'blomster': 1, 'blå': 1, 'blåne': 1, 'blåse': 1, 'blåser': 1,
    # 'blåst': 1, 'blåste': 1, 'bodde': 1, 'bordet': 1, 'bordskuff': 1, 'bort': 1, 'borte': 1, 'bortenfor': 1, 'bortetter': 1, 'bortigjennom': 1, 'bra':
    # ...}
    # ##################################################################################################################################################
    def find_anagrams(clean_words):
        # Pairing Anagrams by Hash value
        clean_words_hash_table = {}

        for i in clean_words:
            if make_hash(i) not in clean_words_hash_table.keys():
                clean_words_hash_table[make_hash(i)] = [i]
            elif i in clean_words_hash_table[make_hash(i)]:
                pass
            else:
                clean_words_hash_table[make_hash(i)].extend([i])
        # clean_words_hash_table ########################################################################################################################################
        # print(clean_words_hash_table)
        # {10537339097141344516: ['akte'], 28998290657399899697: ['aldri'], 16787045441859543998: ['alle'], 23732445378082769830: ['aller'], 
        # 27180652513471585905: ['allfarveien'], 23809318082807862653: ['allting'], 17737889611088371301: ['alt'],.....}
        ##############################################################################################################################################################

        # Clean clean_words_hash_table, only contains 2 letter or more values can be anagrams
        anagram_hash_table = {}
        for k, v in clean_words_hash_table.items():
            if len(v) > 1:
                anagram_hash_table[k] = v
        # anagram_hash_table ##################################################################################################################################################
        # print(anagram_hash_table)
        # {10939202460068486256: ['at', 'ta'], 17281837970771535480: ['bar', 'bra'], 12315734925037834454: ['bry', 'byr'], 17532400063532796767: ['dem', 'med'],
        # 2618809912497743718: ['den', 'ned'], -2761153685103864421: ['denne', 'enden'], 20349972161862677485: ['dra', 'rad'], 8680358601531492200: ['dro', 'ord', 'rod'], 
        # 5174645463386486702: ['ende', 'nede'], 1588363047582415847: ['engang', 'gangen'], -6024695099541763957: ['ens', 'sen'], 15895792231552359859: ['etter', 'rette'], 
        # -2532537009796179565: ['glinset', 'glinste'], -12260620166952086541: ['hellestein', 'steinhelle'], -8284487212338343100: ['kisten', 'skinte'], 
        # -624407728590147382: ['kristent', 'kristnet'], -15939893538409753269: ['krok', 'rokk'], -4968710955115651889: ['lovt', 'tolv'], 
        # -6154867287402045511: ['lysnet', 'lysten'], 952582991967380806: ['løst', 'støl'], 7659376093976842269: ['mor', 'rom'], -6191465735596780239: ['navn', 'vann'], 
        # 26252102582603706: ['niste', 'stien'], 14360235798446913357: ['ordet', 'torde'], 15622130734821150547: ['ristet', 'sitter'], -1010517028449259186: ['rå', 'år'],
        # -7746297740349216639: ['stuen', 'suten'], 8123032883230944162: ['søsteren', 'søstrene'], 8494312393829486020: ['truet', 'turte']}        
        # #############################################################################################################################################################

        # Creates Hash values for all keys in clean_word
        hash_word = {}
        for k, v in clean_words.items():
            if make_hash(k) not in hash_word:
                hash_word[make_hash(k)] = v
            else:
                hash_word[make_hash(k)] += v
        # print(hash_word)
        # {18850452034543600945: 1, -17207395831741420928: 1, 6644983032283399904: 1, 2580367764680674904: 1, 15454304980901650445: 1, -9867980317127503119: 1,
        #  2990827475666454731: 1, -4217911752670662314: 1, 11809067258873332946: 1, 38362979674384232257: 1,
        # ...}

        # Match Clean register with frequency
        anagram_frequency_table = {}
        for k, v in anagram_hash_table.items():
            if k in hash_word:
                anagram_frequency_table['{}'.format(v)] = hash_word[k]

        return anagram_frequency_table

    ```
