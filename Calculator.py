from tkinter import * 
import math 
 
class Application(Frame): 
    def __init__(self, master): 
        super(Application, self).__init__(master) 
        self.grid() 
        # создадим переменную, которая хранит в себе результат подсчёта 
        self.result = "" 
        # создадим функцию, которая отображает кнопки и поле 
        self.createWidgets() 
         
         
     
    def createWidgets(self): 
        # self.textResult = Entry(self, width=21, font='Times 17', justify='right') 
        self.textResult = Text(self, width=21, height=1, font='Times 17', wrap=WORD, ) 
        self.textResult.grid(row=0, column=0, columnspan=22, sticky="W") 
 
        self.bttnDegree = Button(self, text="xⁿ", command=lambda x="xⁿ": self.calculate(x), width=7, height=3) 
        self.bttnDegree.grid(row=1, column=0, sticky="W") 
        self.bttnSqrt = Button(self, text="√", command=lambda x="√": self.calculate(x), width=7, height=3) 
        self.bttnSqrt.grid(row=1, column=1, sticky="W") 
        self.bttnClear = Button(self, text="C", command=lambda x="C": self.calculate(x), width=7, height=3) 
        self.bttnClear.grid(row=1, column=2, sticky="W") 
 
        self.bttnDivision = Button(self, text="/", command=lambda x="/": self.calculate(x), width=7, height=3) 
        self.bttnDivision.grid(row=1, column=3, sticky="W") 
 
 
        self.bttn1 = Button(self, text="7", command=lambda x="7": self.calculate(x), width=7, height=3) 
        self.bttn1.grid(row=2, column=0, sticky="W") 
        self.bttn2 = Button(self, text="8", command=lambda x="8": self.calculate(x), width=7, height=3) 
        self.bttn2.grid(row=2, column=1, sticky="W") 
        self.bttn3 = Button(self, text="9", command=lambda x="9": self.calculate(x), width=7, height=3) 
        self.bttn3.grid(row=2, column=2, sticky="W") 
        self.bttnX = Button(self, text="x", command=lambda x="*": self.calculate(x), width=7, height=3) 
        self.bttnX.grid(row=2, column=3, sticky="W") 
 
        self.bttn4 = Button(self, text="4", command=lambda x="4": self.calculate(x), width=7, height=3) 
        self.bttn4.grid(row=3, column=0, sticky="W") 
        self.bttn5 = Button(self, text="5", command=lambda x="5": self.calculate(x), width=7, height=3) 
        self.bttn5.grid(row=3, column=1, sticky="W") 
        self.bttn6 = Button(self, text="6", command=lambda x="6": self.calculate(x), width=7, height=3) 
        self.bttn6.grid(row=3, column=2, sticky="W") 
        self.bttnMinus = Button(self, text="-", command=lambda x="-": self.calculate(x), width=7, height=3) 
        self.bttnMinus.grid(row=3, column=3, sticky="W") 
 
        self.bttn7 = Button(self, text="1", command=lambda x="1": self.calculate(x), width=7, height=3) 
        self.bttn7.grid(row=4, column=0, sticky="W") 
        self.bttn8 = Button(self, text="2", command=lambda x="2": self.calculate(x), width=7, height=3) 
        self.bttn8.grid(row=4, column=1, sticky="W") 
        self.bttn9 = Button(self, text="3", command=lambda x="3": self.calculate(x), width=7, height=3) 
        self.bttn9.grid(row=4, column=2, sticky="W") 
        self.bttnPlus = Button(self, text="+", command=lambda x="+": self.calculate(x), width=7, height=3) 
        self.bttnPlus.grid(row=4, column=3, sticky="W") 
 
        self.bttnNegative = Button(self, text="±", command=lambda x="±": self.calculate(x),width=7, height=3) 
        self.bttnNegative.grid(row=5, column=0, sticky="W") 
        self.bttnNull = Button(self, text="0", command=lambda x="0": self.calculate(x), width=7, height=3) 
        self.bttnNull.grid(row=5, column=1, sticky="W") 
        self.bttnPoint = Button(self, text=".", command=lambda x=".": self.calculate(x), width=7, height=3) 
        self.bttnPoint.grid(row=5, column=2, sticky="W") 
        self.bttnEquality = Button(self, text="=", command=lambda x="=": self.calculate(x), width=7, height=3) 
        self.bttnEquality.grid(row=5, column=3, sticky="W") 
     
    # создадим функцию, которая будет определять, какая из кнопок выбрана, а затем добавлять/изменять ее в результат 
    def calculate(self, value):
        if(value == "xⁿ"):
            try: 
                self.result = str(float(self.result) * float(self.result)) 
                self.textResult.delete(0.0, END)
                self.textResult.insert(0.0, self.result)
            except ValueError:
                pass
        elif(value == "√"):
            try: 
                self.result = str(math.sqrt(float(self.result)))
                self.textResult.delete(0.0, END)
                self.textResult.insert(0.0, self.result)
            except ValueError:
                pass
        elif(value == "±"):
            try:
                self.result = str(-int(self.result))
                self.textResult.delete(0.0, END)
                self.textResult.insert(0.0, self.result)
            except ValueError:
                pass
        elif(value == "="):
            try:
                self.result = str(eval(self.result))
                self.textResult.delete(0.0, END)
                self.textResult.insert(0.0, self.result)
            except:
                pass
        elif(value == "C"):
            self.textResult.delete(0.0, END)
            self.result = ""
        else:
            self.result += str(value)
            self.textResult.delete(0.0, END)
            self.textResult.insert(0.0, self.result)

        
         
root =Tk() 
root.title("Калькулятор") 
# root.geometry("320x530") 
root.geometry("235x309")
 
app = Application(root) 
 
root.mainloop()