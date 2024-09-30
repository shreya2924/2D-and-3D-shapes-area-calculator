from tkinter import *
import math
from tkinter import messagebox
#import mysql.connector
#from PIL import ImageTk, Image
#E0DC1F
title_styles = {"font": ("Trebuchet MS Bold", 20), "background": "white",'fg':'black'}
title_styles2 = {"font": ("Trebuchet MS Bold", 20)}
font_styles = {"font": ("Bahnchschrift SemiLight SemiConde BOLD", 19), "background": "white"}
but = {"font": ("Trebuchet MS Bold", 20)}
property_font={'font':('ariel' ,19),'background':'#f4cac9','fg':'#D2042D'}


def back_btn():
    masters.destroy()
    mainn.destroy()
    mainmenu()


def main_menuu():
    roots.destroy()
    menuu()

def check_one():
    global name
    name=''
    global area 
    global a
    a=e1.get()
    if a:
        try:
            a=int(a)
        except:
            messagebox.showinfo('showinfo','Enter Integers')
        if type(a)==int :
            getting_one()  
    else:
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
        if type(a)==int and type(b)==int and type(c)==int :
            getting_three()  
    else:
        messagebox.showinfo('showinfo','Enter Valid Numbers')    

def check_two():
    global name
    name=''
    global area 
    global a,b
    a=e1.get()
    b=e1.get()
    if a and b :
        try:
            a=int(a)
            b=int(b)
        except:
            messagebox.showinfo('showinfo','Enter Integers')
        if type(a)==int and type(b)==int :
            getting_two()  
    else:
        messagebox.showinfo('showinfo','Enter Valid Numbers')          

    


def mainmenu():
    global masters
    masters=Tk()
    masters.title('Main Page')
    frms=Frame(masters, bg="#3fd7de", height=431, width=626).pack(fill='both',expand='true')
    masters.geometry('590x500')
    masters.resizable(0,0)
    l1=Label(masters,title_styles,text=".....Welcome to Area Calculator.....")
    l1.place(x=70,y=0)
    but1=Button(masters,font_styles,text='Start Calculating',command=menuu,height=4,width=15).place(x=170,y=75)
    but2=Button(masters,font_styles,text='EXIT',command=dead,height=4,width=15).place(x=170,y=240)
    masters.mainloop()
   
def dead(): 
    masters.destroy()

def twoD():
    global roots
    mainn.destroy()
    roots=Tk()
    roots.geometry('1300x650')
    frms=Frame(roots, bg="#3fd7de", height=431, width=626).pack(fill='both',expand='true')
    triangle=Button(roots,but,text="triangle",command=triangle_properties,height=6,width=16).place(x=90,y=60)
    square=Button(roots,but,text="square",command=square_properties,height=6,width=16).place(x=380,y=60)
    rectangle=Button(roots,but,text="rectangle",command=rectangle_properties,height=6,width=16).place(x=90,y=315)
    circle=Button(roots,but,text="circle",command=circle_properties,height=6,width=16).place(x=380,y=315)
    parallel=Button(roots,but,text="parallelogram",command=parallelogram_properties,height=6,width=16).place(x=670,y=60)
    trap=Button(roots,but,text="trapezium",command=trapezium_properties,height=6,width=16).place(x=670,y=315)
    rhom=Button(roots,but,text="rhombus",command=rhombus_properties,height=6,width=16).place(x=960,y=60)
    kite=Button(roots,but,text="kite",command=kite_properties,height=6,width=16).place(x=960,y=315)
    main_menu_button=Button(roots,text="main menu",command=main_menuu).place(x=626,y=580)
    roots.mainloop()
 
def sqr():
    root.destroy()
    global i
    i=0
    global e1
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 270, height = 240)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="SQUARE.png")      
    canvas.create_image(20,10, anchor=NW, image=img)
    Label(cu, text='Enter length of the side').place(x=0,y=200)
    e1 = Entry(cu)
    e1.place(x=150,y=200)
    calc=Button(cu,text="Calculate Area",command=check_one).place(x=155,y=250)
    cu.mainloop()

