answerText = ""
for a in range(97, 123):
    for b in range(97, 123):
        for c in range(97, 123):
            with open("p059.txt", 'r') as myFile:
                text = ""
                answer = 0
                key = [a,b,c]
                for char in myFile.read().strip().split(','):
                    letter = int(char) ^ key[0]
                    answer += letter
                    key.append(key.pop(0))
                    if letter > 123 or letter < 32:
                        break
                    letter = chr(letter)
                    text += letter 
                if text.count(" ") > answerText.count(" "):
                    answerText = str(answer) + " " + text

print answerText
