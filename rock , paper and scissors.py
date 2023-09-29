n1=input("enter the name of player1 : ")
n2=input("enter the name of player2 : ")
times=int(input("Number of times "))
s1=0
s2=0
x=1
print("""enter
r --> rock
s-->Scissors 
p--> paper""")
while(x<=times):
    p1=input("palyer 1 choice : ")
    p2=input("palyer 2 choice : ")

    if p1=="r" and p2=="s":
        s1+=1
    elif p1=="s" and p2=="r":
        s2+=1
    elif p1=="r" and p2=="p":
        s2+=1
    elif p1=="p" and p2=="r":
        s1+=1
    elif p1=="p" and p2=="s":
        s2+=1
    elif p1=="s" and p2=="p":
        s1+=1
    x+=1
    
#**************************************************************************************************
if s1>s2:
    print(n1, " is win")
elif s1<s2:
    print(n2 , " is win")
else:
    print("tie")