def rect():
    root.destroy()
    global i
    i=1
    global e1
    global e2
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 700, height = 600)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="RECTANGLE.png")      
    canvas.create_image(0,0, anchor=NW, image=img)
    Label(cu,text='Enter Length').place(x=0,y=200)
    Label(cu,text='Enter Breadth').place(x=0,y=230)
    e1 = Entry(cu)
    e1.place(x=100,y=200)
    e2 = Entry(cu)
    e2.place(x=100,y=230)
    calc=Button(cu,text="Calculate Area",command=check_two).place(x=155,y=250)
    cu.mainloop()
    
def tri():
    root.destroy()
    global i
    i=2
    global e1
    global e2
    global e3
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 300, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="Unknown.png")      
    canvas.create_image(20,0, anchor=NW, image=img)
    Label(cu, text='Enter side 1').place(x=0,y=200)
    Label(cu,text='Enter side 2').place(x=0,y=230)
    Label(cu,text='Enter side 3').place(x=0,y=260)
    e1 = Entry(cu)
    e1.place(x=100,y=200)
    e2 = Entry(cu)
    e2.place(x=100,y=230)
    e3 = Entry(cu)
    e3.place(x=100,y=260)
    calc=Button(cu,text="Calculate Area",command=check_three).place(x=155,y=280)
    cu.mainloop()

def rhomb():
    root.destroy()
    global i
    i=11
    global e1
    global e2
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 200, height = 200)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="RHOMBUS.png")      
    canvas.create_image(-185,-222, anchor=NW, image=img)
    Label(cu,text='Enter Diagonal 1').place(x=0,y=200)
    Label(cu,text='Enter Diagonal 2').place(x=0,y=230)
    e1 = Entry(cu)
    e1.place(x=100,y=200)
    e2 = Entry(cu)
    e2.place(x=100,y=230)
    calc=Button(cu,text="Calculate Area",command=check_two).place(x=155,y=250)
    cu.mainloop()
    
def circ():
    root.destroy()
    global i
    i=3
    global e1
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 300, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="CIRCLE.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    Label(cu, text='Enter radius').place(x=0,y=200)
    e1 = Entry(cu)
    e1.place(x=100,y=200)
    calc=Button(cu,text="Calculate Area",command=check_one).place(x=155,y=250)
    cu.mainloop()

def parallelogram():
    root.destroy()
    global i
    i=8
    global e1
    global e2
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 350, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="PARALLELOGRAM.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    Label(cu,text='Enter base').place(x=0,y=200)
    Label(cu,text='Enter height').place(x=0,y=230)
    e1 = Entry(cu)
    e1.place(x=100,y=200)
    e2 = Entry(cu)
    e2.place(x=100,y=230)
    calc=Button(cu,text="Calculate Area",command=check_two).place(x=155,y=250)
    cu.mainloop()

def trapezium():
    root.destroy()
    global i
    i=10
    global e1
    global e2
    global e3
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 300, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="TRAPEZIUM.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    Label(cu, text='Enter first side').place(x=0,y=200)
    Label(cu,text='Enter second side').place(x=0,y=230)
    Label(cu,text='Enter height').place(x=0,y=260)
    e1 = Entry(cu)
    e1.place(x=130,y=200)
    e2 = Entry(cu)
    e2.place(x=130,y=230)
    e3 = Entry(cu)
    e3.place(x=130,y=260)
    calc=Button(cu,text="Calculate Area",command=check_three).place(x=155,y=300)
    cu.mainloop()

def kites():
    root.destroy()
    global i
    i=9
    global e1
    global e2
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 180, height = 200)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="KITE.png")      
    canvas.create_image(-190,-230, anchor=NW, image=img)
    Label(cu,text='Enter diagonal 1').place(x=0,y=200)
    Label(cu,text='Enter diagonal 2').place(x=0,y=230)
    e1 = Entry(cu)
    e1.place(x=130,y=200)
    e2=Entry(cu)
    e2.place(x=130,y=230)
    calc=Button(cu,text="Calculate Area",command=check_two).place(x=155,y=270)
    cu.mainloop()
    
