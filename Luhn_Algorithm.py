# Implements the Luhn Algorithm to validate Credit Card Numbers.
def checkLuhn(cardNumber):
    digits = [int(digit) for digit in str(cardNumber)]
    total = 0
    for i in range(-1, -len(digits) - 1, -1):
        if i % 2 == 0:
            digits[i] = (2*digits[i])//10 + (2*digits[i])%10
        total += digits[i]
    if total % 10 == 0:
        print("Credit Card", cardNumber, "is valid.")
    else:
        print("Credit Card", cardNumber, "is not valid.")
