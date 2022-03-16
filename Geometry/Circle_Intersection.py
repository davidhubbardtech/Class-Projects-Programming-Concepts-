# This program will compute the intersection of a circle with a horizontal line
# and display the information textually and graphically

# Import graphics/math modules
from graphics import *
from math import sqrt

def main():
    # name program and set display coordinates
    win = GraphWin('Circle Intersection Calculator' , 300, 330)
    win.setCoords(-10, -12, 10, 10)
    # describe program
    description = Text(Point(0, 0), 'compute the intersection of a circle with horizontal line')
    # give user instructions
    click = Text (Point(0, -11), 'Click to start')
    # program size of description display
    description.setSize(8)
    click.setSize(8)
    description.draw(win)
    click.draw(win)
    # receive mouse input from user
    win.getMouse()
    description.undraw()

    # prompt the user to enter the radius and y intercept and draw the outcome
    # create variables for the user's inputs for both radius and y intercept

    radius_prompt = Text(Point(-5,5), 'The Radius is: ')
    Y_intercept_prompt = Text(Point(-5,0), 'The y intercept is: ')
    radius_prompt.setSize(8)
    Y_intercept_prompt.setSize(8)
    radius_prompt.draw(win)
    Y_intercept_prompt.draw(win)
    radius_input = Entry(Point(0, 5), 3)
    Y_intercept_input = Entry(Point(0, 0), 3)
    radius_input.setSize(8)
    Y_intercept_input.setSize(8)
    radius_input.draw(win)
    Y_intercept_input.draw(win)

# Evaluate the radius and intercept inputs

    win.getMouse()
    radius = eval(radius_input.getText())
    intercept = eval(Y_intercept_input.getText())
    radius_prompt.undraw()
    Y_intercept_prompt.undraw()
    radius_input.undraw()
    Y_intercept_input.undraw()
    click.undraw()

    # Create variables for the both x intercepts

    xint1 = -sqrt(radius ** 2 - intercept ** 2)
    xint2 = sqrt(radius ** 2 - intercept ** 2)

    # program coordinates for x and y axis display
    # color the lines and point

    xaxis = Line(Point(-10,0), Point(10,0))
    xaxis.setArrow('last')
    yaxis = Line(Point(0,-10), Point(0,10))
    yaxis.setArrow('last')
    circle = Circle(Point(0,0), radius)
    circle.setOutline('black')
    line = Line(Point(-10, intercept), Point(10, intercept))
    line.setOutline('green')
    int1 = Circle(Point(xint1, intercept), 0.2)
    int1.setFill('yellow')
    int1.setOutline('yellow')
    int2 = Circle(Point(xint2, intercept), 0.2)
    int2.setFill('yellow')
    int2.setOutline('yellow')
    xaxis.draw(win)
    yaxis.draw(win)
    circle.draw(win)
    line.draw(win)
    int1.draw(win)
    int2.draw(win)

    # create variable for intercept info for final result

    intercept_info = Text(Point(0,-11), 'x values of points of\n' +
                          'intersection: ' + str(xint1) + ', ' + \
                          str(xint2))
    intercept_info.setSize(8)
    intercept_info.draw(win)

    win.getMouse()
    win.close()

main()