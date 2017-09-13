from getlastlines import getlastlines

def getinformation(filename, lines):
    """Devuelve la informacion ya procesada de las lineas dadas del archivo en cuestion"""
    array = getlastlines(filename, lines)

    temperature = 0
    humidity = 0
    pressure = 0
    wind = 0
    size = len(array)

    for i in range(0, size):
        values = array[i].split('|')
        temperature += float(values[0])
        humidity += float(values[1])
        pressure += float(values[2])
        wind += float(values[3])

    values = array[size - 1].split('|')
    return [float(values[0]), float(values[1]), float(values[2]), float(values[3]),
            round(temperature / size, 2), round(humidity / size, 2), round(pressure / size, 2),
            round(wind / size, 2)]
