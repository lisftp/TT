resultWordLen  = 1 

word = "shkolla"

wordLength = len(word)

albanianCharList = ["dh","gj","ll","nj","rr","sh","th","xh","zh"]

for charPos in range(wordLength - 1):
    firstLetter = word[charPos]
    secondLetter = word[charPos + 1]
    bothLetters = firstLetter + secondLetter
    resultWordLen = resultWordLen + 1

    if bothLetters in albanianCharList:
       resultWordLen = resultWordLen - 1

print(resultWordLen)