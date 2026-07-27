def equilateral(sides):
    return triangle(sides) and sides[0]==sides[1] and sides[1]==sides[2]


def isosceles(sides):
    return triangle(sides) and (sides[0]==sides[1] or sides[0]==sides[2] or sides[1]==sides[2])


def scalene(sides):
    return not equilateral(sides) and not isosceles(sides) and triangle(sides)

def triangle(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    return (a+b>=c) and (b+c>=a) and (a+c>=b) and not(a==b==c==0)