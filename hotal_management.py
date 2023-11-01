from tkinter import *
from datetime import datetime

root = Tk()
root.geometry("2000x1090")
root.title("Bill management")
root.resizable(True, True)


def exit():
    root.destroy()


def calculator():
    win = Tk()
    win.geometry("400x290")
    win.title("calculator")
    win.resizable(0, 0)

    def clear():
        global e
        e = ""
        input_t.set("")

    def click_bt(item):
        global e
        e = e + str(item)
        input_t.set(e)

    def equal():
        global e
        result = eval(input_t.get())
        input_t.set(result)
        e = ""

    input_t = StringVar()
    e = ""

    input_frames = Frame(win, width=500, height=80, background="lightgreen", border=5, relief=RAISED)
    input_frames.pack(side=TOP)

    input_Text = Entry(input_frames, font=("aria", 10, "bold"), width=52, background="#eee", border=10,
                       textvariable=input_t, justify=RIGHT)
    input_Text.grid(row=0, column=0, columnspan=3, pady=1, padx=1)

    button_frames = Frame(win, width=500, height=500, background="lightblue", border=5, relief=RAISED)
    button_frames.place(x=0, y=50)
    ###################################################################______row_____1_________################################################################################
    b_clear = Button(button_frames, text="Clear", font=("aria", 10, "bold"), border=2, height=2, width=35,
                     cursor="hand2", command=lambda: clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)

    b_division = Button(button_frames, text="/", font=("aria", 10, "bold"), border=2, height=2, width=10,
                        cursor="hand2", command=lambda: click_bt("/")).grid(row=0, column=3, padx=1, pady=1)
    ######################################################################################
    b_1 = Button(button_frames, text="1", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                 command=lambda: click_bt("1")).grid(row=1, column=0, padx=1, pady=1)
    b_2 = Button(button_frames, text="2", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                 command=lambda: click_bt("2")).grid(row=1, column=1, padx=1, pady=1)
    b_3 = Button(button_frames, text="3", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                 command=lambda: click_bt("3")).grid(row=1, column=2, padx=1, pady=1)

    b_4 = Button(button_frames, text="4", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                 command=lambda: click_bt("4")).grid(row=2, column=0, padx=1, pady=1)
    b_5 = Button(button_frames, text="5", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                 command=lambda: click_bt("5")).grid(row=2, column=1, padx=1, pady=1)
    b_6 = Button(button_frames, text="6", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                 command=lambda: click_bt("6")).grid(row=2, column=2, padx=1, pady=1)

    b_7 = Button(button_frames, text="7", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                 command=lambda: click_bt("7")).grid(row=3, column=0, padx=1, pady=1)
    b_8 = Button(button_frames, text="8", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                 command=lambda: click_bt("8")).grid(row=3, column=1, padx=1, pady=1)
    b_9 = Button(button_frames, text="9", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                 command=lambda: click_bt("9")).grid(row=3, column=2, padx=1, pady=1)

    b_add = Button(button_frames, text="+", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                   command=lambda: click_bt("+")).grid(row=1, column=3, padx=1, pady=1)
    b_sub = Button(button_frames, text="-", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                   command=lambda: click_bt("-")).grid(row=2, column=3, padx=1, pady=1)
    b_mul = Button(button_frames, text="*", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                   command=lambda: click_bt("*")).grid(row=3, column=3, padx=1, pady=1)

    b_0 = Button(button_frames, text="0", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                 command=lambda: click_bt("0")).grid(row=4, column=0, padx=1, pady=1)
    b_dot = Button(button_frames, text=".", font=("aria", 10, "bold"), border=2, height=2, width=10, cursor="hand2",
                   command=lambda: click_bt(".")).grid(row=4, column=1, padx=1, pady=1)
    b_equal = Button(button_frames, text="=", font=("aria", 10, "bold"), border=2, height=2, width=22, cursor="hand2",
                     command=lambda: equal()).grid(row=4, column=2, columnspan=3, padx=1, pady=1)

    win.mainloop()


def reset():
    dosa_enter.delete(0, END)
    tea_enter.delete(0, END)
    coffee_enter.delete(0, END)
    rise_enter.delete(0, END)
    eggs_enter.delete(0, END)
    pancakes_enter.delete(0, END)
    juice_enter.delete(0, END)


