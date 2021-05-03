class Person: 
    def __init__(self, first_name, last_name): 
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def full_name(self): 
        return '{} {}'.format(self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name): 
        parts = name.split()
        if len(parts) != 2: 
            raise ValueError('Sorry, too difficult name')

        self.first_name, self.last_name = parts

p = Person('John', 'Doe')
print(p.full_name)
p.full_name = 'Lisa Doe'
print(p.full_name)