import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
from tkcalendar import DateEntry
import mysql.connector
from PIL import ImageTk, Image

# region WINDOW SETTINGS
window = tk.Tk()
window.title("STUDENT MANAGEMENT SYSTEM")
window.resizable(width=False, height=False)
window.geometry('1050x650+60+10')
window.configure(bg='#000000')
# endregion
# region IMAGE Import
background_image = Image.open("Images/adu.jpg").resize((1050, 1000))
bg = ImageTk.PhotoImage(background_image)

# endregion

# region MYSQL DATABASE CONNECTOR & CONNECTION
conn = mysql.connector.connect(host='localhost', user='root', port='3306', password='jrkian2016', database='sms')
c = conn.cursor()
# endregion


# region FRAME

# CANVAS image background

mainframe = tk.Frame(window, width=1000, height=800)
mainframe.pack(fill='both', expand=True)
background_canvas = tk.Canvas(mainframe)
background_canvas.pack(fill='both', expand=1)
background_canvas.create_image(0, -260, image=bg, anchor=NW)
background_canvas.create_text(535, 80, text='ENGINEERING STUDENTS MANAGEMENT SYSTEM', font=('verdana', 25, 'bold'),
                              fill='#1e4382')
# MAINFRAME connected to CANVAS
loginframe = tk.Frame(mainframe, bg='#1e4382')
loginframe.place(x=350, y=200)


# endregion

# region FUNCTIONS

# goes to the database frame
def gotodatabase():
    loginframe.place_forget()
    database_frame.place(x=70, y=100)
    registerframe.place(x=170, y=370)
    db_button_frame.place(x=180, y=560)

# login for admin
def login():
    conn.connect()
    admin_username = admin_username_entry.get().strip()
    admin_password = admin_password_entry.get().strip()
    vals = (admin_username, admin_password)
    select_query = "SELECT * FROM `admin_sms` WHERE `admin_username` = %s and `admin_password` = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        messagebox.showinfo('Admin Login', 'Admin Logged in')
        gotodatabase()
        c.execute("SELECT * FROM student_records")

        for item in tree.get_children():
            tree.delete(item)

        # loop for database records
        rows = c.fetchall()
        for row in rows:
            print(row)
            tree.insert("", END, values=row)
        conn.close()

        # deletes the entries
        admin_username_entry.delete(0, END)
        admin_password_entry.delete(0, END)

    else:
        messagebox.showwarning('Admin Login', 'Wrong Admin Username or Password')

# refresh the records
def refresh():
    #deletes the redundant data
    for item in tree.get_children():
        tree.delete(item)

    conn.connect()
    c.execute("SELECT * FROM student_records")

    # loop for database records

    rows = c.fetchall()

    for row in rows:
        print(row)
        tree.insert("", END, values=row)
    conn.close()

#clears entries
def clear():
    sid_entry_reg.delete(0, END)
    fn_entry_reg.delete(0, END)
    mn_entry_reg.delete(0, END)
    ln_entry_reg.delete(0, END)


#select a record
def select(e):

    clear()
    selected = tree.focus()
    values = tree.item(selected, 'values')
    sid_entry_reg.insert(0, values[0])
    fn_entry_reg.insert(0, values[1])
    mn_entry_reg.insert(0, values[2])
    ln_entry_reg.insert(0, values[3])

# deselect a record
def deselect(e):
    x = tree.selection()
    tree.selection_remove(x)
    clear()

# deletes a record
def delete():
    x = tree.selection()[0]
    tree.delete(x)

    conn.connect()
    student_id = sid_entry_reg.get().strip()
    vals = (student_id,)
    delete_query = "DELETE FROM `student_records` WHERE `student_id` = %s"
    c.execute(delete_query, vals)
    conn.commit()
    conn.close()
    sid_entry_reg.delete(0, END)


