r = 0
g = 0
b = 0

def setup() :
    background(255)
    size (600,600)
    strokeWeight(6)
def draw ():
    textSize(50)
    text(u"очистить",40,150)
    fill(33,55,86)
    rect (20,70,60,40)
    
    fill(100)
    rect (510,10,60,40)
    
    fill(255,255,255)
    rect (440,10,60,40)
    
    fill("#FC00EC")
    rect (370,10,60,40)
    fill("#00FCFA")
    rect (300,10,60,40)
    fill("#DEFC00")
    rect (230,10,60,40)
    fill(255,0,0)
    rect (20,10,60,40)
    fill(0,255,0)
    rect (90,10,60,40)
    fill(0,0,255)
    rect (160,10,60,40)
    
    
    if mousePressed:
        line(pmouseX,pmouseY,mouseX,mouseY)
def mouseClicked():
    if mouseX > 20 and mouseX < 20+60 and mouseY > 10 and mouseY< 10+40:
        strokeWeight(6)
        fill(255,0,0)
        stroke(255,0,0)
        
    if mouseX > 90 and mouseX < 90+60 and mouseY > 10 and mouseY< 10+40:
        strokeWeight(6)
        fill(0,255,0)
        stroke(0,255,0)

    if mouseX > 160 and mouseX < 160+60 and mouseY > 10 and mouseY< 10+40:
        strokeWeight(6)
        fill(0,0,255)
        stroke(0,0,255)
        
    if mouseX > 230 and mouseX < 230+60 and mouseY > 10 and mouseY< 10+40:
        strokeWeight(6)
        fill("#DEFC00")
        stroke("#DEFC00")
        
    if mouseX > 300 and mouseX < 300+60 and mouseY > 10 and mouseY< 10+40:
        strokeWeight(6)
        fill("#00FCFA")
        stroke("#00FCFA")
    
    if mouseX > 370 and mouseX < 370+60 and mouseY > 10 and mouseY< 10+40:
        strokeWeight(6)
        fill("#FC00EC")
        stroke("#FC00EC")
        
    if mouseX > 440 and mouseX < 440+60 and mouseY > 10 and mouseY< 10+40:
        strokeWeight(32)
        fill(255,255,255)
        stroke(255,255,255)

    if mouseX > 510 and mouseX < 510+60 and mouseY > 10 and mouseY< 10+40:
        strokeWeight(6)
        fill(255)
        stroke(90)
        
    if mouseX > 20 and mouseX < 20+60 and mouseY > 70 and mouseY< 70+40:
        background(255)

 
        
