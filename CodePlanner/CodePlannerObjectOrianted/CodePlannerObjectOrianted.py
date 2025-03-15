import tkinter as tk
import tkinter.ttk as ttk
import json
import time
import os

#Veriables
isMainActive=0
isSaved=1
currentpage=1
totalpage=0

#Colors
darkpurple = "#08050B"
mypurple = "#470790"
activepurple = "#140030"
gray = "#2A2A2A"
darkgray = "#101010"
darkred = "#4E0000"
lightgreen = "#47E249"

#Classes And Functions

#User Interface

class PlannerOpen(tk.Frame):
    def __init__(self,master=None,**kwags):
        super().__init__(master,**kwags)
        global interpreterbutton,iseditmode,statedisabledtextbox,line,stepline,steplast,forturn,countturn
        iseditmode=line=stepline=steplast=forturn=countturn=0 # Line için konuşmam gerekirse en başta 0 olucak sonra next ve previous ile değişicek
        self.config(bg=darkgray)
        upline = tk.Label(self,bg=mypurple)
        upline.place(x=0,y=0,width=1620,height=1)
        downline = tk.Label(self,bg=mypurple)
        downline.place(x=0,y=899,width=1620,height=1)
        downline2 = tk.Label(self,bg=mypurple)
        downline2.place(x=0,y=863,width=1620,height=1)
        leftline = tk.Label(self,bg=mypurple)
        leftline.place(x=0,y=0,width=1,height=900)
        rightline = tk.Label(self,bg=mypurple)
        rightline.place(x=1619,y=0,width=1,height=900)
        closebutton = tk.Button(self,bg=gray,fg="red",text="Close",border=0,command=self.closeplanner)
        closebutton.place(x=1554,y=869,width=60,height=25)
        previousbutton = tk.Button(self,bg=gray,fg=lightgreen,text="<",border=0,anchor="s",font="default 12 bold",command=self.previousstep)
        previousbutton.place(x=1,y=1,width=20,height=862)
        nextbutton = tk.Button(self,bg=gray,fg=lightgreen,text=">",border=0,anchor="s",font="default 12 bold",command=self.nextstep)
        nextbutton.place(x=1599,y=1,width=20,height=862)
        editplannerbutton = tk.Button(self,bg=gray,fg="orange",text="Edit Planner",border=0,command=self.editplanner)
        editplannerbutton.place(x=6,y=869,width=80,height=25)
        statedisabledtextbox = tk.Text(self,bg="black",fg="white",border=0,state="disabled")
        statedisabledtextbox.place(x=21,y=1,width=1578,height=702)
        terminallabel = tk.Label(self,bg=darkgray,fg="white",text="   Running Without Errors            Integrated Terminal",anchor="w")
        terminallabel.place(x=21,y=703,width=1578,height=25)
        bigleftlabel = tk.Label(self,bg="black",fg="white",anchor="w")
        bigleftlabel.place(x=21,y=729,width=789,height=133)
        bigrightlabel = tk.Label(self,bg="black",fg="white",text="\n  Y/N: ",anchor="nw")
        bigrightlabel.place(x=810,y=729,width=789,height=133)
        interpreterbutton = tk.Button(self,command=self.interpreterrunner)
    
    def interpreterrunner(self):
        self.plannerinterpreter()

    def plannerinterpreter(self):
        global name,plannersfolder,statedisabledtextbox,fortabspace,whiletabspace,iftabspace,ifandbreakcontrol,line,breakcolor,passedlines,foractive,whileactive,forturn,countturn
        with open(f"{plannersfolder}\\{interpretername}.json","r",encoding="utf-8") as runningplanner:
            global fortabspace,whiletabspace,iftabspace,ifandbreakcontrol
            foractive=[];whileactive=[];ifactive=[];breakcolor=[];passedlines=[]
            fortabspace = whiletabspace = iftabspace = ifandbreakcontrol = line = 0 
            statedisabledtextbox.config(state="normal")
            plannersyntaxtext = runningplanner.read()
            syntaxtextlist = list(plannersyntaxtext.replace('""','\n').replace('"','').split('\n'))
            statedisabledtextbox.delete("1.0","end")
            statedisabledtextbox.insert("1.0","\n")
            for i in range(0,len(syntaxtextlist)):
                if('/for' in f'{syntaxtextlist[i]}'):
                    fortabspace=1
                    foractive.append(1)
                    if(iftabspace==1):
                        text = f'      {syntaxtextlist[i][1:]} | {countturn}\n'
                    else:
                        text = f'   {syntaxtextlist[i][1:]} | {countturn}\n'
                    line+=1
                elif('/while' in f'{syntaxtextlist[i]}'):
                    whiletabspace=1
                    whileactive.append(1)
                    if(iftabspace==1):
                        text = f'      {syntaxtextlist[i][1:]}\n'
                    else:
                        text = f'   {syntaxtextlist[i][1:]}\n'
                    line+=1
                elif('/break' in f'{syntaxtextlist[i]}'):
                    if(ifandbreakcontrol==1):
                        ifandbreakcontrol=0
                        if(fortabspace==1 or whiletabspace==1):
                            text = f'           {syntaxtextlist[i][1:]}\n'
                        else:
                            text = f'       {syntaxtextlist[i][1:]}\n'
                        line+=1
                        breakcolor.append(i)
                    else:
                        iftabspace=whiletabspace=fortabspace=0
                        text="/passthisline"
                        passedlines.append(i)
                elif('/ifend' in f'{syntaxtextlist[i]}'):
                    iftabspace=0
                    ifandbreakcontrol=0
                    text="/passthisline"
                    passedlines.append(i)
                elif('/if' in f'{syntaxtextlist[i]}'):
                    iftabspace=ifandbreakcontrol=1
                    ifactive.append(1)
                    if(fortabspace==1 or whiletabspace==1):
                        text = f'       {syntaxtextlist[i][1:]}\n'
                    else:
                        text = f'   {syntaxtextlist[i][1:]}\n'
                    line+=1
                elif('/else' in f'{syntaxtextlist[i]}'):
                    if(fortabspace==1 or whiletabspace==1):
                        text = f'       {syntaxtextlist[i][1:]}\n'
                    else:
                        text = f'   {syntaxtextlist[i][1:]}\n'
                    ifandbreakcontrol=1
                    line+=1
                else:
                    if(fortabspace==1 or whiletabspace==1):
                        if(iftabspace==1):
                            text = f'           {syntaxtextlist[i]}\n'
                            if(fortabspace==1):
                                foractive.append(1)
                            else:
                                foractive.append(0)
                            if(whiletabspace==1):    
                                whileactive.append(1)
                            else:
                                whileactive.append(0)
                            ifactive.append(1)
                        else:
                            text = f'       {syntaxtextlist[i]}\n'
                            if(fortabspace==1):
                                foractive.append(1)
                            else:
                                foractive.append(0)
                            if(whiletabspace==1):    
                                whileactive.append(1)
                            else:
                                whileactive.append(0)
                            ifactive.append(0)
                        line+=1
                    elif(iftabspace==1):
                        text = f'       {syntaxtextlist[i]}\n'
                        ifactive.append(1)
                        foractive.append(0)
                        whileactive.append(0)
                        line+=1
                    else:
                        text = f'   {syntaxtextlist[i]}\n'
                        ifactive.append(0)
                        foractive.append(0)
                        whileactive.append(0)
                        line+=1
                if("/passthisline"!=text):
                    statedisabledtextbox.insert(f"{float(i+2)}",text)
                line=0
                for i in range(0,len(syntaxtextlist)):
                    if('/ifend' not in f'{syntaxtextlist[i]}'):
                        if('/break' in f'{syntaxtextlist[i]}'):
                            for color in breakcolor:
                                if(color == i):
                                    line+=1
                        else:
                            line+=1
                    if('/for' in f'{syntaxtextlist[i]}'):
                        statedisabledtextbox.tag_configure("custom_color10",foreground="red")
                        statedisabledtextbox.tag_add("custom_color10",float(line+1),f"{line+1}.0 lineend")
                    elif('/while' in f'{syntaxtextlist[i]}'):
                        statedisabledtextbox.tag_configure("custom_color11",foreground="orange")
                        statedisabledtextbox.tag_add("custom_color11",float(line+1),f"{line+1}.0 lineend")
                    elif('/break' in f'{syntaxtextlist[i]}'):
                        for color in breakcolor:
                                if(color == i):
                                    statedisabledtextbox.tag_configure("custom_color12",foreground="blue")
                                    statedisabledtextbox.tag_add("custom_color12",float(line+1),f"{line+1}.0 lineend")
                    elif('/if' in f'{syntaxtextlist[i]}'):
                        if('/ifend' not in f'{syntaxtextlist[i]}'):
                            statedisabledtextbox.tag_configure("custom_color13",foreground="pink")
                            statedisabledtextbox.tag_add("custom_color13",float(line+1),f"{line+1}.0 lineend")
                    elif('/else' in f'{syntaxtextlist[i]}'):
                            statedisabledtextbox.tag_configure("custom_color14",foreground="yellow")
                            statedisabledtextbox.tag_add("custom_color14",float(line+1),f"{line+1}.0 lineend")        
            statedisabledtextbox.config(state="disabled")

    def editplanner(self):
        global planneropener,textname,newplannereditor,editorhelper,name,interpretername,iseditmode,plannertext,runcolorededitor
        iseditmode=1
        name = interpretername
        with open(f"{plannersfolder}\\{interpretername}.json","r",encoding="utf-8") as runningplanner:
            plannersyntaxtext = runningplanner.read()
            syntaxtextlist = plannersyntaxtext.replace('""','\n').replace('"','')
            plannertext.insert("1.0",syntaxtextlist)
        planneropener.place_forget()
        newplannereditor.place(x=100,y=90,width=1300,height=850)
        editorhelper.place(height=850,width=370,x=1450,y=90)
        runcolorededitor.invoke()

    def fornextstep(self):
        global stepline,steplog,steplast,forturn,statedisabledtextbox,interpreterbutton,countturn
        statedisabledtextbox.config(state="normal")
        interpreterbutton.invoke()
        if(stepline==steplast):
            if(forturn==2):
                stepline=steplog+1
            else:
                stepline=steplog
            countturn+=1
            forturn-=1
        else:
            statedisabledtextbox.tag_configure("custom_color20",foreground=lightgreen)
            statedisabledtextbox.tag_add("custom_color20",float(stepline+2),f"{stepline+2}.0 lineend")
            stepline+=1
        statedisabledtextbox.config(state="disabled")
    
    def nextstep(self):
        with open(f"{plannersfolder}\\{interpretername}.json","r",encoding="utf-8") as runningplanner:
            global breakcolor,stepline,interpreterbutton,statedisabledtextbox,foractive,whileactive,steplast,steplog,forturn,countturn
            if(forturn>1):
                self.fornextstep()
            else:
                plannersyntaxtext = runningplanner.read()
                syntaxtextlist = list(plannersyntaxtext.replace('""','\n').replace('"','').split('\n'))
                if(stepline<len(syntaxtextlist)-1):
                    interpreterbutton.invoke()
                    statedisabledtextbox.config(state="normal")
                    if('/for' in f'{syntaxtextlist[stepline]}'):
                        countturn=1
                        forturn = int(syntaxtextlist[stepline].split(' ')[1])
                        print(forturn)
                        steplog = stepline
                        for i in range(stepline,len(foractive)):
                            if(foractive[i]==0):
                                steplast = i
                                break
                            else:
                                if(foractive[len(foractive)-1]==1):
                                    steplast = len(foractive)-1
                        self.fornextstep
                    statedisabledtextbox.tag_configure("custom_color20",foreground=lightgreen)
                    statedisabledtextbox.tag_add("custom_color20",float(stepline+2),f"{stepline+2}.0 lineend")
                    stepline+=1   
            statedisabledtextbox.config(state="disabled")
           
    def previousstep(self):
        pass    

    def closeplanner(self):
        global planneropener,isMainActive,tabbuttonlist
        for tabutton in tabbuttonlist:
            tabutton.config(bg=darkpurple)
        with open(f"{planner_configfolder}\\lasttab.json","w",encoding="utf-8") as lasttabinfo:
            pass
        planneropener.place_forget()
        isMainActive=0

