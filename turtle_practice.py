import turtle

DIST = 100
for x in range(0,6):
    print "x", x
    for y in range(1,9):
        print "y", y
        turtle.fillcolor('red')
        
        turtle.right(45)
        
        turtle.circle(DIST)
    
        turtle.stamp()
    DIST += 20