# return_stars(3)
# '***'

def return_stars(num):
    if num == 0:
        print('')
        return ''
    
    if num >= 1:
        stars = '*' + return_stars(num-1)
        print(stars) 
        return stars

print(return_stars(3))
print(return_stars(0))
print(return_stars(5))


