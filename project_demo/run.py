
# triggering the entire project
# to execute this project, in terminal enter: python run.py


# to use the variables we need to import them
from demo_1 import variables as v1

# to use the functions in helper_functions.py file we need to import them
from demo_1 import helper_functions as hf
# to use the things in demo_2 folder, we can import them as modules.
# because the sub-folder contains __init__.py file
from demo_2 import email
import demo_2.helper_functions
from demo_2 import variables
from demo_2.email import Email # -> this is how we import class from the other sub-folder


# this is the main function calling other functions in this project
def run():
    result = hf.function(start = v1.START, end = v1.END)
    # the function function is in helper_functions.py file
    
    # storing the result in a different format
    pretty = hf.prettify(result)
    print(pretty)

    # this class methods are from different sub-folder of this project
    mail = Email() # -> this is an object initiation of the class Email
    mail.to = 'name@email.com'
    mail.subject = 'Subject'
    mail.body = pretty
    mail.send() # -> this is method of the Email class


# this conditional is for when in terminal "python run.py" is executed then this file will run
if __name__ == '__main__':
    run()

