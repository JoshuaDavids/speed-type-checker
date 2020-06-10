import time

string = 'I am extremely bored'

word_count = len(string.split())
while str(input("Are you ready?[Y/N]\n")):
    t0 = time.time()
    inputPhrase = str(input('Enter the phrase "%s" as fast as possible: \n' % string))
    t1 = time.time()
    acc = len(set(inputPhrase.split() and set(string.split())))
    acc = acc/word_count*100
    totTime = t1 - t0
    wordPm = (word_count/totTime)*5
    print("\nWords per minute:", wordPm, "\nAccuracy:", acc, "% accurate", "\nTotal time:", totTime)
