import turtle 

def numberOfPolygons(ans:str) -> int:
    num = 0
    for word in ans.split(' '):
        if word.startswith('P'):
            num += 1
    return num        

def parsePolygon(polyString:str) -> str:
    tempString = ''
    polySide = int(polyString.split(' ')[0][1:])
    polyLength = polyString.split(' ')[1]
    stringToRepeat = 'F' + polyLength + ' L' + str(360/polySide) + ' '
    for i in range(polySide):
        tempString += stringToRepeat
    return tempString[:-1] #Removes extra space at the end of string
    
def numberOfIterations(ans:str) -> int:
    num = 0
    for word in ans.split(' '):
        if word.startswith('I'):
            num += 1
    return num

def parseIteration(iterString:str) -> str:
    tempString = ''
    stringToRepeat = iterString.split(' ',1)[-1] + ' '
    iterAmount = int(iterString.split(' ')[0][1:])
    for i in range(iterAmount):
        tempString += stringToRepeat
    return tempString[:-1] #Removes extra space at the end of string
    
def evaluate(commandsLine:str):
    for command in commandsLine.split(' '):
        if command.startswith('F'):
            turtle.forward(int(command[1:]))
        elif command.startswith('B'):
            turtle.backward(int(command[1:]))
        elif command.startswith('L'):
            turtle.left(int(command[1:]))
        elif command.startswith('R'):
            turtle.right(int(command[1:]))
        elif command.startswith('C'):
            turtle.circle(int(command[1:]))
        elif command.startswith('D'):
            turtle.down()
        elif command.startswith('U'):
            turtle.up()
        else:
            pass
    
def readCommandLine(ans:str) -> str:
    replaceString = ''
    polyString = ''
    iterString = ''
    tempString = ans
    index = 0
    iCounter = 0
    #handling nested iterations
    #I2 I4 F100 L090 @ F100 @
    while numberOfIterations(tempString)>0:       
        for word in tempString.split(' '):
            if word.startswith('I'):
                iCounter += 1
            if word.startswith('@'):
                iterString = tempString[tempString.find('I',iCounter):tempString.find('@')-1]
                replaceString = parseIteration(iterString)
                break
        tempString = tempString.replace(iterString, replaceString)
        iCounter = 0
    while numberOfPolygons(tempString)>0:
        for word in tempString.split(' '):
            if word.startswith('P'):
                polyString = tempString[tempString.find('P'):(len(tempString.split(' ')[index]) + len(tempString.split(' ')[index + 1]) + 1)]
                replaceString = parsePolygon(polyString)
                break
            index += 1  
        tempString = tempString.replace(polyString, replaceString)
        index = 0    
    print('\n' + tempString)    
    evaluate(tempString)
        
if __name__ == '__main__':
    ans = input('Enter Tiny Turtle program (CMD+D or CTRL+D to terminate): \n')
    readCommandLine(ans)
    turtle.exitonclick()
