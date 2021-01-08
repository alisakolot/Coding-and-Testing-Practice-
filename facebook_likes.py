def likes(names):
    #your code here
    if len(names) == 0:
        return 'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    
    if len(names) == 2: 
        return f'{names[0]} and {names[1]} like this'

    if len(names) == 3: 
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    
    if len(names) >= 4:
        j = len(names) - 2 
        return f'{names[0]}, {names[1]} and {j} others like this'

likes(["Jacob", "Alex"]) # must be "Jacob and Alex like this"
likes(["Max", "John", "Mark", "peter", "asdfsaf", "sadfsafsad"]) # must be "Max, John and Mark like this"

# likes(["Alex", "Jacob", "Mark", "Max"]) 'Alex, Jacob and 2 others like this'