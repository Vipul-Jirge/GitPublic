from requirements import *
from globalModules import save_output
# for vs-code type check
try:
    from globalModules.Processing3 import *
except:
    pass

def settings():
    global IF_PLOT_CIRCLES
    # frameRate(10)
    size(900, 900)
    smooth()
    IF_PLOT_CIRCLES = True

def setup():
    global D1, D2, theta, psy, HOLE, linePX, linePY, STORE_LINES, PG_CURVE, PG_C1, TRACK_POINTS
    D1 = 300
    D2 = 180
    theta = PI/180
    psy = (theta * D1/2) / D2/2
    HOLE = 130
    x1 = x2 = x3 = width/2 + (D1/2 - D2/2)* cos(theta) + HOLE*cos(theta+psy)
    y1 = y2 = y3 = height/2 + (D1/2 - D2/2)* sin(theta) + HOLE*sin(theta+psy)
    TRACK_POINTS = [x1, y1, x2, y2, x3, y3]
    strokeWeight(1.2)
    background(240)
    noFill()
    frameRate(1400)
    PG_CURVE = createGraphics(width,height)
    PG_CURVE.beginDraw()
    PG_CURVE.stroke(1)
    PG_CURVE.noFill()
    PG_CURVE.background(240)
    PG_CURVE.strokeWeight(0.8)
    PG_CURVE.endDraw()

def draw():
    global theta, psy, linePX, linePY, STORE_LINES, PG_CURVE, HOLE, D1,D2, TRACK_POINTS, IF_PLOT_CIRCLES
    
    background(240)
    image(PG_CURVE,0,0)
    
    # Equation for  spiral(?)
    lineNX = width/2 + (D1/2 - D2/2) * cos(theta) + HOLE*cos(theta+psy)
    lineNY = height/2 + (D1/2 - D2/2) * sin(theta) + HOLE*sin(theta+psy)

    if IF_PLOT_CIRCLES == True:
        # Center big circle - plot it
        noFill()
        stroke(1)
        circle(width/2,height/2, D1)
        
        # Center of small circle + plot it
        cx = width/2 + (D1/2 - D2/2) * cos(theta)
        cy = height/2 + (D1/2 - D2/2) * sin(theta)
        noFill()
        stroke(1)
        circle(cx, cy, D2)
        # Rotating Line inside the circle + plot it
        line(cx,cy, lineNX,lineNY)

    # Epicycloyd (?)
    stroke(255,0,0)
    fill(255,0,0)
    circle(lineNX,lineNY,5) # Red point tracking the spriral 
    PG_CURVE.beginDraw()
    PG_CURVE.curve(TRACK_POINTS[0], TRACK_POINTS[1], TRACK_POINTS[0], TRACK_POINTS[1], lineNX, lineNY, lineNX, lineNY)
    # PG_CURVE.line(linePX,linePY,lineNX,lineNY)
    PG_CURVE.endDraw()
    TRACK_POINTS[4] = lineNX
    TRACK_POINTS[5] = lineNY
    TRACK_POINTS[2] = TRACK_POINTS[4]
    TRACK_POINTS[3] = TRACK_POINTS[5]
    TRACK_POINTS[0] = TRACK_POINTS[2]
    TRACK_POINTS[1] = TRACK_POINTS[3]

    theta += 4*PI/180 # move ahead by 1 radian
    psy = (theta * D1/2) / D2/2

    if keyPressed == True:
        background(240)
        PG_CURVE = createGraphics(width,height)
        PG_CURVE.beginDraw()
        PG_CURVE.stroke(1)
        PG_CURVE.noFill()
        PG_CURVE.background(240)
        PG_CURVE.strokeWeight(0.8)
        PG_CURVE.endDraw()
        # redraw()


def keyPressed():
    global HOLE, D1, D2, IF_PLOT_CIRCLES
    if key == CODED:
        if keyCode == UP:
            HOLE += 5
        elif keyCode == DOWN:
            HOLE -= 5

    if key == 'q':
        D1 += 5
    elif key == 'a':
        D1 -= 5
    elif key == 'w':
        D2 += 5
    elif key == 's':
        D2 += 5
    elif key == 'o':
        IF_PLOT_CIRCLES = True
    elif key == 'f':
        IF_PLOT_CIRCLES = False
    elif key == 'x':
        noLoop()
    elif key == 'z':
        loop()
    # print("typed %s %d" % (key, keyCode))
