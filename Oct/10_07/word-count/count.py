"""Count words in a sentence, and print in ascending order.

For example::

    >>> word_count("berry cherry cherry cherry berry apple")
    apple: 1
    berry: 2
    cherry: 3

If there is a tie for a count, make sure the words are printed in
ascending order within the tie::

    >>> word_count("hey hi hello")
    hello: 1
    hey: 1
    hi: 1

Capitalized words are considered distinct::

    >>> word_count("hi Hi hi")
    Hi: 1
    hi: 2
"""


def word_count(phrase):
    """Count words in a sentence, and print in ascending order."""
    phrase = phrase.split(' ')

    # words = []
    # count = 0

    # #iterate through phrase and add unique words to a new list
    # #for every repetition add 1 to count
    # # if the word is not repeated count is 1
    # #

    # for word in phrase:
    #     if word not in words:
    #         words.append(word)
    
    # for word in phrase:
    #     print(word)
    #     if word in words:
    #         count+=1

    # print(words)
    # print(count)
    
    word_counts = {}

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; NICE JOB! ***\n")