class EditorHelper(tk.Frame):
    def __init__(self,master=None,**kwags):
        super().__init__(master,**kwags)
        self.config(bg=darkgray)
        global savevalue,forandwhilentry,entryLabel,entryButton,fororwhile
        savevalue=0
        fororwhile=""
        upLine = tk.Label(self,bg=mypurple)
        upLine.place(x=0,y=0,width=370,height=1)
        downLine = tk.Label(self,bg=mypurple)
        downLine.place(x=0,y=849,width=370,height=1)
        leftLine = tk.Label(self,bg=mypurple)
        leftLine.place(x=0,y=0,width=1,height=850)
        rightLine = tk.Label(self,bg=mypurple)
        rightLine.place(x=369,y=0,width=1,height=850)
        titleLabel = tk.Label(self,bg=gray,fg="white",text="Editor Helper")
        titleLabel.place(x=1,y=1,width=368,height=29)
        savebutton = tk.Button(self,bg=gray,fg="white",text="Save",border=0,command=self.savePlanner)
        savebutton.place(width=80,height=25,x=285,y=820)
        forbutton = tk.Button(self,bg=gray,fg="red",text="/for",border=0,font="default 11 bold",command=self.forButton)
        forbutton.place(width=60,height=30,x=6,y=50)
        forLabel = tk.Label(self,bg=gray,fg="white",text="This command repeats your plan block till the integer you enter.",font="default 7")
        forLabel.place(width=295,height=30,x=70,y=50)
        whilebutton = tk.Button(self,bg=gray,fg="orange",text="/while",border=0,font="default 11 bold",command=self.whileButton)
        whilebutton.place(width=60,height=30,x=6,y=50+40)
        whileLabel = tk.Label(self,bg=gray,fg="white",text="This command repeats your plan block till the term is false.",font="default 7")
        whileLabel.place(width=295,height=30,x=70,y=50+40)
        entryLabel = tk.Label(self,bg="black")
        entryLabel.place(width=350,height=30,x=10,y=750)
        entryLabelLine1 = tk.Label(self,bg="gray")
        entryLabelLine1.place(width=350,height=1,x=10,y=745)
        entryLabelLine2 = tk.Label(self,bg="gray")
        entryLabelLine2.place(width=350,height=1,x=10,y=784)
        entryButton = tk.Button(self,bg=gray,fg="white",text="Enter",command=self.forandwhilEntry,border=0)
        forandwhilentry = tk.Entry(self,bg="black",fg="white",insertbackground="white",border=0)
        breakbutton = tk.Button(self,bg=gray,fg="blue",text="/break",border=0,font="default 11 bold",command=self.breakButton)
        breakbutton.place(width=60,height=30,x=6,y=50+40*2)
        breakLabel = tk.Label(self,bg=gray,fg="white",text="This command ends /for and /while cycles.",font="default 7")
        breakLabel.place(width=295,height=30,x=70,y=50+40*2)
        ifbutton = tk.Button(self,bg=gray,fg="pink",text="/if",command=self.ifButton,border=0,font="default 11 bold")
        ifbutton.place(width=60,height=30,x=6,y=50+40*3)
        ifLabel = tk.Label(self,bg=gray,fg="white",text="This command runs when terms value equals true.",font="default 7")
        ifLabel.place(width=295,height=30,x=70,y=50+40*3)
        ifendbutton = tk.Button(self,bg=gray,fg="purple",text="/ifend",command=self.ifendButton,border=0,font="default 11 bold")
        ifendbutton.place(width=60,height=30,x=6,y=50+40*4)
        ifendLabel = tk.Label(self,bg=gray,fg="white",text="This command ends /if statements.",font="default 7")
        ifendLabel.place(width=295,height=30,x=70,y=50+40*4)
        elsebutton = tk.Button(self,bg=gray,fg="yellow",text="/else",command=self.elseButton,border=0,font="default 11 bold")
        elsebutton.place(width=60,height=30,x=6,y=50+40*5)
        elseLabel = tk.Label(self,bg=gray,fg="white",text="This command runs when if term equals false.",font="default 7")
        elseLabel.place(width=295,height=30,x=70,y=50+40*5)
        deleteall = tk.Button(self,bg=darkred,fg="white",text="Delete All",command=self.deleteAll,border=0)
        deleteall.place(width=80,height=25,x=45,y=715)
        deleteline = tk.Button(self,bg=darkred,fg="white",text="Delete Line",command=self.deleteLine,border=0)
        deleteline.place(width=80,height=25,x=135,y=715)
        deleteerror = tk.Button(self,bg=darkred,fg="white",text="Delete Error",command=self.deleteError,border=0)
        deleteerror.place(width=80,height=25,x=225,y=715)
        deleteplanner = tk.Button(self,bg=darkred,fg="white",text="Delete Planner",command=self.deletePlanner,border=0)
        deleteplanner.place(width=80,height=25,x=6,y=820)

    def deletePlanner(self):
        global name,removedname,newplannereditor,editorhelper,isSaved,plannertext,isMainActive,plannersfolder
        with open(f"{planner_configfolder}\\planners.json","r",encoding="utf-8") as planr:
            global removedname
            plans = planr.read().split('.json"')
            for i in range(0,len(plans)):
                plans[i] = plans[i][1:]
                if(plans[i]==f"{name}"):
                    removedname = i
                    os.remove(f"{plannersfolder}\\{name}.json")
        with open(f"{planner_configfolder}\\planners.json","w",encoding="utf-8") as plnr:
            for i in range(0,len(plans)-1):
                if(removedname!=i):
                    plnr.write(json.dumps(f"{plans[i]}.json",ensure_ascii=False))
        newplannereditor.place_forget()
        editorhelper.place_forget()
        plannertext.delete("1.0","end")
        isSaved=1          
        isMainActive=0

    def deleteError(self):
        global plannertext,errorline
        plannertext.delete(f"{float(errorline)}-1c",f"{float(errorline+1)}-1c")
        NewPlannerEditor.colorededitor(NewPlannerEditor)

    def deleteLine(self):
        global plannertext
        linelist = plannertext.get("1.0","end").split("\n")
        plannertext.delete(f"{float(len(linelist)-1)}","end")
        NewPlannerEditor.colorededitor(NewPlannerEditor)

    def deleteAll(self):
        global plannertext
        plannertext.delete("1.0","end")
        NewPlannerEditor.colorededitor(NewPlannerEditor)
    
    def elseButton(self):
        global plannertext
        linelist = plannertext.get("1.0","end").split("\n")
        plannertext.insert(f"{float(len(linelist))}","/else\n")
        NewPlannerEditor.colorededitor(NewPlannerEditor)

    def ifendButton(self):
        global plannertext
        linelist = plannertext.get("1.0","end").split("\n")
        plannertext.insert(f"{float(len(linelist))}","/ifend\n")
        NewPlannerEditor.colorededitor(NewPlannerEditor)
    
    def ifButton(self):
        global fororwhile
        fororwhile = "/if"
        self.forandwhilEntry()
        entryLabel.place_forget()
        forandwhilentry.place(width=290,height=30,x=10,y=750)
        entryButton.place(width=60,height=30,x=301,y=750)
    
    def forandwhilEntry(self):
        global plannertext,fororwhile
        linelist = plannertext.get("1.0","end").split("\n")
        value = forandwhilentry.get()
        if(value=="" or value==" " or value=="\n"):
            forandwhilentry.insert(0,"Please enter value.")
            forandwhilentry.delete(0,"end")
        else:
            plannertext.insert(f"{float(len(linelist))}",f"{fororwhile} {value}\n") 
            NewPlannerEditor.colorededitor(NewPlannerEditor)
            entryLabel.place(width=350,height=30,x=10,y=750)
            forandwhilentry.delete(0,"end")
            forandwhilentry.place_forget()
            entryButton.place_forget()
    
    def breakButton(self):
        global plannertext
        linelist = plannertext.get("1.0","end").split("\n")
        plannertext.insert(f"{float(len(linelist))}","/break\n")
        NewPlannerEditor.colorededitor(NewPlannerEditor)
        
    
    def whileButton(self):
        global fororwhile
        fororwhile = "/while"
        self.forandwhilEntry()
        entryLabel.place_forget()
        forandwhilentry.place(width=290,height=30,x=10,y=750)
        entryButton.place(width=60,height=30,x=301,y=750)
    
    def forButton(self):
        global fororwhile
        fororwhile = "/for"
        self.forandwhilEntry()
        entryLabel.place_forget()
        forandwhilentry.place(width=290,height=30,x=10,y=750)
        entryButton.place(width=60,height=30,x=301,y=750)

    def savePlanner(self):
        global isSaved,programinfo2,plannertext,name,textline,errorvalue,whilevalue,forvalue,ifvalue,savevalue,isMainActive,iseditmode,planneropener,interpreterbutton
        if(errorvalue==0):
            if(savevalue==1):
                downLabel4.config(text="  Warning: Can't save planner with active commands.",fg="orange")
            else:    
                editorhelper.place_forget()
                newplannereditor.place_forget()
                programinfo2.config(text=f"{name}")
                with open(f"{plannersfolder}\\{name}.json","w",encoding="utf-8") as theplanner:
                    texts = plannertext.get("1.0","end-1c")
                    text = texts.split("\n")
                    for i in range(0,len(text)):
                        theplanner.write(json.dumps(f'{text[i]}',ensure_ascii=False))
                plannertext.delete("1.0","end")
                isMainActive=0
                textline = 1.0
                isSaved=1
        else:
            downLabel4.config(text="  Warning: Can't save planner with errors.",fg="orange")
        if(iseditmode==1):
            planneropener.place(x=150,y=80,width=1620,height=900)
            iseditmode=0
        