def total():
    global c1, c2, c3, c4, c5, c6, c7
    try:
        a1 = int(dosa_enter.get())
    except:
        a1 = 0

    try:
        a2 = int(tea_enter.get())
    except:
        a2 = 0

    try:
        a3 = int(coffee_enter.get())
    except:
        a3 = 0

    try:
        a4 = int(rise_enter.get())
    except:
        a4 = 0

    try:
        a5 = int(eggs_enter.get())
    except:
        a5 = 0

    try:
        a6 = int(pancakes_enter.get())
    except:
        a6 = 0

    try:
        a7 = int(juice_enter.get())
    except:
        a7 = 0

    # calculation
    c1 = 60 * a1
    c2 = 20 * a2
    c3 = 20 * a3
    c4 = 60 * a4
    c5 = 10 * a5
    c6 = 40 * a6
    c7 = 50 * a7

    lab_total = Label(f2, font=("aria", 20, "bold"), text="TOTAL", background="black", foreground="lightyellow")
    lab_total.place(x=160, y=80)

    entry_total = Entry(f2, font=("aria", 20, "bold"), textvariable=total_bill, borderwidth=6, width=16,
                        background="lightgreen")
    entry_total.place(x=100, y=150)

    total_cost_1 = c1 + c2 + c3 + c4 + c5 + c6 + c7
    total_cost.set(total_cost_1)
    bil = "Rs.", str(total_cost_1)
    total_bill.set(bil)


def recept():
    text_area.delete(1.0, END)
    text_area.insert(END, 'Items\tNumber of items\tCost of items')
    text_area.insert(END, f'\n========================================')
    text_area.insert(END, f'\nDosa\t\t{dosa_enter.get()}\t\t{c1}')
    text_area.insert(END, f'\nTea\t\t{tea_enter.get()}\t\t{c2}')
    text_area.insert(END, f'\nCoffee\t\t{coffee_enter.get()}\t\t{c3}')
    text_area.insert(END, f'\nRise\t\t{rise_enter.get()}\t\t{c4}')
    text_area.insert(END, f'\nEggs\t\t{eggs_enter.get()}\t\t{c5}')
    text_area.insert(END, f'\nJuice\t\t{juice_enter.get()}\t\t{c6}')
    text_area.insert(END, f'\nPancakes\t\t{pancakes_enter.get()}\t\t{c7}')
    text_area.insert(END, f'\n=======================================')
    text_area.insert(END, f'\n \t\t\t\tRs.{total_cost.get()}')
    text_area.insert(END, f'\n \t\t\t\t\t\t\t\t\t\t\t\t\t time:{today_3}')
    text_area.insert(END, f'\n \t\t\t\t\t\t\t\t\t\t\t\t\t time:{today_2}')


today = datetime.today()
today_2 = today.strftime("%d/%m/%y")
today_3 = datetime.now()

Label(text="BILL MANAGEMENT", bg="black", fg="white", font=("Arial", 33), width="300", height="2").pack()
# ************menu**************
f = Frame(root, bg="lightgreen", highlightcolor="black", highlightthickness=1, width=350, height=450, borderwidth=50)
f.place(x=15, y=120)
# ******************LABEL FOR FIRST FRAME MENU********************
Label(f, text="MENU BAR", font=("Gabriola", 40, "bold"), foreground="black", background="lightgreen").place(x=40, y=0)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Dosa...Rs.60/Plate", foreground="black",
      background="lightgreen").place(x=20, y=80)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Tea...Rs.20/cup", foreground="black",
      background="lightgreen").place(x=20, y=120)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Coffee...Rs.20/cup", foreground="black",
      background="lightgreen").place(x=20, y=160)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Rise...Rs.60/Plate", foreground="black",
      background="lightgreen").place(x=20, y=200)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="Eggs...Rs.10/egg", foreground="black",
      background="lightgreen").place(x=20, y=240)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="juice...Rs.40/cup", foreground="black",
      background="lightgreen").place(x=20, y=280)
Label(f, font=("Lucida Calligraphy", 15, "bold"), text="pancakes...Rs.50/Plate", foreground="black",
      background="lightgreen").place(x=20, y=320)

# ***********************FRAME 2 ENTRY WORK*********************
f1 = Frame(root, borderwidth=10, height=550, width=400, relief=RAISED)
f1.pack()
f1.place(x=400, y=120)

