"""
Test Code1
print(palindrome("abcba", 0))

output1
abcba is a palindrome

Test Code2
print(palindrome("peter", 0))

output2
peter is not a palindrome

"""

def palindrome(word, index):
    if index >= len(word) // 2:
        return f'{word} is a palindrome'

    left = word[index]
    right = word[-1 - index]

    if left != right:
        return f'{word} is not a palindrome'

    return palindrome(word, index + 1)

print(palindrome("abcba", 0))
print(palindrome("peter", 0))