class NewPlannerEditor(tk.Frame):
    def __init__(self,master=None,**kwags):
        super().__init__(master,**kwags)
        self.config(bg=darkgray)
        upLine = tk.Label(self,bg=mypurple)
        upLine.place(x=0,y=0,width=1300,height=1)
        downLine = tk.Label(self,bg=mypurple)
        downLine.place(x=0,y=849,width=1300,height=1)
        leftLine = tk.Label(self,bg=mypurple)
        leftLine.place(x=0,y=0,width=1,height=850)
        rightLine = tk.Label(self,bg=mypurple)
        rightLine.place(x=1299,y=0,width=1,height=850)
        
        global plannertext,textline,forvalue,whilevalue,ifvalue,errorvalue,downLabel1,downLabel2,downLabel3,downLabel4,errorline,runcolorededitor
        forvalue=whilevalue=ifvalue=errorvalue=errorline=0
        plannertext = tk.Text(self,bg="black",fg="white",insertbackground="white",border=0,font="Arial 10 bold")
        plannertext.place(x=10,y=10,width=1280,height=715)
        downLabel1 = tk.Label(self,bg=gray,fg="white",text=f"  Errors: {errorvalue}     Integreted Terminal",anchor="w")
        downLabel1.place(x=10,y=725,width=1280,height=25)
        downLabel2 = tk.Label(self,bg="black",fg="white",anchor="w")
        downLabel2.place(x=10,y=750,width=1280,height=30)
        downLabel3 = tk.Label(self,bg="black",fg="white",anchor="w")
        downLabel3.place(x=10,y=780,width=1280,height=30)
        downLabel4 = tk.Label(self,bg="black",fg="white",anchor="w")
        downLabel4.place(x=10,y=810,width=1280,height=30)
        runcolorededitor = tk.Button(self,command=self.colorededitor)
        plannertext.bind("<Return>",self.colorededitor)
        plannertext.bind("<BackSpace>",self.colorededitor)
        plannertext.bind("<space>",self.colorededitor)
        plannertext.bind("<Up>",self.colorededitor)
        plannertext.bind("<Down>",self.colorededitor)
        plannertext.bind("<Left>",self.colorededitor)
        plannertext.bind("<Right>",self.colorededitor)
        plannertext.bind("<Button-1>",self.colorededitor)
    
    def colorededitor(self,event=None):
        time.sleep(0.1)
        global plannertext,forvalue,whilevalue,ifvalue,ifvaluebreak,downLabel1,downLabel2,downLabel3,downLabel4,errorvalue,name,breakvalue,ifnum,savevalue,errorline,elsevalue
        allLines = plannertext.get("1.0","end")
        allLinen = allLines.split("\n")
        errorvalue=fornum=whilenum=breakvalue=ifvaluebreak=ifnum=elsevalue=0
        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
        downLabel2.config(text=" ")
        downLabel3.config(text=" ")
        for i in range(1,(len(allLinen))):
            line = plannertext.get(f"{float(i)}",f"{float(i)+1.0}-1c")
            keywords = line.split(" ")
            if(whilenum==0 and fornum==0):
                forvalue=whilevalue=0
            if(ifnum==0):
                ifvalue=0
            if(len(keywords)==1): 
                if(keywords[0]=="/for"):
                    if(whilevalue!=0):
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _ /for")
                        downLabel3.config(text=f"  Active /while cycle. Expected /break before /for.")
                        errorline = i
                    else:    
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /for _")
                        downLabel3.config(text=f"  Expected integer (turn).")
                        errorline = i
                elif(keywords[0]=="/while"):
                    if(forvalue!=0):
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _ /while")
                        downLabel3.config(text=f"  Active /for cycle. Expected /break before /while.")
                        errorline = i
                    else:    
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /while _")
                        downLabel3.config(text=f"  Expected string (term).")
                        errorline = i
                if(keywords[0]=="/break"):
                    if(forvalue==1 or whilevalue==1):
                        plannertext.tag_configure("custom_color4",foreground="blue")
                        plannertext.tag_add("custom_color4",float(i),f"{float(i)} lineend")
                        breakvalue=1
                        if(ifvaluebreak==0):
                            forvalue=whilevalue=savevalue=0
                        else:
                           ifvaluebreak=0    
                    else:
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _/break")
                        downLabel3.config(text=f"  Unexpected command. No active cycle before /break.")
                        errorline = i
                if(keywords[0]=="/if"):
                    errorvalue+=1
                    downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                    downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /if _")
                    downLabel3.config(text=f"  Expected string (term).")
                    errorline = i
                if(keywords[0]=="/else"):
                    if(ifvalue==1):
                        if(elsevalue==0):
                            plannertext.tag_configure("custom_color6",foreground="yellow")
                            plannertext.tag_add("custom_color6",float(i),f"{float(i)} lineend")
                            breakvalue=0
                            ifvaluebreak=elsevalue=1
                        else:
                            errorvalue+=1
                            downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                            downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _ /else")
                            downLabel3.config(text=f"  Unexpected command. No active /if before /else.")
                            errorline = i    
                    else:
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _/else")
                        downLabel3.config(text=f"  Unexpected command. No active /if before /else.")
                        errorline = i
                if(keywords[0]=="/ifend"):
                    if(ifvalue!=1):
                            errorvalue+=1
                            downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                            downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _/ifend")
                            downLabel3.config(text=f"  Unexpected command. No active /if before /ifend.")
                            errorline = i
                    else:
                            plannertext.tag_configure("custom_color7",foreground="purple")
                            plannertext.tag_add("custom_color7",float(i),f"{float(i)} lineend")
                            ifvalue=savevalue=elsevalue=ifvaluebreak=0
            if(len(keywords)==2):              
                if(keywords[0]=="/for"):
                    if(whilevalue!=0):
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _ /for")
                        downLabel3.config(text=f"  Active /while cycle. Expected /break before /for.")
                        errorline = i
                    else:
                        if(keywords[1]==None or keywords[1]=="" or keywords[1]==" " or keywords[1]=="\n"):
                            errorvalue+=1
                            downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                            downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /for _")
                            downLabel3.config(text=f"  Expected integer (turn).")
                            errorline = i
                        else:
                            if(forvalue==0):
                                try:
                                    value = str(keywords[1])
                                    a = int(value)
                                    plannertext.tag_configure("custom_color1",foreground="red")
                                    plannertext.tag_add("custom_color1",float(i),f"{float(i)} lineend")
                                    forvalue=savevalue=1
                                    fornum+=1
                                except:
                                    errorvalue+=1
                                    downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                                    downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /for _")
                                    downLabel3.config(text=f"  Expected integer (turn).")
                                    errorline = i
                            else:
                                errorvalue+=1
                                downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                                downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _ /for")
                                downLabel3.config(text=f"  Expected /break before /for.")
                                errorline = i
                if(keywords[0]=="/while"):
                    if(forvalue!=0):    
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i} _ /while")
                        downLabel3.config(text=f"  Active /for cycle. Expected /break before /while.")
                        errorline = i
                    if(whilevalue!=0):
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _ /while")
                        downLabel3.config(text=f"  Expected /break before /while.")
                        errorline = i
                    if(forvalue==0 and whilevalue==0):
                        if(keywords[1]==None or keywords[1]=="" or keywords[1]==" " or keywords[1]=="\n"):
                            errorvalue+=1
                            downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                            downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /while _")
                            downLabel3.config(text=f"  Expected string (term).")
                            errorline = i
                        else:
                            plannertext.tag_configure("custom_color2",foreground="orange")
                            plannertext.tag_add("custom_color2",float(i),f"{float(i)} lineend")
                            whilevalue=savevalue=1
                            whilenum+=1
                if(keywords[0]=="/break"):
                    if(keywords[1]==None or keywords[1]=="" or keywords[1]==" " or keywords[1]=="\n"):
                        pass
                    if(forvalue==0 and whilevalue==0):
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _/break")
                        downLabel3.config(text=f"  Unexpected command. No active cycle before /break.")
                        errorline = i
                    else:
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /break _")
                        downLabel3.config(text=f"  Unexpected string.")
                        errorline = i
                if(keywords[0]=="/if"):
                    if(ifvalue==1):
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _ /if")
                        downLabel3.config(text=f"  Expected /ifend before /if.")
                        errorline = i
                    if(keywords[1]==None or keywords[1]=="" or keywords[1]==" " or keywords[1]=="\n"):
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /if _")
                        downLabel3.config(text=f"  Expected string (term).")
                        errorline = i
                    if(ifvalue==0):
                        plannertext.tag_configure("custom_color3",foreground="pink")
                        plannertext.tag_add("custom_color3",float(i),f"{float(i)} lineend")
                        ifvalue=ifvaluebreak=savevalue=1
                        ifnum +=1
                if(keywords[0]=="/else"):
                    errorvalue+=1
                    downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                    downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /else _")
                    downLabel3.config(text=f"  Unexpected string.")
                    errorline = i
                if(keywords[0]=="/ifend"):
                    errorvalue+=1
                    downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                    downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /ifend _")
                    downLabel3.config(text=f"  Unexpected string.")
                    errorline = i
            if(len(keywords)>2):
                if(keywords[0]=="/for"):
                    if(whilevalue!=0): 
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _ /for")
                        downLabel3.config(text=f"  Active /while cycle. Expected /break before /while.")
                        errorline = i
                    else:    
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /for (turn) _")
                        downLabel3.config(text=f"  Unexpected string.")
                        errorline = i
                if(keywords[0]=="/while"):
                    if(forvalue!=0):                                                                           
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _ /while")
                        downLabel3.config(text=f"  Active /for cycle. Expected /break before /while.")
                        errorline = i
                    if(whilevalue!=0):                                                                            
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _ /while")
                        downLabel3.config(text=f"  Active /for cycle. Expected /break before /while.")
                        errorline = i
                if(keywords[0]=="/break"):
                    if(forvalue==0 and whilevalue==0):
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _/break")
                        downLabel3.config(text=f"  Unexpected command. No active cycle before /break.")
                        errorline = i
                    else:
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /break _")
                        downLabel3.config(text=f"  Unexpected string.")
                        errorline = i
                if(keywords[0]=="/if"):
                    if(ifvalue==0):
                        plannertext.tag_configure("custom_color3",foreground="pink")                                
                        plannertext.tag_add("custom_color3",float(i),f"{float(i)} lineend")
                        ifvalue=savevalue=1
                    else:
                        errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  _ /if")
                        downLabel3.config(text=f"  Expected /ifend before /if.")
                        errorline = i
                if(keywords[0]=="/else"):
                    errorvalue+=1  
                    downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                    downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /else _")
                    downLabel3.config(text=f"  Unexpected string.")
                    errorline = i
                if(keywords[0]=="/ifend"):
                    errorvalue+=1
                    downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                    downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {i}  /ifend _")
                    downLabel3.config(text=f"  Unexpected string.")
                    errorline = i
        if(errorvalue==0):
            downLabel4.config(text=" ") 

