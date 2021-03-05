Intro = input("Enter Introduction:")
characterCount = 0
wordCount = 1
for i in Intro:
    characterCount = characterCount+1
    if(i == ' '):
        wordCount = wordCount+1
print("word count:")
print(wordCount)
print("char count:")
print(characterCount)
