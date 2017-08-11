from tkinter import *
from tkinter import messagebox
import math
#LINKED LIST IMPLEMENTATION:
class Node :
    def __init__( self, intime,carno ) :
        self.intime = intime
        self.carno = carno
        self.next = None
        self.prev = None

class LinkedList :
    def __init__( self ) :
        self.head = None

    def add( self, intime,carno ) :
        node = Node( intime,carno )
        if self.head == None :
            self.head = node
        else :
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search( self,k) :
        p = self.head
        if p != None :
            while p.next != None :
                if ( p.carno == k ) :
                    return p
                p = p.next
            if ( p.carno == k ) :
                return p

    def remove( self, p ) :
        if p==None:
            p.next=None
        else:
            p.carno=p.next.carno
            p.next=p.next.next
    def __str__( self ) :
        s = ""
        p = self.head
        if p != None :
            while p.next != None :
                s += p.carno
                p = p.next
            s += p.carno
        return s
#Creating a object of the class Linked List
l=LinkedList()
#Creating a root object of the Tkinter Class
root=Tk()
#Creating a frame(a empty box like thing)
frame=Frame(root)
#Pack it in a window
frame.pack(fill=BOTH)
#FUNCTION FOR MAIN MENU
def mainmenu():
    L1=Label(frame,text="CLICK ON ANY OF THE BUTTONS ACCORDINGLY")
    L1.pack(side=TOP)
    Entrybutton=Button(frame,text="Entry",fg="Green",height=5,width=10,padx=10,pady=10,relief=RAISED,command=Enter)
    Entrybutton.pack(fill=X)
    Exitbutton=Button(frame,text="Exit",fg="Red",height=5,width=10,padx=10,pady=10,relief=RAISED,command=Exit)
    Exitbutton.pack(fill=X)
    def close_main():
        root.destroy()
    close_button=Button(frame,text="Close",command=close_main)
    close_button.pack()
    root.mainloop()
#FUNCTION TO VALIDATE THE DATA ENTERED IN THE ENTRY OPTION
def success_enter():
    root1=Tk()
    frame=Frame(root1)
    frame.pack(fill=BOTH)
    text=In.get()
    vno=Vnenter.get()
    if(text=="" or vno=="" ):
        messagebox.showinfo(frame,message="Incomplete Entries")
    elif int(text[0:2])>24 or int(text[3:])>60:
        messagebox.showinfo(frame,message="Invalid Entry")
    elif text[2]!=':':
        messagebox.showinfo(frame,message="Did you miss a colon??")
    elif vno.isnumeric()==FALSE or len(vno)!=4:
        messagebox.showinfo(frame,message="Enter four digit Car Number")
    else:
        messagebox.showinfo(frame,message="Information submitted successfully \n TIME:%s\nCAR NUMBER:%s"%(text,vno))
        l.add(text,vno)
    rootenter.destroy()
#FUNCTION TO VALIDATE THE DATA ENTERED IN THE EXIT OPTION
def success_exit():
    root1=Tk()
    frame=Frame(root1)
    frame.pack(fill=BOTH)
    text=ex.get()
    vno=Vnexit.get()
    if(text=="" or vno=="" or len(text)<4 or len(vno)<4):
        messagebox.showinfo(frame,message="Incomplete Entries")
    elif int(text[0:2])>24 or int(text[3:])>60:
        messagebox.showinfo(frame,message="Invalid Entry")
    elif vno.isnumeric()==FALSE or len(vno)!=4:
        messagebox.showinfo(frame,message="Enter four digit Car Number")
    else:
        if l.search(vno)==None:
            messagebox.showinfo(frame,message="Car not parked")
        else:
            t=l.search(vno)
            h2=int(text[:2]);m2=int(text[3:]);h1=int(t.intime[:2]);m1=int(t.intime[3:])
            if m2<m1:
                h2-=1
                mindiff=60-(m1-m2)
                hdiff=abs(h2-h1)
            else:
                hdiff=abs(h2-h1)
                mindiff=abs(m2-m1)
            if(hdiff<2):
                messagebox.showinfo(frame,message="Your in time was %s\nYour bill amount is 10"%t.intime)
            elif(hdiff>=2 and hdiff<8):
                messagebox.showinfo(frame,message="Your in time was %s\nYour bill amount is 20"%t.intime)
            elif(hdiff>=8):
                messagebox.showinfo(frame,message="Your in time was %s\nYour bill amount is 30"%t.intime)
            l.remove(t)



    rootexit.destroy()
#TO CREATE THE ENTRY DIALOG BOX
def Enter():
    global In,rootenter,Vnenter,fw,tw
    vno=StringVar()
    var=IntVar()
    rootenter=Tk()
    intime=StringVar()
    frame1=Frame(rootenter)
    frame1.pack(fill=BOTH)
    Intime=Label(frame1,text="Enter the current time in HH:MM 24 hour format")
    Intime.grid(row=1,column=1)
    In=Entry(frame1,bd=5,textvariable=intime)
    In.grid(row=1,column=2)
    Vno=Label(frame1,text="Enter your vehicle number")
    Vno.grid(row=3,column=1)
    Vnenter=Entry(frame1,bd=5,textvariable=vno)
    Vnenter.grid(row=3,column=2)
    VT=Label(frame1,text="Select your vehicle type")
    VT.grid(row=5,column=1)
    fw=Radiobutton(frame1,text="Four Wheeler",textvariable="Four",value=1)
    fw.grid(row=7,column=1)
    tw=Radiobutton(frame1,text="Two Wheeler",textvariable="Two",value=0)
    tw.grid(row=8,column=1)
    submit=Button(frame1,text="Submit",command=success_enter)
    submit.grid(row=9,column=1)
    rootenter.mainloop()
#TO CREATE THE EXIT DIALOG BOX
	
def Exit():
	global rootexit,Vnexit,ex
	vno_exit=StringVar()
	exittime=StringVar()
	rootexit=Tk()
	frame2=Frame(rootexit)
	frame2.pack(fill=BOTH)
	exittime=Label(frame2,text="Enter the current time")
	exittime.grid(row=1,column=1)
	ex=Entry(frame2,bd=5,textvariable=exittime)
	ex.grid(row=1,column=2)
	Vno=Label(frame2,text="Enter your vehicle number")
	Vno.grid(row=2,column=1)
	Vnexit=Entry(frame2,bd=5,textvariable=vno_exit)
	Vnexit.grid(row=2,column=2)
	submit=Button(frame2,text="Submit",command=success_exit)
	submit.grid(row=9,column=1)
	rootexit.mainloop()
mainmenu()