class NewPlanner(tk.Frame):
    def __init__(self,master=None,**kwags):
        super().__init__(master,**kwags)
        self.config(bg=darkgray)
        upLine = tk.Label(self,bg=mypurple)
        upLine.place(x=0,y=0,width=500,height=1)
        downLine = tk.Label(self,bg=mypurple)
        downLine.place(x=0,y=349,width=500,height=1)
        leftLine = tk.Label(self,bg=mypurple)
        leftLine.place(x=0,y=0,width=1,height=350)
        rightLine = tk.Label(self,bg=mypurple)
        rightLine.place(x=499,y=0,width=1,height=350)
        titlelabel = tk.Label(self,bg=gray,fg=lightgreen,text="Create New Planner",border=0)
        titlelabel.place(x=1,y=1,width=498,height=25)
        entergrouplabel = tk.Label(self,bg=gray,fg="white",text="  Please enter group: ",border=0)
        entergrouplabel.place(x=40,y=100,width=110,height=30)
        enterlabel = tk.Label(self,bg=gray,fg="white",text="  Please enter name: ",border=0)
        enterlabel.place(x=40,y=130,width=110,height=30)
        global enterplannername,enterplannergroup,createlabel
        enterplannergroup = tk.Entry(self,bg=gray,fg="white",insertbackground="white",border=0)
        enterplannergroup.place(x=150,y=100,width=310,height=30)
        enterplannername = tk.Entry(self,bg=gray,fg="white",insertbackground="white",border=0)
        enterplannername.place(x=150,y=130,width=310,height=30)
        closebutton = tk.Button(self,bg=gray,fg="red",border=0,text="Close",command=self.closeNewPlannerFrame)
        closebutton.place(x=5,y=320,width=80,height=25)
        createbutton = tk.Button(self,bg=gray,fg=lightgreen,border=0,text="Create",command=self.createNewPlanner)
        createbutton.place(x=414,y=320,width=80,height=25)
        createlabel = tk.Label(self,bg=gray,fg="orange",border=0,anchor="w")
        createlabel.place(x=40,y=160,width=420,height=30)

    def closeNewPlannerFrame(self):
        global programinfo2,isMainActive
        newplannerframe.place_forget()
        programinfo2.config(text="Running")
        enterplannername.delete(0,'end')
        enterplannergroup.delete(0,"end")
        isMainActive=0

    def createNewPlanner(self):
        global programinfo2,isMainActive,enterplannername,isSaved,newplannereditor,name,enterplannergroup,groupvalue,groupindex,createlabel
        groupvalue=0
        name = enterplannername.get()
        if(name=="" or name==" " or name=="\n"):
            createlabel.config(text="  You must enter name.")
        else:
            createlabel.config(text="")
            group = enterplannergroup.get()
            if(group=="" or group==" " or group=="\n"):
                group = "Unnamed Group"
            with open(f"{planner_configfolder}\\planners.json","r",encoding="utf-8") as planners:
                planer = planners.read().split('.json"')
                for i in range(0,len(planer)):
                    planer[i] = planer[i][1:]
                    if(f"/group:{group}" == planer[i]):
                        groupvalue=1
                        groupindex = i
                if(groupvalue==1):
                    planer.insert(groupindex+1,f"{name}")    
                    with open(f"{planner_configfolder}\\planners.json","w",encoding="utf-8") as planners:
                        for i in range(0,len(planer)-1):
                            planners.write(json.dumps(f"{planer[i]}.json",ensure_ascii=False))
                else:
                    with open(f"{planner_configfolder}\\planners.json","a",encoding="utf-8") as planners:
                        planners.write(json.dumps(f"/group:{group}.json",ensure_ascii=False))
                        planners.write(json.dumps(f"{name}.json",ensure_ascii=False))
            with open(f"{plannersfolder}\\{name}.json","w",encoding="utf-8") as newPlanner:
                newPlanner.write(json.dumps("0:Planner Starts",ensure_ascii=False))
            newplannereditor.place(x=100,y=90,width=1300,height=850)
            editorhelper.place(height=850,width=370,x=1450,y=90)
            enterplannername.delete(0,'end')
            enterplannergroup.delete(0,'end')
            newplannerframe.place_forget()
            isSaved=0
            programinfo2.config(text="Planning")
        
