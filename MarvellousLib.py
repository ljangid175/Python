
def filterX(Task, Elements):
    result = list()

    for no in Elements:
        ret = Task(no)  
        if(ret == True):
            result.append(no)
    
    return result

def mapX(Task,Elements):
    result = list()

    for no in Elements:
        ret = Task(no)  
        result.append(ret)

    return result

def reduceX(Task,Elements):
    sum = 0
    
    for no in Elements:
        sum = Task(sum, no)

    return sum
