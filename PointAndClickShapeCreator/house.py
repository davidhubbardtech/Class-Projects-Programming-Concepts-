# David Hubbard's 5 point House Project
# Program that allos user to draw a house with 5 clicks

# Import graphics from same file location
from graphics import *


def main():
    # Name program and set coordinates
    win = GraphWin('5 Click House Assignment', 600, 600)
    win.setCoords(0, 0, 100, 100)
    # create variables for Points 1 and 2
    P1 = win.getMouse()
    P2 = win.getMouse()
    # create variable for the frame to be a rectangle based on p1 and p2
    frame = Rectangle(P1, P2)
    # command program to draw frame
    frame.draw(win)

    # create variables for all four sides of house
    houseBottomY = min(P1.getY(), P2.getY())
    houseTopY = max(P1.getY(), P2.getY())
    houseLeftX = min(P1.getX(), P2.getX())
    houseRighX = max(P1.getX(), P2.getX())

    # create variable for point 3
    P3 = win.getMouse()

    # create variables for width and height of door
    doorW = abs(P1.getX() - P2.getX()) * 0.2
    doorH = abs(P3.getY() - houseBottomY)
    # create 2 points to base the rectangle that forms the door
    doorP1 = Point(P3.getX() - doorW * 0.5, houseBottomY)
    doorP2 = Point(P3.getX() + doorW * 0.5, P3.getY())

    door = Rectangle(doorP1, doorP2)
    door.draw(win)
    # create variable for point 4 (the house's window)
    P4 = win.getMouse()
    # make window height equivalent tp the door width multiplied by 1/2
    # This gives the window the proper size
    windowH = doorW * 0.5
    # describes the formula for both points of the window
    windowP1 = Point(P4.getX() - windowH * 0.5, P4.getY() - windowH * 0.5)
    windowP2 = Point(P4.getX() + windowH * 0.5, P4.getY() + windowH * 0.5)

    window = Rectangle(windowP1, windowP2)
    window.draw(win)
    # make variable for point 5
    P5 = win.getMouse()
    # create the 3 points for the roof
    RoofP1 = Point(houseLeftX, houseTopY)
    RoofP2 = Point(houseRighX, houseTopY)
    RoofP3 = P5

    roof = Polygon(RoofP1, RoofP2, RoofP3)
    roof.draw(win)
# The first two clicks form the frame of the house
# The third click forms the door
# The fourth click forms the window
# the fifth click forms the roof

main()