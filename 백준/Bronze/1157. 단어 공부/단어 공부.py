from collections import Counter
import sys
input = sys.stdin.readline
#print = sys.stdout.write

word = list(input().rstrip().lower())
counter = Counter(word).most_common()

if len(counter) == 1:
    print(word[0].upper())
else:
    if counter[0][1] == counter[1][1]:
        print("?")
    else:
        print(counter[0][0].upper())
