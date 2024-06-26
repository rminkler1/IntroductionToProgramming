names = ['Robert', 'John', 'Sam', 'Barbara', 'Jacob', 'Jeremiah', 'Patricia', 'William', 'Robert']

for index, name in enumerate(names):
    print(index, name)

    # Stop printing the next name when we reach the end of the list to avoid an IndexError
    if index < (len(names) - 1):
        print(f'The next name is {names[index + 1]}\n')
    else:
        print('You have reached the end of the list.')

student_scores = [("Julie", 99), ("Josh", 94), ("Shelby", 75)]
julie_name, julie_score = student_scores[0]
print(f"Julie’s score is: {julie_score}")