def threeD():
    global roots
    mainn.destroy()
    roots=Tk()
    roots.geometry('1300x650')
    frms=Frame(roots, bg="#3fd7de", height=431, width=626).pack(fill='both',expand='true')
    cube=Button(roots,but,text="Cube",command=cube_properties,height=6,width=16).place(x=90,y=60)
    cuboid=Button(roots,but,text="Cuboid",command=cuboid_properties,height=6,width=16).place(x=380,y=60)
    cylinder=Button(roots,but,text="Cylinder",command=cylinder_properties,height=6,width=16).place(x=90,y=315)
    cone=Button(roots,but,text="Cone",command=cone_properties,height=6,width=16).place(x=380,y=315)
    sphere=Button(roots,but,text="Sphere",command=sphere_properties,height=6,width=16).place(x=670,y=60)
    hemi=Button(roots,but,text="Hemisphere",command=hemisphere_properties,height=6,width=16).place(x=670,y=315)
    pyramid=Button(roots,but,text="Pyramid",command=pyramid_properties,height=6,width=16).place(x=960,y=60)
    prism=Button(roots,but,text="Prism",command=prism_properties,height=6,width=16).place(x=960,y=315)
    main_menu_button=Button(roots,text="main menu",command=main_menuu).place(x=626,y=580)
    roots.mainloop()

def cubes():
    root.destroy()
    global i
    i=4
    global e1
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 240, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="CUBE.png")      
    canvas.create_image(-180,-170, anchor=NW, image=img)
    Label(cu, text='Enter length of the side').place(x=0,y=200)
    e1 = Entry(cu)
    e1.place(x=150,y=200)
    calc=Button(cu,text="Calculate Area",command=check_one).place(x=155,y=250)
    cu.mainloop()

def cuboi():
    root.destroy()
    global i
    i=5
    global e1
    global e2
    global e3
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 300, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="CUBOID.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    Label(cu, text='Enter length').place(x=0,y=200)
    Label(cu, text='Enter breadth').place(x=0,y=230)
    Label(cu, text='Enter height').place(x=0,y=260)
    e1 = Entry(cu)
    e1.place(x=100,y=200)
    e2 = Entry(cu)
    e2.place(x=100,y=230)
    e3 = Entry(cu)
    e3.place(x=100,y=260)
    calc=Button(cu,text="Calculate Area",command=check_three).place(x=155,y=310)
    cu.mainloop()
    
def cones():
    root.destroy()
    global i
    i=6
    global e1
    global e2
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 300, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="CONE.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    Label(cu, text='Enter radius').place(x=0,y=200)
    Label(cu,text='Enter height').place(x=0,y=230)
    e1 = Entry(cu)
    e1.place(x=100,y=200)
    e2 = Entry(cu)
    e2.place(x=100,y=230)
    calc=Button(cu,text="Calculate Area",command=check_two).place(x=155,y=280)
    cu.mainloop()
    

def cylin():
    root.destroy()
    global i
    i=7
    global e1
    global e2
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 300, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="CYLINDER.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    Label(cu, text='Enter radius').place(x=0,y=200)
    Label(cu,text='Enter height').place(x=0,y=230)
    e1 = Entry(cu)
    e1.place(x=100,y=200)
    e2 = Entry(cu)
    e2.place(x=100,y=230)
    calc=Button(cu,text="Calculate Area",command=check_two).place(x=155,y=280)

def spheres():
    root.destroy()
    global i
    i=9
    global e1
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 300, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="CIRCLE.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    Label(cu, text='Enter radius').place(x=0,y=200)
    e1 = Entry(cu)
    e1.place(x=150,y=200)
    calc=Button(cu,text="Calculate Area",command=check_one).place(x=155,y=250)
    cu.mainloop()    

def hemisphere():
    root.destroy()
    global i
    i=13
    global e1
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 300, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="HEMISPHERE.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    Label(cu, text='Enter radius').place(x=0,y=200)
    e1 = Entry(cu)
    e1.place(x=150,y=200)
    calc=Button(cu,text="Calculate Area",command=check_one).place(x=155,y=250)
    cu.mainloop()

def square_pyramid():
    root.destroy()
    i=14
    global e1
    global e2
    cu=Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 300, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="SQUARE_PYRAMID.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    Label(cu, text='Enter length of side').place(x=0,y=200)
    Label(cu,text='Enter height').place(x=0,y=230)
    e1 = Entry(cu)
    e1.place(x=100,y=200)
    e2 = Entry(cu)
    e2.place(x=100,y=230)
    calc = Button(cu, text="Calculate Area").place(x=155, y=280)
    cu.mainloop()

