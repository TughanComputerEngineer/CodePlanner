def colorededitor(self,event):
        global plannertext,forvalue,whilevalue,ifvalue,downLabel1,downLabel2,downLabel3,downLabel4,errorvalue,name,errorline
        allLines = plannertext.get("1.0","end")
        allLinen = allLines.split("\n")
        for i in range(1,(len(allLinen))):
            line = plannertext.get(f"{float(i)}",f"{float(i)+1.0}-1c")
            keywords = line.split(" ") 
            if(forvalue==0 and whilevalue==0):
                if(keywords[0]=="/for"):
                    if(len(keywords)==1):
                        errorline = float(i)
                        if(errorline==float(i)):
                            errorvalue+=1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {int(errorline)}  /for _")
                        downLabel3.config(text=f"  Expected integer (turn).")
                    elif(keywords[1]==None or keywords[1]=="" or keywords[1]==" " or keywords[1]=="\n"):
                        errorline = float(i)
                        if(errorline==float(i)):
                            errorvalue += 1
                        downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                        downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {int(i)}  /for _")
                        downLabel3.config(text=f"  Expected integer (turn).")
                    else:
                        plannertext.tag_configure("custom_color1",foreground="red")
                        plannertext.tag_add("custom_color1",float(i),f"{float(i)} lineend")
                        errorvalue-=1
                        if(errorvalue==0):
                            downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                            downLabel2.config(text=" ")
                            downLabel3.config(text=" ")
                        else:
                            downLabel1.config(text=f"  Errors: {errorvalue}     Integreted Terminal")
                            downLabel2.config(text=f"  C:\\CodePlanner\\{name}  line: {int(errorline)}  /for _")
                            downLabel3.config(text=f"  Expected integer (turn).")
                        forvalue=1
                elif(keywords[0]=="/while"):
                    plannertext.tag_configure("custom_color2",foreground="orange")
                    plannertext.tag_add("custom_color2",float(i),f"{float(i)} lineend")
                    whilevalue=1
                elif(keywords[0]=="/if"):
                    plannertext.tag_configure("custom_color3",foreground="pink")
                    plannertext.tag_add("custom_color3",float(i),f"{float(i)} lineend")
            else:
                if(keywords[0]=="/break"):
                    plannertext.tag_configure("custom_color4",foreground="blue")
                    plannertext.tag_add("custom_color4",float(i),f"{float(i)} lineend")
                    forvalue=whilevalue=0
                elif(keywords[0]=="/if"):
                    plannertext.tag_configure("custom_color5",foreground="pink")
                    plannertext.tag_add("custom_color5",float(i),f"{float(i)} lineend")