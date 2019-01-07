import tkinter as tk

class Welcome_Page(tk.Frame):
    def __init__(self, root):
        super().__init__(root, height=root.height, background="#ebf4f2")
        root.master.update_idletasks()


    def add_buttons(self, root):
        self.next = tk.Button(self, text="Next page", width=35, height=3, command=self.master.layers[1].tkraise)
        self.next.place(relx=1, rely=1, anchor="se")

        self.prev = tk.Button(self, text="Quit", width=35, height=3, command=self.master.master.destroy)
        self.prev.place(relx=0, rely=1, anchor="sw")

    def add_form(self, root):

        self.title_label = tk.Label(self, text="Sole/Joint Lloyds Bank account", font=("Courier", 24, "bold"), fg="#006e51")
        self.title_label["bg"] = self.title_label.master["bg"]
        self.title_label.grid(row=1, column=0, columnspan=2, sticky="w", padx=(10,0))
    
        self.sub_title_label = tk.Label(self, text="This form is not to be used for an Added Value Account", font=("Courier", 16, "bold"), fg="#006e51", wraplength=500, justify="left")
        self.sub_title_label["bg"] = self.sub_title_label.master["bg"]
        self.sub_title_label.grid(row=2, column=0, columnspan=2, sticky="w", padx=(10,0), pady=(5,5))

        self.container_left = tk.Frame(self, background="#ebf4f2")
        self.container_right = tk.Frame(self, background="#d9eae5")
        self.container_left.grid(row=3, column=0, sticky="nsew", padx=10)
        self.container_right.grid(row=3, column=1, sticky="nsew", padx=10)
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_rowconfigure(3, weight=1)
        self.container_left.grid_propagate(False)
        self.container_right.grid_propagate(False)
        
        self.container_left_wrapper = tk.Frame(self.container_left)
        self.container_left_wrapper.place(relx=0.2, rely=0.3)
        self.container_left_wrapper["bg"] = self.container_left_wrapper.master["bg"]

        self.username_label = tk.Label(self.container_left_wrapper, text="Username 1: ", anchor="s")
        self.username_label.grid(row=0, column=0, sticky="s")
        self.username_label["bg"] = self.username_label.master["bg"]

        self.id1 = tk.StringVar()
        self.username = tk.Entry(self.container_left_wrapper, textvariable=self.id1)
        self.username.grid(row=0, column=1)

        self.password_label = tk.Label(self.container_left_wrapper, text="Password 1: ", anchor="center")
        self.password_label.grid(row=1, column=0, sticky="nsew")
        self.password_label["bg"] = self.password_label.master["bg"]

        self.pw1 = tk.StringVar()
        self.password = tk.Entry(self.container_left_wrapper, textvariable=self.pw1)
        self.password.grid(row=1, column=1)


        self.username2_label = tk.Label(self.container_left_wrapper, text="Username 1: ", anchor="s")
        self.username2_label.grid(row=0, column=2, sticky="s")
        self.username2_label["bg"] = self.username_label.master["bg"]

        self.id2 = tk.StringVar()
        self.username2 = tk.Entry(self.container_left_wrapper, textvariable=self.id2)
        self.username2.grid(row=0, column=3)

        self.password2_label = tk.Label(self.container_left_wrapper, text="Password 1: ", anchor="center")
        self.password2_label.grid(row=1, column=2, sticky="nsew")
        self.password2_label["bg"] = self.password_label.master["bg"]

        self.pw2 = tk.StringVar()
        self.password2 = tk.Entry(self.container_left_wrapper, textvariable=self.pw2)
        self.password2.grid(row=1, column=3)

        self.load_button = tk.Button(self.container_left_wrapper, text="Load users", command=lambda :self.master.placeholder.login_button(self.id1.get(), self.id2.get(), self.pw1.get(), self.pw2.get(), self))
        self.load_button.grid(row=3, columnspan=4, column=0, sticky="nsew")

 
        self.explanation = tk.Label(self.container_right, font=("Courier", 14), wraplength=516, justify="left",
                                   text= "This program was made by Rolf Vidar Hoksaas for\na school project.\n")
        self.explanation["bg"] = self.explanation.master["bg"]
        self.explanation.grid(row=0, column=0, padx=(10,10))
        