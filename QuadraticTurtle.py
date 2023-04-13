import turtle



class QuadraticTurtle (turtle.RawTurtle):
    
    #Variables
    __factor = 10
  
    #Constructor
    def __init__(self,canvas):
        super(QuadraticTurtle,self).__init__(canvas)
        

    #Getter and setter methods
    def set_factor(self, change):
        self.__factor = change

    def get_factor(self):
        return self.__factor

    #Plots points for a graph, if the turtle's pen is up
    #it will also draw a line.
    #The position set will be x * the factor and y * the factor.
    #Preconditions: Takes two parameters an x and y coordiate as real numbers.
    #Postcondtions: None
    def plot_points(self, x, y):
        self.setpos(x * self.__factor ,y * self.__factor)
        self.dot()

    #A brute force algortihm to create a quadratic curve.
    #Preconditions: a is the gradient of the curve, b 
    def solve_y(self, a, b, c, x1 = -10, x2 = 10):
        self.penup()
        first_point = True
        for x in range(x1, x2):
            if first_point:
                self.penup()
                first_point = False
            else:
                self.pendown()
            y = (a*(pow(x,2)))+(b*x)+c
            print(x,y)
            self.plot_points(x, y)

    
