#Comments
#{{{Comments are annotations to code youcan use to make it easier to understand.}}}
#{{{They decribe what the code is doing and help other developers understand it.}}}

#{{{ Creat Comment using the # symbol: }}}

#ex

x = 43
# printing the value of x
print(x)


#____________________________________________________________________________________-

#Docstrings
#{{{Docstring (document string) are used to describe what function do.}}}
#{{{They're created by putting a multiline string containing an explanation of the function below the function's first line.}}}
#ex
def shout(word):
    '''
    Print a word with an
    exclamation mark following it.
    '''
    
    """
    Print a word with an
    exclamation mark following it.
    """
    print(word + '!')