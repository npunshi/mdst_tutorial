
def is_odd(x):
    """
    returns True if x is odd and False otherwise
    """
    if (x % 2 == 0):
        print("false")
    else:
        print("true")


def is_palindrome(word):
    """
    returns whether `word` is spelled the same forwards and backwards
    """
    revWord = reversed(word)

    if list(word) == list(revWord):
        print("Word is palindrome")
    else:
        print("Word not palindrome")


def only_odds(numlist):
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """
    newList = []
    for i in numlist:
        if is_odd(i) == "true":
            newList.append(i)
    print(newList)


def count_words(text):
    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
    """
    wordic = {}
    for word in text:
        if word in wordic:
            wordic[word] +=1
        else:
            wordic[word] = 1
    return wordic