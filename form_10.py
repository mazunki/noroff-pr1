import tkinter as tk

class Form_10(tk.Frame):
    def __init__(self, root):
        super().__init__(root, height=root.height, background="#ebf4f2")
        root.master.update_idletasks()

    def add_buttons(self, root):
        self.next = tk.Button(self, text="Save", width=35, height=3, command=lambda:self.master.placeholder.login_button("","","","",self,2))
        self.next.place(relx=1, rely=1, anchor="se")

        self.prev = tk.Button(self, text="Back", width=35, height=3, command=self.master.layers[9].tkraise)
        self.prev.place(relx=0, rely=1, anchor="sw")

    def add_form(self, root):
        import focus_handler as focus

        self.text_label = tk.Label(self, text="Personal data")
        self.text_label.place(relx=0.5, rely=0, anchor="n")

        self.title_1_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_1_container.grid(row=0, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_1_number = tk.Label(self.title_1_container, fg="#006e51", text="8.2", bg="white", font="-weight bold", bd=2, relief="solid")
        self.title_1 = tk.Label(self.title_1_container, background="#499a86", text="Your credit card details", anchor="w", fg="white", font="-weight bold")
        self.title_1_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title_1.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)
        

        self.container_1_left = tk.Frame(self, background="#ebf4f2")
        self.container_1_right = tk.Frame(self, background="#d9eae5")
        #self.container_left.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_rowconfigure(3, weight=1)
        self.container_1_left.grid(row=1, column=0, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_1_right.grid(row=1, column=1, sticky="nsew", ipadx=root.margin, ipady=35)

        self.container_2_left = tk.Frame(self, background="#ebf4f2")
        self.container_2_right = tk.Frame(self, background="#d9eae5")
        #self.container_left.grid_propagate(False)
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

        self.container_1_left.grid_columnconfigure(3, weight=1)

        self.hold_credit_card_label_left = tk.Label(self.container_1_left, text="Do you hold\n a credit card?\n(if yes, how many)", anchor="e", justify="right")
        self.hold_credit_card_label_left["bg"] = self.hold_credit_card_label_left.master["bg"]
        self.hold_credit_card_label_left.grid(row=1, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.hold_credit_card_value_left = tk.IntVar()
        self.hold_credit_card_true_left = tk.Radiobutton(self.container_1_left, variable=self.hold_credit_card_value_left, value=True, text="Yes")
        self.hold_credit_card_true_left["bg"] = self.hold_credit_card_true_left.master["bg"]
        self.hold_credit_card_true_left["activebackground"] = self.hold_credit_card_true_left.master["bg"]
        self.hold_credit_card_false_left = tk.Radiobutton(self.container_1_left, variable=self.hold_credit_card_value_left, value=False, text="No")
        self.hold_credit_card_false_left["bg"] = self.hold_credit_card_false_left.master["bg"]
        self.hold_credit_card_false_left["activebackground"] = self.hold_credit_card_false_left.master["bg"]
        self.hold_credit_card_true_left.grid(row=1, column=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.hold_credit_card_false_left.grid(row=1, column=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.how_many_credit_card_left = tk.StringVar()
        self.how_many_credit_entry_card_left = tk.Entry(self.container_1_left, textvariable=self.how_many_credit_card_left)
        self.how_many_credit_entry_card_left.grid(row=1, column=3, sticky="we", columnspan=2, padx=root.margin, pady=(10,0))



        self.credit_lloyd_banks_label_left = tk.Label(self.container_1_left, text="Are any\nLloyd Bank?\n(if yes, what credit limit?)", anchor="e", justify="right")
        self.credit_lloyd_banks_label_left["bg"] = self.credit_lloyd_banks_label_left.master["bg"]
        self.credit_lloyd_banks_label_left.grid(row=2, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.credit_lloyd_banks_value_left = tk.IntVar()
        self.credit_lloyd_banks_true_left = tk.Radiobutton(self.container_1_left, variable=self.credit_lloyd_banks_value_left, value=True, text="Yes")
        self.credit_lloyd_banks_true_left["bg"] = self.credit_lloyd_banks_true_left.master["bg"]
        self.credit_lloyd_banks_true_left["activebackground"] = self.credit_lloyd_banks_true_left.master["bg"]
        self.credit_lloyd_banks_false_left = tk.Radiobutton(self.container_1_left, variable=self.credit_lloyd_banks_value_left, value=False, text="No")
        self.credit_lloyd_banks_false_left["bg"] = self.credit_lloyd_banks_false_left.master["bg"]
        self.credit_lloyd_banks_false_left["activebackground"] = self.credit_lloyd_banks_false_left.master["bg"]
        self.credit_lloyd_banks_true_left.grid(row=2, column=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.credit_lloyd_banks_false_left.grid(row=2, column=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.credit_lloyd_bank_limit_left = tk.StringVar()
        self.credit_lloyd_bank_entry_limit = tk.Entry(self.container_1_left, textvariable=self.credit_lloyd_bank_limit_left)
        self.credit_lloyd_bank_entry_limit.grid(row=2, column=3, sticky="we", columnspan=2, padx=root.margin, pady=(10,0))



        self.other_cards_label_left = tk.Label(self.container_1_left, text="What other card types\ndo you hold?\n(please specify)", anchor="e", justify="right")
        self.other_cards_label_left["bg"] = self.other_cards_label_left.master["bg"]
        self.other_cards_label_left.grid(row=3, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.other_cards_value_left = tk.IntVar()
        self.other_cards_chargecard_left = tk.Radiobutton(self.container_1_left, variable=self.other_cards_value_left, value="chargecard", text="Chargecard")
        self.other_cards_chargecard_left["bg"] = self.other_cards_chargecard_left.master["bg"]
        self.other_cards_chargecard_left["activebackground"] = self.other_cards_chargecard_left.master["bg"]
        self.other_cards_storecard_left = tk.Radiobutton(self.container_1_left, variable=self.other_cards_value_left, value="storecard", text="Storecard")
        self.other_cards_storecard_left["bg"] = self.other_cards_storecard_left.master["bg"]
        self.other_cards_storecard_left["activebackground"] = self.other_cards_storecard_left.master["bg"]
        self.other_cards_chargecard_left.grid(row=3, column=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.other_cards_storecard_left.grid(row=3, column=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.other_cards_left = tk.StringVar()
        self.other_cards_entry_left = tk.Entry(self.container_1_left, textvariable=self.other_cards_left)
        self.other_cards_entry_left.grid(row=3, column=3, sticky="we", columnspan=2, padx=root.margin, pady=(10,0))



        # Right Side
        self.customer_label_right = tk.Label(self.container_1_right, text="Second customer", font=("Courier", 12, "bold"), justify="left")
        self.customer_label_right.grid(row=0, column=0, padx=(10,0), pady=(10,0), columnspan=5)
        self.customer_label_right["bg"] = self.customer_label_right.master["bg"]

        self.container_1_right.grid_columnconfigure(3, weight=1)

        self.hold_credit_card_label_right = tk.Label(self.container_1_right, text="Do you hold\n a credit card?\n(if yes, how many)", anchor="e", justify="right")
        self.hold_credit_card_label_right["bg"] = self.hold_credit_card_label_right.master["bg"]
        self.hold_credit_card_label_right.grid(row=1, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.hold_credit_card_value_right = tk.IntVar()
        self.hold_credit_card_true_right = tk.Radiobutton(self.container_1_right, variable=self.hold_credit_card_value_right, value=True, text="Yes")
        self.hold_credit_card_true_right["bg"] = self.hold_credit_card_true_right.master["bg"]
        self.hold_credit_card_true_right["activebackground"] = self.hold_credit_card_true_right.master["bg"]
        self.hold_credit_card_false_right = tk.Radiobutton(self.container_1_right, variable=self.hold_credit_card_value_right, value=False, text="No")
        self.hold_credit_card_false_right["bg"] = self.hold_credit_card_false_right.master["bg"]
        self.hold_credit_card_false_right["activebackground"] = self.hold_credit_card_false_right.master["bg"]
        self.hold_credit_card_true_right.grid(row=1, column=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.hold_credit_card_false_right.grid(row=1, column=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.how_many_credit_card_right = tk.Entry(self.container_1_right)
        self.how_many_credit_card_right.grid(row=1, column=3, sticky="we", columnspan=2, padx=root.margin, pady=(10,0))



        self.credit_lloyd_banks_label_right = tk.Label(self.container_1_right, text="Are any\nLloyd Bank?\n(if yes, what credit limit?)", anchor="e", justify="right")
        self.credit_lloyd_banks_label_right["bg"] = self.credit_lloyd_banks_label_right.master["bg"]
        self.credit_lloyd_banks_label_right.grid(row=2, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.credit_lloyd_banks_value_right = tk.IntVar()
        self.credit_lloyd_banks_true_right = tk.Radiobutton(self.container_1_right, variable=self.credit_lloyd_banks_value_right, value=True, text="Yes")
        self.credit_lloyd_banks_true_right["bg"] = self.credit_lloyd_banks_true_right.master["bg"]
        self.credit_lloyd_banks_true_right["activebackground"] = self.credit_lloyd_banks_true_right.master["bg"]
        self.credit_lloyd_banks_false_right = tk.Radiobutton(self.container_1_right, variable=self.credit_lloyd_banks_value_right, value=False, text="No")
        self.credit_lloyd_banks_false_right["bg"] = self.credit_lloyd_banks_false_right.master["bg"]
        self.credit_lloyd_banks_false_right["activebackground"] = self.credit_lloyd_banks_false_right.master["bg"]
        self.credit_lloyd_banks_true_right.grid(row=2, column=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.credit_lloyd_banks_false_right.grid(row=2, column=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.credit_lloyd_bank_limit_right = tk.StringVar()
        self.credit_lloyd_bank_entry_limit_right = tk.Entry(self.container_1_right, textvariable=self.credit_lloyd_bank_limit_right)
        self.credit_lloyd_bank_entry_limit_right.grid(row=2, column=3, sticky="we", columnspan=2, padx=root.margin, pady=(10,0))



        self.other_cards_label_right = tk.Label(self.container_1_right, text="What other card types\ndo you hold?\n(please specify)", anchor="e", justify="right")
        self.other_cards_label_right["bg"] = self.other_cards_label_right.master["bg"]
        self.other_cards_label_right.grid(row=3, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.other_cards_value_right = tk.IntVar()
        self.other_cards_chargecard_right = tk.Radiobutton(self.container_1_right, variable=self.other_cards_value_right, value="chargecard", text="Chargecard")
        self.other_cards_chargecard_right["bg"] = self.other_cards_chargecard_right.master["bg"]
        self.other_cards_chargecard_right["activebackground"] = self.other_cards_chargecard_right.master["bg"]
        self.other_cards_storecard_right = tk.Radiobutton(self.container_1_right, variable=self.other_cards_value_right, value="storecard", text="Storecard")
        self.other_cards_storecard_right["bg"] = self.other_cards_storecard_right.master["bg"]
        self.other_cards_storecard_right["activebackground"] = self.other_cards_storecard_right.master["bg"]
        self.other_cards_chargecard_right.grid(row=3, column=1, sticky="nsew", padx=root.margin, pady=(10,0))
        self.other_cards_storecard_right.grid(row=3, column=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.other_cards_right = tk.StringVar()
        self.other_cards_entry_right = tk.Entry(self.container_1_right, textvariable=self.other_cards_right)
        self.other_cards_entry_right.grid(row=3, column=3, sticky="we", columnspan=2, padx=root.margin, pady=(10,0))



        # 8.3

        self.title_2_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_2_container.grid(row=2, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_1_number = tk.Label(self.title_2_container, fg="#006e51", text="8.3", bg="white", font="-weight bold", bd=2, relief="solid")
        self.title_1 = tk.Label(self.title_2_container, background="#499a86", text="Your mortage details", anchor="w", fg="white", font="-weight bold")
        self.title_1_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title_1.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)

        self.container_2_left.grid_columnconfigure(0, weight=1)
        self.container_2_left.grid_columnconfigure(1, weight=1)
        self.container_2_left.grid_columnconfigure(2, weight=1)
        self.container_2_left.grid_columnconfigure(3, weight=1)

        self.container_2_right.grid_columnconfigure(0, weight=1)
        self.container_2_right.grid_columnconfigure(1, weight=1)
        self.container_2_right.grid_columnconfigure(2, weight=1)
        self.container_2_right.grid_columnconfigure(3, weight=1)

        # Left
        self.have_mortage_label_left = tk.Label(self.container_2_left, text="Do you have a mortage?", anchor="w", justify="right")
        self.have_mortage_label_left["bg"] = self.have_mortage_label_left.master["bg"]
        self.have_mortage_label_left.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.have_mortage_value_left = tk.IntVar()
        self.have_mortage_true_left = tk.Radiobutton(self.container_2_left, variable=self.have_mortage_value_left, value=True, text="Yes")
        self.have_mortage_true_left["bg"] = self.have_mortage_true_left.master["bg"]
        self.have_mortage_true_left["activebackground"] = self.have_mortage_true_left.master["bg"]
        self.have_mortage_false_left = tk.Radiobutton(self.container_2_left, variable=self.have_mortage_value_left, value=False, text="No")
        self.have_mortage_false_left["bg"] = self.have_mortage_false_left.master["bg"]
        self.have_mortage_false_left["activebackground"] = self.have_mortage_false_left.master["bg"]
        self.have_mortage_true_left.grid(row=0, column=2, sticky="nsew", padx=root.margin, pady=(10,0))
        self.have_mortage_false_left.grid(row=0, column=3, sticky="nsew", padx=root.margin, pady=(10,0))


        self.mortage_with_lloyd_label_left = tk.Label(self.container_2_left, text="If yes, is it with Lloyds Bank?", anchor="w", justify="right")
        self.mortage_with_lloyd_label_left["bg"] = self.mortage_with_lloyd_label_left.master["bg"]
        self.mortage_with_lloyd_label_left.grid(row=1, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.mortage_with_lloyd_value_left = tk.IntVar()
        self.mortage_with_lloyd_true_left = tk.Radiobutton(self.container_2_left, variable=self.mortage_with_lloyd_value_left, value=True, text="Yes")
        self.mortage_with_lloyd_true_left["bg"] = self.mortage_with_lloyd_true_left.master["bg"]
        self.mortage_with_lloyd_true_left["activebackground"] = self.mortage_with_lloyd_true_left.master["bg"]
        self.mortage_with_lloyd_false_left = tk.Radiobutton(self.container_2_left, variable=self.mortage_with_lloyd_value_left, value=False, text="No")
        self.mortage_with_lloyd_false_left["bg"] = self.mortage_with_lloyd_false_left.master["bg"]
        self.mortage_with_lloyd_false_left["activebackground"] = self.mortage_with_lloyd_false_left.master["bg"]
        self.mortage_with_lloyd_true_left.grid(row=1, column=2, sticky="nsew", padx=root.margin, pady=(10,0))
        self.mortage_with_lloyd_false_left.grid(row=1, column=3, sticky="nsew", padx=root.margin, pady=(10,0))


        self.balance_mortage_label_left = tk.Label(self.container_2_left, text="What is the outstanding balance\non your mortage?", anchor="e", justify="right")
        self.balance_mortage_label_left["bg"] = self.balance_mortage_label_left.master["bg"]
        self.balance_mortage_label_left.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.balance_mortage_left = tk.StringVar()
        self.balance_mortage_entry_left = tk.Entry(self.container_2_left, textvariable=self.balance_mortage_left)
        self.balance_mortage_entry_left.grid(row=2, column=2, sticky="we", columnspan=2, padx=root.margin, pady=(10,0))


        self.value_house_label_left = tk.Label(self.container_2_left, text="What is the value\non your house?", anchor="e", justify="right")
        self.value_house_label_left["bg"] = self.value_house_label_left.master["bg"]
        self.value_house_label_left.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.value_house_left = tk.StringVar()
        self.value_house_entry_left = tk.Entry(self.container_2_left, textvariable=self.value_house_left)
        self.value_house_entry_left.grid(row=3, column=2, sticky="we", columnspan=2, padx=root.margin, pady=(10,0))


        # Right
        self.have_mortage_label_right = tk.Label(self.container_2_right, text="Do you have a mortage?", anchor="w", justify="right")
        self.have_mortage_label_right["bg"] = self.have_mortage_label_right.master["bg"]
        self.have_mortage_label_right.grid(row=0, column=0, columnspan=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.have_mortage_value_right = tk.IntVar()
        self.have_mortage_true_right = tk.Radiobutton(self.container_2_right, variable=self.have_mortage_value_right, value="yes", text="Yes")
        self.have_mortage_true_right["bg"] = self.have_mortage_true_right.master["bg"]
        self.have_mortage_true_right["activebackground"] = self.have_mortage_true_right.master["bg"]
        self.have_mortage_false_right = tk.Radiobutton(self.container_2_right, variable=self.have_mortage_value_right, value="no", text="No")
        self.have_mortage_false_right["bg"] = self.have_mortage_false_right.master["bg"]
        self.have_mortage_false_right["activebackground"] = self.have_mortage_false_right.master["bg"]
        self.have_mortage_true_right.grid(row=0, column=2, sticky="nsew", padx=root.margin, pady=(10,0))
        self.have_mortage_false_right.grid(row=0, column=3, sticky="nsew", padx=root.margin, pady=(10,0))


        self.mortage_with_lloyd_label_right = tk.Label(self.container_2_right, text="If yes, is it with Lloyds Bank?", anchor="w", justify="right")
        self.mortage_with_lloyd_label_right["bg"] = self.mortage_with_lloyd_label_right.master["bg"]
        self.mortage_with_lloyd_label_right.grid(row=1, column=0, columnspan=1, sticky="nsew", padx=root.margin, pady=(10,0))

        self.mortage_with_lloyd_value_right = tk.IntVar()
        self.mortage_with_lloyd_true_right = tk.Radiobutton(self.container_2_right, variable=self.mortage_with_lloyd_value_right, value="yes", text="Yes")
        self.mortage_with_lloyd_true_right["bg"] = self.mortage_with_lloyd_true_right.master["bg"]
        self.mortage_with_lloyd_true_right["activebackground"] = self.mortage_with_lloyd_true_right.master["bg"]
        self.mortage_with_lloyd_false_right = tk.Radiobutton(self.container_2_right, variable=self.mortage_with_lloyd_value_right, value="no", text="No")
        self.mortage_with_lloyd_false_right["bg"] = self.mortage_with_lloyd_false_right.master["bg"]
        self.mortage_with_lloyd_false_right["activebackground"] = self.mortage_with_lloyd_false_right.master["bg"]
        self.mortage_with_lloyd_true_right.grid(row=1, column=2, sticky="nsew", padx=root.margin, pady=(10,0))
        self.mortage_with_lloyd_false_right.grid(row=1, column=3, sticky="nsew", padx=root.margin, pady=(10,0))


        self.balance_mortage_label_right = tk.Label(self.container_2_right, text="What is the outstanding balance\non your mortage?", anchor="e", justify="right")
        self.balance_mortage_label_right["bg"] = self.balance_mortage_label_right.master["bg"]
        self.balance_mortage_label_right.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.balance_mortage_entry_right = tk.Entry(self.container_2_right)
        self.balance_mortage_entry_right.grid(row=2, column=2, sticky="we", columnspan=2, padx=root.margin, pady=(10,0))


        self.value_house_label_right = tk.Label(self.container_2_right, text="What is the value\non your house?", anchor="e", justify="right")
        self.value_house_label_right["bg"] = self.value_house_label_right.master["bg"]
        self.value_house_label_right.grid(row=3, column=0, columnspan=2, sticky="nsew", padx=root.margin, pady=(10,0))

        self.value_house_entry_right = tk.Entry(self.container_2_right)
        self.value_house_entry_right.grid(row=3, column=2, sticky="we", columnspan=2, padx=root.margin, pady=(10,0))