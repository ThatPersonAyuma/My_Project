import tkinter as tk

class Call:
    def __init__(self):
        self.display_number=0
        self.input_number=0
        self.type=0
        self.place_holder=0
        self.number_store=["a"]

    def instruction_dis(self):
        number=0
        if "." in self.number_store:
            temporaly=""
            for i in self.number_store:
                temporaly+=str(i)
            float_num=(temporaly).split(".")
            count=0
            for i in float_num[1]:
                if i == "0":
                    pass
                else:
                    count+=1
            if count != 0:
                temporaly1=""
                for i in float_num[0]:
                    if i == "a" or i == "-":
                        pass
                    else:
                        temporaly1+=str(i)  
                temporaly1+="."
                for i in float_num[1]:
                    temporaly1+=str(i)
                number=round(float(temporaly1),4)
                if len(float_num[1])>4:
                    for i in range(0, len(float_num[1])-4):
                        self.number_store.pop()
            else:
                temporaly1=""
                for i in float_num[0]:
                    if i == "a" or i == "-":
                        pass
                    else:
                        temporaly1+=str(i)
                number=int(temporaly1)
                self.number_store.pop()
                self.number_store.pop()
        else:
            for i, item in enumerate(reversed(self.number_store)):
                try:
                    number+=item*10**i
                except:
                    break
        if self.number_store[0]=="-":
            number=number*(-1)
        if self.type==0:
            self.display_number=number
        elif self.type==1:
            self.input_number=number
        else:
            pass
        display.config(text=number)

    def init(self, inpnum:int)->list:
        if "." in self.number_store:
            count=""
            for i in self.number_store:
                try:
                    count+=str(i)
                except:
                    pass
            count=count.split(".")
            if len(count[1])>3:
                pass
            else:
                self.number_store.append(inpnum)
                self.instruction_dis()
        else:
            self.number_store.append(inpnum)
            self.instruction_dis()

    def instruction_sum(self):
        self.number_store.clear()
        self.number_store.append("a")
        self.place_holder=1
        self.type=1
        self.instruction_dis()
    def get_instruction_sum(self):
        self.instruction_sum()

    def instruction_float(self):
        if "." not in self.number_store:
            for i in ["."]:
                self.number_store.append(i)
        self.instruction_dis
    def get_instruction_float(self):
        self.instruction_float()

    def instruction_subtrac(self):
        if len(self.number_store)==1:
            self.type=0
            if self.display_number!=0:
                self.type=1
        else:
            self.type=1
            self.place_holder=1
        self.number_store.clear()
        self.number_store.append("-")
        self.instruction_dis()
    def get_instruction_subtrac(self):
        self.instruction_subtrac()

    def instruction_multiply(self):
        self.number_store.clear()
        self.number_store.append("a")
        self.place_holder=2
        self.type=1
        self.instruction_dis()
    def get_instruction_multiply(self):
        self.instruction_multiply()

    def instruction_divide(self):
        self.number_store.clear()
        self.number_store.append("a")
        self.place_holder=3
        self.type=1
        self.instruction_dis()
    def get_instruction_divide(self):
        self.instruction_divide()

    def instruction_power(self):
        self.number_store.clear()
        self.number_store.append("a")
        self.place_holder=4
        self.type=1
        self.instruction_dis()
    def get_instruction_power(self):
        self.instruction_power()

    def instruction_root(self):
        self.number_store.clear()
        self.number_store.append("a")
        self.place_holder=5
        self.type=1
        self.instruction_dis()
    def get_instruction_root(self):
        self.instruction_root()

    def backspace(self):
        if len(self.number_store)!=1:
            try:
                self.number_store.pop()
                self.instruction_dis()
            except:
                pass
        elif len(self.number_store)==1:
            self.number_store[0]="a"
            if self.input_number==0:
                self.type=0
                self.place_holder=0
                self.number_store[0]="a"
                for x in str(self.display_number):
                    if x == "-":
                        self.number_store[0]="-"
                    else:
                        self.number_store.append(int(x))
                self.instruction_dis()
        return self.number_store, self.place_holder, self.type, self.display_number, self.input_number
    def get_backspace(self):
        self.backspace()

    def clear(self):
        self.number_store.clear()
        self.number_store.append("a")
        self.place_holder=0
        self.display_number=0
        self.input_number=0
        self.type=0
        self.instruction_dis()
    def output(self): 
        if self.place_holder==1:
            self.display_number += self.input_number
        elif self.place_holder==2:
            self.display_number*=self.input_number     
        elif self.place_holder==3:
            self.display_number=self.display_number/self.input_number
        elif self.place_holder==4:
            count=1
            if "-"in self.number_store:
                for i in range(0, self.input_number*-1):
                    count*=self.display_number
                self.display_number=1/count
            else:
                for i in range(0, self.input_number):
                    count*=self.display_number
            self.display_number=count
        elif self.place_holder==5:
            self.display_number**=(1/self.input_number)
        self.number_store=["a"]
        for x in str(self.display_number):
            if x == "-":
                self.number_store[0]="-"
            elif x=="a":
                self.number_store[0]="a"
            elif x==".":
                self.number_store.append(x)
            elif x=="e":
                pass
            else:    
                self.number_store.append(int(x))
        if int(self.display_number)==self.display_number:
            self.display_number=int(self.display_number)
        self.place_holder=0
        self.input_number=0
        self.type=0
        self.instruction_dis()
    def get_output(self):
        self.output()

call=Call()
#the app
window=tk.Tk()
window.geometry("350x400+500+150")
window.resizable(width=True,height=True)
window.title("CALCULATOR")

