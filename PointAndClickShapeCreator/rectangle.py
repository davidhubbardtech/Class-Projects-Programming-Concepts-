# A program to allow the user to draw a rectangle
# Tells the user the perimeter and area after program closes

# Import graphic module from same file location
from graphics import *
from math import sqrt

def main():
    # Create "Win" variable so program is capable of drawing rectangle
    # Set size to 600, 600 so it fills screen
    Win = GraphWin("David's Rectangle Drawer", 600, 600)

    # Ask user to click on two points within window
    # These two points will be the basis for the rectangle
    text = Text(Point(300,40), 'Click any two points to draw rectangle')
    # Establish the size of the text (16 worked best for me)
    text.setSize(16)
    # Use draw feature
    text.draw(Win)

    # Establish feedback from the user's mouse inputs
    pt1 = Win.getMouse()
    pt1.draw(Win)
    pt2 = Win.getMouse()
    pt1.undraw()
    # Set to two points
    line = Rectangle(pt1, pt2)
    line.draw(Win)

    # Create variable for length
    length = abs(pt2.getY() - pt1.getY())
    # Create variable for width
    width = abs(pt2.getX() - pt1.getX())
    # Create variable for area
    area = float(length * width)
    # Create variable for perimeter
    perimeter = float(2*(length + width))

    # Display area and Perimeter
    text.setText('Perimeter:'+ format(perimeter, '0.4') + ' px\nArea: ' + \
                 format(area, '0.0f') + 'sq px')

    # So that the window will close on the final mouse click
    Win.getMouse
    Win.close()

    # Print the area after window closes
    print("area = " + str(area))
    # Print the perimeter after the window closes
    print("perimeter = " + str(perimeter))


main()

