from tkinter import *
root = Tk()
root.geometry("380x550")
ent1 = Entry(root,font = 'verdana 14 bold ', width  = 22 ,justify=RIGHT , bd = 6, bg="#ebe6fa")
ent1.insert(0,'0')
ent1.place(x = 30,y = 10)
button_no = []
def get_no(x):
    if ent1.get()=='0':
        ent1.delete(0,'end')
        ent1.insert(0,str(x))
    else:
        length=len(ent1.get())
        ent1.insert(length,str(x))
def clear():
    ent1.delete(0,'end')
    ent1.insert(0,'0')

def delete():
    ent1.delete(len(ent1.get())-1,'end')
    if ent1.get()=='':
        ent1.insert(0,'0')
        
def insert_dot():
    ent1.insert(len(ent1.get()),'.')
    
"""
def plus():
    if ent1.get() != '0':
        ent1.insert(len(ent1.get()),'+')
"""
def enter(x):
    if ent1.get() != '0':
        length = len(ent1.get())
        all_text = ent1.get()
        last_character = all_text[-1:]
        if last_character in ["+","-","/"] or all_text[-2:]=="**":
            pass
        else:
             ent1.insert(length,but1[x]['text'])
result2 = []
history = []
def equal():
    variable= ent1.get()
    result = eval(variable)
    result2.insert(0,result)
    #print(result2)
    ent1.delete(0,'end')
    ent1.insert(0,result)
    history.insert(0,variable)
    #history.append(variable)
    #history.reverse()
    status.configure(text="History \n " +'\n'.join(history[0:5]),font = 'verdane 11 bold ' )
    return result
"""
def enter_dot(x):
    if ent1.get() != '0':
        length = len(ent1.get())
        ent1.insert(length,x)
""" 
for i  in range(10):
    button_no.append(Button(width = 4,text = str(i),bd = 6,command = lambda x = i : get_no(x)))
button_text = 1
for i in range (0,3):
    for j in range (0,3):
        button_no[button_text].place(x=30+j*90,y=70+i*70)
        button_text+=1
button_zero = Button(root,text="0",width=30,bd=6, command = lambda x =0 : get_no(x))
button_zero.place(x=30,y=280)

but1 = []
for i in range (4):
    but1.append(Button(width=5,bd = 6,command=lambda x = i: enter(x)))
but1[0]['text']='+'
but1[1]['text']='-'
but1[2]['text']='*'
but1[3]['text']='/'
#but1[0]['command'] = plus
for i in range(4):
    but1[i].place(x=290,y=70+i*70)
button_clear= Button(root,text="C",bd=6,width=5,command = clear).place(x=30,y=340)
button_dot= Button(root,text=".",bd=6,width=5,command = insert_dot).place(x=110,y=340)
button_equal= Button(root,text="=",bd=6,width=5,command=equal).place(x=200,y=340)
button_del= Button(root,text="Del",bd=6,width=5,command=delete).place(x=290,y=340)
status =Label(root,text="History",height = 7,font = 'verdena 11 bold ',anchor = NW,relief = SUNKEN )
status.pack(side =BOTTOM ,fill = X)



"""
for utton in but1:
    Button(root,text = button,width=5, bd=6).place(x=290,y=70+a)
    a = a+70
but2=["C",".","="]
b = 0
for button2 in but2:
    Button(root,text = button2,width = 5,bd = 6).place(x = 30+b,y = 350)
    b = b+90
"""
root.resizable(0,0)

                     
root.mainloop()    



