I=input
length,height,asciiInput,letters,asciiBox=int(I()),int(I()),I(),[],[]
for _ in range(height):
    letters.append(I())
    asciiBox.append([])
for c in asciiInput:
    index = ord(c.capitalize()) - 65
    index = 26 if  index > 26 or index < 0 else index
    for y in range(height):
        asciiBox[y].append(letters[y][index*length:(index+1)*length])
for x in asciiBox:
    print(*x, sep="")
