a=list(input("enter:").split())
def unique(list):
    result = []          
    for item in list:     
        if list.count(item) == 1:  
            result.append(item)
    return result 

print(unique(a))
