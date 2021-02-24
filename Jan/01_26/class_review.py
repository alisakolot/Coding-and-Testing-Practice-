class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greeting(self):
        print("hi, my name is " * 3 + self.name)
    
    # def __repr__(self, name, age):
    #     self.name = name
    #     self.age = age
    #     return repr(self.name, self.age)

p1 = Person("Slim shady", 45) 


class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string
    
    # print rows
    def rows(self):
        rows = []
        matrix_string_rows = matrix_string.split('\n')

        # for item in matrix_string_rows:
        #     r = []
        #     r.append(item)
        #     rows.append(r)

        for item in matrix_string_rows:
            lst = item.split(' ')
            r = []
            for num in lst:
                r.append(int(num))
            rows.append(r)
        return rows

    # print columns
    def columns(self):
        column = []

        # [1,2]
        # [3,4]

        # [4, 5, 6]
        # [3, 4, 5]
        #  each column number can be repr by the lst = len(row)
        
        amt_columns = len(self.rows()[0])

        for i in range(amt_columns):
            c = []
            for row in self.rows():
                c.append(row[i])

            column.append(c)
        return column
        
matrix_string = "1 2\n3 4"
matrix1 = Matrix(matrix_string)

# [1,2]
# [3,4]