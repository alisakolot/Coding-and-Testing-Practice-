import random 

number = random.randint(1, 10)
print(f">>>>> chosen number: {number} <<<<<") 
user_guesses = input("We're thinking of a number between 1 and 10. You get five guesses. What's the number? \n")


def guessing_game(number, user_guesses):
    # guess count 
    count = 0
    if int(user_guesses) == number: 
        return f"you got it on the first try! you got it in {count} tries"

    else:
        
        while int(user_guesses) != number: 
            if count == 4: 
                return f"Sorry. You had five guesses. The number is {number}."
                
            if int(user_guesses) > number:
                count += 1
                print("too high")
                new_guess = input(f"try again. this is guess number {count} \n")
                user_guesses = int(new_guess)

                if user_guesses == number: 
                    return f"you got it in {count} tries"
            else: 
                if int(user_guesses) < number: 
                    count += 1
                    print("too low")
                    new_guess = input(f"try again. this is guess number {count} \n")
                    user_guesses = int(new_guess)


print(guessing_game(number, user_guesses))