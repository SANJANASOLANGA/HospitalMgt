import pathlib
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox


class all_register:
    def __init__(self, reg):
        self.reg = reg

        self.reg.title("Register Here")

        Label(self.reg, text="Register Here", bg="light yellow", fg="black", font="Times 36 italic bold",
              width="500").pack()

        self.reg['bg'] = 'light yellow'
        self.reg.option_add("*Font", ('Verdana', 12))

        possi = Label(self.reg, text="Are you ", width="10", bg="light yellow", font="Times 16 bold").place(x=0, y=60)
        first_name = Label(self.reg, text="First Name", width="30", bg="light yellow", font="Times 14 bold").place(x=95,
                                                                                                                   y=90)
        last_name = Label(self.reg, text="Last Name", width="30", bg="light yellow", font="Times 14 bold").place(x=95,
                                                                                                                 y=150)
        address = Label(self.reg, text="Address", width="30", bg="light yellow", font="Times 14 bold").place(x=95,
                                                                                                             y=210)
        contact_no = Label(self.reg, text="Contact Number", width="30", bg="light yellow", font="Times 14 bold").place(
            x=95, y=270)
        age = Label(self.reg, text="Age", width="30", bg="light yellow", font="Times 14 bold").place(x=95, y=330)
        gender = Label(self.reg, text="Gender", width="30", bg="light yellow", font="Times 14 bold").place(x=95, y=390)
        username = Label(self.reg, text="Username", width="30", bg="light yellow", font="Times 14 bold").place(x=95,
                                                                                                               y=450)
        password = Label(self.reg, text="Password", width="30", bg="light yellow", font="Times 14 bold").place(x=95,
                                                                                                               y=510)

        pos = StringVar()
        self.pos_entry = Combobox(self.reg, width=37, textvariable=pos)
        self.pos_entry.place(x=120, y=65)
        self.pos_entry['values'] = ("A Patient", "in Health sector", "in Administrative Division")

        fina = StringVar()
        lana = StringVar()
        addre = StringVar()
        conta = StringVar()
        ag = StringVar()
        ge = StringVar()
        userna = StringVar()
        pw = StringVar()

        self.fina_entry = Entry(reg, textvariable=fina, width="50")
        self.fina_entry.place(x=15, y=120)
        self.lana_entry = Entry(reg, textvariable=lana, width="50")
        self.lana_entry.place(x=15, y=180)
        self.addre_entry = Entry(reg, textvariable=addre, width="50")
        self.addre_entry.place(x=15, y=240)
        self.conta_entry = Entry(reg, textvariable=conta, width="50")
        self.conta_entry.place(x=15, y=300)
        self.ag_entry = Entry(reg, textvariable=ag, width="50")
        self.ag_entry.place(x=15, y=360)
        self.ge_entry = Entry(reg, textvariable=ge, width="50")
        self.ge_entry.place(x=15, y=420)
        self.userna_entry = Entry(reg, textvariable=userna, width="50")
        self.userna_entry.place(x=15, y=480)
        self.pw_entry = Entry(reg, textvariable=pw, width="50", show='*')
        self.pw_entry.place(x=15, y=540)

        sub_button = Button(self.reg, text="Register", width="20", height="2", bg="red", activeforeground="blue",
                            cursor="dot",
                            command=self.reg_info_save).place(x=55, y=600)
        reg_clear_button = Button(self.reg, text="Clear", width="20", height="2", bg="red", activeforeground="blue",
                                  cursor="dot", command=self.clear).place(x=350, y=600)
        reg_log_button = Button(self.reg, text="LogIn", width="20", height="2", bg="red", activeforeground="blue",
                                cursor="dot", command=self.logi).place(x=640, y=120)

    def exit(self):
        self.reg.destroy()
        import home_window

    def logi(self):
        a = pathlib.Path("All_Login_Details.txt")
        if a.exists():
            self.reg.destroy()
            import LOGIN
        else:
            messagebox.showinfo("Information", "Be Registerd First", parent=self.reg)

    def reg_info_save(self):
        # get user inputs
        pos_info = self.pos_entry.get()
        fina_info = self.fina_entry.get()
        lana_info = self.lana_entry.get()
        addre_info = self.addre_entry.get()
        conta_info = self.conta_entry.get()
        age_info = self.ag_entry.get()
        gender_info = self.ge_entry.get()
        userna_info = self.userna_entry.get()
        pw_info = self.pw_entry.get()

        # checking user inputs are blank
        if pos_info == "" or fina_info == "" or lana_info == "" or addre_info == "" or conta_info == "" or age_info == "" or gender_info == "" or userna_info == "" or pw_info == "":
            messagebox.showwarning("Information!", "Blank Not Allowed!!")
        else:
            save_log_file = open("All_Login_Details.txt", "a")
            save_log_file.write(userna_info)
            save_log_file.write(" ")
            save_log_file.write(pw_info)
            save_log_file.write("\n")
            save_log_file.close()
            if pos_info == "A Patient":
                save_reg_file = open("Patients_Register_Details.txt", "a")
                save_reg_file.write("Position : " + pos_info + "\n")
                save_reg_file.write("First Name : " + fina_info + "\n")
                save_reg_file.write("Last Name : " + lana_info + "\n")
                save_reg_file.write("Address : " + addre_info + "\n")
                save_reg_file.write("Contact Number : " + conta_info + "\n")
                save_reg_file.write("Age : " + age_info + "\n")
                save_reg_file.write("Gender : " + gender_info + "\n")
                save_reg_file.write("Username : " + userna_info + "\n" + "\n")
                save_reg_file.write(("** " + "Next Patient Details " + "** ") * 3 + "\n")

                save_reg_file.close()

                messagebox.showinfo("Successful!", "Your registration is successful!!")
                self.reg.destroy()
                import LOGIN
            elif pos_info == "in Health sector":
                save_reg_file = open("Medical_Register_Details.txt", "a")
                save_reg_file.write("Position : " + pos_info + "\n")
                save_reg_file.write("First Name : " + fina_info + "\n")
                save_reg_file.write("Last Name : " + lana_info + "\n")
                save_reg_file.write("Address : " + addre_info + "\n")
                save_reg_file.write("Contact Number : " + conta_info + "\n")
                save_reg_file.write("Age : " + age_info + "\n")
                save_reg_file.write("Gender : " + gender_info + "\n")
                save_reg_file.write("Username : " + userna_info + "\n" + "\n")
                save_reg_file.write(("** " + "Next Details " + "** ") * 5 + "\n")

                save_reg_file.close()

                messagebox.showinfo("Successful!", "Your registration is successful!!")
                self.reg.destroy()
                import LOGIN
            elif pos_info == "in Administrative Division":
                save_reg_file = open("Admin_Register_Details.txt", "a")
                save_reg_file.write("Position : " + pos_info + "\n")
                save_reg_file.write("First Name : " + fina_info + "\n")
                save_reg_file.write("Last Name : " + lana_info + "\n")
                save_reg_file.write("Address : " + addre_info + "\n")
                save_reg_file.write("Contact Number : " + conta_info + "\n")
                save_reg_file.write("Age : " + age_info + "\n")
                save_reg_file.write("Gender : " + gender_info + "\n")
                save_reg_file.write("Username : " + userna_info + "\n" + "\n")
                save_reg_file.write(("** " + "Next Admin Division Details " + "** ") * 3 + "\n")

                save_reg_file.close()

                save_log_file = open("Admin_Login_Details.txt", "a")
                save_log_file.write(userna_info)
                save_log_file.write(" ")
                save_log_file.write(pw_info)
                save_log_file.write("\n")
                save_log_file.close()

                messagebox.showinfo("Successful!", "Your registration is successful!!")
                self.reg.destroy()
                import LOGIN

            else:
                messagebox.showinfo("Information", "Please select 'Are you' field Correctly")

    def clear(self):
        pos_del = self.pos_entry.delete(0, "end")
        fina_del = self.fina_entry.delete(0, "end")
        lana_del = self.lana_entry.delete(0, "end")
        addre_del = self.addre_entry.delete(0, "end")
        conta_del = self.conta_entry.delete(0, "end")
        age_del = self.ag_entry.delete(0, "end")
        gender_del = self.ge_entry.delete(0, "end")
        userna_del = self.userna_entry.delete(0, "end")
        pw_del = self.pw_entry.delete(0, "end")


reg = Tk()
obj = all_register(reg)
reg.minsize(900, 700)
reg.maxsize(900, 700)
reg.mainloop()
