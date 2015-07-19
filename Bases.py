

""" Functions dealing with different counting bases and strings """


def getStrChar(n):
    #for bases > 10
    if n < 10:
        return str(n)
    else:
        return chr(n+ 55)

def getNum(strng, base):
    base = int(base)
    result = 0
    power = 0
    for i in range(1, len(strng)+ 1):
        if strng[-i].isdigit():
            add = int(strng[-i])
        else:
            add = (ord(strng[-i]) - 55)
        if add >= base:
            raise OverflowError
        result += add * (base**power)
        power += 1
    return result

def getStr(n, base):
    base = int(base)
    result = ""
    if n == 0:
        return "0"
    while n != 0:
        remainder = n % base
        n = n//base
        result = getStrChar(remainder) + result
    return result

def getSequenceDisplay(base, incr, start, length, nCols, nRows):
    rows = []
    sequence = []
    n = start
    while len(sequence) < length:
        sequence.append(getStr(n, base))
        n += incr
    
    while len(rows) < nRows:
        thisRow = ""
        while len(thisRow) < nCols:
            #add next number and space if they fit
            if len(sequence) == 0 or len(thisRow + " " + sequence[0]) > nCols:
                thisRow += " " * (nCols - len(thisRow))
            else:
                thisRow += " " + sequence[0]
                sequence.remove(sequence[0])
        rows.append(thisRow)
    return rows
                
def getSequenceStr(base, incr, start, length):
    result = ""
    for n in range(start, incr*length + start, incr): 
        result += getStr(n, base)
        n += incr
    return result




    
