from turtle import Turtle

class Snake():
    
    def __init__(self):
        self.snake = []
        self.init_snake()
        self.head = self.snake[0]

    def add_snake(self):
        """adds a piece of the snake"""
        t = Turtle('square')
        t.ht()
        t.penup()

        if len(self.snake):
            last_pos = self.snake[-1].pos
            
            if self.snake[-1].heading == 0: # last is going right
                t.goto(last_pos[0]-20, last_pos[1])
                self.head().forward(20)
            elif self.snake[-1].heading == 180: # last is going left
                t.goto(last_pos[0]+20, last_pos[1])
                self.head().forward(20)
            elif self.snake[-1].heading == 90: # last is going up
                t.goto(last_pos[0], last_pos[1]-20)
                self.head().forward(20)
            elif self.snake[-1].heading == 270: # last is going down
                t.goto(last_pos[0], last_pos[1]+20)
                self.head().forward(20)
        
        t.color('grey')
        
        self.snake.append(t)
        t.st()
    
    def init_snake(self):
        """base snake at the start of the game all snake objects start as this"""
        self.add_snake()
        self.add_snake()
        self.add_snake()

    def move_up(self):
        """moves the snake head up"""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        """moves the snake head down"""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        """moves the snake head left"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        """moves the snake head right"""
        if self.head.heading() != 180:
            self.head.setheading(0)

    def move_forward(self):
        """moves all pieces of snake forward by moving each piece to the front piece position"""
        for current_part in range(len(self.snake) - 1, 0, -1):
            xcord = self.snake[current_part - 1].xcor()
            ycord = self.snake[current_part - 1].ycor()
            self.snake[current_part].goto(xcord, ycord)
        self.head.forward(20)