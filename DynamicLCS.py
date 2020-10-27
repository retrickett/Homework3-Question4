#Rachel Trickett
#Dynamic Programming LCS Solution

#this function only returns LCS for entire length of both strings
#the number two represents diagonal arrow, number 1 represents up arrow
#number -1 represents left arrow
#these arrows are to rebuild how we got the length of the longest subsequence

def LCS(x,y):
    m=len(x)
    n=len(y)
    b=[]
    c=[]
    for i in range(0,m+1):
        new=[]
        for j in range(0,n+1):
            new.append(0)
        c.append(new)

    for i in range(0,m+1):
        new=[]
        for j in range(0,n+1):
            new.append(0)
        b.append(new)

    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                c[i][j]=c[i-1][j-1]+1
                b[i][j]=2 #remembers to back track diagonally

            elif c[i-1][j]>=c[i][j-1]:
                c[i][j]=c[i-1][j]
                b[i][j]=1 #remembers to back track up

            else:
                c[i][j]=c[i][j-1]
                b[i][j]=-1 #remembers to back track left 

    return c,b



def printLCS(b,x,i,j):
    if (i==0 or j==0):
        return
    if (b[i][j]==2):
        printLCS(b,x,i-1,j-1)
        print(x[i-1])
    elif(b[i][j]==1):
        printLCS(b,x,i-1,j)
    else:
        printLCS(b,x,i,j-1)



x=input("Enter a Word: ")
y=input("Enter another Word: ")

c=[]
b=[]

c,b=LCS(x,y)

#printing the table used to find the length of longest common subsequence
for i in range(0,len(x)+1):
    print(c[i])

printLCS(b,x,len(x),len(y))

