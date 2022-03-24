from turtle import*
def trait(longueur_cote):
    if longueur_cote<5:
        forward(longueur_cote/3)
        left(360/-6)
        forward(longueur_cote/3)
        left(360/3)
        forward(longueur_cote/3)
        left(360/-6)
        forward(longueur_cote/3)
    else:
        trait(longueur_cote/3)
        left(360/-6)
        trait(longueur_cote/3)
        left(360/3)
        trait(longueur_cote/3)
        left(360/-6)
        trait(longueur_cote/3)

def triangle():
    l = 200
    left(360/-6)
    trait(l)
    left(360/3)
    trait(l)
    left(360/3)
    trait(l)


triangle()
done()