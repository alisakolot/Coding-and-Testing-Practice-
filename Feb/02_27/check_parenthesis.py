"""Write a function that takes a string of parentheses, 
and determines if the order of the parentheses is valid. 
The function should return true if the string is valid, 
and false if it's invalid.
Examples

"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true

Constraints

0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input 
may contain any valid ASCII characters. Furthermore, the 
input string may be empty and/or not contain any parentheses 
at all. Do not treat other forms of brackets as parentheses 
(e.g. [], {}, <>)."""

def valid_parentheses(string):
    paren_str = ''
    
    for char in string:
        if char == '(':
            paren_str += char
            li = string.index(char)
            char = char[(li + 1):]
        elif char == ')':
            paren_str += char
            ri = string.index(char)
            char = char[(ri + 1):]
        else:
            print(char)
    print(paren_str)

    culprit = ')('
    if culprit in paren_str:
        print('False')
    else:
        print('True')

    
# Reason for error:
# Parenthesis that do not face each other cannot count as a match
