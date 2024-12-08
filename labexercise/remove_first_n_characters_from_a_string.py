import random
print('This is a code where a random amount of a given word will disappear')
user_input_word = input('Can you give me a word ')
random_amount_to_be_eaten = random.randint(1, len(str(user_input_word)))

def word_eater(word, amount_to_be_eaten):
    print('Your inputted word is:', user_input_word)
    new_word = user_input_word[amount_to_be_eaten: ]
    return new_word

print(word_eater(user_input_word,random_amount_to_be_eaten))