frame1 = tk.Frame(window, background="black", relief="raised", bd=5, height=50)
frame1.pack(fill="both")
display = tk.Label(
    frame1,
    text="0",
    font=('ariel',40,'bold'),
    fg="green",
    relief="raised",
    justify="right",
    background="black",
    bd=0
    )
display.grid(row=0, column= 0, sticky="NE")

frame2 = tk.Frame(window)
frame2.pack(fill="both", expand=True) #expand true to follow the parent that is frame1

button1 = tk.Button(
    frame2,
    text="1",
    bg="orange",
    activebackground="yellow",
    command=lambda:call.init(1)
)
button1.grid(row=2,column=0, sticky="NSEW")

button2 = tk.Button(
    frame2,
    text="2",
    bg="orange",
    activebackground="yellow",
    command=lambda:call.init(2)
)
button2.grid(row=2,column=1, sticky="NSEW")

button3 = tk.Button(
    frame2,
    text="3",
    bg="orange",
    activebackground="yellow",
    command=lambda:call.init(3)
)
button3.grid(row=2,column=2, sticky="NSEW")

button4 = tk.Button(
    frame2,
    text="4",
    bg="orange",
    activebackground="yellow",
    command=lambda:call.init(4)
)
button4.grid(row=3,column=0, sticky="NSEW")

button5 = tk.Button(
    frame2,
    text="5",
    bg="orange",
    activebackground="yellow",
    command=lambda:call.init(5)
)
button5.grid(row=3,column=1, sticky="NSEW")

button6 = tk.Button(
    frame2,
    text="6",
    bg="orange",
    activebackground="yellow",
    command=lambda:call.init(6)
)
button6.grid(row=3,column=2, sticky="NSEW")

button7 = tk.Button(
    frame2,
    text="7",
    bg="orange",
    activebackground="yellow",
    command=lambda:call.init(7)
)
button7.grid(row=4,column=0, sticky="NSEW")

button8 = tk.Button(
    frame2,
    text="8",
    bg="orange",
    activebackground="yellow",
    command=lambda:call.init(8)
)
button8.grid(row=4,column=1, sticky="NSEW")

button9 = tk.Button(
    frame2,
    text="9",
    bg="orange",
    activebackground="yellow",
    command=lambda:call.init(9)
)
button9.grid(row=4,column=2, sticky="NSEW")

button0 = tk.Button(
    frame2,
    text="0",
    bg="orange",
    activebackground="yellow",
    command=lambda:call.init(0)
)
button0.grid(row=5,column=1, sticky="NSEW")

buttonBack = tk.Button(
    frame2,
    text="<x|",
    bg="orange",
    activebackground="yellow",
    command=call.get_backspace
)
buttonBack.grid(row=6,column=2, sticky="NSEW")


buttonClear = tk.Button(
    frame2,
    text="Clear",
    bg="orange",
    activebackground="yellow",
    command=call.clear
)
buttonClear.grid(row=5,column=2, sticky="NSEW")

buttonA = tk.Button(
    frame2,
    text="+",
    bg="orange",
    activebackground="yellow",
    command=call.get_instruction_sum
)
buttonA.grid(row=1,column=0, sticky="NSEW")

buttonB = tk.Button(
    frame2,
    text="-",
    bg="orange",
    activebackground="yellow",
    command=call.get_instruction_subtrac
)
buttonB.grid(row=1,column=1, sticky="NSEW")

buttonC = tk.Button(
    frame2,
    text="x",
    bg="orange",
    activebackground="yellow",
    command=call.get_instruction_multiply
)
buttonC.grid(row=1,column=2, sticky="NSEW")

buttonD = tk.Button(
    frame2,
    text=":",
    bg="orange",
    activebackground="yellow",
    command=call.get_instruction_divide
)
buttonD.grid(row=1,column=3, sticky="NSEW")

buttonF = tk.Button(
    frame2,
    text=".",
    bg="orange",
    activebackground="yellow",
    command=call.get_instruction_float
)
buttonF.grid(row=5,column=0, sticky="NSEW")

buttonG = tk.Button(
    frame2,
    text="power",
    bg="orange",
    activebackground="yellow",
    command=call.get_instruction_power
)
buttonG.grid(row=6,column=0, sticky="NSEW")

buttonH = tk.Button(
    frame2,
    text="√x",
    bg="orange",
    activebackground="yellow",
    command=call.get_instruction_root
)
buttonH.grid(row=6,column=1, sticky="NSEW")

buttonR = tk.Button(
    frame2,
    text="=",
    bg="orange",
    activebackground="yellow",
    command=call.get_output
)
buttonR.grid(row=2,column=3, sticky="NSEW", rowspan=5)

frame1.rowconfigure(0, weight=1, minsize=50)
frame1.grid_columnconfigure(0, weight=1, minsize=50)
frame2.rowconfigure(1, weight=1, minsize=50)
frame2.rowconfigure(2, weight=1, minsize=50)
frame2.rowconfigure(3, weight=1, minsize=50)
frame2.rowconfigure(4, weight=1, minsize=50)
frame2.rowconfigure(5, weight=1, minsize=50)
frame2.rowconfigure(6, weight=1, minsize=50)
frame2.grid_columnconfigure(0, weight=1, minsize=50)
frame2.grid_columnconfigure(1, weight=1, minsize=50)
frame2.grid_columnconfigure(2, weight=1, minsize=50)
frame2.grid_columnconfigure(3, weight=1, minsize=50)

window.mainloop()