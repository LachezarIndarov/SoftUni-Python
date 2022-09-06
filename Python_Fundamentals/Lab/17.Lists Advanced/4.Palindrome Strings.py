"""
input1
wow father mom wow shirt stats
wow

output1
['wow', 'mom', 'wow', 'stats']
Found palindrome 2 times

input2
hey how you doin? lol
mom

output2
['lol']
Found palindrome 0 times


"""
words = input().split(" ")
palindrome = input()
palindrome_words = []


for word in words:
    rev_list = reversed(word)
    rev_word = "".join(rev_list)
    if rev_word == word:
        palindrome_words.append(word)




print(palindrome_words)
palindrome_count = words.count(palindrome)
print(f"Found palindrome {palindrome_count} times")