def update():

    student_id = sid_entry_reg.get().strip()
    first_name = fn_entry_reg.get().strip()
    middle_name = mn_entry_reg.get().strip()
    last_name = ln_entry_reg.get().strip()
    department = dep_var.get().strip()
    cour_prog = cp_var.get().strip()
    dt = bd_de_reg.get_date()
    birth_date = dt.strftime("%Y-%m-%d")
    sx = sex.get()
    vals = (first_name, middle_name, last_name, department, cour_prog, birth_date, sx, student_id)
    conn.connect()
    update_query ="""UPDATE `student_records` SET `first_name` = %s, `middle_name` = %s,
    `last_name` = %s,`department` = %s,`course_program` = %s, `birthdate` = %s, `sex` = %s 
    WHERE `student_id` = %s"""
    c.execute(update_query, vals)
    conn.commit()

    refresh()

    clear()


# check existing sid
def check_studentid(student_id):
    student_id = sid_entry_reg.get().strip()
    vals = (student_id,)
    select_query = "SELECT * FROM `student_records` WHERE `student_id` = %s"
    c.execute(select_query, vals)
    user = c.fetchone()
    if user is not None:
        return True
    else:
        return False

# add/register record
def register():
    conn.connect()
    student_id = sid_entry_reg.get().strip()
    first_name = fn_entry_reg.get().strip()
    middle_name = mn_entry_reg.get().strip()
    last_name = ln_entry_reg.get().strip()
    department = dep_var.get().strip()
    cour_prog = cp_var.get().strip()
    dt = bd_de_reg.get_date()
    birth_date = dt.strftime("%Y-%m-%d")
    sx = sex.get()

    if len(student_id) > 0 and len(first_name) > 0 and len(middle_name) > 0 and len(last_name) > 0:
        if check_studentid(student_id) == False:
            vals = (student_id, first_name, middle_name, last_name, department, cour_prog, birth_date, sx)
            insert_query = "INSERT INTO `sms`.`student_records` (`student_id`, `first_name`, `middle_name`, `last_name`, `department`, `course_program`, `birthdate`, `sex`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
            c.execute(insert_query, vals)
            conn.commit()
            messagebox.showinfo('Student Registered', "Student's Data has been uploaded successfully")

            refresh()

            #clears the entries
            clear()


        else:
            messagebox.showwarning('Existing StudentID',
                                   'This StudentID Already Exists or Has an Existing Record in the Database')
    else:
        messagebox.showwarning('Empty/Incomplete Fields', 'Please fill all the information')

# logout admin
def logout():
    database_frame.place_forget()
    registerframe.place_forget()
    db_button_frame.place_forget()
    loginframe.place(x=350, y=200)
    messagebox.showinfo('Admin Logout', "Admin Logged out")

# get department
def get_dep(event):
    value = dep_var.get()
    cp_var.set(dep_courses[value][0])
    cp_cb_reg.config(values=dep_courses[value])

# maximum sid length
def max_sid(*args):
    max_len = 9
    s = sid_var.get()
    if len(s) > max_len:
        sid_var.set(s[:max_len])



# endregion

# region MAINFRAME
style = ttk.Style(window)
style.theme_use('clam')
style.configure('tree.heading', background="blue")

# MENUBAR
menubar = tk.Menu(mainframe)
account_menu = Menu(menubar)
database_menu = Menu(menubar)
account_menu.add_command(label='Logout', command=logout)
account_menu.add_command(label='Exit', command=quit)
menubar.add_cascade(menu=account_menu, label='Admin')
window.configure(menu=menubar)
# endregion

# region DATABASE FRAME
database_frame = Frame(window)

tree = ttk.Treeview(database_frame, column=("c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8"), show='headings')

