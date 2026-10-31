import pgzrun,random

WIDTH,HEIGHT = 800,500
harry=Actor("harry_potter.png")
harry.pos=400,200
dumbledore=Actor("dumbledore.png")
dumbledore.pos=400,400
message="catch the harry potter and avoid the dumbledore!"
score=0

def draw():
    screen.blit("bg.jpg",(0,0))
    harry.draw()
    dumbledore.draw()

    screen.draw.text(message,(20,20))
    screen.draw.text("score"+ str(score),(20,40))



def on_mouse_down(pos):
    global score,message
    print(pos)
    if harry.collidepoint(pos):
        score+=10
        message="Yay, you caught the Harry Potter!"
        x=random.randint(50,750)
        y=random.randint(50,450)
        harry.pos=x,y

        x=random.randint(50,750)
        y=random.randint(50,450)
        dumbledore.pos=x,y

    elif dumbledore.collidepoint(pos):
        score-=5
        message="Oops, you caught the wrong guy"
        x=random.randint(50,750)
        y=random.randint(50,450)
        dumbledore.pos=x,y
        
        x=random.randint(50,750)
        y=random.randint(50,450)
        harry.pos=x,y

    else:
        message="Catch the Harry Potter, Oops you missed him this time"


pgzrun.go()

