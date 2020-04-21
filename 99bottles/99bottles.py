n = 9
while n>=1:
    if(n>1):
        print(str(n) + " bottles of beer on the wall, " + str(n) + " bottles of beer.")
        n-=1
        print("take one down and pass it around, " + str(n) + " bottles of beer on the wall.\n\n")
    else:
        print(str(n) + " bottles of beer on the wall, " + str(n) + " bottle of beer.")
        n-=1
        print("take one down and pass it around, there are no bottles of beer on the wall.\n\n")
    pass
