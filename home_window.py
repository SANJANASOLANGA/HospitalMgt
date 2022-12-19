import pathlib
from tkinter import *
from tkinter import messagebox


class first:
    def __init__(self, homewin):
        self.homewin = homwin
        self.homewin.title("Aragi Hospital")

        self.homewin['bg'] = 'light yellow'
        self.homewin.option_add("*Font", ('Verdana', 12))

        la1 = Label(homewin, text="Welcome\nAragi Hospital", bg="light yellow", font="Times 36 italic bold",
                    width="500", height="2").pack()
        la2 = Label(homewin, text="If you are new to us,\nPlease fill out the register form first and login",
                    bg="light yellow",
                    font="Times 15 bold", fg="gray", width="50", height="2").place(x=-50, y=240)
        bt1 = Button(homewin, text="Register", width="30", height="2", bg="red", activeforeground="blue",
                     cursor="circle", command=self.regis).place(x=100, y=130)
        bt2 = Button(homewin, text="Login", width="30", height="2", bg="red", activeforeground="blue",
                     cursor="circle", command=self.logi).place(x=100, y=190)

    def regis(self):
        self.homewin.destroy()
        import registerp

    def logi(self):
        a = pathlib.Path("All_Login_Details.txt")
        if a.exists():
            self.homewin.destroy()
            import LOGIN
        else:
            messagebox.showinfo("Information", "Be Registerd First", parent=self.homewin)

homwin = Tk()
obj = first(homwin)
homwin.minsize(500, 300)
homwin.maxsize(500, 300)
homwin.mainloop()
