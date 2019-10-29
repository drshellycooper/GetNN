# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 12:18:17 2019

@author: Hilmi
"""

import random 
def GetNN1D(A,k1, P0, RN,RP):
    A[RP] = 0
    if(k1 > 0): 
        if(RP == 0):
            NN = 1
            if(A[1] == 1):
                A[1] = 0
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[1] = 1
                P0[RN] = 1
        elif(RP == len(A) - 1):
            NN = len(A) - 2
            if(A[NN] == 1):
                A[NN] = 0
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN] = 1
                P0[RN] = NN
        else:
            val = random.randint(1, 2) 
            if val == 1:    # Left-border travelling right
                NN = RP + 1
            elif val == 2:  # Left-border travelling up
                NN = RP - 1
                
            if(A[NN] == 1):
                A[NN] = 0
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN] = 1
                P0[RN] = NN  
        return(k1, A, P0 )
    elif(k1 == 0):
        return(k1, A, 0)
    else:
        print('For some reason the number of particles went below in the nearest neighbour phase, changing it to 0')
        return(0,A,0)
            
def GetNN2D(A,B,G, RPx, RPy, k1, P0, RN):
    A[RPx,RPy]= 0 # Assuming continuous lattices, meaning that no particle is trapped in one point
    if(k1 > 0): 
        if(B[RPx,RPy] == 1):
            val = random.randint(1, 3) 
            if val == 1:    # Left-border travelling right
                NN = [RPx+1,RPy]
            elif val == 2:  # Left-border travelling up
                NN = [RPx,RPy+1]
            elif val == 3:  # Left-border travelling down
                NN = [RPx,RPy-1]  
            if(A[NN[0],NN[1]] ==1):
                A[NN[0],NN[1]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1]] =1
                P0[RN] = NN    
                
        elif(B[RPx,RPy] == 2):
            val = random.randint(1, 3) 
            if val == 1:    # Right-border travelling left
                NN = [RPx-1,RPy]
            elif val == 2:  # Right-border travelling up
                NN = [RPx,RPy+1]
            elif val == 3:  # Right-border travelling down
                NN = [RPx,RPy-1]
            if(A[NN[0],NN[1]] ==1):
                A[NN[0],NN[1]] =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1]] =1
                P0[RN] = NN
                
        elif(B[RPx,RPy] == 3):    
            val = random.randint(1, 3) 
            if val == 1:    # Left-border travelling right
                NN = [RPx+1,RPy]
            elif val == 2:  # Left-border travelling up
                NN = [RPx-1,RPy]
            elif val == 3:  # Left-border travelling down
                NN = [RPx,RPy+1]
            if(A[NN[0],NN[1]] ==1):
                A[NN[0],NN[1]] =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1]] =1
                P0[RN] = NN
                
        elif(B[RPx,RPy] == 4):        
            val = random.randint(1, 3) 
            if val == 1:    # Left-border travelling right
                NN = [RPx+1,RPy]
            elif val == 2:  # Left-border travelling up
                NN = [RPx-1,RPy]
            elif val == 3:  # Left-border travelling down
                NN = [RPx,RPy-1]
            if(A[NN[0],NN[1]] ==1):
                A[NN[0],NN[1]] =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1]] =1
                P0[RN] = NN
        elif(B[RPx,RPy] == 5):    
            val = random.randint(1, 2) 
            if val == 1:    # Top left corner going right
                NN = [RPx+1,RPy]
            elif val == 2:  #  Top left corner going down
                NN = [RPx,RPy+1] 
            if(A[NN[0],NN[1]] ==1):
                A[NN[0],NN[1]] =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1]] =1
                P0[RN] = NN
                
        elif(B[RPx,RPy] == 6):        
            val = random.randint(1, 2) 
            if val == 1:    # Bottom- Left corner going right
                NN = [RPx+1,RPy]
            elif val == 2:  # Left-border travelling up
                NN = [RPx,RPy-1]
            if(A[NN[0],NN[1]] ==1):
                A[NN[0],NN[1]] =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1]] =1
                P0[RN] = NN    
        elif(B[RPx,RPy] == 7):        
            val = random.randint(1, 2) 
            if val == 1:    # Top-Right corner going left
                NN = [RPx-1,RPy]
            elif val == 2:  # Top - right corner going down
                NN = [RPx,RPy+1]
            if(A[NN[0],NN[1]] ==1):
                A[NN[0],NN[1]] =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1]] =1
                P0[RN] = NN
     
        elif(B[RPx,RPy] == 8):        
            val = random.randint(1, 2) 
            if val == 1:    # Top-Right corner going left
                NN = [RPx-1,RPy]
            elif val == 2:  # Top - right corner going down
                NN = [RPx,RPy-1]
            if(A[NN[0],NN[1]] ==1):
                A[NN[0],NN[1]] =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1]] =1
                P0[RN] = NN  
                               
        elif(isinstance(G,int) == False):
            if(G[RPx,RPy] == 1):
                val = random.randint(1, 3) 
                if val == 1:    # Left-border travelling right
                    NN = [RPx+1,RPy]
                elif val == 2:  # Left-border travelling up
                    NN = [RPx,RPy+1]
                elif val == 3:  # Left-border travelling down
                    NN = [RPx,RPy-1]  
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]]  =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN    
                    
            elif(G[RPx,RPy] == 2):
                val = random.randint(1, 3) 
                if val == 1:    # Right-border travelling left
                    NN = [RPx-1,RPy]
                elif val == 2:  # Right-border travelling up
                    NN = [RPx,RPy+1]
                elif val == 3:  # Right-border travelling down
                    NN = [RPx,RPy-1]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN
                    
            elif(G[RPx,RPy] == 3):    
                val = random.randint(1, 3) 
                if val == 1:    # Left-border travelling right
                    NN = [RPx+1,RPy]
                elif val == 2:  # Left-border travelling up
                    NN = [RPx-1,RPy]
                elif val == 3:  # Left-border travelling down
                    NN = [RPx,RPy+1]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN
                    
            elif(G[RPx,RPy] == 4):        
                val = random.randint(1, 3) 
                if val == 1:    # Left-border travelling right
                    NN = [RPx+1,RPy]
                elif val == 2:  # Left-border travelling up
                    NN = [RPx-1,RPy]
                elif val == 3:  # Left-border travelling down
                    NN = [RPx,RPy-1]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN
            elif( G[RPx,RPy] == 5):    
                val = random.randint(1, 2) 
                if val == 1:    # Top left corner going right
                    NN = [RPx+1,RPy]
                elif val == 2:  #  Top left corner going down
                    NN = [RPx,RPy+1] 
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN
                    
            elif(G[RPx,RPy] == 6):        
                val = random.randint(1, 2) 
                if val == 1:    # Bottom- Left corner going right
                    NN = [RPx+1,RPy]
                elif val == 2:  # Left-border travelling up
                    NN = [RPx,RPy-1]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN    
            elif(G[RPx,RPy] == 7):        
                val = random.randint(1, 2) 
                if val == 1:    # Top-Right corner going left
                    NN = [RPx-1,RPy]
                elif val == 2:  # Top - right corner going down
                    NN = [RPx,RPy+1]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN
         
            elif(G[RPx,RPy] == 8):        
                val = random.randint(1, 2) 
                if val == 1:    # Top-Right corner going left
                    NN = [RPx-1,RPy]
                elif val == 2:  # Top - right corner going down
                    NN = [RPx,RPy-1]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN 
                     
            elif(G[RPx,RPy] == 9):        
                NN = [RPx,RPy + 1]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN  
                    
            elif(G[RPx,RPy] == 10):        
                NN = [RPx,RPy - 1]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN  
                    
            elif(G[RPx,RPy] == 11):        
                NN = [RPx + 1,RPy]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN  
                    
            elif(G[RPx,RPy] == 12):        
                NN = [RPx - 1,RPy]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN  

            elif(G[RPx,RPy] == 13):        
                val = random.randint(1, 2) 
                if val == 1:    # Top-Right corner going left
                    NN = [RPx,RPy-1]
                elif val == 2:  # Top - right corner going down
                    NN = [RPx,RPy+1]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN

            elif(G[RPx,RPy] == 14):        
                val = random.randint(1, 2) 
                if val == 1:    # Top-Right corner going left
                    NN = [RPx+1,RPy]
                elif val == 2:  # Top - right corner going down
                    NN = [RPx-1,RPy]
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN
            
            else:     # Not on any boundary
                val = random.randint(1, 4) 
                if val == 1:    # 
                    NN = [RPx+1,RPy]
                elif val == 2:  #
                    NN = [RPx-1,RPy]
                elif val == 3:  # 
                    NN = [RPx,RPy+1]
                else:
                    NN = [RPx, RPy-1]
                A[RPx,RPy]= 0  # Should this be 0 or something else to keep track of it ?
                if(A[NN[0],NN[1]] ==1):
                    A[NN[0],NN[1]] =0 
                    k1 -= 2
                    del P0[RN]
                    P0.remove(NN)
                else:
                    A[NN[0],NN[1]] =1
                    P0[RN] = NN    
        else:     # Not on any boundary
            val = random.randint(1, 4) 
            if val == 1:    # 
                NN = [RPx+1,RPy]
            elif val == 2:  #
                NN = [RPx-1,RPy]
            elif val == 3:  # 
                NN = [RPx,RPy+1]
            else:
                NN = [RPx, RPy-1]
            A[RPx,RPy]= 0  # Should this be 0 or something else to keep track of it ?
            if(A[NN[0],NN[1]] ==1):
                A[NN[0],NN[1]] =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1]] =1
                P0[RN] = NN                                                                
        return(k1, A, P0 )
    elif(k1 == 0):
        return(k1, A, 0)
    else:
        print('For some reason the number of particles went below 0 in the GetNN phase, changing it to 0')
        return(0,A,0)
                
def GetNN3D(A,B,RPx,RPy,RPz,k1,P0,RN):     
    if(k1 > 0): 
        if(B[RPx,RPy,RPz] == 1):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 5):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
                
        elif(B[RPx,RPy,RPz] == 2):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 5):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
                
        elif(B[RPx,RPy,RPz] == 3):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx -1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 5):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 4):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx -1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 5):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 5):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1 ,RPy , RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 5):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
     
        elif(B[RPx,RPy,RPz] == 6):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1 ,RPy , RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 5):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
     
        elif(B[RPx,RPy,RPz] == 7):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
      
        elif(B[RPx,RPy,RPz] == 8):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
       
        elif(B[RPx,RPy,RPz] == 9):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
     
        elif(B[RPx,RPy,RPz] == 10):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 11):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 12):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx ,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
                
        elif(B[RPx,RPy,RPz] == 13):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 14):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 15):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 16):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 17):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 18):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 19):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 20):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 21):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 22):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 23):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 24):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 25):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 26):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
        else:
            val = random.randint(1, 6) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx -1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 5):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 6):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
        return(k1, A, P0 )    
    elif(k1 == 0):
        return(k1, A, 0)
    else:
        print('For some reason the number of particles went below 0 in the GetNN phase, changing it to 0')
        return(0,A,0)

def GetNN3DSphere(A,B,G,RPx,RPy,RPz,k1,P0,RN):     
    if(k1 > 0): 
        if(B[RPx,RPy,RPz] == 1 or G[RPx,RPy,RPz] == 1 ):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 5):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
                
        elif(B[RPx,RPy,RPz] == 2 or G[RPx,RPy,RPz] == 2):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 5):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
                
        elif(B[RPx,RPy,RPz] == 3 or G[RPx,RPy,RPz] == 3):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx -1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 5):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 4 or G[RPx,RPy,RPz] == 4):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx -1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 5):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 5 or G[RPx,RPy,RPz] == 5):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1 ,RPy , RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 5):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
     
        elif(B[RPx,RPy,RPz] == 6 or G[RPx,RPy,RPz] == 6):
            val = random.randint(1, 5) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1 ,RPy , RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 5):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
     
        elif(B[RPx,RPy,RPz] == 7 or G[RPx,RPy,RPz] == 7):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
      
        elif(B[RPx,RPy,RPz] == 8 or G[RPx,RPy,RPz] == 8):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
       
        elif(B[RPx,RPy,RPz] == 9 or G[RPx,RPy,RPz] == 9):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
     
        elif(B[RPx,RPy,RPz] == 10 or G[RPx,RPy,RPz] == 10):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 11 or G[RPx,RPy,RPz] == 12):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 12 or G[RPx,RPy,RPz] == 11):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx ,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
                
        elif(B[RPx,RPy,RPz] == 13 or G[RPx,RPy,RPz] == 13):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 14 or G[RPx,RPy,RPz] == 14):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 15 or G[RPx,RPy,RPz] == 15):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 16 or G[RPx,RPy,RPz] == 16):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 17 or G[RPx,RPy,RPz] == 17):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 18 or G[RPx,RPy,RPz] == 18):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 19 or G[RPx,RPy,RPz] == 19):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 20 or G[RPx,RPy,RPz] == 20):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 21 or G[RPx,RPy,RPz] == 21):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 22 or G[RPx,RPy,RPz] == 22):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 23 or G[RPx,RPy,RPz] == 23):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 24 or G[RPx,RPy,RPz] == 24):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 25 or G[RPx,RPy,RPz] == 25):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
    
        elif(B[RPx,RPy,RPz] == 26 or G[RPx,RPy,RPz] == 26):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx - 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
        elif(G[RPx,RPy,RPz] == 27):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx ,RPy + 1, RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN   
        elif(G[RPx,RPy,RPz] == 28):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx ,RPy + 1, RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN                            
        elif(G[RPx,RPy,RPz] == 29):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx ,RPy - 1, RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN                            
        elif(G[RPx,RPy,RPz] == 30):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx ,RPy - 1, RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN      
                
        elif(G[RPx,RPy,RPz] == 31):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx + 1 ,RPy , RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN                     
        elif(G[RPx,RPy,RPz] == 32):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx + 1 ,RPy , RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN                   
                
        elif(G[RPx,RPy,RPz] == 33):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx - 1 ,RPy , RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz + 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN                   
                
        elif(G[RPx,RPy,RPz] == 34):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx - 1 ,RPy , RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN                   
                
        elif(G[RPx,RPy,RPz] == 35):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx + 1 ,RPy , RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN                  

        elif(G[RPx,RPy,RPz] == 36):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx + 1 ,RPy , RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN                        
                
        elif(G[RPx,RPy,RPz] == 37):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx - 1 ,RPy , RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN                        
                
        elif(G[RPx,RPy,RPz] == 38):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx - 1 ,RPy , RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN  
                      
        elif(G[RPx,RPy,RPz] == 39):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx ,RPy + 1 , RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]                
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN

        elif(G[RPx,RPy,RPz] == 40):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx+1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx-1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]
            elif(val == 4):  
                NN = [RPx,RPy, RPz - 1]                
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN         

        elif(G[RPx,RPy,RPz] == 41):
            val = random.randint(1, 4) 
            if(val == 1):    
                NN = [RPx ,RPy + 1 , RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 3):  
                NN = [RPx + 1,RPy, RPz]
            elif(val == 4):  
                NN = [RPx - 1,RPy, RPz]                
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN         

        elif(G[RPx,RPy,RPz] == 42):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx ,RPy, RPz + 1]
            elif(val == 2):  
                NN = [RPx,RPy, RPz - 1]             
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN         

        elif(G[RPx,RPy,RPz] == 43):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx ,RPy + 1, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]             
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN       

        elif(G[RPx,RPy,RPz] == 44):
            val = random.randint(1, 2) 
            if(val == 1):    
                NN = [RPx + 1 ,RPy, RPz]
            elif(val == 2):  
                NN = [RPx - 1,RPy, RPz]             
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN       

        elif(G[RPx,RPy,RPz] == 45):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx ,RPy + 1, RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz + 1]  
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN       

        elif(G[RPx,RPy,RPz] == 46):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx ,RPy - 1, RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz + 1]  
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN    

        elif(G[RPx,RPy,RPz] == 47):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx ,RPy + 1, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]  
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN    

        elif(G[RPx,RPy,RPz] == 48):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx ,RPy + 1, RPz]
            elif(val == 2):  
                NN = [RPx,RPy - 1, RPz]  
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN    

        elif(G[RPx,RPy,RPz] == 49):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx +1 ,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz + 1]  
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN    

        elif(G[RPx,RPy,RPz] == 50):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx -1 ,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy, RPz + 1]  
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN    

        elif(G[RPx,RPy,RPz] == 51):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx +1 ,RPy, RPz]
            elif(val == 2):  
                NN = [RPx -1,RPy, RPz]  
            elif(val == 3):  
                NN = [RPx,RPy, RPz + 1]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN    

        elif(G[RPx,RPy,RPz] == 52):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx +1 ,RPy, RPz]
            elif(val == 2):  
                NN = [RPx -1,RPy, RPz]  
            elif(val == 3):  
                NN = [RPx,RPy, RPz - 1]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN    

        elif(G[RPx,RPy,RPz] == 53):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx +1 ,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]  
            elif(val == 3):  
                NN = [RPx,RPy -1, RPz]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN    

        elif(G[RPx,RPy,RPz] == 54):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx -1 ,RPy, RPz]
            elif(val == 2):  
                NN = [RPx,RPy + 1, RPz]  
            elif(val == 3):  
                NN = [RPx,RPy -1, RPz]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN    

        elif(G[RPx,RPy,RPz] == 55):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx +1 ,RPy, RPz]
            elif(val == 2):  
                NN = [RPx -1,RPy, RPz]  
            elif(val == 3):  
                NN = [RPx,RPy +1, RPz]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN    

        elif(G[RPx,RPy,RPz] == 56):
            val = random.randint(1, 3) 
            if(val == 1):    
                NN = [RPx +1 ,RPy, RPz]
            elif(val == 2):  
                NN = [RPx -1,RPy, RPz]  
            elif(val == 3):  
                NN = [RPx,RPy -1, RPz]                   
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN    
                
        else:
            val = random.randint(1, 6) 
            if(val == 1):    
                NN = [RPx + 1,RPy, RPz]
            elif(val == 2):  
                NN = [RPx -1,RPy, RPz]
            elif(val == 3):  
                NN = [RPx,RPy + 1, RPz]
            elif(val == 4):  
                NN = [RPx,RPy - 1, RPz]
            elif(val == 5):  
                NN = [RPx,RPy, RPz + 1]
            elif(val == 6):  
                NN = [RPx,RPy, RPz - 1]
            A[RPx,RPy,RPz] = 0  
            if(A[NN[0],NN[1],NN[2]] ==1):
                A[NN[0],NN[1],NN[2]]  =0 
                k1 -= 2
                del P0[RN]
                P0.remove(NN)
            else:
                A[NN[0],NN[1],NN[2]] =1
                P0[RN] = NN
        return(k1, A, P0 )    
    elif(k1 == 0):
        return(k1, A, 0)
    else:
        print('For some reason the number of particles went below 0 in the GetNN phase, changing it to 0')
        return(0,A,0)        
        
