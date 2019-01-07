import tkinter as tk
import welcome_page, form_1, form_2, form_3, form_4, form_5, form_6, form_7, form_8, form_9, form_10
import user as users
from importedframe import *

#class Layers(VerticalScrolledFrame):
class Layers(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        self.margin = 20
        self.height = 500
        self.button_height = 0

        self.layers = []

        self.layers.append(welcome_page.Welcome_Page(self))
        self.layers.append(form_1.Form_1(self))
        self.layers.append(form_2.Form_2(self))
        self.layers.append(form_3.Form_3(self))
        self.layers.append(form_4.Form_4(self))
        self.layers.append(form_5.Form_5(self))
        self.layers.append(form_6.Form_6(self))
        self.layers.append(form_7.Form_7(self))
        self.layers.append(form_8.Form_8(self))
        self.layers.append(form_9.Form_9(self))
        self.layers.append(form_10.Form_10(self))

        self.heading = tk.Frame(self, background="#006e51", height=50)
        self.heading.grid(row=0, column=0, sticky="nsew")
        self.title = tk.Label(self.heading, text="Lloyd Bank registration form", font=("Courier", 18, "bold"), fg="white")
        self.title["bg"] = self.title.master["bg"]
        #self.heading.pack_propagate(0)
        self.title.pack(anchor="center", expand=True)

        self.placeholder = users.User("0")


        for layer in self.layers:
            layer.add_buttons(self)
            layer.add_form(self)
            layer.add_buttons(self)
            layer.grid(row=1, column=0, sticky="nsew")
        self.grid_rowconfigure(1, weight=1)
        self.layers[0].tkraise()

        self.layers[0].update()
        self.layers[0].explanation["wraplength"] = self.layers[0].explanation.winfo_width()
        self.layers[0].explanation.update()



if __name__ == '__main__':
    root = tk.Tk()
    #root.geometry("1000x500")
    root.title("Lloyd Registration App")
    root.resizable(False, True)
    window = Layers(root)
    window.pack(expand=True, fill="both")
    root.mainloop()