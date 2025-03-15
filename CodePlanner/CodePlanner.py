import tkinter as tk
import tkinter.ttk as ttk 

#Functions
sidebarvariable = 0
isfunctionactive = 0
labelcount = 0
sdbpage = 1
sdbtotalpage=0
intt = 0
NameListed = []
NameListe = []

def PlannerBarSetter(int)->None:
    pass
    

#SideBar

def OpenSideBar():
    global sidebarvariable,isfunctionactive
    if(isfunctionactive==0):
        if(sidebarvariable==0):
            sidebar.place(width=320,height=1040,x=1600,y=41)
            isfunctionactive=sidebarvariable=1
            NameButtons()
            sdbpagenumber.config(text=f"{sdbpage}/{sdbtotalpage}")

def CloseSideBar():
    global sidebarvariable,isfunctionactive
    sidebar.place_forget()
    isfunctionactive=sidebarvariable=0

def sdbButtonLeft():
    global sdbpage,NameListed
    if(sdbpage>1):
        sdbpage-=1
        sdbpagenumber.config(text=f"{sdbpage}/{sdbtotalpage}")
        NameButtons() 
    
def sdbButtonRight():
    global sdbpage,NameListed
    if(sdbpage<sdbtotalpage):
        sdbpage+=1
        sdbpagenumber.config(text=f"{sdbpage}/{sdbtotalpage}")
        NameButtons()

def NameButtons():
    global sdbtotalpage,sdbpage,NameListed
    with open("planners.txt","r") as PlannerNames:
        NameList = PlannerNames.read()
        NameListed = NameList.split(".txt\n")
        print(f"{len(NameListed)}")
        sdbtotalpage = int((len(NameListed)//15)+1)
        if(sdbpage==sdbtotalpage):
            maxvalue = int(len(NameListed))
            for i in range(maxvalue,15*sdbpage):
                sdbbuttonlist[int(i-(15*(sdbpage-1)))].config(text=" ")
        else:
            maxvalue = 15*sdbpage
        for i in range((15*(sdbpage-1)),(maxvalue)):
            sdbbuttonlist[int(i-(15*(sdbpage-1)))].config(text=f"{NameListed[i]}")
            print(f"Button list index: {int(i-(15*(sdbpage-1)))}")
            print(f"Name list index: {i}") 


def sdbButtonDeleter1():
    global NameListed,sdbpage
    a=0
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter2():
    global NameListed,sdbpage
    a=1
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter3():
    global NameListed,sdbpage
    a=2
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter4():
    global NameListed,sdbpage
    a=3
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter5():
    global NameListed,sdbpage
    a=4
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter6():
    global NameListed,sdbpage
    a=5
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter7():
    global NameListed,sdbpage
    a=6
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter8():
    global NameListed,sdbpage
    a=7
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter9():
    global NameListed,sdbpage
    a=8
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter10():
    global NameListed,sdbpage
    a=9
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter11():
    global NameListed,sdbpage
    a=10
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter12():
    global NameListed,sdbpage
    a=11
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter13():
    global NameListed,sdbpage
    a=12
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter14():
    global NameListed,sdbpage
    a=13
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
def sdbButtonDeleter15():
    global NameListed,sdbpage
    a=14
    Names = list(NameListed)
    print(Names)
    if(Names[a]==''):
        pass
    else:
        with open("planners.txt","w") as NameDeleted:
            for i in range(0,(len(Names))):
                if(i==a):
                    continue
                else:
                    NameDeleted.write(f"{Names[i]}.txt\n")
    
def sdbButtonOpener():
    pass






#NewPlanner

def NewPlannerLabel():
    global isfunctionactive
    if(isfunctionactive==0):
        NewPlannerFrame.place(width=600,height=400,x=660,y=340)
        isfunctionactive=1
    
def NewPlannerCloseButton():
    global isfunctionactive
    NewPlannerFrame.place_forget()
    isfunctionactive=0




























#User Interface
darkpurple = "#08050B"
mypurple = "#470790"
gray = "#2A2A2A"
darkgray = "#101010"
darkred = "#4E0000"


root = tk.Tk()
root.title("Code Planner V0.1 Beta")
root.geometry("1920x1080")
root.state("zoomed")
root.config(bg=darkpurple)

up_line1 = tk.Label(root,bg=mypurple)
up_line1.place(x=0,y=10,width=1920,height=1)

up_line2 = tk.Label(root,bg=mypurple)
up_line2.place(x=0,y=40,width=1920,height=1)

up_lineh1 = tk.Label(root,bg=mypurple)
up_lineh1.place(x=150,y=10,width=1,height=30)

up_lineh2 = tk.Label(root,bg=mypurple)
up_lineh2.place(x=1740,y=10,width=1,height=30)


tabs = tk.Label(root,bg=darkpurple,text="Active Planners: ",fg="white",font="Arial 12 bold")
tabs.place(x=0,y=13,width=150,height=25)

OpenButton = tk.Button(root,bg=gray,text="Open",fg="white",border=0,command=OpenSideBar)
OpenButton.place(x=1835,y=13,width=80,height=25)


#Sidebar

sidebar = tk.Frame(root,bg=darkgray)
SideBarClose = tk.Button(sidebar,bg=gray,text="Close",fg="white",border=0,command=CloseSideBar)
sdbleftline = tk.Label(sidebar,bg=mypurple)
sdbrightline = tk.Label(sidebar,bg=mypurple)
sdbdownline = tk.Label(sidebar,bg=mypurple)
sdbdownline2 = tk.Label(sidebar,bg=mypurple)
SideBarClose.place(width=80,height=25,x=235,y=945)
sdbleftline.place(width=0,height=1040,x=0,y=0)
sdbrightline.place(width=0,height=1040,x=319,y=0)
sdbdownline.place(width=320,height=1,x=0,y=939)
sdbdownline2.place(width=320,height=1,x=0,y=975)
sdbbuttonlist = ["buton1","buton2","buton3","buton4","buton5","buton6","buton7","buton8","buton9","buton10","buton11","buton12","buton13","buton14","buton15"]
sdbdeletebuttonlist = ["del1","del2","del3","del4","del5","del6","del7","del8","del9","del10","del11","del12","del13","del14","del15"]

buton1 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter1)
buton2 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter2)
buton3 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter3)
buton4 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter4)
buton5 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter5)
buton6 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter6)
buton7 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter7)
buton8 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter8)
buton9 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter9)
buton10 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter10)
buton11 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter11)
buton12 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter12)
buton13 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter13)
buton14 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter14)
buton15 = tk.Button(sidebar,bg=darkred,fg="white",text=f"Delete",border=0,command=sdbButtonDeleter15)

