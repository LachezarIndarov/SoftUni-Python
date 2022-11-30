"""
Input1
ice
kicegiciceeb

Output1
kgb

Comments:
We remove ice once and we get "kgiciceeb"
We match "ice" one more time and we get "kgiceb"
There is one more match. The finam result is "kgb"

"""

search = input()
text = input()


while search in text:
   text = text.replace(search, "")

print(text)