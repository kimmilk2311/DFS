import turtle                   
import time
from collections import deque

wn = turtle.Screen()               
wn.bgcolor("black")               
wn.title("Breath First Search")
wn.setup(1388,768)                

start_x = 0
start_y = 0
end_x = 0
end_y = 0

# Vẽ turtle trắng dùng để vẽ mê cung
class Maze(turtle.Turtle):               
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            
        self.color("white")           
        self.penup()                   
        self.speed(0)
# Sử dụng turtle xanh lá cây dùng để vẽ mê cung
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)
# Sử dụng turtle xanh nước biển đễ hiển thị các frontier
class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)
# Sử dụng turtle đỏ để đại diện cho vị trí bắt đầu 
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.setheading(270)
        self.penup()
        self.speed(0)
# Sử dụng turtle vàng để biểu thị vị trí cuối cùng và đường dẫn giải cho thuật toán
class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

grid1 = [
"++++++++++++++++++++++++++++++++++++++++++++++",
"+ s                                          +",
"+++++++++++++ +++++++++++++++ ++++++++++++++ +",
"+           +                 +              +",
"++ +++++++ ++++++++++++++ ++++++++++++ +++++++",
"++ ++    + ++           + ++                 +",
"++ ++ ++ + ++ ++ +++++ ++ ++ +++++++++++++++ +",
"++ ++ ++ + ++ ++ +     ++ ++ ++ ++        ++ +",
"++ ++ ++++ ++ +++++++++++ ++ ++ +++++ +++ ++ +",
"++ ++   ++ ++             ++          +++ ++ +",
"++ ++++ ++ +++++++++++++++++ +++++++++++++++ +",
"++    + ++                   ++              +",
"+++++ + +++++++++++++++++++++++ ++++++++++++ +",
"++ ++ +                   ++          +++ ++ +",
"++ ++ ++++ ++++++++++++++ ++ +++++ ++ +++ ++ +",
"++ ++ ++   ++     +    ++ ++ ++    ++     ++ +",
"++ ++ ++ +++++++ +++++ ++ ++ +++++++++++++++ +",
"++                     ++ ++ ++              +",
"+++++ ++ + +++++++++++ ++e++ ++ ++++++++++++++",
"++++++++++++++++++++++++++++++++++++++++++++++",
 ]
grid2 = [
"++++++",
"+++ ++",
"+++ ++",
"+s   +",
"+++ ++",
"++  e+",
"++++++",
]
#hàm xây dựng thực toán
def setup_maze(grid):                          
    global start_x, start_y, end_x, end_y      
    for y in range(len(grid)):                          # số hàng mà grid có                       
        for x in range(len(grid[y])):                   # số cột mà grid có    
            character = grid[y][x]             
            screen_x = -550 + (x * 24)        
            screen_y = 250 - (y * 24)        

            if character == "+":               
                maze.goto(screen_x, screen_y)     
                maze.stamp()                            # đánh dấu turtle trắng              
                walls.append((screen_x, screen_y))      # thêm ô vào danh sách của walls

            if character == " ":                   
                path.append((screen_x, screen_y))       # thêm ô trống vào danh sách path

            if character == "s":                       
                start_x, start_y = screen_x, screen_y   # gắn các biến vị trí bắt đầu cho start_x và start_y
                red.goto(screen_x, screen_y)  
                
            if character == "e":                    
                yellow.goto(screen_x, screen_y)     
                yellow.stamp()                          # đánh dấu turtle vàng
                end_x, end_y = screen_x, screen_y       # gắn các biến vị trí cuối cho end_x và end_y
                path.append((screen_x, screen_y))       # thêm ô vào danh sách path

def search(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y
    while len(frontier) > 0:         
        time.sleep(0)
        x, y = frontier.popleft()     # Lấy và loại bỏ phần tử đầu tiên trong hàng đợi, gắn tọa độ cho x và y       
 
        if(x - 24, y) in path and (x - 24, y) not in visited:  # check left
            cellleft = (x - 24, y)
            solution[cellleft] = x, y                           # quay lui ô trước đó
            blue.goto(cellleft)         
            blue.stamp()              
            frontier.append(cellleft)                           # thêm ô cuối vào cuối danh sách frontier           
            visited.add((x-24, y))                              # thêm ô vào danh sách visited 

        
        if(x + 24, y) in path and (x + 24, y) not in visited:   # check right
            cellright = (x + 24, y)
            solution[cellright] = x, y                          # quay lui ô trước đó        
            blue.goto(cellright)
            blue.stamp()
            frontier.append(cellright)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cellup = (x, y + 24)
            solution[cellup] = x, y
            blue.goto(cellup)
            blue.stamp()
            frontier.append(cellup)
            visited.add((x, y + 24))


        if (x, y - 24) in path and (x, y - 24) not in visited:  # check down
            celldown = (x, y - 24)
            solution[celldown] = x, y                           # quay lui ô trước đó
            blue.goto(celldown)
            blue.stamp()
            frontier.append(celldown)
            visited.add((x, y - 24))

        green.goto(x,y)
        green.stamp()

def backRoute(x, y):                                          # solution funtion
    yellow.goto(x, y)                      
    yellow.stamp()
    while (x, y) != (start_x, start_y):                       # Dừng vòng lập khi các ô hiện tại = ô bắt đầu
        yellow.goto(solution[x, y])                           # Di chuyển turtle vàng theo đường đi ngược bằng cách sử dụng giá trị trong solution
        yellow.stamp()                                            
        x, y = solution[x, y]              
        

# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()
walls = []
path = []
visited = set()
frontier = deque()
solution = {}                           

setup_maze(grid1)
search(start_x,start_y)
backRoute(end_x, end_y)

wn.exitonclick()
