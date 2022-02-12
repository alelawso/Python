'''Mad Libs Generator'''

def madLib():
    
    #all the questions asked
    name = input('What is your name? ')
    home = input('Where are you from? ')
    adj1 = input('Using one word what is it like where you are from? ')
    job = input('What is your job? ')
    employer = input('Who do you work for? ')
    hobby = input('What do you do for fun? ')

    #the story based on what the user inputted
    print('\n\nThis is {0}. He is from {2} {1}. He works for {4} as a {3}. {0} likes to {5} for fun.\n'
      .format(name, home, adj1, job, employer, hobby))


play_again = input("Play Mad Libs? (y/n) ")

if play_again == 'y':
    madLib()    
else:
    quit()

#https://www.instructables.com/Mad-Lib-With-Python/
