#  ###  ### 
#  # #  # # 
#  ###  ### 

#  ********
#  ********


class Canvas:

    def __init__(self):
        #create the canvas
        self.shapes = []
        #create a list of shapes inherited from rectangle
        

    def get_data(self):
        data = [['.']*10 for _ in range(10)]

        #get data from rectangles class/self.shapes
        
        for s in self.shapes:
            s.draw(data)
        return data

    def render_canvas(self):
        for row in self.get_data():
            print(''.join(row))
            #creating a canvas that is displayed as dots 

    def add_shape(self, shapes):
        #add shapes from rectangle class 
        self.shapes.append(shapes)

    def clear(self):
        self.shapes.clear()

    
    
class Rectangle:

    def __init__(self, start_x, start_y, end_x, end_y, fill_char):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.fill_char= fill_char     

    def draw(self, data):
        for x in range(self.start_x, self.end_x+1):
            for y in range(self.start_y, self.end_y+1):
                data[y][x] = self.fill_char
        

    def change_fill(self):
        pass




#User Input:
c = Canvas()

r1 = Rectangle(start_x=1, start_y=0, end_x=3, end_y=2, fill_char='#')
r2 = Rectangle(start_x=6, start_y=0, end_x=8, end_y=2, fill_char='#')
r3 = Rectangle(start_x=1, start_y=4, end_x=8, end_y=5, fill_char='*')

#spaces/pupils

s1= Rectangle(start_x=2, start_y=1, end_x=2, end_y=1, fill_char=' ')
s2= Rectangle(start_x=7, start_y=1, end_x=7, end_y=1, fill_char=' ')

#add shape to the canvas

c.add_shape(r1)
c.add_shape(r2)
c.add_shape(r3)

c.add_shape(s1)
c.add_shape(s2)

#render canvas

c.render_canvas()