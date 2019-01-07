import tkinter as tk

class Form_7(tk.Frame):
    def __init__(self, root):
        super().__init__(root, height=root.height, background="#ebf4f2")
        root.master.update_idletasks()

    def add_buttons(self, root):
        self.next = tk.Button(self, text="Next page", width=35, height=3, command=self.master.layers[8].tkraise)
        self.next.place(relx=1, rely=1, anchor="se")

        self.prev = tk.Button(self, text="Back", width=35, height=3, command=self.master.layers[6].tkraise)
        self.prev.place(relx=0, rely=1, anchor="sw")

    def add_form(self, root):
        import focus_handler as focus

        self.text_label = tk.Label(self, text="Personal data")
        self.text_label.place(relx=0.5, rely=0, anchor="n")

        self.title_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_container.grid(row=0, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_number = tk.Label(self.title_container, background="#006e51", text="6", fg="white", font="-weight bold")
        self.title = tk.Label(self.title_container, background="#499a86", text="Your monthly household income and expenditure details", anchor="w", fg="white", font="-weight bold")
        self.title_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)
        

        self.container_1_left = tk.Frame(self, background="#ebf4f2")
        self.container_1_right = tk.Frame(self, background="#ebf4f2")
        #self.container_1_left.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_rowconfigure(1, weight=1)
        self.container_1_left.grid(row=1, column=0, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_1_right.grid(row=1, column=1, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_1_left.grid_columnconfigure(2, weight=1)


        self.container_2_left = tk.Frame(self, background="#d9eae5")
        self.container_2_right = tk.Frame(self, background="#d9eae5")
        #self.container_2_left.grid_propagate(False)
        self.container_2_left.grid(row=3, column=0, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_2_right.grid(row=3, column=1, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_2_left.grid_columnconfigure(2, weight=1)

        def gray_out(*whats):
            for what in whats:
                    what["state"] = "disabled"
        def ungray(*whats):
            for what in whats:
                what["state"] = "normal"  

        # Top Side
        self.customer_label_top = tk.Label(self.container_1_left, text="First customer's income", font=("Courier", 12, "bold"), justify="left")
        self.customer_label_top.grid(row=0, column=0, padx=root.margin, pady=(10,0), columnspan=5, sticky="nsew")
        self.customer_label_top["bg"] = self.customer_label_top.master["bg"]

        self.source_label_top = tk.Label(self.container_1_left, text="Source:")
        self.source_label_top.grid(row=1, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.source_label_top["bg"] = self.source_label_top.master["bg"]

        self.conditions_label_top = tk.Label(self.container_1_left, text="If yes")
        self.conditions_label_top.grid(row=1, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.conditions_label_top["bg"] = self.conditions_label_top.master["bg"]

        self.frequency_label_top = tk.Label(self.container_1_left, text="Frequency e.g. weekly")
        self.frequency_label_top.grid(row=1, column=2, padx=root.margin, pady=(10,0), sticky="nsew")
        self.frequency_label_top["bg"] = self.conditions_label_top.master["bg"]


        self.salary_label_top = tk.Label(self.container_1_left, text="Salary/wages")
        self.salary_label_top.grid(row=2, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.salary_label_top["bg"] = self.salary_label_top.master["bg"]

        self.salary_checkbox_value_top = tk.IntVar()
        self.salary_checkbox_top = tk.Checkbutton(self.container_1_left, variable=self.salary_checkbox_value_top)
        self.salary_checkbox_top.grid(row=2, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.salary_checkbox_top["bg"] = self.salary_checkbox_top.master["bg"]
        self.salary_checkbox_top["activebackground"] = self.salary_checkbox_top.master["bg"]

        self.salary_top = tk.StringVar()
        self.salary_entry_field_top = tk.Entry(self.container_1_left, textvariable=self.salary_top)
        self.salary_entry_field_top.grid(row=2, column=2, padx=root.margin, pady=(10,0), sticky="nsew")



        self.benefits_label_top = tk.Label(self.container_1_left, text="Benefits")
        self.benefits_label_top.grid(row=3, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.benefits_label_top["bg"] = self.benefits_label_top.master["bg"]

        self.benefits_checkbox_value_top = tk.IntVar()
        self.benefits_checkbox_top = tk.Checkbutton(self.container_1_left, variable=self.benefits_checkbox_value_top)
        self.benefits_checkbox_top.grid(row=3, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.benefits_checkbox_top["bg"] = self.benefits_checkbox_top.master["bg"]
        self.benefits_checkbox_top["activebackground"] = self.benefits_checkbox_top.master["bg"]

        self.benefits_top = tk.StringVar()
        self.benefits_entry_top = tk.Entry(self.container_1_left, textvariable=self.benefits_top)
        self.benefits_entry_top.grid(row=3, column=2, padx=root.margin, pady=(10,0), sticky="nsew")



        self.pension_label_top = tk.Label(self.container_1_left, text="Pension")
        self.pension_label_top.grid(row=4, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.pension_label_top["bg"] = self.salary_label_top.master["bg"]

        self.pension_checkbox_value_top = tk.IntVar()
        self.pension_checkbox_top = tk.Checkbutton(self.container_1_left, variable=self.pension_checkbox_value_top)
        self.pension_checkbox_top.grid(row=4, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.pension_checkbox_top["bg"] = self.pension_checkbox_top.master["bg"]
        self.pension_checkbox_top["activebackground"] = self.pension_checkbox_top.master["bg"]

        self.pension_top = tk.StringVar()
        self.pension_entry_top = tk.Entry(self.container_1_left, textvariable=self.pension_top)
        self.pension_entry_top.grid(row=4, column=2, padx=root.margin, pady=(10,0), sticky="nsew")



        self.investments_label_top = tk.Label(self.container_1_left, text="Investments")
        self.investments_label_top.grid(row=5, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.investments_label_top["bg"] = self.salary_label_top.master["bg"]

        self.investments_checkbox_value_top = tk.IntVar()
        self.investments_checkbox_top = tk.Checkbutton(self.container_1_left, variable=self.investments_checkbox_value_top)
        self.investments_checkbox_top.grid(row=5, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.investments_checkbox_top["bg"] = self.investments_checkbox_top.master["bg"]
        self.investments_checkbox_top["activebackground"] = self.investments_checkbox_top.master["bg"]

        self.investments_top = tk.StringVar()
        self.investments_entry_top = tk.Entry(self.container_1_left, textvariable=self.investments_top)
        self.investments_entry_top.grid(row=5, column=2, padx=root.margin, pady=(10,0), sticky="nsew")


        self.other_label_top = tk.Label(self.container_1_left, text="Other")
        self.other_label_top.grid(row=6, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.other_label_top["bg"] = self.salary_label_top.master["bg"]

        self.other_checkbox_value_top = tk.IntVar()
        self.other_checkbox_top = tk.Checkbutton(self.container_1_left, variable=self.other_checkbox_value_top)
        self.other_checkbox_top.grid(row=6, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.other_checkbox_top["bg"] = self.other_checkbox_top.master["bg"]
        self.other_checkbox_top["activebackground"] = self.other_checkbox_top.master["bg"]

        self.other_top = tk.StringVar()
        self.other_entry_top = tk.Entry(self.container_1_left, textvariable=self.other_top)
        self.other_entry_top.grid(row=6, column=2, padx=root.margin, pady=(10,0), sticky="nsew")



        self.other_explain_label_top = tk.Label(self.container_1_left, text="If other, explain")
        self.other_explain_label_top.grid(row=7, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.other_explain_label_top["bg"] = self.salary_label_top.master["bg"]

        self.other_explain_top = tk.StringVar()
        self.other_explain_entry_top = tk.Entry(self.container_1_left, textvariable=self.other_explain_top)
        self.other_explain_entry_top.grid(row=7, column=1, padx=root.margin, pady=(10,0), sticky="nsew", columnspan=2)


        self.total_net_label_top = tk.Label(self.container_1_left, text="Total net monthly income")
        self.total_net_label_top.grid(row=8, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.total_net_label_top["bg"] = self.total_net_label_top.master["bg"]

        self.total_net_top = tk.StringVar()
        self.total_net_entry_top = tk.Entry(self.container_1_left, textvariable=self.total_net_top)
        self.total_net_entry_top.grid(row=8, column=1, padx=root.margin, pady=(10,0), sticky="nsew", columnspan=2)


        # Right side

        self.container_1_right.grid_columnconfigure(0, weight=1)
        self.container_1_right.grid_columnconfigure(1, weight=1)
        self.container_1_right.grid_columnconfigure(2, weight=1)
        self.container_1_right.grid_columnconfigure(3, weight=1)

        self.direct_to_a_bank_label_top = tk.Label(self.container_1_right, text="Direct to\na bank")
        self.direct_to_a_bank_label_top.grid(row=0, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.direct_to_a_bank_label_top["bg"] = self.direct_to_a_bank_label_top.master["bg"]

        self.cheque_label_top = tk.Label(self.container_1_right, text="Cheque")
        self.cheque_label_top.grid(row=0, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.cheque_label_top["bg"] = self.cheque_label_top.master["bg"]

        self.cash_label_top = tk.Label(self.container_1_right, text="Cash")
        self.cash_label_top.grid(row=0, column=2, padx=root.margin, pady=(10,0), sticky="s", rowspan=2)
        self.cash_label_top["bg"] = self.cash_label_top.master["bg"]

        self.into_this_account_label_top = tk.Label(self.container_1_right, text="Into this\naccount")
        self.into_this_account_label_top.grid(row=0, column=3, padx=root.margin, pady=(10,0), sticky="nsew")
        self.into_this_account_label_top["bg"] = self.into_this_account_label_top.master["bg"]

        self.salary_type_top = tk.IntVar()
        self.type_salary_direct_bank_top = tk.Radiobutton(self.container_1_right, variable=self.salary_type_top, value="direct_to_bank")
        self.type_salary_cheque_top = tk.Radiobutton(self.container_1_right, variable=self.salary_type_top, value="cheque")
        self.type_salary_cash_top = tk.Radiobutton(self.container_1_right, variable=self.salary_type_top, value="cash")
        self.type_salary_into_account_top = tk.Radiobutton(self.container_1_right, variable=self.salary_type_top, value="into_account")
        self.type_salary_direct_bank_top.grid(row=2, column=0, sticky="nsew", pady=(25,2))
        self.type_salary_cheque_top.grid(row=2, column=1, sticky="nsew", pady=(25,2))
        self.type_salary_cash_top.grid(row=2, column=2, sticky="nsew", pady=(25,2))
        self.type_salary_into_account_top.grid(row=2, column=3, sticky="nsew", pady=(25,2))
        self.type_salary_direct_bank_top["bg"] = self.type_salary_direct_bank_top.master["bg"]
        self.type_salary_cheque_top["bg"] = self.type_salary_cheque_top.master["bg"]
        self.type_salary_cash_top["bg"] = self.type_salary_cash_top.master["bg"]
        self.type_salary_into_account_top["bg"] = self.type_salary_into_account_top.master["bg"]
        self.type_salary_direct_bank_top["activebackground"] = self.type_salary_direct_bank_top.master["bg"]
        self.type_salary_cheque_top["activebackground"] = self.type_salary_cheque_top.master["bg"]
        self.type_salary_cash_top["activebackground"] = self.type_salary_cash_top.master["bg"]
        self.type_salary_into_account_top["activebackground"] = self.type_salary_into_account_top.master["bg"]


        self.benefits_type_top = tk.IntVar()
        self.type_benefits_direct_bank_top = tk.Radiobutton(self.container_1_right, variable=self.benefits_type_top, value="direct_to_bank")
        self.type_benefits_cheque_top = tk.Radiobutton(self.container_1_right, variable=self.benefits_type_top, value="cheque")
        self.type_benefits_cash_top = tk.Radiobutton(self.container_1_right, variable=self.benefits_type_top, value="cash")
        self.type_benefits_into_account_top = tk.Radiobutton(self.container_1_right, variable=self.benefits_type_top, value="into_account")
        self.type_benefits_direct_bank_top.grid(row=3, column=0, sticky="nsew", pady=(10,2))
        self.type_benefits_cheque_top.grid(row=3, column=1, sticky="nsew", pady=(10,2))
        self.type_benefits_cash_top.grid(row=3, column=2, sticky="nsew", pady=(10,2))
        self.type_benefits_into_account_top.grid(row=3, column=3, sticky="nsew", pady=(10,2))
        self.type_benefits_direct_bank_top["bg"] = self.type_benefits_direct_bank_top.master["bg"]
        self.type_benefits_cheque_top["bg"] = self.type_benefits_cheque_top.master["bg"]
        self.type_benefits_cash_top["bg"] = self.type_benefits_cash_top.master["bg"]
        self.type_benefits_into_account_top["bg"] = self.type_benefits_into_account_top.master["bg"]
        self.type_benefits_direct_bank_top["activebackground"] = self.type_benefits_direct_bank_top.master["bg"]
        self.type_benefits_cheque_top["activebackground"] = self.type_benefits_cheque_top.master["bg"]
        self.type_benefits_cash_top["activebackground"] = self.type_benefits_cash_top.master["bg"]
        self.type_benefits_into_account_top["activebackground"] = self.type_benefits_into_account_top.master["bg"]


        self.pension_type_top = tk.IntVar()
        self.type_pension_direct_bank_top = tk.Radiobutton(self.container_1_right, variable=self.pension_type_top, value="direct_to_bank")
        self.type_pension_cheque_top = tk.Radiobutton(self.container_1_right, variable=self.pension_type_top, value="cheque")
        self.type_pension_cash_top = tk.Radiobutton(self.container_1_right, variable=self.pension_type_top, value="cash")
        self.type_pension_into_account_top = tk.Radiobutton(self.container_1_right, variable=self.pension_type_top, value="into_account")
        self.type_pension_direct_bank_top.grid(row=4, column=0, sticky="nsew", pady=(10,2))
        self.type_pension_cheque_top.grid(row=4, column=1, sticky="nsew", pady=(10,2))
        self.type_pension_cash_top.grid(row=4, column=2, sticky="nsew", pady=(10,2))
        self.type_pension_into_account_top.grid(row=4, column=3, sticky="nsew", pady=(10,2))
        self.type_pension_direct_bank_top["bg"] = self.type_pension_direct_bank_top.master["bg"]
        self.type_pension_cheque_top["bg"] = self.type_pension_cheque_top.master["bg"]
        self.type_pension_cash_top["bg"] = self.type_pension_cash_top.master["bg"]
        self.type_pension_into_account_top["bg"] = self.type_pension_into_account_top.master["bg"]
        self.type_pension_direct_bank_top["activebackground"] = self.type_pension_direct_bank_top.master["bg"]
        self.type_pension_cheque_top["activebackground"] = self.type_pension_cheque_top.master["bg"]
        self.type_pension_cash_top["activebackground"] = self.type_pension_cash_top.master["bg"]
        self.type_pension_into_account_top["activebackground"] = self.type_pension_into_account_top.master["bg"]


        self.investment_type_top = tk.IntVar()
        self.type_investment_direct_bank_top = tk.Radiobutton(self.container_1_right, variable=self.investment_type_top, value="direct_to_bank")
        self.type_investment_cheque_top = tk.Radiobutton(self.container_1_right, variable=self.investment_type_top, value="cheque")
        self.type_investment_cash_top = tk.Radiobutton(self.container_1_right, variable=self.investment_type_top, value="cash")
        self.type_investment_into_account_top = tk.Radiobutton(self.container_1_right, variable=self.investment_type_top, value="into_account")
        self.type_investment_direct_bank_top.grid(row=5, column=0, sticky="nsew", pady=(10,2))
        self.type_investment_cheque_top.grid(row=5, column=1, sticky="nsew", pady=(10,2))
        self.type_investment_cash_top.grid(row=5, column=2, sticky="nsew", pady=(10,2))
        self.type_investment_into_account_top.grid(row=5, column=3, sticky="nsew", pady=(10,2))
        self.type_investment_direct_bank_top["bg"] = self.type_pension_direct_bank_top.master["bg"]
        self.type_investment_cheque_top["bg"] = self.type_pension_cheque_top.master["bg"]
        self.type_investment_cash_top["bg"] = self.type_pension_cash_top.master["bg"]
        self.type_investment_into_account_top["bg"] = self.type_pension_into_account_top.master["bg"]
        self.type_investment_direct_bank_top["activebackground"] = self.type_investment_direct_bank_top.master["bg"]
        self.type_investment_cheque_top["activebackground"] = self.type_investment_cheque_top.master["bg"]
        self.type_investment_cash_top["activebackground"] = self.type_investment_cash_top.master["bg"]
        self.type_investment_into_account_top["activebackground"] = self.type_investment_into_account_top.master["bg"]


        self.other_type_top = tk.IntVar()
        self.type_other_direct_bank_top = tk.Radiobutton(self.container_1_right, variable=self.other_type_top, value="direct_to_bank")
        self.type_other_cheque_top = tk.Radiobutton(self.container_1_right, variable=self.other_type_top, value="cheque")
        self.type_other_cash_top = tk.Radiobutton(self.container_1_right, variable=self.other_type_top, value="cash")
        self.type_other_into_account_top = tk.Radiobutton(self.container_1_right, variable=self.other_type_top, value="into_account")
        self.type_other_direct_bank_top.grid(row=6, column=0, sticky="nsew", pady=(10,2))
        self.type_other_cheque_top.grid(row=6, column=1, sticky="nsew", pady=(10,2))
        self.type_other_cash_top.grid(row=6, column=2, sticky="nsew", pady=(10,2))
        self.type_other_into_account_top.grid(row=6, column=3, sticky="nsew", pady=(10,2))
        self.type_other_direct_bank_top["bg"] = self.type_other_direct_bank_top.master["bg"]
        self.type_other_cheque_top["bg"] = self.type_other_cheque_top.master["bg"]
        self.type_other_cash_top["bg"] = self.type_other_cash_top.master["bg"]
        self.type_other_into_account_top["bg"] = self.type_other_into_account_top.master["bg"]
        self.type_other_direct_bank_top["activebackground"] = self.type_other_direct_bank_top.master["bg"]
        self.type_other_cheque_top["activebackground"] = self.type_other_cheque_top.master["bg"]
        self.type_other_cash_top["activebackground"] = self.type_other_cash_top.master["bg"]
        self.type_other_into_account_top["activebackground"] = self.type_other_into_account_top.master["bg"]



        self.expected_month_label_top = tk.Label(self.container_1_right, text="Total expected through\n this account per month")
        self.expected_month_label_top.grid(row=7, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.expected_month_label_top["bg"] = self.expected_month_label_top.master["bg"]

        self.expected_month_top = tk.StringVar()
        self.expected_month_entry_top = tk.Entry(self.container_1_right, textvariable=self.expected_month_top)
        self.expected_month_entry_top.grid(row=7, column=1, padx=root.margin, pady=(10,0), sticky="nsew", columnspan=3)




        # Bottom
        # Left Side
        self.customer_label_bottom = tk.Label(self.container_2_left, text="Second customer's income", font=("Courier", 12, "bold"), justify="left")
        self.customer_label_bottom.grid(row=0, column=0, padx=root.margin, pady=(10,0), columnspan=5, sticky="nsew")
        self.customer_label_bottom["bg"] = self.customer_label_bottom.master["bg"]

        self.source_label_bottom = tk.Label(self.container_2_left, text="Source:")
        self.source_label_bottom.grid(row=1, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.source_label_bottom["bg"] = self.source_label_bottom.master["bg"]

        self.conditions_label_bottom = tk.Label(self.container_2_left, text="If yes")
        self.conditions_label_bottom.grid(row=1, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.conditions_label_bottom["bg"] = self.conditions_label_bottom.master["bg"]

        self.frequency_label_bottom = tk.Label(self.container_2_left, text="Frequency e.g. weekly")
        self.frequency_label_bottom.grid(row=1, column=2, padx=root.margin, pady=(10,0), sticky="nsew")
        self.frequency_label_bottom["bg"] = self.conditions_label_bottom.master["bg"]


        self.salary_label_bottom = tk.Label(self.container_2_left, text="Salary/wages")
        self.salary_label_bottom.grid(row=2, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.salary_label_bottom["bg"] = self.salary_label_bottom.master["bg"]

        self.salary_checkbox_value_bottom = tk.IntVar()
        self.salary_checkbox_bottom = tk.Checkbutton(self.container_2_left, variable=self.salary_checkbox_value_bottom)
        self.salary_checkbox_bottom.grid(row=2, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.salary_checkbox_bottom["bg"] = self.salary_checkbox_bottom.master["bg"]
        self.salary_checkbox_bottom["activebackground"] = self.salary_checkbox_bottom.master["bg"]

        self.salary_bottom = tk.StringVar()
        self.salary_entry_field_bottom = tk.Entry(self.container_2_left, textvariable=self.salary_bottom)
        self.salary_entry_field_bottom.grid(row=2, column=2, padx=root.margin, pady=(10,0), sticky="nsew")



        self.benefits_label_bottom = tk.Label(self.container_2_left, text="Benefits")
        self.benefits_label_bottom.grid(row=3, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.benefits_label_bottom["bg"] = self.benefits_label_bottom.master["bg"]

        self.benefits_checkbox_value_bottom = tk.IntVar()
        self.benefits_checkbox_bottom = tk.Checkbutton(self.container_2_left, variable=self.benefits_checkbox_value_bottom)
        self.benefits_checkbox_bottom.grid(row=3, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.benefits_checkbox_bottom["bg"] = self.benefits_checkbox_bottom.master["bg"]
        self.benefits_checkbox_bottom["activebackground"] = self.benefits_checkbox_bottom.master["bg"]

        self.benefits_bottom = tk.StringVar()
        self.benefits_entry_bottom = tk.Entry(self.container_2_left, textvariable=self.benefits_bottom)
        self.benefits_entry_bottom.grid(row=3, column=2, padx=root.margin, pady=(10,0), sticky="nsew")



        self.pension_label_bottom = tk.Label(self.container_2_left, text="Pension")
        self.pension_label_bottom.grid(row=4, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.pension_label_bottom["bg"] = self.salary_label_bottom.master["bg"]

        self.pension_checkbox_value_bottom = tk.IntVar()
        self.pension_checkbox_bottom = tk.Checkbutton(self.container_2_left, variable=self.pension_checkbox_value_bottom)
        self.pension_checkbox_bottom.grid(row=4, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.pension_checkbox_bottom["bg"] = self.pension_checkbox_bottom.master["bg"]
        self.pension_checkbox_bottom["activebackground"] = self.pension_checkbox_bottom.master["bg"]

        self.pension_bottom = tk.StringVar()
        self.pension_entry_bottom = tk.Entry(self.container_2_left, textvariable=self.pension_bottom)
        self.pension_entry_bottom.grid(row=4, column=2, padx=root.margin, pady=(10,0), sticky="nsew")



        self.investments_label_bottom = tk.Label(self.container_2_left, text="Investments")
        self.investments_label_bottom.grid(row=5, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.investments_label_bottom["bg"] = self.salary_label_bottom.master["bg"]

        self.investments_checkbox_value_bottom = tk.IntVar()
        self.investments_checkbox_bottom = tk.Checkbutton(self.container_2_left, variable=self.investments_checkbox_value_bottom)
        self.investments_checkbox_bottom.grid(row=5, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.investments_checkbox_bottom["bg"] = self.investments_checkbox_bottom.master["bg"]
        self.investments_checkbox_bottom["activebackground"] = self.investments_checkbox_bottom.master["bg"]

        self.investments_bottom = tk.StringVar()
        self.investments_entry_bottom = tk.Entry(self.container_2_left, textvariable=self.investments_bottom)
        self.investments_entry_bottom.grid(row=5, column=2, padx=root.margin, pady=(10,0), sticky="nsew")


        self.other_label_bottom = tk.Label(self.container_2_left, text="Other")
        self.other_label_bottom.grid(row=6, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.other_label_bottom["bg"] = self.salary_label_bottom.master["bg"]

        self.other_checkbox_value_bottom = tk.IntVar()
        self.other_checkbox_bottom = tk.Checkbutton(self.container_2_left, variable=self.other_checkbox_value_bottom)
        self.other_checkbox_bottom.grid(row=6, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.other_checkbox_bottom["bg"] = self.other_checkbox_bottom.master["bg"]
        self.other_checkbox_bottom["activebackground"] = self.other_checkbox_bottom.master["bg"]

        self.other_bottom = tk.StringVar()
        self.other_entry_bottom = tk.Entry(self.container_2_left, textvariable=self.other_bottom)
        self.other_entry_bottom.grid(row=6, column=2, padx=root.margin, pady=(10,0), sticky="nsew")



        self.other_explain_label_bottom = tk.Label(self.container_2_left, text="If other, explain")
        self.other_explain_label_bottom.grid(row=7, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.other_explain_label_bottom["bg"] = self.salary_label_bottom.master["bg"]

        self.other_explain_bottom = tk.StringVar()
        self.other_explain_entry_bottom = tk.Entry(self.container_2_left, textvariable=self.other_explain_bottom)
        self.other_explain_entry_bottom.grid(row=7, column=1, padx=root.margin, pady=(10,0), sticky="nsew", columnspan=2)


        self.total_net_label_bottom = tk.Label(self.container_2_left, text="Total net monthly income")
        self.total_net_label_bottom.grid(row=8, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.total_net_label_bottom["bg"] = self.total_net_label_bottom.master["bg"]

        self.total_net_bottom = tk.StringVar()
        self.total_net_entry_bottom = tk.Entry(self.container_2_left, textvariable=self.total_net_bottom)
        self.total_net_entry_bottom.grid(row=8, column=1, padx=root.margin, pady=(10,0), sticky="nsew", columnspan=2)


        # Right side

        self.container_2_right.grid_columnconfigure(0, weight=1)
        self.container_2_right.grid_columnconfigure(1, weight=1)
        self.container_2_right.grid_columnconfigure(2, weight=1)
        self.container_2_right.grid_columnconfigure(3, weight=1)

        self.direct_to_a_bank_label_bottom = tk.Label(self.container_2_right, text="Direct to\na bank")
        self.direct_to_a_bank_label_bottom.grid(row=0, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.direct_to_a_bank_label_bottom["bg"] = self.direct_to_a_bank_label_bottom.master["bg"]

        self.cheque_label_bottom = tk.Label(self.container_2_right, text="Cheque")
        self.cheque_label_bottom.grid(row=0, column=1, padx=root.margin, pady=(10,0), sticky="nsew")
        self.cheque_label_bottom["bg"] = self.cheque_label_bottom.master["bg"]

        self.cash_label_bottom = tk.Label(self.container_2_right, text="Cash")
        self.cash_label_bottom.grid(row=0, column=2, padx=root.margin, pady=(10,0), sticky="s", rowspan=2)
        self.cash_label_bottom["bg"] = self.cash_label_bottom.master["bg"]

        self.into_this_account_label_bottom = tk.Label(self.container_2_right, text="Into this\naccount")
        self.into_this_account_label_bottom.grid(row=0, column=3, padx=root.margin, pady=(10,0), sticky="nsew")
        self.into_this_account_label_bottom["bg"] = self.into_this_account_label_bottom.master["bg"]

        self.salary_type_bottom = tk.IntVar()
        self.type_salary_direct_bank_bottom = tk.Radiobutton(self.container_2_right, variable=self.salary_type_bottom, value="direct_to_bank")
        self.type_salary_cheque_bottom = tk.Radiobutton(self.container_2_right, variable=self.salary_type_bottom, value="cheque")
        self.type_salary_cash_bottom = tk.Radiobutton(self.container_2_right, textvariable=self.salary_type_bottom, value="cash")
        self.type_salary_into_account_bottom = tk.Radiobutton(self.container_2_right, variable=self.salary_type_bottom, value="into_account")
        self.type_salary_direct_bank_bottom.grid(row=2, column=0, sticky="nsew", pady=(25,2))
        self.type_salary_cheque_bottom.grid(row=2, column=1, sticky="nsew", pady=(25,2))
        self.type_salary_cash_bottom.grid(row=2, column=2, sticky="nsew", pady=(25,2))
        self.type_salary_into_account_bottom.grid(row=2, column=3, sticky="nsew", pady=(25,2))
        self.type_salary_direct_bank_bottom["bg"] = self.type_salary_direct_bank_bottom.master["bg"]
        self.type_salary_cheque_bottom["bg"] = self.type_salary_cheque_bottom.master["bg"]
        self.type_salary_cash_bottom["bg"] = self.type_salary_cash_bottom.master["bg"]
        self.type_salary_into_account_bottom["bg"] = self.type_salary_into_account_bottom.master["bg"]
        self.type_salary_direct_bank_bottom["activebackground"] = self.type_salary_direct_bank_bottom.master["bg"]
        self.type_salary_cheque_bottom["activebackground"] = self.type_salary_cheque_bottom.master["bg"]
        self.type_salary_cash_bottom["activebackground"] = self.type_salary_cash_bottom.master["bg"]
        self.type_salary_into_account_bottom["activebackground"] = self.type_salary_into_account_bottom.master["bg"]


        self.benefits_type_bottom = tk.IntVar()
        self.type_benefits_direct_bank_bottom = tk.Radiobutton(self.container_2_right, variable=self.benefits_type_bottom, value="direct_to_bank")
        self.type_benefits_cheque_bottom = tk.Radiobutton(self.container_2_right, variable=self.benefits_type_bottom, value="cheque")
        self.type_benefits_cash_bottom = tk.Radiobutton(self.container_2_right, variable=self.benefits_type_bottom, value="cash")
        self.type_benefits_into_account_bottom = tk.Radiobutton(self.container_2_right, variable=self.benefits_type_bottom, value="into_account")
        self.type_benefits_direct_bank_bottom.grid(row=3, column=0, sticky="nsew", pady=(10,2))
        self.type_benefits_cheque_bottom.grid(row=3, column=1, sticky="nsew", pady=(10,2))
        self.type_benefits_cash_bottom.grid(row=3, column=2, sticky="nsew", pady=(10,2))
        self.type_benefits_into_account_bottom.grid(row=3, column=3, sticky="nsew", pady=(10,2))
        self.type_benefits_direct_bank_bottom["bg"] = self.type_benefits_direct_bank_bottom.master["bg"]
        self.type_benefits_cheque_bottom["bg"] = self.type_benefits_cheque_bottom.master["bg"]
        self.type_benefits_cash_bottom["bg"] = self.type_benefits_cash_bottom.master["bg"]
        self.type_benefits_into_account_bottom["bg"] = self.type_benefits_into_account_bottom.master["bg"]
        self.type_benefits_direct_bank_bottom["activebackground"] = self.type_benefits_direct_bank_bottom.master["bg"]
        self.type_benefits_cheque_bottom["activebackground"] = self.type_benefits_cheque_bottom.master["bg"]
        self.type_benefits_cash_bottom["activebackground"] = self.type_benefits_cash_bottom.master["bg"]
        self.type_benefits_into_account_bottom["activebackground"] = self.type_benefits_into_account_bottom.master["bg"]


        self.pension_type_bottom = tk.IntVar()
        self.type_pension_direct_bank_bottom = tk.Radiobutton(self.container_2_right, variable=self.pension_type_bottom, value="direct_to_bank")
        self.type_pension_cheque_bottom = tk.Radiobutton(self.container_2_right, variable=self.pension_type_bottom, value="cheque")
        self.type_pension_cash_bottom = tk.Radiobutton(self.container_2_right, variable=self.pension_type_bottom, value="cash")
        self.type_pension_into_account_bottom = tk.Radiobutton(self.container_2_right, variable=self.pension_type_bottom, value="into_account")
        self.type_pension_direct_bank_bottom.grid(row=4, column=0, sticky="nsew", pady=(10,2))
        self.type_pension_cheque_bottom.grid(row=4, column=1, sticky="nsew", pady=(10,2))
        self.type_pension_cash_bottom.grid(row=4, column=2, sticky="nsew", pady=(10,2))
        self.type_pension_into_account_bottom.grid(row=4, column=3, sticky="nsew", pady=(10,2))
        self.type_pension_direct_bank_bottom["bg"] = self.type_pension_direct_bank_bottom.master["bg"]
        self.type_pension_cheque_bottom["bg"] = self.type_pension_cheque_bottom.master["bg"]
        self.type_pension_cash_bottom["bg"] = self.type_pension_cash_bottom.master["bg"]
        self.type_pension_into_account_bottom["bg"] = self.type_pension_into_account_bottom.master["bg"]
        self.type_pension_direct_bank_bottom["activebackground"] = self.type_pension_direct_bank_bottom.master["bg"]
        self.type_pension_cheque_bottom["activebackground"] = self.type_pension_cheque_bottom.master["bg"]
        self.type_pension_cash_bottom["activebackground"] = self.type_pension_cash_bottom.master["bg"]
        self.type_pension_into_account_bottom["activebackground"] = self.type_pension_into_account_bottom.master["bg"]


        self.investment_type_bottom = tk.IntVar()
        self.type_investment_direct_bank_bottom = tk.Radiobutton(self.container_2_right, variable=self.investment_type_bottom, value="direct_to_bank")
        self.type_investment_cheque_bottom = tk.Radiobutton(self.container_2_right, variable=self.investment_type_bottom, value="cheque")
        self.type_investment_cash_bottom = tk.Radiobutton(self.container_2_right, variable=self.investment_type_bottom, value="cash")
        self.type_investment_into_account_bottom = tk.Radiobutton(self.container_2_right, variable=self.investment_type_bottom, value="into_account")
        self.type_investment_direct_bank_bottom.grid(row=5, column=0, sticky="nsew", pady=(10,2))
        self.type_investment_cheque_bottom.grid(row=5, column=1, sticky="nsew", pady=(10,2))
        self.type_investment_cash_bottom.grid(row=5, column=2, sticky="nsew", pady=(10,2))
        self.type_investment_into_account_bottom.grid(row=5, column=3, sticky="nsew", pady=(10,2))
        self.type_investment_direct_bank_bottom["bg"] = self.type_pension_direct_bank_bottom.master["bg"]
        self.type_investment_cheque_bottom["bg"] = self.type_pension_cheque_bottom.master["bg"]
        self.type_investment_cash_bottom["bg"] = self.type_pension_cash_bottom.master["bg"]
        self.type_investment_into_account_bottom["bg"] = self.type_pension_into_account_bottom.master["bg"]
        self.type_investment_direct_bank_bottom["activebackground"] = self.type_investment_direct_bank_bottom.master["bg"]
        self.type_investment_cheque_bottom["activebackground"] = self.type_investment_cheque_bottom.master["bg"]
        self.type_investment_cash_bottom["activebackground"] = self.type_investment_cash_bottom.master["bg"]
        self.type_investment_into_account_bottom["activebackground"] = self.type_investment_into_account_bottom.master["bg"]


        self.other_type_bottom = tk.IntVar()
        self.type_other_direct_bank_bottom = tk.Radiobutton(self.container_2_right, variable=self.other_type_bottom, value="direct_to_bank")
        self.type_other_cheque_bottom = tk.Radiobutton(self.container_2_right, variable=self.other_type_bottom, value="cheque")
        self.type_other_cash_bottom = tk.Radiobutton(self.container_2_right, variable=self.other_type_bottom, value="cash")
        self.type_other_into_account_bottom = tk.Radiobutton(self.container_2_right, variable=self.other_type_bottom, value="into_account")
        self.type_other_direct_bank_bottom.grid(row=6, column=0, sticky="nsew", pady=(10,2))
        self.type_other_cheque_bottom.grid(row=6, column=1, sticky="nsew", pady=(10,2))
        self.type_other_cash_bottom.grid(row=6, column=2, sticky="nsew", pady=(10,2))
        self.type_other_into_account_bottom.grid(row=6, column=3, sticky="nsew", pady=(10,2))
        self.type_other_direct_bank_bottom["bg"] = self.type_other_direct_bank_bottom.master["bg"]
        self.type_other_cheque_bottom["bg"] = self.type_other_cheque_bottom.master["bg"]
        self.type_other_cash_bottom["bg"] = self.type_other_cash_bottom.master["bg"]
        self.type_other_into_account_bottom["bg"] = self.type_other_into_account_bottom.master["bg"]
        self.type_other_direct_bank_bottom["activebackground"] = self.type_other_direct_bank_bottom.master["bg"]
        self.type_other_cheque_bottom["activebackground"] = self.type_other_cheque_bottom.master["bg"]
        self.type_other_cash_bottom["activebackground"] = self.type_other_cash_bottom.master["bg"]
        self.type_other_into_account_bottom["activebackground"] = self.type_other_into_account_bottom.master["bg"]



        self.expected_month_label_bottom = tk.Label(self.container_2_right, text="Total expected through\n this account per month")
        self.expected_month_label_bottom.grid(row=7, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.expected_month_label_bottom["bg"] = self.expected_month_label_bottom.master["bg"]

        self.expected_month_bottom = tk.StringVar()
        self.expected_month_entry_bottom = tk.Entry(self.container_2_right, textvariable=self.expected_month_bottom)
        self.expected_month_entry_bottom.grid(row=7, column=1, padx=root.margin, pady=(10,0), sticky="nsew", columnspan=3)
