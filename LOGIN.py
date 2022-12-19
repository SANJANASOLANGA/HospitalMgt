from tkinter import *
import tkinter as tk
from tkinter import messagebox


class all_login:
    def __init__(self, log):

        self.log = log

        self.log.title("Login")

        self.log['bg'] = 'light yellow'
        self.log.option_add("*Font", ('Verdana', 12))

        la1 = tk.Label(self.log, text="Welcome to Aragi Hospital\nLogin to Your Account", bg="light yellow",
                       font="Times 30 italic bold",
                       width="50", height="3").pack()
        la2 = tk.Label(self.log, text="Username : ", bg="light yellow", font="calibre 20 bold").place(x=40, y=145)
        la3 = tk.Label(self.log, text="Password : ", bg="light yellow", font="calibre 20 bold").place(x=40, y=205)

        name_var = tk.StringVar()
        passw_var = tk.StringVar()

        self.name_entry = tk.Entry(self.log, textvariable=name_var, font=('calibre', 10, 'normal'), width=35)
        self.name_entry.place(x=205, y=157)
        self.passw_entry = tk.Entry(self.log, textvariable=passw_var, font=('calibre', 10, 'normal'), width=35,
                                    show='*')
        self.passw_entry.place(x=205, y=215)

        btn1 = tk.Button(self.log, text="Login", width="20", height="2", bg="red", activeforeground="blue",
                         cursor="dot",
                         command=self.login).place(x=160, y=275)

    def clear(self):
        self.name_entry.delete(0, "end")
        self.passw_entry.delete(0, "end")

    def login(self):
        username = self.name_entry.get()
        password = self.passw_entry.get()
        if username == "" or password == "":
            messagebox.showwarning("Information", "Blank Not Allowed")

        self.clear()

        # checking username & pw are correct
        for x in open("All_Login_Details.txt", "r").readlines():
            login_info = x.split()  # Split on the space, and store the results in a list of two strings

            if username == login_info[0] and password == login_info[1]:
                tk.Label(self.log, text="   Successfully Login!!", bg="light yellow", fg="blue", width="30", height="1",
                         font="calibre 15").place(x=80, y=240)
                messagebox.showinfo("Successfully Login!!", "Successfully Login!!")
                self.log.destroy()
                import aragi_main_menu

                return True

        tk.Label(self.log, text="Invalid Username or Password", bg="light yellow", fg="red", width="30", height="1",
                 font="calibre 15").place(x=80, y=240)
        messagebox.showwarning("Invalid Username or Password", "Invalid Username or Password\nPlease Try Again!!")

        return False


log = Tk()
obj = all_login(log)
log.minsize(500, 350)
log.maxsize(500, 350)
log.mainloop()
