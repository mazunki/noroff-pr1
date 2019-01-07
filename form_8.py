import tkinter as tk

class Form_8(tk.Frame):
    def __init__(self, root):
        super().__init__(root, height=root.height, background="#ebf4f2")
        root.master.update_idletasks()

    def add_buttons(self, root):
        self.next = tk.Button(self, text="Next page", width=35, height=3, command=self.master.layers[9].tkraise)
        self.next.place(relx=1, rely=1, anchor="se")

        self.prev = tk.Button(self, text="Back", width=35, height=3, command=self.master.layers[7].tkraise)
        self.prev.place(relx=0, rely=1, anchor="sw")

    def add_form(self, root):
        import focus_handler as focus

        self.text_label = tk.Label(self, text="Personal data")
        self.text_label.place(relx=0.5, rely=0, anchor="n")

        self.title_1_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_1_container.grid(row=0, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_1_number = tk.Label(self.title_1_container, fg="#006e51", text="6.1", bg="white", font="-weight bold", bd=2, relief="solid")
        self.title_1 = tk.Label(self.title_1_container, background="#499a86", text="Monthly commitments", anchor="w", fg="white", font="-weight bold")
        self.title_1_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title_1.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)
        

        self.container_1_left = tk.Frame(self, background="#ebf4f2")
        self.container_1_right = tk.Frame(self, background="#d9eae5")
        #self.container_1_left.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_rowconfigure(3, weight=1)
        self.container_1_left.grid(row=1, column=0, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_1_right.grid(row=1, column=1, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_1_left.grid_columnconfigure(1, weight=1)
        self.container_1_right.grid_columnconfigure(1, weight=1)

        self.container_2_left = tk.Frame(self, background="#ebf4f2")
        self.container_2_right = tk.Frame(self, background="#d9eae5")
        #self.container_1_left.grid_propagate(False)
        self.container_2_left.grid(row=3, column=0, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_2_right.grid(row=3, column=1, sticky="nsew", ipadx=root.margin, ipady=35)

        def gray_out(*whats):
            for what in whats:
                    what["state"] = "disabled"
        def ungray(*whats):
            for what in whats:
                what["state"] = "normal"  


        # Left Side
        self.customer_label_left = tk.Label(self.container_1_left, text="First customer", font=("Courier", 12, "bold"), justify="left")
        self.customer_label_left.grid(row=0, column=0, padx=(10,0), pady=(10,0), columnspan=5)
        self.customer_label_left["bg"] = self.customer_label_left.master["bg"]


        self.mortage_label_left = tk.Label(self.container_1_left, text="Mortage/rent", justify="left")
        self.mortage_label_left.grid(row=1, column=0, padx=(10,0), pady=(10,0))
        self.mortage_label_left["bg"] = self.mortage_label_left.master["bg"]

        self.mortage_left = tk.StringVar()
        self.mortage_entry_left = tk.Entry(self.container_1_left, textvariable=self.mortage_left)
        self.mortage_entry_left.grid(row=1, column=1, padx=root.margin, pady=(10,0), columnspan=3, sticky="nsew")


        self.other_loans_label_left = tk.Label(self.container_1_left, text="HP/other loans", justify="left")
        self.other_loans_label_left.grid(row=2, column=0, padx=(10,0), pady=(10,0))
        self.other_loans_label_left["bg"] = self.other_loans_label_left.master["bg"]

        self.other_loans_left = tk.StringVar()
        self.other_loans_entry_left = tk.Entry(self.container_1_left, textvariable=self.other_loans_left)
        self.other_loans_entry_left.grid(row=2, column=1, padx=root.margin, pady=(10,0), columnspan=3, sticky="nsew")


        self.lloyd_loans_label_left = tk.Label(self.container_1_left, text="Lloyd Bank loans", justify="left")
        self.lloyd_loans_label_left.grid(row=3, column=0, padx=(10,0), pady=(10,0))
        self.lloyd_loans_label_left["bg"] = self.lloyd_loans_label_left.master["bg"]

        self.lloyd_loans_left = tk.StringVar()
        self.lloyd_loans_entry_left = tk.Entry(self.container_1_left, textvariable=self.lloyd_loans_left)
        self.lloyd_loans_entry_left.grid(row=3, column=1, padx=root.margin, pady=(10,0), columnspan=3, sticky="nsew")


        self.total_label_left = tk.Label(self.container_1_left, text="Total each month", justify="left")
        self.total_label_left.grid(row=4, column=0, padx=(10,0), pady=(10,0))
        self.total_label_left["bg"] = self.total_label_left.master["bg"]

        self.total_left = tk.StringVar()
        self.total_entry_left = tk.Entry(self.container_1_left, textvariable=self.total_left)
        self.total_entry_left.grid(row=4, column=1, padx=root.margin, pady=(10,0), columnspan=3, sticky="nsew")


        # Right Side
        self.customer_label_right = tk.Label(self.container_1_right, text="First customer", font=("Courier", 12, "bold"), justify="left")
        self.customer_label_right.grid(row=0, column=0, padx=(10,0), pady=(10,0), columnspan=5)
        self.customer_label_right["bg"] = self.customer_label_right.master["bg"]


        self.mortage_label_right = tk.Label(self.container_1_right, text="Mortage/rent", justify="left")
        self.mortage_label_right.grid(row=1, column=0, padx=(10,0), pady=(10,0))
        self.mortage_label_right["bg"] = self.mortage_label_right.master["bg"]

        self.mortage_right = tk.StringVar()
        self.mortage_entry_right = tk.Entry(self.container_1_right, textvariable=self.mortage_right)
        self.mortage_entry_right.grid(row=1, column=1, padx=root.margin, pady=(10,0), columnspan=3, sticky="nsew")


        self.other_loans_label_right = tk.Label(self.container_1_right, text="HP/other loans", justify="left")
        self.other_loans_label_right.grid(row=2, column=0, padx=(10,0), pady=(10,0))
        self.other_loans_label_right["bg"] = self.other_loans_label_right.master["bg"]

        self.other_loans_right = tk.StringVar()
        self.other_loans_entry_right = tk.Entry(self.container_1_right, textvariable=self.other_loans_right)
        self.other_loans_entry_right.grid(row=2, column=1, padx=root.margin, pady=(10,0), columnspan=3, sticky="nsew")


        self.lloyd_loans_label_right = tk.Label(self.container_1_right, text="Lloyd Bank loans", justify="left")
        self.lloyd_loans_label_right.grid(row=3, column=0, padx=(10,0), pady=(10,0))
        self.lloyd_loans_label_right["bg"] = self.lloyd_loans_label_right.master["bg"]

        self.lloyd_loans_right = tk.StringVar()
        self.lloyd_loans_entry_right = tk.Entry(self.container_1_right, textvariable=self.lloyd_loans_right)
        self.lloyd_loans_entry_right.grid(row=3, column=1, padx=root.margin, pady=(10,0), columnspan=3, sticky="nsew")


        self.total_label_right = tk.Label(self.container_1_right, text="Total each month", justify="left")
        self.total_label_right.grid(row=4, column=0, padx=(10,0), pady=(10,0))
        self.total_label_right["bg"] = self.total_label_right.master["bg"]

        self.total_right = tk.StringVar()
        self.total_entry_right = tk.Entry(self.container_1_right, textvariable=self.total_right)
        self.total_entry_right.grid(row=4, column=1, padx=root.margin, pady=(10,0), columnspan=3, sticky="nsew")



        # Part 7
        self.title_2_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_2_container.grid(row=2, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_2_number = tk.Label(self.title_2_container, background="#006e51", text="7", fg="white", font="-weight bold")
        self.title_2 = tk.Label(self.title_2_container, background="#499a86", text="Details of your savings", anchor="w", fg="white", font="-weight bold")
        self.title_2_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title_2.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)


        # Left
        self.type_of_savings_label_left = tk.Label(self.container_2_left, text="What type of savings do you have?")
        self.type_of_savings_label_left.grid(row=0, column=0, padx=root.margin, pady=(10,0))
        self.type_of_savings_label_left["bg"] = self.type_of_savings_label_left.master["bg"]

        self.type_of_savings_value_left = tk.IntVar()
        
        self.no_savings_left = tk.Radiobutton(self.container_2_left, text="No savings", variable=self.type_of_savings_value_left, value="no_savings")
        self.no_savings_left.grid(row=1, column=0, padx=root.margin, pady=(10,0))
        self.no_savings_left["bg"] = self.no_savings_left.master["bg"]
        self.no_savings_left["activebackground"] = self.no_savings_left.master["bg"]
        
        self.lloyd_bank_savings_left = tk.Radiobutton(self.container_2_left, text="Only Lloyd", variable=self.type_of_savings_value_left, value="lloyd_only")
        self.lloyd_bank_savings_left.grid(row=1, column=1, padx=root.margin, pady=(10,0))
        self.lloyd_bank_savings_left["bg"] = self.lloyd_bank_savings_left.master["bg"]
        self.lloyd_bank_savings_left["activebackground"] = self.lloyd_bank_savings_left.master["bg"]
        
        self.lloyd_and_other_left = tk.Radiobutton(self.container_2_left, text="Lloyd and non-Lloyd", variable=self.type_of_savings_value_left, value="lloyd_and_other")
        self.lloyd_and_other_left.grid(row=1, column=2, padx=root.margin, pady=(10,0))
        self.lloyd_and_other_left["bg"] = self.lloyd_and_other_left.master["bg"]
        self.lloyd_and_other_left["activebackground"] = self.lloyd_and_other_left.master["bg"]
        
        self.other_only_left = tk.Radiobutton(self.container_2_left, text="Other only", variable=self.type_of_savings_value_left, value="other_only")
        self.other_only_left.grid(row=2, column=0, padx=root.margin, pady=(10,0))
        self.other_only_left["bg"] = self.other_only_left.master["bg"]
        self.other_only_left["activebackground"] = self.other_only_left.master["bg"]


        self.total_savings_label_left = tk.Label(self.container_2_left, text="Total savings")
        self.total_savings_label_left.grid(row=2, column=1, padx=root.margin, pady=(10,0))
        self.total_savings_label_left["bg"] = self.total_savings_label_left.master["bg"]

        self.total_savings_left = tk.StringVar()
        self.total_savings_entry_left = tk.Entry(self.container_2_left, textvariable=self.total_savings_left)
        self.total_savings_entry_left.grid(row=2, column=2, sticky="we")


        # Right
        self.type_of_savings_label_right = tk.Label(self.container_2_right, text="What type of savings do you have?")
        self.type_of_savings_label_right.grid(row=0, column=0, padx=root.margin, pady=(10,0))
        self.type_of_savings_label_right["bg"] = self.type_of_savings_label_right.master["bg"]

        self.type_of_savings_value_right = tk.IntVar()
        
        self.no_savings_right = tk.Radiobutton(self.container_2_right, text="No savings", variable=self.type_of_savings_value_right, value="no_savings")
        self.no_savings_right.grid(row=1, column=0, padx=root.margin, pady=(10,0))
        self.no_savings_right["bg"] = self.no_savings_right.master["bg"]
        self.no_savings_right["activebackground"] = self.no_savings_right.master["bg"]
        
        self.lloyd_bank_savings_right = tk.Radiobutton(self.container_2_right, text="Only Lloyd", variable=self.type_of_savings_value_right, value="lloyd_only")
        self.lloyd_bank_savings_right.grid(row=1, column=1, padx=root.margin, pady=(10,0))
        self.lloyd_bank_savings_right["bg"] = self.lloyd_bank_savings_right.master["bg"]
        self.lloyd_bank_savings_right["activebackground"] = self.lloyd_bank_savings_right.master["bg"]
        
        self.lloyd_and_other_right = tk.Radiobutton(self.container_2_right, text="Lloyd and non-Lloyd", variable=self.type_of_savings_value_right, value="lloyd_and_other")
        self.lloyd_and_other_right.grid(row=1, column=2, padx=root.margin, pady=(10,0))
        self.lloyd_and_other_right["bg"] = self.lloyd_and_other_right.master["bg"]
        self.lloyd_and_other_right["activebackground"] = self.lloyd_and_other_right.master["bg"]
        
        self.other_only_right = tk.Radiobutton(self.container_2_right, text="Other only", variable=self.type_of_savings_value_right, value="other_only")
        self.other_only_right.grid(row=2, column=0, padx=root.margin, pady=(10,0))
        self.other_only_right["bg"] = self.other_only_right.master["bg"]
        self.other_only_right["activebackground"] = self.other_only_right.master["bg"]


        self.total_savings_label_right = tk.Label(self.container_2_right, text="Total savings")
        self.total_savings_label_right.grid(row=2, column=1, padx=root.margin, pady=(10,0))
        self.total_savings_label_right["bg"] = self.total_savings_label_right.master["bg"]

        self.total_savings_right = tk.StringVar()
        self.total_savings_entry_right = tk.Entry(self.container_2_right, textvariable=self.total_savings_right)
        self.total_savings_entry_right.grid(row=2, column=2, sticky="we")