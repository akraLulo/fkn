# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define v = Character("Victoria", image="vic") #when Elizabeth arrives, the 'tired' portrait appears instead of the image
#that she had of her before her Obsession
define a = Character("Abel", image="abel")
## Might change this so that it BECOMES abel after some interactions--could also have a placeholder that's just the
## ??? or Creation for a few of the first scenes.
define e = Character("Elizabeth", image="eliza")
define h = Character("Henry", image="henry")

##remember to use monologue mode

###image declarations###
#group sides right under their normals, for legibility
#yes the sides will be convuluted. shut up
image vic = "vic.jpg"
image side vic = "side vic.png"
image vic tired = "vic.jpg"
image side vic tired = "side vic tired.png"
image vic smile = "vic.jpg"
image side vic smile = "side vic smile.png"
image vic happy = "vic.jpg"
image side vic happy = "side vic happy.png"
image vic cry = "vic.jpg"
image side vic cry = "side vic cry.png"

image vic young = "vic young.jpg"


image henry = "henry.jpg"
image eliza = "eliza.jpg"
image abel = "abel.jpg"
image abel 1 = "abel 1.jpg"
image abel 10 = "abel 10.jpg"


# The game starts here.

label start: #this is the testing block until need to lint the whole program!

    scene bg room

    show vic young
    v "I was youthful"

    show vic
    v "now i'm FKN tired."
    show vic tired
    v "Really. Fucking. Tired."
    hide vic

    show eliza
    e "I'm tired's sister."
    hide eliza

    show henry
    h "I take care of FKN tired."
    hide henry

    show abel
    a "I was created..."

    show abel 1
    a "goosterday."

    show abel 10
    a "i'm grewed up now."

    # This ends the game.

    return
