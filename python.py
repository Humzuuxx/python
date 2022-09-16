def circumf():
    r=int(input("radius:"))
    pie=3.14
    area=2*pie*r**2
    circ=2*pie*r
    return(circ,area)

ans=circumf()
print("The circumfrence and area of the circle=",ans)