def prisms():
    root.destroy()
    global i
    i = 15
    global e1
    global e2
    global e3
    cu = Tk()
    cu.geometry('400x400')
    cu.configure(bg='#3fd7de')
    canvas = Canvas(cu, width = 300, height = 300)      
    canvas.pack()      
    img = PhotoImage(master = canvas ,file="PRISM.png")      
    canvas.create_image(20,20, anchor=NW, image=img)
    Label(cu, text='Enter first side').place(x=0, y=200)
    Label(cu, text='Enter second side').place(x=0, y=230)
    Label(cu, text='Enter the length').place(x=0, y=260)
    e1 = Entry(cu)
    e1.place(x=100, y=200)
    e2 = Entry(cu)
    e2.place(x=100, y=230)
    e3 = Entry(cu)
    e3.place(x=100, y=260)
    calc = Button(cu, text="Calculate Area",command=check_three).place(x=155, y=310)
    cu.mainloop()

#get funtion always returns a string
    
def getting_one():
    global name
    name=''
    global area
    global a,e1
    a=e1.get()
    
    if i==0:
        name='SQUARE'
        area=a*a
        area=round(area,2)
    elif i==3:
        name='CIRCLE'
        area=3.14*a*a
        area=round(area,2)
    elif i==4:
        name='CUBE'
        area=a*a*a
        area=round(area,2)
    elif i==9:
        name='SPHERE'
        area=(4/3)*3.14*a**3
        area=round(area,2)
    elif i==13:
        name='HEMISPHERE'
        area=(2/3)*3.14*a**3
        area=round(area,2)
       
        
        
    final()    
def getting_two():
    global name
    name=''
    global area
    global a
    global b,e1,e2
 
  
    if i==1:
        name='RECTANGLE'
        area=a*b
        area=round(area,2)
    elif i==6:
        name='CONE'
        area=(3.14*a*a*b)/3
        area=round(area,2)
    elif i==7:
        name='CYLINDER'
        area=3.14*a*a*b
        area=round(area,2)
    elif i==8:
        name='PARALLELOGRAM'
        area=a*b
        area=round(area,2)
    elif i==9:
        name='KITE'
        area=0.5*a*b
        area=round(area,2)
    final()
       
def getting_three():
    global name
    name=''
    global area
    global a
    global b
    global c,e1,e2,e3
   
  
    if i==5:
        name='CUBOID'
        area=a*b*c
        area=round(area,2)
    elif i==2:
        name='TRIANGLE'
        sem=(a+b+c)/2
        area=math.sqrt(sem*(sem-a)*(sem-b)*(sem-c))
        area=round(area,2)
    elif i==10:
        name='TRAPEZIUM'
        area=(1/2)*c*(a+b)
        area=round(area,2)
    elif i==15:
        name='PRISM'
        area=(1/2)*(a*b*c)
        area=round(area,2)
    final()
    
    
    
def final():
    final=Tk()
    final.geometry('200x200')
    #final.configure(bg='white')
    Label(final,text="The Area of the %s is %s"%(name,area)).place(x=0,y=0)
    final.mainloop()

def menuu():
    global mainn
    mainn=Tk()
    mainn.geometry('650x550')
    frms=Frame(mainn, bg="#3fd7de", height=431, width=626).pack(fill='both',expand='true')
    b1=Button(mainn,font_styles,text="2D MENU",command=twoD,height=8,width=16).place(x=70,y=100)
    b2=Button(mainn,font_styles,text="3D MENU",command=threeD,height=8,width=16).place(x=350,y=100)
    back_button=Button(mainn,text="back",command=back_btn).place(x=770,y=520)
    mainn.mainloop()

     ##### place this after establishing the mysql connection thingy



###################### PROPERTIESSSS ########################

def rectangle_properties():
    global root
    root=Tk()
    root.geometry('720x500')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='The Opposite sides are parallel and equal to each other.')
    label2=Label(root,property_font,text='Each interior angle is equal to 90 degrees.')
    label3=Label(root,property_font,text='The diagonals are equal.')
    label4=Label(root,property_font,text='Perimeter is equal to twice the sum of its length and breadth.')
    b1=Button(root,text='Proceed',command=rect,width = 9 , height=2)
    b1.place(x=320,y=350)

    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)

    root.mainloop()