class SideBarDeleteButtons(tk.Button):
    def __init__(self,index,text,master=None,**kwags):
        super().__init__(master,**kwags)
        self.index = index
        self.text = text
        self.config(bg=darkred,fg="white",text="Delete",border=0,command=self.deleteindexplanner)

    def deleteindexplanner(self):
        global currentpage,plannersfolder,planner_configfolder,refreshbutton
        removegroup = -1
        os.remove(f"{plannersfolder}\\{self.text}.json")
        with open(f"{planner_configfolder}\\planners.json","r",encoding="utf-8") as planners:
            global removename
            planer = planners.read().split('.json"')
            for i in range(0,len(planer)):
                planer[i] = planer[i][1:]
                if(planer[i]==f"{self.text}"):
                    removename = i
            if(removename+2>len(planer)-1):
                if('/group' in planer[removename-1]):  
                    removegroup = removename-1
            else:
                if('/group' in planer[removename-1] and '/group' in planer[removename+1]):
                    removegroup = removename-1
        with open(f"{planner_configfolder}\\planners.json","w",encoding="utf-8") as plnr:
            for i in range(0,len(planer)-1):
                if(removename!=i and removegroup!=i):
                    plnr.write(json.dumps(f"{planer[i]}.json",ensure_ascii=False))  
        refreshbutton.invoke()

