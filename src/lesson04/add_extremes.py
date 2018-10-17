def addExtremes(n1, n2, n3):
    smallest = n1
    largest = n1
    
    if (n2 < smallest):
        smallest = n2
    if (n3 < smallest):
        smallest = n3

    if (n2 > largest):
        largest = n2
    if (n3 > largest):
        largest = n3

    return smallest + largest

n1 = int(input("enter n1: "))
n2 = int(input("enter n2: "))
n3 = int(input("enter n3: "))
answer = addExtremes(n1, n2, n3)
print(answer)