def square_properties():
    global root
    root=Tk()
    root.geometry('825x500')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='All sides are equal to each other.')
    label2=Label(root,property_font,text='The diagonals bisect each other at 90 degrees.')
    label3=Label(root,property_font,text='The diagonal of the square divide it into two similar isosceles triangles.')
    label4=Label(root,property_font,text='The length of the diagonals is greater than the sides of the square.')
    b1=Button(root,text='Proceed',command=sqr,width = 9 , height=2)
    b1.place(x=320,y=350)

    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()



def triangle_properties():
    global root
    root=Tk()
    root.geometry('1050x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='The sum of all the angles of a triangle is equal to 180 degrees.')
    label2=Label(root,property_font,text="The perimeter of the triangle is equal to sum of all its three sides.")
    label3=Label(root,property_font,text='The side opposite the greater angle is the longest side of all the three sides of the triangle.')
    label4=Label(root,property_font,text='Triangle has three sides.')
    b1=Button(root,text='Proceed',command=tri,width = 9 , height=2)
    b1.place(x=320,y=350)

    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()



def parallelogram_properties():
    global root
    root=Tk()
    root.geometry('850x450')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='The opposite angles are equal.')
    label2=Label(root,property_font,text='The consecutive or adjacent angles are complementary.')
    label3=Label(root,property_font,text='Each diagonal bisects the parallelogram into two congruent triangles.')
    label4=Label(root,property_font,text='The opposite sides are equal and parallel.')

    b1=Button(root,text='Proceed',command=parallelogram,width = 9 , height=2)
    b1.place(x=320,y=350)
    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()



