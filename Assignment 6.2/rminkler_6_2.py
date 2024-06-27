# Robert Minkler
# June 26, 2024
# Module 6.2 Assignment - Tuples

# Create and iterate through a tuple in two directions to build two sentences.

# CONSTANTS

# ASCII art generate from
# https://patorjk.com/software/taag/#p=display&h=2&f=JS%20Cursive&t=Tuple%20Playground
ASCII_ART = """
             _              _                                  
 -/-   ,_   // _      ,_   //__,      __  ,_  _,_    ,__,  __/ 
_/_(_/_/_)_(/_(/_    _/_)_(/(_/(_(_/_(_/_/ (_(_/(_/_/ / (_(_/(_
      /              /           _/_ _/_                       
     /              /           (/  (/                                                                                  
"""

# Initialize a tuple
# List of 25 instruments generated using ChatGPT
# then converted into a tuple by Robert Minkler
INSTRUMENTS = ("Piano",
               "Violin",
               "Guitar",
               "Flute",
               "Trumpet",
               "Drum kit",
               "Saxophone",
               "Cello",
               "Clarinet",
               "Harp",
               "Banjo",
               "Accordion",
               "Trombone",
               "French horn",
               "Organ",
               "Ukulele",
               "Mandolin",
               "Xylophone",
               "Double bass",
               "Electric keyboard",
               "Bagpipes",
               "Theremin",
               "Oboe",
               "Steel drums",
               "Didgeridoo",
               )


def main():
    # Display ASCII ART
    print(ASCII_ART)

    # Display the contents of the tuple in s single statement
    print(f'\nThe following Tuple is a list of {len(INSTRUMENTS)} instruments.')
    # print just the tuple in a single statement
    print(INSTRUMENTS)

    # Display the contents of the tuple in s single statement again.
    # I wanted to do this in a slightly more interesting way
    # that looked less like simply printing a tuple.
    for item in INSTRUMENTS: print(item, end=', ')

    print('\n\nForward:\n')

    # Iterate through the collection displaying the output as a complete sentence using
    # each value. Use the f-string format to control the output.
    for instrument in INSTRUMENTS:
        print(f'I want to learn how to play the {instrument.lower()}.')

    print('\nReverse:\n')

    # Repeat the output in reverse order using a different context string.
    for instrument in reversed(INSTRUMENTS):
        print(f'The {instrument.lower()} is my favorite instrument of all time.')


if __name__ == '__main__':
    main()