tree.column("#1", minwidth=0, width=90, stretch=NO, anchor=CENTER)
tree.heading("#1", text="STUDENT ID")
tree.column("#2", minwidth=0, width=120, stretch=NO, anchor=CENTER)
tree.heading("#2", text="FIRST NAME")
tree.column("#3", minwidth=0, width=100, stretch=NO, anchor=CENTER)
tree.heading("#3", text="MIDDLE NAME")
tree.column("#4", minwidth=0, width=140, stretch=NO, anchor=CENTER)
tree.heading("#4", text="LAST NAME")
tree.column("#5", minwidth=0, width=130, stretch=NO, anchor=CENTER)
tree.heading("#5", text="DEPARTMENT")
tree.column("#6", minwidth=0, width=170, stretch=NO, anchor=CENTER)
tree.heading("#6", text="COURSE PROGRAM")
tree.column("#7", minwidth=0, width=90, stretch=NO, anchor=CENTER)
tree.heading("#7", text="BIRTH DATE")
tree.column("#8", minwidth=0, width=60, stretch=NO, anchor=CENTER)
tree.heading("#8", text="SEX")
tree.configure()
tree.pack( ipady=10, side=LEFT)

#treeview keybinds
tree.bind("<ButtonRelease-1>", select)
tree.bind("<Button-1>", deselect)

sb = tk.Scrollbar(database_frame, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=sb.set, selectmode='browse')
sb.config(command=tree.yview)

# endregion


# region LOGIN PAGE DESIGN
welcome_label = tk.Label(loginframe, text='Welcome Admin!', bg='#1e4382', fg='white', font=('Arial', 17, 'bold'))
welcome_label.grid(row=0, column=0,columnspan=2, padx=10, pady=10)
admin_username_label = tk.Label(loginframe, text='Username:', bg='#1e4382', fg='white', font=('Arial', 15, 'bold'))
admin_username_label.grid(row=1, column=0, padx=10, pady=30)
admin_password_label = tk.Label(loginframe, text='Password:', bg='#1e4382', fg='white', font=('Arial', 15, 'bold'))
admin_password_label.grid(row=2, column=0)

admin_username_entry = tk.Entry(loginframe, font=('Arial', 15))
admin_username_entry.grid(row=1, column=1, padx=10, pady=30)
admin_password_entry = tk.Entry(loginframe, show='x', font=('Arial', 15))
admin_password_entry.grid(row=2, column=1)

admin_login_but1 = tk.Button(loginframe, text='LOGIN', fg='white', bg='black', font=('Arial', 15, 'bold'), width=28,
                             command=login)
admin_login_but1.grid(row=3, column=0, columnspan=2, pady=30)
window.bind('<Return>', lambda event: login())

# endregion


# region REGISTRATION PAGE DESIGN
registerframe = tk.Frame(mainframe, bg='#1e4382')


sid_reg = tk.Label(registerframe, text='Student ID:', bg='#1e4382', fg='white', font=('Arial', 12, 'bold'))
sid_reg.grid(row=0, column=0, padx=6, pady=6)
fn_reg = tk.Label(registerframe, text='First Name:', bg='#1e4382', fg='white', font=('Arial', 12, 'bold'))
fn_reg.grid(row=1, column=0, padx=6, pady=6)
mn_reg = tk.Label(registerframe, text='Middle Name:', bg='#1e4382', fg='white', font=('Arial', 12, 'bold'))
mn_reg.grid(row=2, column=0, padx=6, pady=6)
ln_reg = tk.Label(registerframe, text='Last Name:', bg='#1e4382', fg='white', font=('Arial', 12, 'bold'))
ln_reg.grid(row=3, column=0, padx=6, pady=6)
dep_reg= tk.Label(registerframe, text='Department:', bg='#1e4382', fg='white', font=('Arial', 12, 'bold'))
dep_reg.grid(row=0, column=2, padx=6, pady=6)
cp_reg = tk.Label(registerframe, text='Course Program:', bg='#1e4382', fg='white', font=('Arial', 12, 'bold'))
cp_reg.grid(row=1, column=2, padx=6, pady=6)
be_reg = tk.Label(registerframe, text='Birth Date:', bg='#1e4382', fg='white', font=('Arial', 12, 'bold'))
be_reg.grid(row=2, column=2, padx=6, pady=6)
gender_reg = tk.Label(registerframe, text='Sex:', bg='#1e4382', fg='white', font=('Arial', 12, 'bold'))
gender_reg.grid(row=3, column=2, padx=6, pady=6)

