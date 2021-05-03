class Animal: 
    # Class Attributes: shared by all instances
    species = "dog"
    

    # Class attributes can be defined on a class: 
        # ex Animal.species = "dog"
    
    """Initialization""" 
    # special method that Python will all after making an instance 
    # must take in self and return none

    def __init__(self, name): 
        self.name = name
        self.walk = 0


    """Methods"""

    def speak(self): 
        print('Woof')

    def dance(self): 
        return ':prance, prance, prance'
    
    """Self""" 
    # instance the method was called on 
    # through self we can access attributes

    def walkies(self): 
        self.walk += 1
        if self.walk > 1:
            print(f"we already went on {self.walk} walks today!")
        else: 
            self.walk == 1 
            print("let's go on a another walk!")
            

    
    