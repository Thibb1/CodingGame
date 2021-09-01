I=input
gymnasts={ i : [0, 0, 0] for i in I().split(",") }
categories=I().split(",")
n=int(I())
for i in range(n):
    row=I().split(",")
    if row[0] in gymnasts:
        if float(row[1]) > gymnasts[row[0]][0]:
            gymnasts[row[0]][0]=float(row[1])
        if float(row[2]) > gymnasts[row[0]][1]:
            gymnasts[row[0]][1]=float(row[2])
        if float(row[3]) > gymnasts[row[0]][2]:
            gymnasts[row[0]][2]=float(row[3])
for gymnast in gymnasts:
    if "bars" in categories:
        print("%g" %gymnasts[gymnast][0],end="")
        if "beam" in categories or "floor" in categories:
            print(",",end="")
    if "beam" in categories:
        print("%g" %gymnasts[gymnast][1],end="")
        if "floor" in categories:
            print(",",end="")
    if "floor" in categories:
        print("%g" %gymnasts[gymnast][2],end="")
    print()
