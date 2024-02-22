def findWordsContaining(words, x):
        l = []
        for element in words:
            # a = element.split()
            if x in element:
                l.append(element)
        return l

words = ["leet","code"]
x = "e"
print(findWordsContaining(words,x))