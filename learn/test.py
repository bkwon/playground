
#initialize Global Variables for program
myname=""
x=3 #number of tries for a valid name
count = 0
cmd_array = ['Encouragement','Reminder','exit']
# create a function so it is easy to go back to the beginning. You cannot easily navigate logic with just if and else statements!!

#helper function to start/stop the program

def new_session(myname):
    myname = raw_input('What is your name? --> ')

def session_handler1(x):
    x -= 1


new_session(myname)
{
    if x != '':
    {
        session_handler1(x)
            if myname is not '' and x > 0:
                print 'Welcome', myname, '! '
                print '------------------------'

            elif myname is '' and x > 0:
            x -= 1
            print 'You have 3 chances total with only', x, 'chances remaining.'
            print ''

            else:
            print 'Sorry but I do not know who you are. Shutting down.'
            exit()
    }
}
bkcommand = raw_input('Your command, sir: "Encouragement", "Reminder" or "Exit" --> ')
if bkcommand == 'Encouragement':
    print('Forget the rest, you are the best!')
elif bkcommand == 'Reminder':
    print('Make sure to revisit your Coursera class from Michigan State University')
elif bkcommand == 'Exit':
    print('Very good, sir. Exiting now.')
else:
    print('You entered an invald command. Please try again.')
#else:
#    print('Sorry Bryant, but I did not recognize that command. Please run me again.')