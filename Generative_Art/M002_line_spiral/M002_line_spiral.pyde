from requirements import *
from globalModules import save_output
# for vs-code type check
try:
    from globalModules.Processing3 import *
except:
    pass

def setup():
    global delta,circle_radius
    background(220)
    size(500, 500)
    noFill()
    delta = 0
    circle_radius = 200

def draw():
    global delta,circle_radius
    # hexagon()
    orgX,orgY = [width/2,height/2]
    
    poly_sides = 3#int(map(mouseX,0,width,3,10))
    poly_theta = 360/poly_sides
    twin_theta = (180 - poly_theta)/2.0

    if circle_radius > 50:
        pushMatrix()
        translate(orgX, orgY)
        rotate(delta)
        
        frac = map(mouseY,0,height,0.0001,1)
        
        beginShape()
        for iplot in range(poly_sides):
            theta = iplot*poly_theta
            vertex(circle_radius*cos(radians(theta)),circle_radius*sin(radians(theta)))
        endShape(CLOSE)
        
        popMatrix()

        side = 2*circle_radius*sin(radians(poly_theta/2))
        pfy = atan((frac*side*sin(radians(twin_theta)))/(circle_radius-frac*side*cos(radians(twin_theta))))
        
        if pfy < 0:
            pfy = radians(180)+pfy          
            # print('pfy: ', pfy)
        new_radius = frac * side* sin(radians(twin_theta)) / sin(pfy)

        delta += pfy
        circle_radius = abs(new_radius)
        # print('circle_radius: ', circle_radius)

        # For angle method:

        # mult = map(mouseY,0,height,0,poly_theta)
        # mult = 20   
        
        # delta += mult
        # circle_radius = circle_radius*sin(radians(twin_theta)) / sin(radians(180-twin_theta-mult))

def mouseMoved():
    global circle_radius, pfy
    global delta
    background(220) 
    circle_radius = 200
    delta = 0