class SideBarGroupLabels(tk.Label):
    def __init__(self,text,master=None,**kwags):
        super().__init__(master,**kwags)
        self.text = text
        self.config(bg=gray,fg="orange",text=f"{text}",border=0)

class SideBarOpenButtons(tk.Button):
    def __init__(self,index,text,master=None,**kwags):
        super().__init__(master,**kwags)
        self.index = index
        self.text = text
        self.config(bg=gray,fg="white",text=f"{text}",border=0,command=self.openplanner)
    
    def openplanner(self):
        global planneropener,isMainActive,textname,planner_configfolder,refreshbutton,tabcurrent,tabtotal,tabbuttonlist,name,interpretername,interpreterbutton
        textname = self.text
        sidebar.place_forget()
        isMainActive=1
        with open(f"{planner_configfolder}\\tabs.json","a",encoding="utf-8") as tabs:
            tabs.write(json.dumps(f"{textname}.json",ensure_ascii=False))
        planneropener.place(x=150,y=80,width=1620,height=900)
        tabcurrent = int((len(tabbuttonlist)/6)+1)
        tabrefresh.invoke()
        tabbuttonlist[len(tabbuttonlist)-1].config(bg=activepurple)
        tabbuttonlist[len(tabbuttonlist)-1].focusplanner()
        interpretername=name=tabbuttonlist[len(tabbuttonlist)-1].text
        interpreterbutton.invoke()
        
