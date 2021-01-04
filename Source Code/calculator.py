from tkinter import *


window= Tk() #create a basic window
window.geometry("312x350")  #the size of the window 
window.resizable(0, 0)  #to prevent from resizing the window
window.title("Calculator")


# 'on_click' function : 
# This Function continuously updates the input field whenever you enters a number
def on_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

# 'on_clear' function :This is used to clear  the input field
def on_clear(): 
    global expression 
    expression = "" 
    input_text.set("")
    result_field_data.set("")

# 'on_equal':This method calculates the expression present in input field
def on_equal():
    try:
         result=str(eval(expression)) # 'eval':This function is used to evaluates the string expression directly
    except:
       result="Math Error" 
    result_field_data.set(result)
    
expression = ""
 
# 'StringVar()' :It is used to get the instance of input field
input_text = StringVar()
result_field_data=StringVar()


#creating a frame for the input field
 
input_frame = Frame(window, width=312, height=50, bd=0)
 
input_frame.pack(side=TOP)
 
#create a input field inside the 'Frame'
 
input_field = Entry(input_frame, font=('arial', 18), textvariable=input_text, width=50,  bg="#232323",foreground="white", bd=0, justify=LEFT)
 
input_field.grid(row=0, column=0)
 
input_field.pack(ipady=10) # 'ipady' is internal padding to increase the height of input field
 
#the Result
#Canvas widget to display graphical elements like lines .
canvas=Canvas(window, width=350, height=1,bd=0,highlightthickness=0,bg="grey")
canvas.pack()

result_field = Entry(window, font=('arial', 18), textvariable=result_field_data, width=50, bg="#232323",foreground="white",bd=0, justify=RIGHT).pack()

#creating another 'Frame' for the button below the 'input_frame'
 
buttons_frame = Frame(window, width=312, height=272.5, bg="grey")
 
buttons_frame.pack()
 
# first row
 

plus = Button(buttons_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("+")).grid(row = 0, column = 0, padx = 1, pady = 1)

multiply = Button(buttons_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("*")).grid(row = 0, column = 1, padx = 1, pady = 1)

divide = Button(buttons_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("/")).grid(row = 0, column = 2, padx = 1, pady = 1)

minus = Button(buttons_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("-")).grid(row = 0, column = 3, padx = 1, pady = 1) 

# second row
 
seven = Button(buttons_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: on_click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
eight = Button(buttons_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: on_click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
nine = Button(buttons_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: on_click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
opened_bracket=Button(buttons_frame, text = "(", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("(")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
four = Button(buttons_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: on_click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
five = Button(buttons_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: on_click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
six = Button(buttons_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: on_click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

closed_bracket=Button(buttons_frame, text = ")", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click(")")).grid(row = 2, column = 3, padx = 1, pady = 1)

remainder=opened_bracket=Button(buttons_frame, text = "%", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: on_click("%")).grid(row = 3, column = 3, padx = 1, pady = 1) 

 
# fourth row
 
one = Button(buttons_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: on_click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
two = Button(buttons_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: on_click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
three = Button(buttons_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: on_click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 

 
# fifth row
 
zero = Button(buttons_frame, text = "0", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda:on_click(0)).grid(row = 4, column = 0, padx = 1, pady = 1)
 
point = Button(buttons_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: on_click(".")).grid(row = 4, column = 1, padx = 1, pady = 1)

clear = Button(buttons_frame, text = "AC", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: on_clear()).grid(row = 4, column = 2, padx = 1, pady = 1)

equals = Button(buttons_frame, text = "=", fg = "black", width = 10,height=3, bd = 0, bg = "#ff8c00", cursor = "hand2", command =on_equal).grid(row=4, column = 3, padx = 1, ipady = 1)



window.mainloop()