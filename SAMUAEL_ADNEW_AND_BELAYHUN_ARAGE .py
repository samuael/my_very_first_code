## group members  SAMUAEL ADNEW  ATR/0631/10
##                BELAYHUN ARAGE ATR/0950/10
# WE USE THE TURTLE SCREEN TO USE THE THE FOUR DIRECTIO KEYS
## AND WE IMPORTED THE RANDOM MODULE TO PRODUCE A RANDOM NUMBERS IN THE MOVEMENT OF THE KEYS

import random
import turtle
s=turtle.Screen()

n=eval(input("enter the ORDER OF THE MATRIX::"))
box=[[0]*n for i in range(n)]

choose2=[2,2,2,4]
over=1

row1=random.randint(0,n-1)
col1=random.randint(0,n-1)
box[row1][col1]=random.choice(choose2)
c=False
print("________________________________________________")
def generate_random_num(box):## this function randomly generates a random number
    c=False
    i_in=[]
    j_in=[]
    for i in range(n):
        for j in range(n):
            if box[i][j]==0:
                c=True
                i_in.append(i)
                j_in.append(j)

    if c:
        if len(i_in)>1:            
            m=len(i_in)
            c=random.randint(0,m-1)
            row2=i_in[c]
            col2=j_in[c]
            
            box[row2][col2]=random.choice(choose2)
        elif len(i_in)==1:
            row2=i_in[0]
            col2=j_in[0]
            box[row2][col2]=random.choice(choose2)
    
def show(box):## htis functiion shows the box or the matrix with the appropriate spacing
    for i in range(n):
        for j in range(n):
            print(format(box[i][j],"6d"),end="")
        print()
        print()
    print("_______________________________________________")

generate_random_num(box)
show(box)
        
def up_move(box): ## controls the up ward movement
    for k in range(n):
        for j in range(n):
            for i in range(n):
                if box[i][j]==0:
                    m=i
                    while m<n-1:
                        box[m][j]=box[m+1][j]
                        m+=1
                    box[m][j]=0
    
def up_merge(box): ## CONTROLS THE UP WARD MERGING OR THE UPWARD  ADDITION
    for j in range(n):
        for i in range(n-1):
            if box[i][j]==box[i+1][j]:
                box[i][j]=box[i][j]+box[i+1][j]
                e=i+1
                while e<n-1:
                    box[e][j]=box[e+1][j]
                    e+=1
                box[e][j]=0
    
    
def down_move(box):## controls the downward movement
    for l in range(n):
        for j in range(n):
            for i in range(n-1,-1,-1):
                if box[i][j]==0:
                    g=i
                    while g>0:
                        box[g][j]=box[g-1][j]
                        g-=1
                    box[g][j]=0
    
def down_merge(box):## CONTROLS THE DOWNWARD ADDITION OR  MERGING
    for j in range(n):
        for i in range(n-1,0,-1):
            if box[i][j]==box[i-1][j]:
                box[i][j]=box[i][j]+box[i-1][j]
                l=i-1
                while l>0:
                    box[l][j]=box[l-1][j]
                    l-=1
                box[l][j]=0
    
def left_move(box):## CONTROLS THE LEFT MOVEMENT
    for m in range(n):   # i use this funcion because of the zeros replace the place of preceeding element or zero::
        for i in range(n):
            for j in range(n):
                if box[i][j]==0:
                    c=j
                    while c<n-1:
                        box[i][c]=box[i][c+1]
                        c+=1
                    box[i][c]=0
    
def left_merge(box):## CONTROL THE LEFT MERGING OF THE MATRIX
    for i in range(n):
        for j in range(n-1):
            if box[i][j]==box[i][j+1]:
                box[i][j]=box[i][j]+box[i][j+1]
                c=j+1
                while c<n-2:
                    box[i][c]=box[i][c+1]
                    c+=1
                box[i][c]=0
    
def right_move(box):## CONTROL THE RIGHT MOVEMENT 
    for m in range(n):
        for i in range(n):
            for j in range(n-1,-1,-1):
                if box[i][j]==0:
                    c=j
                    while c>0:
                        box[i][c]=box[i][c-1]
                        c-=1
                    box[i][c]=0

    
def winn(box):## THIS DISPLAYS THE WINNING NOTIFICATION IF THE PLAYER REACHES  SCORE 2048
    for i in range(n):
        for j in box[i]:
            if j==2048:
                print("CONGRATULATION!! YOU WIN")
                break    
def right_merge(box):##MERGES TO THE RIGHT 
    for i in range(n):
        for j in range(n-1,0,-1):
            if box[i][j]==box[i][j-1]:
                box[i][j]=box[i][j]+box[i][j-1]
                c=j-1
                while c>0:
                    box[i][c]=box[i][c-1]
                    c-=1
                box[i][c]=0
def game_over(box):## RETURNS THE GAME OVER  NOTIFICATION WHEN THERE IS NO CHOICE OF MOVMENT
    ctr=0
    for i in range(n):
        for j in range(n):
            if box[i][j]==0:
                ctr+=1
                return ctr
                break
    if ctr<1:
        for i in range(n-1):
            for j in range(n-1):
                if box[i][j]==box[i][j+1] or box[i][j]==box[i+1][j]:
                    ctr+=1
                    
    if ctr<1:
        for i in range(n-1):
            if box[n-1][j]==box[n-1][j+1]:
                ctr+=1
                return ctr
    else:
        ctr=0
        print("GAME OVER .............")



 
    
    
        
def up():# controls the up ward operation
    up_move(box)
    up_merge(box)
    generate_random_num(box)
    show(box)
    winn(box)
    game_over(box)
   
    
def down():
    down_move(box)
    down_merge(box)
    generate_random_num(box)
    game_over(box)
    show(box)
    winn(box)
    
def left():
    left_move(box)
    left_merge(box)
    generate_random_num(box)
    show(box)
    winn(box)
    game_over(box)
    
def right():
    right_move(box)
    right_merge(box)
    generate_random_num(box)
    show(box)
    winn(box)
    game_over(box)
    
    
s.onkey(up,"Up")
s.onkey(down,"Down")
s.onkey(left,"Left")
s.onkey(right,"Right")
s.listen()
s.mainloop()
            
    

        
        

        
        
