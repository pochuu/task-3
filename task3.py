"""Input: words = "Hey there mate, it’s nice to finally meet you!",
maximum_width = 16
Output:
[
"Hey  there mate,"
"it’s   nice   to",
"finally     meet",
"you."
]
Note: Please keep in mind that the last line is aligned left.
"""

maximum_width = 16


def list_justify(words, max_width):
    test = []
    modified_text = []
    words = words.split(" ")
    while len(words) > 0:
        total = 0
        words_line = 0
        # counting len(word) in line and how many words in  line
        for word in words:
            if total + len(word) < max_width - words_line:
                total = total + len(word)
                test.append(word)
                words_line += 1
        del words[:words_line] #deleting used words
        x = 0
        # filling lines with spacebars
        if len(words) != 0:
            for i in range(max_width - total):
                test[x] = test[x] + " "
                if x < words_line - 2:
                    x += 1
                else:
                    x = 0

        test = ''.join(test)
        modified_text.append(test)
        test = []
    return modified_text


print(list_justify("Hey there mate, it’s nice to finally meet you!", maximum_width))
