# Implements the Luhn Algorithm to validate Credit Card Numbers.
def checkLuhn(cardNumber):
    cardNumbers = [int(digit) for digit in str(cardNumber)]
    isOdd = True
    total = 0
    for digit in cardNumbers:
        if isOdd:
            digit = 2*digit
            digit = digit//10 + digit%10
            total += digit
            isOdd = False
        else:
            total += digit
            isOdd = True
    valid = (total % 10 == 0)
    if valid:
        print("Credit Card", cardNumber, "is valid.")
    else:
        print("Credit Card", cardNumber, "is not valid.")
