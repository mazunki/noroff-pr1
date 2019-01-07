import tkinter as tk

class Form_9(tk.Frame):
    def __init__(self, root):
        super().__init__(root, height=root.height, background="#ebf4f2")
        root.master.update_idletasks()

    def add_buttons(self, root):
        self.next = tk.Button(self, text="Next page", width=35, height=3, command=self.master.layers[10].tkraise)
        self.next.place(relx=1, rely=1, anchor="se")

        self.prev = tk.Button(self, text="Back", width=35, height=3, command=self.master.layers[8].tkraise)
        self.prev.place(relx=0, rely=1, anchor="sw")

    def add_form(self, root):
        import focus_handler as focus

        self.text_label = tk.Label(self, text="Personal data")
        self.text_label.place(relx=0.5, rely=0, anchor="n")

        self.title_1_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_1_container.grid(row=0, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_1_number = tk.Label(self.title_1_container, background="#006e51", text="8", fg="white", font="-weight bold")
        self.title_1 = tk.Label(self.title_1_container, background="#499a86", text="Your banking details", anchor="w", fg="white", font="-weight bold")
        self.title_1_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title_1.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)
        

        self.container_1_left = tk.Frame(self, background="#ebf4f2")
        self.container_1_right = tk.Frame(self, background="#d9eae5")
        #self.container_left.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_rowconfigure(4, weight=1)
        self.container_1_left.grid(row=1, column=0, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_1_right.grid(row=1, column=1, sticky="nsew", ipadx=root.margin, ipady=35)
        

        self.container_2_left = tk.Frame(self, background="#ebf4f2")
        self.container_2_right = tk.Frame(self, background="#d9eae5")
        #self.container_left.grid_propagate(False)
        self.container_2_left.grid(row=4, column=0, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_2_right.grid(row=4, column=1, sticky="nsew", ipadx=root.margin, ipady=35)

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

        self.personal_or_business_label_left = tk.Label(self.container_1_left, text="Is this a personal or a business account?", anchor="w")
        self.personal_or_business_label_left["bg"] = self.personal_or_business_label_left.master["bg"]
        self.personal_or_business_label_left.grid(row=1, column=0, sticky="nsew", padx=root.margin, pady=(10,0))
        self.container_1_left.grid_columnconfigure(0, weight=1)

        self.personal_or_business_value_left = tk.IntVar()
        self.personal_left = tk.Radiobutton(self.container_1_left, variable=self.personal_or_business_value_left, value="personal", text="Personal")
        self.business_left = tk.Radiobutton(self.container_1_left, variable=self.personal_or_business_value_left, value="business", text="Business")
        self.personal_left["bg"] = self.personal_left.master["bg"]
        self.business_left["bg"] = self.business_left.master["bg"]
        self.personal_left["activebackground"] = self.personal_left.master["bg"]
        self.business_left["activebackground"] = self.business_left.master["bg"]
        self.personal_left.grid(row=1, column=1, padx=root.margin, pady=(10,0))
        self.business_left.grid(row=1, column=2, padx=root.margin, pady=(10,0))


        # Right Side
        self.customer_label_right = tk.Label(self.container_1_right, text="Second customer", font=("Courier", 12, "bold"), justify="left")
        self.customer_label_right.grid(row=0, column=0, padx=(10,0), pady=(10,0), columnspan=5)
        self.customer_label_right["bg"] = self.customer_label_right.master["bg"]

        self.personal_or_business_label_right = tk.Label(self.container_1_right, text="Is this a personal\n or a business account?", anchor="w", justify="right")
        self.personal_or_business_label_right["bg"] = self.personal_or_business_label_right.master["bg"]
        self.personal_or_business_label_right.grid(row=1, column=0, sticky="nsew", padx=root.margin, pady=(10,0))
        self.container_1_right.grid_columnconfigure(0, weight=1)

        self.personal_or_business_value_right = tk.IntVar()
        self.personal_right = tk.Radiobutton(self.container_1_right, variable=self.personal_or_business_value_right, value="personal", text="Personal")
        self.business_right = tk.Radiobutton(self.container_1_right, variable=self.personal_or_business_value_right, value="business", text="Business")
        self.personal_right["bg"] = self.personal_right.master["bg"]
        self.business_right["bg"] = self.business_right.master["bg"]
        self.personal_right["activebackground"] = self.personal_right.master["bg"]
        self.business_right["activebackground"] = self.business_right.master["bg"]
        self.personal_right.grid(row=1, column=1, padx=root.margin, pady=(10,0))
        self.business_right.grid(row=1, column=2, padx=root.margin, pady=(10,0))



        # 8.1
        self.title_2_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_2_container.grid(row=3, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_2_number = tk.Label(self.title_2_container, fg="#006e51", text="8.1", bg="white", font="-weight bold", bd=2, relief="solid")
        self.title_2 = tk.Label(self.title_2_container, background="#499a86", text="Other banking details", anchor="w", fg="white", font="-weight bold")
        self.title_2_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title_2.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)


        # Left
        self.facilities_label_left = tk.Label(self.container_2_left, text="Which of the following\nfacilities do you use?", anchor="e", justify="right")
        self.facilities_label_left["bg"] = self.facilities_label_left.master["bg"]
        self.facilities_label_left.grid(row=0, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.container_2_left.grid_columnconfigure(3, weight=1)

        self.facilities_value_left = tk.IntVar()
        self.facilities_cheque_left = tk.Radiobutton(self.container_2_left, variable=self.facilities_value_left, value="cheque", text="Cheque card")
        self.facilities_cheque_left["bg"] = self.facilities_cheque_left.master["bg"]
        self.facilities_cheque_left["activebackground"] = self.facilities_cheque_left.master["bg"]
        self.facilities_debit_left = tk.Radiobutton(self.container_2_left, variable=self.facilities_value_left, value="debit", text="Debit card")
        self.facilities_debit_left["bg"] = self.facilities_debit_left.master["bg"]
        self.facilities_debit_left["activebackground"] = self.facilities_debit_left.master["bg"]
        self.facilities_cheque_left.grid(row=0, column=3, sticky="nsew", padx=root.margin, pady=(10,0))
        self.facilities_debit_left.grid(row=0, column=4, sticky="nsew", padx=root.margin, pady=(10,0))


        self.banking_time_label_left = tk.Label(self.container_2_left, text="For how long have\nyou banked there?", anchor="e", justify="right")
        self.banking_time_label_left["bg"] = self.banking_time_label_left.master["bg"]
        self.banking_time_label_left.grid(row=1, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.banking_time_left = tk.StringVar()
        self.banking_time_entry_left = tk.Entry(self.container_2_left, textvariable=self.banking_time_left)
        self.banking_time_entry_left.grid(row=1, column=4, sticky="we", columnspan=1, padx=root.margin, pady=(10,0))


        self.to_be_closed_label_left = tk.Label(self.container_2_left, text="Is the account to be closed?\n(explain if not)", anchor="e", justify="right")
        self.to_be_closed_label_left["bg"] = self.to_be_closed_label_left.master["bg"]
        self.to_be_closed_label_left.grid(row=2, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.to_be_closed_value_left = tk.IntVar()
        self.to_be_closed_true_left = tk.Radiobutton(self.container_2_left, variable=self.to_be_closed_value_left, value=True, text="Yes")
        self.to_be_closed_true_left["bg"] = self.to_be_closed_true_left.master["bg"]
        self.to_be_closed_true_left["activebackground"] = self.to_be_closed_true_left.master["bg"]
        self.to_be_closed_false_left = tk.Radiobutton(self.container_2_left, variable=self.to_be_closed_value_left, value=False, text="No")
        self.to_be_closed_false_left["bg"] = self.to_be_closed_false_left.master["bg"]
        self.to_be_closed_false_left["activebackground"] = self.to_be_closed_false_left.master["bg"]
        self.to_be_closed_true_left.grid(row=2, column=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.to_be_closed_false_left.grid(row=2, column=2, sticky="nsew", padx=root.margin, pady=(10,0))


        self.to_be_closed_left = tk.StringVar()
        self.to_be_closed_entry_left = tk.Entry(self.container_2_left, textvariable=self.to_be_closed_left)
        self.to_be_closed_entry_left.grid(row=2, column=3, sticky="we", columnspan=3, padx=root.margin, pady=(10,0))


        self.facilities_label_left = tk.Label(self.container_2_left, text="Would you like us to\ntransfer your account?", anchor="e", justify="right")
        self.facilities_label_left["bg"] = self.facilities_label_left.master["bg"]
        self.facilities_label_left.grid(row=3, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.container_2_left.grid_columnconfigure(3, weight=1)

        self.transfer_value_left = tk.IntVar()
        self.transfer_yes_left = tk.Radiobutton(self.container_2_left, variable=self.transfer_value_left, value=True, text="Yes")
        self.transfer_yes_left["bg"] = self.transfer_yes_left.master["bg"]
        self.transfer_yes_left["activebackground"] = self.transfer_yes_left.master["bg"]
        self.transfer_no_left = tk.Radiobutton(self.container_2_left, variable=self.transfer_value_left, value=False, text="No")
        self.transfer_no_left["bg"] = self.transfer_no_left.master["bg"]
        self.transfer_no_left["activebackground"] = self.transfer_no_left.master["bg"]
        self.transfer_yes_left.grid(row=3, column=3, sticky="nsew", padx=root.margin, pady=(10,0))
        self.transfer_no_left.grid(row=3, column=4, sticky="nsew", padx=root.margin, pady=(10,0))





        # Right
        self.facilities_label_right = tk.Label(self.container_2_right, text="Which of the following\nfacilities do you use?", anchor="e", justify="right")
        self.facilities_label_right["bg"] = self.facilities_label_right.master["bg"]
        self.facilities_label_right.grid(row=0, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.container_2_right.grid_columnconfigure(3, weight=1)

        self.facilities_value_right = tk.IntVar()
        self.facilities_cheque_right = tk.Radiobutton(self.container_2_right, variable=self.facilities_value_right, value="cheque", text="Cheque card")
        self.facilities_cheque_right["bg"] = self.facilities_cheque_right.master["bg"]
        self.facilities_cheque_right["activebackground"] = self.facilities_cheque_right.master["bg"]
        self.facilities_debit_right = tk.Radiobutton(self.container_2_right, variable=self.facilities_value_right, value="debit", text="Debit card")
        self.facilities_debit_right["bg"] = self.facilities_debit_right.master["bg"]
        self.facilities_debit_right["activebackground"] = self.facilities_debit_right.master["bg"]
        self.facilities_cheque_right.grid(row=0, column=3, sticky="nsew", padx=root.margin, pady=(10,0))
        self.facilities_debit_right.grid(row=0, column=4, sticky="nsew", padx=root.margin, pady=(10,0))


        self.banking_time_label_right = tk.Label(self.container_2_right, text="For how long have\nyou banked there?", anchor="e", justify="right")
        self.banking_time_label_right["bg"] = self.banking_time_label_right.master["bg"]
        self.banking_time_label_right.grid(row=1, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.banking_time_right = tk.Entry(self.container_2_right)
        self.banking_time_right.grid(row=1, column=4, sticky="we", columnspan=1, padx=root.margin, pady=(10,0))


        self.to_be_closed_label_right = tk.Label(self.container_2_right, text="Is the account to be closed?\n(explain if not)", anchor="e", justify="right")
        self.to_be_closed_label_right["bg"] = self.to_be_closed_label_right.master["bg"]
        self.to_be_closed_label_right.grid(row=2, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.to_be_closed_value_right = tk.IntVar()
        self.to_be_closed_true_right = tk.Radiobutton(self.container_2_right, variable=self.to_be_closed_value_right, value=True, text="Yes")
        self.to_be_closed_true_right["bg"] = self.to_be_closed_true_right.master["bg"]
        self.to_be_closed_true_right["activebackground"] = self.to_be_closed_true_right.master["bg"]
        self.to_be_closed_false_right = tk.Radiobutton(self.container_2_right, variable=self.to_be_closed_value_right, value=False, text="No")
        self.to_be_closed_false_right["bg"] = self.to_be_closed_false_right.master["bg"]
        self.to_be_closed_false_right["activebackground"] = self.to_be_closed_false_right.master["bg"]
        self.to_be_closed_true_right.grid(row=2, column=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.to_be_closed_false_right.grid(row=2, column=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.to_be_closed_right = tk.StringVar()
        self.to_be_closed_entry_right = tk.Entry(self.container_2_right, textvariable=self.to_be_closed_right)
        self.to_be_closed_entry_right.grid(row=2, column=3, sticky="we", columnspan=3, padx=root.margin, pady=(10,0))


        self.facilities_label_right = tk.Label(self.container_2_right, text="Would you like us to\ntransfer your account?", anchor="e", justify="right")
        self.facilities_label_right["bg"] = self.facilities_label_right.master["bg"]
        self.facilities_label_right.grid(row=3, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.container_2_right.grid_columnconfigure(3, weight=1)

        self.transfer_value_right = tk.IntVar()
        self.transfer_yes_right = tk.Radiobutton(self.container_2_right, variable=self.transfer_value_right, value=True, text="Yes")
        self.transfer_yes_right["bg"] = self.transfer_yes_right.master["bg"]
        self.transfer_yes_right["activebackground"] = self.transfer_yes_right.master["bg"]
        self.transfer_no_right = tk.Radiobutton(self.container_2_right, variable=self.transfer_value_right, value=False, text="No")
        self.transfer_no_right["bg"] = self.transfer_no_right.master["bg"]
        self.transfer_no_right["activebackground"] = self.transfer_no_right.master["bg"]
        self.transfer_yes_right.grid(row=3, column=3, sticky="nsew", padx=root.margin, pady=(10,0))
        self.transfer_no_right.grid(row=3, column=4, sticky="nsew", padx=root.margin, pady=(10,0))


