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
    lp = 0
    rp = 0
    
    for char in string:
        if char == '(':
            lp += 1
            li = string.index(char)
            char = char[(li + 1):]
        elif char == ')':
            rp += 1
            ri = string.index(char)
            char = char[(ri + 1):]
        else:
            print(char)

    if lp != rp:
        print('not match')
        return False
    else:
        print('match')
        return True

# Reason for error:
# Parenthesis that do not face each other cannot count as a match
