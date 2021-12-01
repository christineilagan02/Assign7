# Program 1:
# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex.
# input: Bahala kayo dyan
# output:
# words: 3
# vowels: 6
# consonants: 8

print("\n\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m")
sentence = input("\n\33[1m\33[3mKindly enter the sentence you wanted: \33[0m")
countW = len(sentence.split())
countV = 0
countC = 0

def countCharacterType(sentence):
    countV = 0
    countC = 0
    for c in range(0, len(sentence)):
         
        vc = sentence[c]
 
        if ( (vc >= 'a' and vc <= 'z') or
             (vc >= 'A' and vc <= 'Z') ):
 
            vc = vc.lower()
 
            if (vc == 'a' or vc == 'e' or vc == 'i'
                        or vc == 'o' or vc == 'u'):
                countV += 1
            else:
                countC += 1


    print(f"\n\t\33[1m\33[33mWords      :  \33[0m{countW}")
    print(f"\t\33[35m\33[1mVowels     :  \33[0m{countV}")
    print("\t\33[1m\33[37m\bConsonants  :  \33[0m" + str(countC) + "\n")
    print("\t\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m---+---+---+---\33[1m\33[33m*\33[0m\n")


countCharacterType(sentence)