buton1.place(width=55,height=30,x=240,y=55+(0*45))
buton2.place(width=55,height=30,x=240,y=55+(1*45))
buton3.place(width=55,height=30,x=240,y=55+(2*45))
buton4.place(width=55,height=30,x=240,y=55+(3*45))
buton5.place(width=55,height=30,x=240,y=55+(4*45))
buton6.place(width=55,height=30,x=240,y=55+(5*45))
buton7.place(width=55,height=30,x=240,y=55+(6*45))
buton8.place(width=55,height=30,x=240,y=55+(7*45))
buton9.place(width=55,height=30,x=240,y=55+(8*45))
buton10.place(width=55,height=30,x=240,y=55+(9*45))
buton11.place(width=55,height=30,x=240,y=55+(10*45))
buton12.place(width=55,height=30,x=240,y=55+(11*45))
buton13.place(width=55,height=30,x=240,y=55+(12*45))
buton14.place(width=55,height=30,x=240,y=55+(13*45))
buton15.place(width=55,height=30,x=240,y=55+(14*45))

for sdb in range(0,15):
    sdbbuttonlist[sdb] = tk.Button(sidebar,bg=gray,fg="white",command=sdbButtonOpener,border=0,text=" ")
    sdbbuttonlist[sdb].place(width=200,height=40,x=35,y=50+(sdb*45)) 



sdbbuttonleft = tk.Button(sidebar,bg=gray,fg="white",text="<",border=0,command=sdbButtonLeft)
sdbbuttonright = tk.Button(sidebar,bg=gray,fg="white",text=">",border=0,command=sdbButtonRight)
sdbbuttonleft.place(width=45,height=30,x=61,y=885)
sdbbuttonright.place(width=45,height=30,x=216,y=885)
sdbpagenumber = tk.Label(sidebar,bg=gray,fg="white",text=f"{sdbpage}/{sdbtotalpage}")
sdbpagenumber.place(width=45,height=30,x=140,y=885)





#NewPlanner

NewPlannerButton = tk.Button(root,bg=gray,text="New Planner",fg="white",border=0,command=NewPlannerLabel)
NewPlannerButton.place(x=1752,y=13,width=80,height=25)
NewPlannerFrame = tk.Frame(root)
NewPlannerFrame.config(bg=gray)
NewPlannerClose = tk.Button(NewPlannerFrame,bg=darkgray,text="Close",fg="white",border=0,command=NewPlannerCloseButton)
nplupline = tk.Label(NewPlannerFrame,bg=mypurple)
npldownline = tk.Label(NewPlannerFrame,bg=mypurple)
nplleftline = tk.Label(NewPlannerFrame,bg=mypurple)
nplrightline = tk.Label(NewPlannerFrame,bg=mypurple)
NewPlannerClose.place(width=80,height=25,x=7,y=370)
nplupline.place(width=600,height=1,x=0,y=0)
npldownline.place(width=600,height=1,x=0,y=399)
nplleftline.place(width=1,height=400,x=0,y=0)
nplrightline.place(width=1,height=400,x=599,y=0)

root.mainloop()


