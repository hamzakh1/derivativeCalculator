# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:17:13 2021

@author: Hamza
"""
import tkinter as tk
from tkinter import filedialog, ttk
import os

def derivation(polynome):
#PART_1: extract elements from polynome
    separate = polynome.split() # extract elements from polynome
    sign = [i for i in separate if i == '+' or i =='-'] # extract signs
    monome_der_cmplx = [i for i in separate if 'cos' in i or 'sin' in i or 'ln' in i or 'log' in i]#extract cmplx monomes that are ready to be derivated
    monome_der = [i for i in separate if 'x' in i and i not in monome_der_cmplx] #extract monomes that are ready to be derivated

    exp = [i.rsplit('^') for i in monome_der if '^' in i ] # extract exponents from monomes

#PART_2 but a method
    def simple_derivation(monome_der,exp):
        der = []
        for i,j in enumerate(monome_der):
            if len(exp)-1 >= i: # to avoid 'list index out of range'
                extract_exp = [int(exp[i][0].replace('x',''))*int(exp[i][1]),int(exp[i][1])-1]  #first element of list is quotient * exponent and 2nd element is exponent-1, basically skeletons of derivation
                if extract_exp[1] != 1: # if exponent is 1 no need for '^'
                    der.append(str(extract_exp[0]) +'x^' + str(extract_exp[1]))
                else:
                    der.append(str(extract_exp[0]) +'x')
            if '^' not in j:
                if j[0] == 'x':
                    der.append('1')
                else:
                    der.append(j.replace('x','')) #since it has no exponent, x goes away
        return der

    def trigo(monome_der_cmplx):
    
        der_cmplx = []
        for i in monome_der_cmplx:
            if 'sin' in i:
                sign = ''
                outside = 'cos' # derivate the outside
                inside_to_be_der = str(i[3:]) #extract the inside of the trigo monome
                exp_trigo = [inside_to_be_der.rsplit('^') for j in inside_to_be_der if '^' in j] #separate the inside between the ^ to derivate it
                der_trigo = reassemble((simple_derivation(inside_to_be_der,exp_trigo)))[:1] #derivate and reassemble
                der_cmplx.append(sign + der_trigo + outside + inside_to_be_der)
            
            elif 'cos' in i:
                sign = '-'
                outside = 'sin'
                inside_to_be_der = str(i[3:])
                #repeat same code as sin (maybe turn it into a method)
                exp_trigo = [inside_to_be_der.rsplit('^') for j in inside_to_be_der if '^' in j]
                der_trigo = reassemble((simple_derivation(inside_to_be_der,exp_trigo)))[:1] 
                der_cmplx.append(sign + " " + der_trigo + outside + inside_to_be_der)
            
            elif 'ln' in i:
                der = "x^-1"
                inside_to_be_der = str(i[2:])
                if '^' in inside_to_be_der:
                    der_cmplx.append(inside_to_be_der[-1] + der)
                else:
                    der_cmplx.append(der)
                    
                
            
    
        
        return der_cmplx
    
    #PART_3: reassemble elements from derivated polynome
    def reassemble(der):
        der_poly = ""
        for i,j in enumerate(der):
            der_poly += j + " " 
            if i+1 < len(der):
                der_poly += sign[i] + " "
        return der_poly
    
    derive = simple_derivation(monome_der,exp) 
    derive2 = reassemble(trigo(monome_der_cmplx))
    final = reassemble(derive) + derive2  
    return final 

class MyWindow: #user interface
    def __init__(self, win):
        # Labels
        #self.lbl_op= tk.Label(win, text='Choose Operation')
        self.lbl_fv= tk.Label(win, text='ENTER POLYNOME:')
        #self.lbl_sv= tk.Label(win, text='Second Value')
        self.lbl_status= tk.Label(win, text='RESULT:')
        
        # stockage Input data

        
        self.t_fv= tk.Entry(win, width= 45, bd= 3)
        self.t_fv.insert(tk.INSERT, '2x^2 + 3x + cos2x^2 + ln2x^2 + x + lnx - 1') 
        
        
        self.t_status= tk.Entry(width= 45)
        
         # Poition   
        '''self.lbl_op.place(x=100, y=40)
        self.combo_op.place(x=260, y=40)'''
                
        self.lbl_fv.place(x=100, y=80)
        self.t_fv.place(x=260, y=80)
        
        '''self.lbl_sv.place(x=100, y=120)
        self.t_sv.place(x=260, y=120)'''
        
        self.b1= tk.Button(win, text='COMPUTE DERIVATION', command= self.Compute)
        self.btExit = tk.Button(win, text ="Close", command =self.Close)
        

        self.b1.place(x=300, y=170)
        
        
#        self.lbl_fn.place(x=100, y=200)
#        self.t_fn.place(x=260, y=200)
#        
#        self.lbl_nc.place(x=100, y=240)
#        self.t_nc.place(x=260, y=240) 
        
        self.lbl_status.place(x=100, y=250)
        self.t_status.place(x=180, y=250) 
        
        self.btExit.place(x=500, y=250)
    
        self.win= win
        
    def Compute(self):
        self.t_status.delete(0, 'end')
        
        #id_op= self.combo_op.get()
        fv= (self.t_fv.get())
        res = derivation(fv)
        
        self.t_status.insert(tk.END, str(res))
        self.b1["state"] = tk.NORMAL


        
    def Close(self):
        self.win.destroy()
        
        
        
if __name__ == "__main__":
    window= tk.Tk()
    mywin= MyWindow(window)
    window.title('DERIVATIVE CALCULATOR')
    window.geometry("650x340+10+10")
    window.mainloop()



'''#PART_3: reassemble elements from derivated polynome
der_poly = ""
for i,j in enumerate(der):
    der_poly += j + " " 
    if i+1 < len(der):
        der_poly += sign[i] + " "'''



#SIN,COS,LN,e,NEGATIVES, MULTIPLE DERIVATIVES TO DO

# INTEGRALS TO DO!

