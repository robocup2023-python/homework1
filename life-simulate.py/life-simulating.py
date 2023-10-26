import numpy as np
import random
class Universe:
    def __init__(self,height=10,width=10) -> None:
        self.height=height
        self.width=width
        self.array=np.full((height,width),' ')
    def Show(self):
        for i in range(self.array.shape[0]):
            for j in range(self.array.shape[1]):
                if self.array[i,j]=="*":
                    print("*",end="")
                else:
                    print(" ",end="")
            print()
    def Seed(self):
        count=0
        count_final=self.height*self.width//4
        while count<count_final:
            index=random.randint(0,self.height*self.width-1)
            index_row=index//self.width
            index_column=index-index_row*self.width
            if self.array[index_row,index_column]!="*":
                self.array[index_row,index_column]="*"
                count+=1
    def Counting(self,y_origin,x_origin):
        xl=x_origin-1;xr=x_origin+1;yl=y_origin-1;yr=y_origin+1
        if xl<0:xl+=1
        if xr>=self.width:xr-=1
        if yl<0:yl+=1
        if yr>=self.height:yr-=1
        amount=0
        for i in range(xl,xr+1):
            for j in range(yl,yr+1):
                if self.array[j,i]=="*":
                    amount+=1
        if self.array[y_origin,x_origin]=="*":
            amount-=1

        return amount
    def Next(self):
        self.array_bool=self.array.copy()
        for i in range(self.array.shape[0]):
            for j in range(self.array.shape[1]):
                number_of_survivors=self.Counting(i,j)
                if self.array[i,j]=='*':
                    if number_of_survivors<=1 or number_of_survivors>=4:
                        self.array_bool[i,j]=' '
                    elif number_of_survivors<=3 and number_of_survivors>=2:
                        self.array_bool[i,j]='*'
                elif self.array[i,j]==' ':
                    if number_of_survivors==3:
                        self.array_bool[i,j]='*'
                    else:
                        self.array_bool[i,j]=' '
    def Rebuild(self):
        self.Next()
        self.array=self.array_bool

import time
import IPython
if __name__ =="__main__":
    world=Universe()
    world.Seed()
    world.Show()
    boola=input("PRINT yes TO BEGIN YOUR GAME:")
    print("\033c")
    if boola=="yes":
        while True:
            world.Rebuild()          
            world.Show()           
            time.sleep(2)
            print('\033c')
    