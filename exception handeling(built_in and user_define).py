# user define exception

# practice question
# 31-08-2026

# Age Validation
# Create a user-defined exception called InvalidAgeError.
# Ask the user to enter their age.
# If age is less than 18, raise InvalidAgeError. Otherwise print "Eligible to vote"

class InvalidAgeError(Exception):
    pass
try:
    a=int(input('enter your age: '))

    if a<18:
        raise InvalidAgeError

    else:
        print('Eligible to vote')

except InvalidAgeError:
    print('you are under age, you can not eligible for vote ')

except ValueError as e:    # this is a buil in exception
    print(e)



# Insufficient Balance
# Create a custom exception called InsufficientBalanceError.
# Given:
# balance = 5000
# Ask the user for a withdrawal amount.
# If withdrawal amount > balance → raise InsufficientBalanceError Otherwise deduct the amount and display the remaining balance.


class InsufficientBalanceError(Exception):
    pass
try:
    balance = 5000
    amount=int(input('enter ammount for withdrawal: '))
    if amount > balance:
        raise InsufficientBalanceError

    else:
        print('remainig balance after withdrawal :',balance-amount)

except InsufficientBalanceError:
    print('insufficiant balance . Your withdrawal amount is more than your current balance.')

except ValueError as e:  # this is a buil in exception
    print(e)

