# get user input. Dog or cat adoption?
pet_type = input('Would you like to adopt a dog or a cat? Enter "dog" or "cat": ')

# set default to false
ready_to_adopt = False

# if they select dog
if pet_type.lower() == 'dog':
    # ask dog specific questions
    question1 = input('Do you have a fenced-in yard the dog can run around freely? Enter "y" or "n": ')
    question2 = input('Do you have a collar or harness and a leash to walk your dog? Enter "y" or "n":  ')
    question3 = input('Do you have dog toys the dog can play with? Enter "y" or "n": ')

    # check for dog compatibility
    if question1.lower() == 'y' and question2.lower() == 'y' and question3.lower() == 'y':
        print('It sounds like you’re ready to adopt! Let’s introduce you to Rover.')
        ready_to_adopt = True
    else:
        print('Dog\'s are great, but have you considered a feline? '
              + 'They don\'t need a back yard or walks and can be easier to care for.')

# if they select cat
elif pet_type.lower() == 'cat':
    # ask cat specific questions
    question1 = input('Do you have a litter box for the cat? Enter "y" or "n": ')
    question2 = input('Do you have a cat carrier to transport the cat? Enter "y" or "n": ')
    question3 = input('Do you have an empty cardboard box for the cat to sit in? Enter "y" or "n": ')

    # check for cat compatibility
    if question1.lower() == 'y' and question2.lower() == 'y' and question3.lower() == 'y':
        print('It sounds like you\'re ready to adopt your purrrfect furry friend. '
              + 'You should meet Princess!')
        ready_to_adopt = True
    else:
        print('Cat\'s are gonna stink up that litter box and need that cardboard box to shelter in. '
              + 'Have you considered a dog to fill that void in your home?')

# if they type anything other than dog or cat
else:
    print('We don\'t adopt those other critters.'
          + 'Check out your local zoo where you can watch them, '
          + 'but you have to leave them there.')

if ready_to_adopt:
    print('We are excited to join you on this exciting journey as you explore pet adoption.')
else:
    print('We hope you find fulfillment in other areas of your life. '
          + 'I\'m sorry we couldn\'t make an adoption happen today.')


