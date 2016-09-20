# Reverse a string

TheString = input(str("Please provide a sentence to be reversed: "))

StringLength = len(TheString)

count = StringLength

TheStringReversed = ""

while count > 0:
    ReversedCharacter = TheString[count-1:count]
    TheStringReversed = TheStringReversed + ReversedCharacter
    count = count - 1

print ("Your sentence reversed is: " + TheStringReversed)
print (StringLength)
