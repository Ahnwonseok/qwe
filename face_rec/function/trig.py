import math

def trig(point_1,point_2):# cp가 1이면 반시계방향 회전 -1이면 시계 방향 회전
    x1=point_1[0]
    y1=point_1[1]
    x2=point_2[0]
    y2=point_2[1]

    a=abs((x2-x1))
    b=abs((y2-y1))
    c= math.sqrt(math.pow(a,2)+math.pow(b,2))

    cos=(math.pow(b,2)+math.pow(c,2)-math.pow(a,2))/(2*b*c)

    if y1>=y2:
        direction= -1
    else:
        direction= 1

    return cos,direction