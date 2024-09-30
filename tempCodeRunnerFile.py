
        messagebox.showinfo('showinfo','Enter Valid Numbers')

def check_three():
    global name
    name=''
    global area 
    global a,b,c
    a=e1.get()
    b=e2.get()
    c=e3.get()
    if a and b and c:
        try:
            a=int(a)
            b=int(b)
            c=int(c)
        except:
            messagebox.showinfo('showinfo','Enter Integers')