dosa = StringVar()
tea = StringVar()
coffee = StringVar()
rise = StringVar()
eggs = StringVar()
juice = StringVar()
pancakes = StringVar()
total_bill = StringVar()
total_cost = StringVar()
# ***********************FRAME 2 LABELS*************************
dosa_lab = Label(f1, text="Dosa", font=("aria", 20, "bold"), foreground="black", background="yellow", width=8)
tea_lab = Label(f1, text="Tea", font=("aria", 20, "bold"), foreground="black", background="yellow", width=8)
coffee_lab = Label(f1, text="Coffee", font=("aria", 20, "bold"), foreground="black", background="yellow", width=8)
rise_lab = Label(f1, text="Rise", font=("aria", 20, "bold"), foreground="black", background="yellow", width=8)
eggs_lab = Label(f1, text="eggs", font=("aria", 20, "bold"), foreground="black", background="yellow", width=8)
juice_lab = Label(f1, text="juice", font=("aria", 20, "bold"), foreground="black", background="yellow", width=8)
pancakes_lab = Label(f1, text="pancakes", font=("aria", 20, "bold"), foreground="black", background="yellow", width=8)
dosa_lab.grid(row=1, column=0)
tea_lab.grid(row=2, column=0)
coffee_lab.grid(row=3, column=0)
rise_lab.grid(row=4, column=0)
eggs_lab.grid(row=5, column=0)
juice_lab.grid(row=6, column=0)
pancakes_lab.grid(row=7, column=0)

# ***********************ENTRY BOXES***************************
dosa_enter = Entry(f1, font=("aria", 20, "bold"), textvariable=dosa, borderwidth=6, width=8, background="lightpink")
tea_enter = Entry(f1, font=("aria", 20, "bold"), textvariable=tea, borderwidth=6, width=8, background="lightpink")
coffee_enter = Entry(f1, font=("aria", 20, "bold"), textvariable=coffee, borderwidth=6, width=8, background="lightpink")
rise_enter = Entry(f1, font=("aria", 20, "bold"), textvariable=rise, borderwidth=6, width=8, background="lightpink")
eggs_enter = Entry(f1, font=("aria", 20, "bold"), textvariable=eggs, borderwidth=6, width=8, background="lightpink")
juice_enter = Entry(f1, font=("aria", 20, "bold"), textvariable=juice, borderwidth=6, width=8, background="lightpink")
pancakes_enter = Entry(f1, font=("aria", 20, "bold"), textvariable=pancakes, borderwidth=6, width=8,
                       background="lightpink")

dosa_enter.grid(row=1, column=1)
tea_enter.grid(row=2, column=1)
coffee_enter.grid(row=3, column=1)
rise_enter.grid(row=4, column=1)
eggs_enter.grid(row=5, column=1)
juice_enter.grid(row=6, column=1)
pancakes_enter.grid(row=7, column=1)

# *****************BUTTONS****************

label_frame = Frame(root, background="lightgreen", relief=RIDGE)
label_frame.place(x=100, y=600, width=600, height=100)
reset_button = Button(label_frame, text="Reset", font=("aria", 15, "bold"), borderwidth=6, background="lightblue",
                      width=7, command=reset)
reset_button.grid(row=0, column=1)

total_button = Button(label_frame, text="Total", font=("aria", 15, "bold"), borderwidth=6, background="lightblue",
                      width=7, command=total)
total_button.grid(row=0, column=2)

print_button = Button(label_frame, text="Recept", font=("aria", 15, "bold"), borderwidth=2, background="lightblue",
                      border=6, width=7, command=recept)
print_button.grid(row=0, column=3)

cal_button = Button(label_frame, text="Calculator", font=("aria", 15, "bold"), borderwidth=2, background="lightblue",
                    border=6, width=10, command=calculator)
cal_button.grid(row=0, column=4)

l = Button(label_frame, text="Exit", font=("aria", 15, "bold"), borderwidth=2, background="lightblue", border=6,
           width=7, command=exit)
l.grid(row=0, column=5)

# ******************* FRAME 3 FOR CALCULATOR***********************
f2 = Frame(root, background="lightgreen", highlightbackground="black", highlightthickness=5, width=450, height=580)
f2.place(x=880, y=150)

bill_label = Label(f2, text="BILL", font=("aria", 15, "bold"), background="lightyellow")
bill_label.place(x=180, y=10)

text_area = Text(f2, height=20, width=40, insertwidth=50)
text_area.place(x=60, y=200)

root.mainloop()