def trapezium_properties():
    global root
    root=Tk()
    root.geometry('900x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='A  trapezium has two parallel sides and two non-parallel sides.')
    label2=Label(root,property_font,text='The length of the mid-segment is equal to half the sum of the parallel bases.')
    label3=Label(root,property_font,text='One pair of opposite sides are parallel.')
    label4=Label(root,property_font,text='The diagonals bisect each other.')
    b1=Button(root,text='Proceed',command=trapezium,width = 9 , height=2)
    b1.place(x=320,y=350)

    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()



def circle_properties():
    global root
    root=Tk()
    root.geometry('900x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='The circles are said to be congruent if they have equal radii.')
    label2=Label(root,property_font,text='The diameter of a circle is the longest chord of a circle.')
    label3=Label(root,property_font,text='Circles having different radius are similar.')
    label4=Label(root,property_font,text='The chords that are equidistant from the centre are equal in length.')
    b1=Button(root,text='Proceed',command=circ,width = 9 , height=2)
    b1.place(x=320,y=350)

    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()


def rhombus_properties():
    global root
    root=Tk()
    root.geometry('600x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='The opposite sides of a rhombus are parallel')
    label2=Label(root,property_font,text='Opposite angles of a rhombus are equal')
    label3=Label(root,property_font,text='Diagonals bisect the angles of rhombus')
    label4=Label(root,property_font,text='All sides are equal')
    b1=Button(root,text='Proceed',command=rhomb,width = 9 , height=2)
    b1.place(x=320,y=350)

    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()



def cube_properties():
    global root
    root=Tk()
    root.geometry('650x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='It has all its faces in square shape')
    label2=Label(root,property_font,text='The plane angles of the cube are the right angle')
    label3=Label(root,property_font,text='Each of the faces meets the other four faces')
    label4=Label(root,property_font,text='The edges opposite to each other are parallel')
    b1=Button(root,text='Proceed',command=cubes,width = 9 , height=2)
    b1.place(x=320,y=350)

    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()



def cuboid_properties():
    global root
    root=Tk()
    root.geometry('900x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='The faces of the cuboid are all rectangular in shape')
    label2=Label(root,property_font,text='Opposite edges of the cuboid are parallel to each other')
    label3=Label(root,property_font,text='A cuboid has 6 faces,12 edges and 8 vertices')
    label4=Label(root,property_font,text='Angles formed at the vertices of the cuboid are all 90 degrees')
    b1=Button(root,text='Proceed',command=cuboi,width = 9 , height=2)
    b1.place(x=320,y=350)

    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()



def cylinder_properties():
    global root
    root=Tk()
    root.geometry('1000x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='The bases of the cylinder are always congruent and parallel to each other')
    label2=Label(root,property_font,text='If the bases are circular,then it is called a right circular cylinder')
    label3=Label(root,property_font,text='A cylinder is similar to a prism since it has same cross-section everywhere')
    label4=Label(root,property_font,text='Perimeter is equal to twice the sum of its length and breadth')

    b1=Button(root,text='Proceed',command=cylin,width = 9 , height=2)
    b1.place(x=320,y=350)
    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()


def cone_properties():
    global root
    root=Tk()
    root.geometry('950x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='A cone has only one face,which is circular')
    label2=Label(root,property_font,text='A cone has zero edges')
    label3=Label(root,property_font,text='A cone has only one apex')
    label4=Label(root,property_font,text='The volume of cone is one third the product of its base area and height')

    b1=Button(root,text='Proceed',command=cones,width = 9 , height=2)
    b1.place(x=320,y=350)
    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()


def sphere_properties():
    global root
    root=Tk()
    root.geometry('600x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='A sphere is perfectly symmetrical')
    label2=Label(root,property_font,text='A sphere has constant mean curvature')
    label3=Label(root,property_font,text='A sphere is not a polyhedron')
    label4=Label(root,property_font,text='A sphere has constant width and circumference')

    b1=Button(root,text='Proceed',command=spheres,width = 9 , height=2)
    b1.place(x=320,y=350)
    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()


def kite_properties():
    global root
    root=Tk()
    root.geometry('800x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='A kite is symmetrical about its main diagonal')
    label2=Label(root,property_font,text='Angles opposite to the main diagonal are equal')
    label3=Label(root,property_font,text='The shorter diagonal divides the kite into 2 isosceles triangles')
    label4=Label(root,property_font,text='Kite has diagonals that intersect each other at right angles')

    b1=Button(root,text='Proceed',command=kites,width = 9 , height=2)
    b1.place(x=320,y=350)
    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()

def hemisphere_properties():
    global root
    root=Tk()
    root.geometry('950x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='A Hemisphere has a curved surface area and a flat face,which is a circle')
    label2=Label(root,property_font,text='A Hemisphere has no vertices and one edge')
    label3=Label(root,property_font,text='A Hemisphere is not a polyhedron')
    label4=Label(root,property_font,text='It has one curved edge')

    b1=Button(root,text='Proceed',command=hemisphere,width = 9 , height=2)
    b1.place(x=320,y=350)
    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()

def pyramid_properties():
    global root
    root=Tk()
    root.geometry('800x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='A Triangular Pyramid has 4 faces')
    label2=Label(root,property_font,text='A Pyramid has 4 vertices')
    label3=Label(root,property_font,text='It can be regular,irregular and right-angled')
    label4=Label(root,property_font,text='A regular Pyramid has equilateral triangles for all side faces')

    b1=Button(root,text='Proceed',command=square_pyramid,width = 9 , height=2)
    b1.place(x=320,y=350)
    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()

def prism_properties():
    global root
    root=Tk()
    root.geometry('700x600')
    root.configure(bg='#f4cac9')
    head_label=Label(root,title_styles2,text='PROPERTIES:').place(x=0,y=0)
    label1=Label(root,property_font,text='A prism is a special kind of 3D shape')
    label2=Label(root,property_font,text='A Prism has two identical ends')
    label3=Label(root,property_font,text='A prism is the same shape and size all the way through')
    label4=Label(root,property_font,text='It has 5 Faces, 6 Corners and 9 Edges')

    b1=Button(root,text='Proceed',command=prisms,width = 9 , height=2)
    b1.place(x=320,y=350)
    label1.place(x=30,y=90)
    label2.place(x=30,y=145)
    label3.place(x=30,y=200)
    label4.place(x=30,y=255)
    root.mainloop()


mainmenu()

################### MYSQL INTEGRATION #####################
'''def  establish_connection():
    mydb=mysql.connector.connect(host="localhost",user="root",password='Welcome@12')
    mycursor=mydb.cursor()
    m1='create database if not exists backend'
    m2='use backend'
    m3='create table if not exists history(S_no varchar(10),Shape varchar(100),Length varchar(10),Breadth varchar(10),Height varchar(10),Radius varchar(10),Area_or_Volume varchar(10),Date date)'

    mycursor.execute(m1)
    mycursor.execute(m2)
    mycursor.execute(m3)




    mydb.close()

'''