class SideBar(tk.Frame):
    def __init__(self,master=None,**kwags):
        super().__init__(master,**kwags)
        self.config(bg=darkgray)

        leftLine = tk.Label(self,bg=mypurple)
        leftLine.place(x=0,y=0,height=1005,width=1)
        rightLine = tk.Label(self,bg=mypurple)
        rightLine.place(x=319,y=0,height=1005,width=1)
        upLine = tk.Label(self,bg=gray)
        upLine.place(x=61,y=925,width=200,height=1)
        downLine = tk.Label(self,bg=gray)
        downLine.place(x=61,y=959,width=200,height=1)
        self.plannername()
        closebutton = tk.Button(self,bg=gray,fg="white",border=0,text="Close",command=self.closesidebar)
        closebutton.place(x=235,y=975,width=80,height=25)
        global refreshbutton
        refreshbutton = tk.Button(self,bg=gray,fg="white",border=0,text="Refresh",command=self.plannername)
        refreshbutton.place(x=6,y=975,width=80,height=25)
        nextbutton = tk.Button(self,bg=gray,fg="white",border=0,text=">",command=self.nextpage,font="Arial 12 bold")
        nextbutton.place(x=221,y=930,width=40,height=25)
        previousbutton = tk.Button(self,bg=gray,fg="white",border=0,text="<",command=self.previouspage,font="Arial 12 bold")
        previousbutton.place(x=61,y=930,width=40,height=25) 
        global currentpage,totalpage,namelist,pageinfo
        currentpage=1
        if(len(namelist)%15==0 and len(namelist)>0):
            totalpage = (len(namelist)//15)
        else:
            totalpage = (len(namelist)//15)+1
        pageinfo = tk.Label(self,bg=gray,fg="white",border=0,text=f"{currentpage}/{totalpage}",font="Arial 12")
        pageinfo.place(x=131,y=930,width=60,height=25)

    def closesidebar(self):
        global isMainActive,programinfo2
        sidebar.place_forget()
        programinfo2.config(text="Running")
        isMainActive=0

    def nextpage(self):
        global currentpage,totalpage,pageinfo
        if(currentpage<totalpage):
            currentpage+=1
            pageinfo.config(text=f"{currentpage}/{totalpage}")
            self.plannername()

    def previouspage(self):
        global currentpage
        if(currentpage>1):
            currentpage-=1
            pageinfo.config(text=f"{currentpage}/{totalpage}")
            self.plannername()

    def plannername(self):
        global names,namelist,totalpage
        with open(f"{planner_configfolder}\\planners.json","r",encoding="utf-8") as plannernames:
            names = plannernames.read()
            namelist = names[1:len(names)-1].split('""')
            pageinfo = tk.Label(self,bg=gray,fg="white",border=0,text=f"{currentpage}/{totalpage}",font="Arial 12")
            pageinfo.place(x=131,y=930,width=60,height=25)
            pageinfo.config(text=f"{currentpage}/{totalpage}")    
            if(len(namelist)%15==0 and len(namelist)>0):
                totalpage = (len(namelist)//15)
            else:
                totalpage = (len(namelist)//15)+1
            if(15*currentpage>len(namelist)):
                    for i in range(0+15*(currentpage-1),len(namelist)):
                        if("/group" not in namelist[i]):
                            openbuttons = SideBarOpenButtons(i,f"{namelist[i][0:len(namelist[i])-5]}",self)
                            openbuttons.place(x=30,y=90+45*(i-15*(currentpage-1)),width=200,height=40)
                            deletebuttons = SideBarDeleteButtons(i,f"{namelist[i][0:len(namelist[i])-5]}",self)
                            deletebuttons.place(x=231,y=90+45*(i-15*(currentpage-1)),width=60,height=40)
                        else:
                            grouplabels = SideBarGroupLabels(f"{namelist[i][7:len(namelist[i])-5]}",self)
                            grouplabels.place(x=30,y=90+45*(i-15*(currentpage-1)),width=261,height=40)
                    for i in range(len(namelist)-15*(currentpage-1),15):
                        openbuttons = SideBarOpenButtons(i," ",self)
                        openbuttons.place(x=30,y=90+45*i,width=200,height=40)
                        deletebuttons = SideBarDeleteButtons(i," ",self)
                        deletebuttons.place(x=231,y=90+45*i,width=60,height=40)
            else:
                for i in range(0+15*(currentpage-1),15*currentpage):
                    if("/group" not in namelist[i]):
                        openbuttons = SideBarOpenButtons(i,f"{namelist[i][0:len(namelist[i])-5]}",self)
                        openbuttons.place(x=30,y=90+45*(i-15*(currentpage-1)),width=200,height=40)
                        deletebuttons = SideBarDeleteButtons(i,f"{namelist[i][0:len(namelist[i])-5]}",self)
                        deletebuttons.place(x=231,y=90+45*(i-15*(currentpage-1)),width=60,height=40)
                    else:
                        grouplabels = SideBarGroupLabels(f"{namelist[i][7:len(namelist[i])-5]}",self)
                        grouplabels.place(x=30,y=90+45*(i-15*(currentpage-1)),width=261,height=40)
            if(len(namelist)%15==0 and len(namelist)>0):
                totalpage = (len(namelist)//15)
            else:
                totalpage = (len(namelist)//15)+1
            pageinfo.config(text=f"{currentpage}/{totalpage}")  

class tabclosebuttons(tk.Button):
    def __init__(self,index,text,master=None,**kwags):
        super().__init__(master,**kwags)
        global tabsname
        self.index = index
        self.text = text
        self.config(bg=darkred,fg="white",text="X",width=2,height=1,command=self.closetabs)
        tabsname = self.text

    def closetabs(self):
        global tabsname,tabrefresh,planneropener,isMainActive,tabbuttonlist
        tabsname = self.text
        previoustab = self.index-1
        with open(f"{planner_configfolder}\\tabs.json","r",encoding="utf-8") as tabsread:
            global closetab
            tablist = tabsread.read().split('.json"')
            for i in range(0,len(tablist)):
                tablist[i] = tablist[i][1:]
                if(tablist[i]==tabsname):
                    closetab = i
        with open(f"{planner_configfolder}\\tabs.json","w",encoding="utf-8") as tabswrite:
            for i in range(0,len(tablist)-1):
                if(i!=closetab):
                    tabswrite.write(json.dumps(f"{tablist[i]}.json",ensure_ascii=False))
        with open(f"{planner_configfolder}\\tabs.json","r",encoding="utf-8") as tabsread:
            if(tabsread.read()=='' or tabsread.read()==' ' or tabsread.read()==None or tabsread.read()=='\n'):
                isMainActive=0
        with open(f"{planner_configfolder}\\lasttab.json","w",encoding="utf-8") as lasttabinfo:
            lasttabinfo.write(json.dumps(f"{tabbuttonlist[previoustab].text}",ensure_ascii=False))
        planneropener.place_forget()
        tabrefresh.invoke()


class tabbuttons(tk.Button):
    def __init__(self,index,text,master=None,**kwargs):
        super().__init__(master,**kwargs)
        self.index = index
        self.text = text
        self.config(bg=darkpurple,fg="white",text=f"{text}",width=25,height=1,command=self.focusplanner)
    
    def focusplanner(self):
        global name,planneropener,tabbuttonlist,tablist,isMainActive,planner_configfolder,interpretername,interpreterbutton,iseditmode,stepline,countturn
        if(iseditmode==0):
            index = self.index
            interpretername = name = self.text
            with open(f"{planner_configfolder}\\lasttab.json","w",encoding="utf-8") as lasttabinfo:
                lasttabinfo.write(json.dumps(f"{self.text}",ensure_ascii=False))
            planneropener.place(x=150,y=80,width=1620,height=900)
            for i in range(0,len(tablist)):
                if(i!=index):
                    tabbuttonlist[i].config(bg=darkpurple)
                else:
                    tabbuttonlist[i].config(bg=activepurple)
            isMainActive=1
            countturn=0
            interpreterbutton.invoke()
            stepline=0
            

class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Code Planner V0.1 Beta")
        self.geometry("1920x1080")
        self.resizable(False,False)
        self.state("zoomed")
        self.config(bg=darkpurple)

        self.firstRun()
        upLine1 = tk.Label(self,bg=mypurple)
        upLine1.place(x=0,y=1,width=1920,height=2)
        tabsbar = tk.Label(self,bg=darkpurple,fg="white",text="Active Planners",font="Arial 12")
        tabsbar.place(x=0,y=4,width=150,height=30)
        upLine2 = tk.Label(self,bg=mypurple)
        upLine2.place(x=0,y=35,width=1920,height=1)

        
        downLine1 = tk.Label(self,bg=mypurple)
        downLine1.place(x=0,y=1041,width=1920,height=1)
        global programinfo,programinfo2,programinfo3,filepath,plannersfolder,planner_configfolder,tabrefresh,interpretername
        programinfo = tk.Label(self,bg=darkpurple,fg="white",text="Developed By Chikosfer               Status:",font="Arial 8",anchor="w")
        programinfo.place(x=0,y=1042,width=200,height=14)
        programinfo2 = tk.Label(self,bg=darkpurple,fg="white",text="Running",font="Arial 8",anchor="w")
        programinfo2.place(x=200,y=1042,width=1000,height=14)
        programinfo3 = tk.Label(self,bg=darkpurple,fg="white",text="Code Planner V0.1 Beta",font="Arial 8",anchor="e")
        programinfo3.place(x=1718,y=1042,width=200,height=14)
        downLine2 = tk.Label(self,bg=mypurple)
        downLine2.place(x=0,y=1056,width=1920,height=1)
        
        leftLine = tk.Label(self,bg=mypurple)
        leftLine.place(x=0,y=0,width=1,height=1080)
        leftLine2 = tk.Label(self,bg=mypurple)
        leftLine2.place(x=148,y=1,width=1,height=34)
        rightLine = tk.Label(self,bg=mypurple)
        rightLine.place(x=1919,y=0,width=1,height=1080)
        rightLine2 = tk.Label(self,bg=mypurple)
        rightLine2.place(x=1660,y=1,width=1,height=34)

        openbuton = tk.Button(self,bg=darkgray,fg="white",border=0,text="Open",command=self.opensidebar)
        openbuton.place(x=1780,y=4,width=50,height=30)
        newbutton = tk.Button(self,bg=darkgray,fg="white",border=0,text="New",command=self.openNewPlannerFrame)
        newbutton.place(x=1726,y=4,width=50,height=30)
        fullscreenbutton = tk.Button(self,bg=darkgray,fg="white",border=0,text="Full Screen",command=self.fullscreenmode)
        fullscreenbutton.place(x=1834,y=4,width=80,height=30)
        nexttabsbutton = tk.Button(self,bg=gray,fg=lightgreen,border=0,text=">",command=self.nexttabsbutton)
        nexttabsbutton.place(x=1645,y=4,width=15,height=30)
        previoustabsbutton = tk.Button(self,bg=gray,fg=lightgreen,border=0,text="<",command=self.previoustabsbutton)
        previoustabsbutton.place(x=150,y=4,width=15,height=30)
        tabrefresh = tk.Button(self,bg=darkgray,fg="white",text="Refresh",border=0,command=self.tabplaceforget)
        tabrefresh.place(x=1661,y=4,width=60,height=30)


        global sidebar,newplannerframe,newplannereditor,editorhelper,planneropener,tabcurrent,firsttab
        tabcurrent=firsttab=1
        sidebar = SideBar(self)
        newplannerframe = NewPlanner(self)
        newplannereditor = NewPlannerEditor(self)
        editorhelper = EditorHelper(self)
        planneropener = PlannerOpen(self)
        self.nametabs()
    
    def tabplaceforget(self):
        global tabbuttonlist,tabclosebuttonlist
        for i in range(0,len(tabbuttonlist)):
            tabbuttonlist[i].place_forget()
            tabclosebuttonlist[i].place_forget()
        self.nametabs()
    
    def nametabs(self):
        global refreshbutton,tabbutton,tabdeletebutton,tabbuttonlist,tabclosebuttonlist,tabtotal,tablist,firsttab,tabcurrent # sekmelere önceki ve sonraki butonu ekleme
        tabbuttonlist = []
        tabclosebuttonlist = []
        with open(f"{planner_configfolder}\\tabs.json","r",encoding="utf-8") as tabsread:
            tablist = tabsread.read().split('.json"')
            tablist.pop(-1)
            for i in range(0,len(tablist)):
                if(tablist[i]!='' and tablist[i]!=' ' and tablist[i]!='\n'):
                    tablist[i] = tablist[i][1:]
                    tabbutton = tabbuttons(i,f"{tablist[i]}",self)
                    tabbuttonlist.append(tabbutton)
                    tabdeletebutton = tabclosebuttons(i,f"{tablist[i]}",self)
                    tabclosebuttonlist.append(tabdeletebutton)
            with open(f"{planner_configfolder}\\lasttab.json","r",encoding="utf-8") as lasttabinfo:
                global name
                lasttab = lasttabinfo.read()
                index=0
                if(((lasttab!=' ' and lasttab!='" "') and lasttab!=" ") and ((lasttab!=None and lasttab!='') and lasttab!='\n')):
                    for i in range(0,len(tabbuttonlist)):
                        if(f'"{tabbuttonlist[i].text}"'==lasttab):
                            index = i
                    try:
                        tabbuttonlist[index].config(bg=activepurple)
                        tabbuttonlist[index].focusplanner()
                        name=tabbuttonlist[index].text
                        tabcurrent = int((index/6)+1)
                    except:
                        pass
            if(len(tablist)%6==0):
                tabtotal = len(tabbuttonlist)//6
            else:
                tabtotal = (len(tabbuttonlist)//6)+1
            if(6*tabcurrent>len(tabbuttonlist)):
                for i in range(6*(tabcurrent-1),len(tabbuttonlist)):
                    tabbuttonlist[i].place(x=190+240*(i-6*(tabcurrent-1)),y=6)
                    tabclosebuttonlist[i].place(x=370+240*(i-6*(tabcurrent-1)),y=6)
            else:    
                for i in range(6*(tabcurrent-1),6*tabcurrent):
                    tabbuttonlist[i].place(x=190+240*(i-6*(tabcurrent-1)),y=6)
                    tabclosebuttonlist[i].place(x=370+240*(i-6*(tabcurrent-1)),y=6)

    def previoustabsbutton(self):
        global tabcurrent,tabrefresh
        if(tabcurrent>1):
            tabcurrent-=1
        tabrefresh.invoke()

    def nexttabsbutton(self):
        global tabcurrent,tabrefresh,tabtotal
        if(tabcurrent<tabtotal):
            tabcurrent+=1
        tabrefresh.invoke()
    
    def fullscreenmode(self):
        self.state("zoomed")
    
    def opensidebar(self):
        global isMainActive,sidebar,programinfo2
        if(isMainActive==0):
            sidebar.place(x=1600,y=36,width=320,height=1005)
            programinfo2.config(text="Choosing")
            SideBar.plannername(sidebar)
            isMainActive=1

    def openNewPlannerFrame(self):
        global isMainActive,programinfo2,newplannerframe
        if((isMainActive==0) and (isSaved==1)):
            programinfo2.config(text="Creating")
            newplannerframe.place(x=710,y=360,width=500,height=350)
            isMainActive=1

    def firstRun(self):
        global filepath,plannersfolder,planner_configfolder
        filepathpy = os.path.abspath(__file__)
        filepath = os.path.dirname(filepathpy)
        plannersfolder = f"{filepath}\\planners"
        planner_configfolder = f"{filepath}\\planner_config"        
        if(os.path.exists(plannersfolder)==False):
            os.makedirs(plannersfolder)
        if(os.path.exists(planner_configfolder)==False):
            os.makedirs(planner_configfolder)
        if(os.path.isfile(f"{planner_configfolder}\\planners.json")==False):
            with open(f"{planner_configfolder}\\planners.json","w",encoding="utf-8") as test1:
                pass
        if(os.path.isfile(f"{planner_configfolder}\\tabs.json")==False):    
            with open(f"{planner_configfolder}\\tabs.json","w",encoding="utf-8") as test2:
                pass
        if(os.path.isfile(f"{planner_configfolder}\\lasttab.json")==False):    
            with open(f"{planner_configfolder}\\lasttab.json","w",encoding="utf-8") as test2:
                pass
           

app = MainPage()
app.mainloop()



    
        
