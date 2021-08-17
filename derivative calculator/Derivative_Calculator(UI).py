# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 10:17:13 2021

@author: Hamza
"""
import tkinter as tk
from derivative_calculator import derivation
from tkinter import filedialog, ttk
import os



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

