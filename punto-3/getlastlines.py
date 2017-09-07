def getlastlines( filename, lines ):
    #size=quantity of lines
    size=0 
    #array to return
    array = []
    f = open (filename,"r")
    for i, l in enumerate(f):
        pass
    size=i+1
    f.seek(0,0)
    start=0
    end=0
    if size > lines:
        for x in range(0,(size-lines)):
            f.readline() 
        start=size-lines
        end=size
    else:
        start=0
        end=size
    for x in range(start,end):
        aux = f.readline()
        array.append(aux[0:len(aux)-1])
    f.close()
    return array
