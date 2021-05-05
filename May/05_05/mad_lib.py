import random 

colors = ["red", "orange", "yellow", "green", "blue"]
plural_nouns = ["dogs", "bottles", "lamps", "cars"]
celebrities = ["tom hanks", "tom cruise", "tom holland"]

# color = input("Enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a celebrity name: ")



def mad_lib(colors, plural_nouns, celebrities): 
    color = colors[random.randint(0, len(colors)-1)]
    plural_noun = plural_nouns[random.randint(0, len(plural_nouns)-1)]
    celebrity = celebrities[random.randint(0, len(celebrities)-1)]
    return f"roses are {color} \n", f"{plural_noun} are blue \n", f"i love {celebrity}"

print(mad_lib(colors, plural_nouns, celebrities))