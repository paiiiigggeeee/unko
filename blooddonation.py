""" To be a blood donor in the US, you need to be 17 or older, and weigh at least 110 lbs.
There are other requirements which we will ignore for this program. """


def main():
    age = int(input('Please enter your age, in years: '))
    weight = int(input('Please enter your weight, to the nearest pound: '))

# call eligibility in main, with values
    eligible = check_donor_eligibility(age, weight)

    if eligible:
        print("You are eligible to donate blood, thank you so much for your interest in being a donor.")
    else:
        print('You are not eligible at this time. Sorry.')


def check_donor_eligibility(age, weight):
    if age >= 17 and weight >= 110:
        return True
    else:
        if age < 17:
            print('You are too young, please consider donating blood when you are 17.')
        if weight < 110:
            print('Your weight is too low, for the health and safety of donors, they must be at least 110lbs.')
        return False

main()