sid_var = StringVar()
sid_var.trace_variable("w", max_sid)

# REGISTRATION ENTRIES
sid_entry_reg = tk.Entry(registerframe, font=('Arial', 12), textvariable=sid_var)
sid_entry_reg.grid(row=0, column=1, padx=6, pady=6)
fn_entry_reg = tk.Entry(registerframe, font=('Arial', 12))
fn_entry_reg.grid(row=1, column=1, padx=6, pady=6)
mn_entry_reg = tk.Entry(registerframe, font=('Arial', 12))
mn_entry_reg.grid(row=2, column=1, padx=6, pady=6)
ln_entry_reg = tk.Entry(registerframe, font=('Arial', 12))
ln_entry_reg.grid(row=3, column=1, padx=6, pady=6)


sx_frame = tk.Frame(registerframe)
sx_frame.grid(row=3, column=3, padx=6, pady=6)

sex = StringVar()
sex.set('Male')
gdr_cb_reg = ttk.Combobox(sx_frame, values=['Male', 'Female'], font=('Arial', 10), textvariable=sex, state='readonly', width=23)
gdr_cb_reg .grid(row=0, column=0)

dep_courses = {'College of Engineering': ['B.S. Electrical Engineering', 'B.S. Electronics Engineering', 'B.S. Chemical Engineering',
'B.S. Civil Engineering', 'B.S. Computer Engineering', 'B.S. Geology', 'B.S. Industrial Engineering', 'B.S. Mechanical Engineering',
'B.S. Mining Engineering', 'B.S. Petroleum Engineering']}


dep_cb_values = list(dep_courses.keys())

dep_var = StringVar()
dep_var.set(dep_cb_values[0])

dep_cb_frame = tk.Frame(registerframe)
dep_cb_frame.grid(row=0, column=3, padx=6, pady=6)
dep_cb_reg = ttk.Combobox(dep_cb_frame, values=list(dep_courses.keys()), textvariable=dep_var, font=('Arial', 10), state='readonly', width=23)
dep_cb_reg.grid()
dep_cb_reg.bind('<<ComboboxSelected>>', get_dep)

cp_cb_frame = tk.Frame(registerframe)
cp_cb_frame.grid(row=1, column=3, padx=6, pady=6)
cp_var = StringVar()
cp_var.set(dep_courses[dep_cb_values[0]][0])
cp_cb_reg = ttk.Combobox(cp_cb_frame, values=dep_courses[dep_cb_values[0]], textvariable=cp_var, font=('Arial', 10), state='readonly', width=23)
cp_cb_reg.grid()

birth_date_frame = tk.Frame(registerframe)
birth_date_frame.grid(row=2, column=3, padx=6, pady=6)
bd_de_reg = DateEntry(birth_date_frame, width=20, background="#1e4382", foreground='white', font=('Arial', 11), state='readonly')
bd_de_reg.grid()


db_button_frame = tk.Frame(window)
register_button = tk.Button(db_button_frame, text='REGISTER RECORD', bg='gray', fg='white', font=('Arial', 10, 'bold'),
                            width=17, command=register)
register_button.grid(row=0, column=0, padx=5, pady=10)
refresh_button = tk.Button(db_button_frame, text='REFRESH RECORDS', bg='gray', fg='white', font=('Arial', 10, 'bold'),
                           width=17, command=refresh)
refresh_button.grid(row=0, column=1, padx=5)
delete_button = tk.Button(db_button_frame, text='DELETE RECORD', bg='gray', fg='white', font=('Arial', 10, 'bold'),
                          width=17, command=delete)
delete_button.grid(row=0, column=2, padx=5)
update_button = tk.Button(db_button_frame,  text='UPDATE RECORD', bg='gray', fg='white', font=('Arial', 10, 'bold'),
                          width=17, command=update)
update_button.grid(row=0, column=3, padx=5)

# endregion


window.mainloop()




