"""import tkinter as tk 


#Veriables

buttons = ["button1","button2","button3","button4","button5"]

#Classes And Functions

class index_buton(tk.Button()):
    def __init__(self,index):
        super().__init__()
        self.index = index


#User Interface

root = tk.Tk()
root.title("Trying New Things")
root.geometry("700x550")

for i in range(0,5):
    buttons[i] = index_buton(i)
    buttons[i].config(bg="gray",fg="white",text=f"LittleButton{i}")
    buttons[i].place(width=80,height=30,x=100,y=50+i*35)

root.mainloop()


import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master=None,index=-1, **kwargs):
        super().__init__(master, **kwargs)
        self.index = index

root = tk.Tk()
root.geometry("500x500")
custom_button = CustomButton(root, text="Custom Button",index=7)
custom_button.pack()
print(custom_button.index)
root.mainloop()

import tkinter as tk

class CustomButton(tk.Button):
    def __init__(self, master=None, index=-1, **kwargs):
        super().__init__(master, **kwargs)
        self.index = index
        self.configure(command=self.button_clicked)  # Butonun tıklandığında çağrılacak fonksiyonu ayarla

    def button_clicked(self):
        print(f"Buton {self.index}'a tıklandı")

root = tk.Tk()
root.geometry("500x500")

# 5 farklı index değeri ile butonları oluştur
for i in range(5):
    custom_button = CustomButton(root, text=f"Custom Button {i}", index=i)
    custom_button.pack()

root.mainloop()

import tkinter as tk

def get_text():
    text = text_box.get("1.0", "end-1c")  # Get the text from the Text widget
    print(text)

root = tk.Tk()

text_box = tk.Text(root, height=5, width=30)  # Text widget with height and width parameters
text_box.pack()

button = tk.Button(root, text="Get Text", command=get_text)
button.pack()

root.mainloop()"""