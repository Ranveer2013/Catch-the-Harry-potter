import pgzrun,random

WIDTH,HEIGHT = 800,500
harry=Actor("harry_potter.png")
harry.pos=400,200
#dumbledore=Actor("dumbledore.png")
#dumbledore.pos=400,400
ron=Actor("ron-harry_potter.png")
ron.pos=200,200
#voldemart=Actor("voldemart.png")
#voldemart.pos=200,400

game_over=False
message="catch the harry potter,ron and avoid the dumbledore and voldemart!"
score=0

def draw():
    screen.blit("bg.jpg",(0,0))
    if not game_over:
        harry.draw()
        #dumbledore.draw()
        ron.draw()
       # voldemart.draw()
    else:
        pass
    screen.draw.text(message,(20,20))
    screen.draw.text("score"+ str(score),(20,40))

def random_position():
    x=random.randint(50,750)
    y=random.randint(50,450)
    harry.pos=x,y

    x=random.randint(50,750)
    y=random.randint(50,450)
   # dumbledore.pos=x,y
    x=random.randint(50,750)
    y=random.randint(50,450)
    ron.pos=x,y
    x=random.randint(50,750)
    y=random.randint(50,450)
   # voldemart.pos=x,y
def update():
    if keyboard.up:
        harry.y-=20

    elif keyboard.down:
        harry.y+=20
def on_key_down(key):
    if keys.LEFT==key:
        harry.x-=20

    elif keys.RIGHT==key:
        harry.x+=20

    



       
def game_end():
    global game_over,message
    message="Game is over"
    game_over=True
clock.schedule(game_end,30)
pgzrun.go()
