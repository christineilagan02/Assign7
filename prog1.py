# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

#text = 'pete'
#count = 0
#for c in text:
#    if c == 'e':
#        count = count+1
#print(count)

sentence = input("Kindly enter the sentence you wanted: ")

def countCharacterType(sentence):
    countW = 0
    countV = 0
    countC = 0
    for c in range(0, len(sentence)):
        vc = sentence[c]
        If ( (vc >= 'a' and vc <= 'z') or (v >= 'A' and v <= 'Z') ):
            v = v.lower()
            if (v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u'):
                countV += 1
            else:
                countC += 1

print(countV)
print(countC)

countCharacterType(sentence)