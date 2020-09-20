from bangtal import*

import random



setGameOption(GameOption.INVENTORY_BUTTON, False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON, False)

scene = Scene('벤허 마상 경기', 'SantaRace/background.jpg')
benhur = Object('SantaRace/benhur.png')
play = Object('SantaRace/play.png')
timer = Timer(10.)
switchstart = Object('SantaRace/start.png')
switchend = Object('SantaRace/end.png')

benhur.X = 0
benhur.Y = 300



play.locate(scene, 100, 100)
benhur.locate(scene, benhur.X, benhur.Y)
switchstart.locate(scene, 600, 200)
switchend.locate(scene, 600, 100)
benhur.setScale(0.5)


benhur.show()
switchstart.show()
switchend.show()
showTimer(timer)

def PlayOnMouseClick(x,y,action):
    moveran = random.randrange(-1,2)
    benhur.X = benhur.X +30
    benhur.Y = benhur.Y + 15 * moveran
    benhur.locate(scene, benhur.X, benhur.Y)


    if benhur.X > 1200:
        showMessage("벤허가 승리하였다")
        switchstart.show()
        switchend.show()
        play.hide()
        timer.stop()

def endOnMouseClick(x,y,action):
    endGame()

def startOnMouseClick(x,y,action):
    
    switchstart.hide()
    switchend.hide()
    play.show()
    timer.set(10.)
    timer.start()
    benhur.X = 0
    benhur.Y = 300

play.onMouseAction = PlayOnMouseClick
switchstart.onMouseAction = startOnMouseClick
switchend.onMouseAction = endOnMouseClick

def timeout():
    benhur.x = 0
    benhur.y = 300
    switchstart.show()
    switchend.show()
    play.hide()
    switchstart.setImage('SantaRace/restart.png')
    showMessage("벤허는 사형당하였다")


timer.onTimeout = timeout
timer.start



startGame(scene)
