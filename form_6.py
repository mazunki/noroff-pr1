import tkinter as tk

class Form_6(tk.Frame):
    def __init__(self, root):
        super().__init__(root, height=root.height, background="#ebf4f2")
        root.master.update_idletasks()

    def add_buttons(self, root):
        self.next = tk.Button(self, text="Next page", width=35, height=3, command=self.master.layers[7].tkraise)
        self.next.place(relx=1, rely=1, anchor="se")

        self.prev = tk.Button(self, text="Back", width=35, height=3, command=self.master.layers[5].tkraise)
        self.prev.place(relx=0, rely=1, anchor="sw")

    def add_form(self, root):
        import focus_handler as focus

        self.text_label = tk.Label(self, text="Personal data")
        self.text_label.place(relx=0.5, rely=0, anchor="n")

        self.title_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_container.grid(row=0, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_number = tk.Label(self.title_container, background="#006e51", text="5", fg="white", font="-weight bold")
        self.title = tk.Label(self.title_container, background="#499a86", text="Additional personal and employment details", anchor="w", fg="white", font="-weight bold")
        self.title_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)
        

        self.container_left = tk.Frame(self, background="#ebf4f2")
        self.container_right = tk.Frame(self, background="#d9eae5")
        #self.container_left.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_rowconfigure(1, weight=1)
        self.container_left.grid(row=1, column=0, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_right.grid(row=1, column=1, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_left.grid_columnconfigure(0, weight=1)
        self.container_right.grid_columnconfigure(0, weight=1)

        def gray_out(*whats):
            for what in whats:
                    what["state"] = "disabled"
        def ungray(*whats):
            for what in whats:
                what["state"] = "normal"  


        # Left

        self.customer_label_left = tk.Label(self.container_left, text="First customer", font=("Courier", 12, "bold"), anchor="w")
        self.customer_label_left.grid(row=0, column=0, padx=root.margin, pady=(10,0), columnspan=5, sticky="nsew")
        self.customer_label_left["bg"] = self.customer_label_left.master["bg"]

        self.please_fill_all = tk.Label(self.container_left, text="Please complete all sections of this form", anchor="w")
        self.please_fill_all.grid(row=1, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.please_fill_all["bg"] = self.please_fill_all.master["bg"]

        self.working_status_label_left = tk.Label(self.container_left, text="Are you working?", anchor="w")
        self.working_status_label_left.grid(row=2, column=0, sticky="nsew", padx=root.margin)
        self.working_status_label_left["bg"] = self.working_status_label_left.master["bg"]

        self.working_status_value_left = tk.IntVar()
        self.working_status_yes_left = tk.Radiobutton(self.container_left, text="Yes", variable=self.working_status_value_left, value="yes")
        self.working_status_no_left = tk.Radiobutton(self.container_left, text="No", variable=self.working_status_value_left, value="no")
        self.working_status_yes_left.grid(row=2, column=1, padx=root.margin)
        self.working_status_no_left.grid(row=2, column=2, padx=root.margin)
        self.working_status_yes_left["bg"] = self.working_status_yes_left.master["bg"]
        self.working_status_no_left["bg"] = self.working_status_no_left.master["bg"]
        self.working_status_yes_left["activebackground"] = self.working_status_yes_left.master["bg"]
        self.working_status_no_left["activebackground"] = self.working_status_no_left.master["bg"]

        self.occupation_label_left = tk.Label(self.container_left, text="Your occupation", anchor="w")
        self.occupation_label_left.grid(row=3, column=0, sticky="nsew", padx=root.margin)
        self.occupation_label_left["bg"] = self.occupation_label_left.master["bg"]

        self.occupation_left = tk.StringVar()
        self.occupation_field_left = tk.Entry(self.container_left, textvariable=self.occupation_left)
        self.occupation_field_left.grid(row=4, column=0, sticky="nsew", columnspan=3, padx=root.margin)


        self.employer_name_label_left = tk.Label(self.container_left, text="Your employer\'s name", anchor="w")
        self.employer_name_label_left.grid(row=5, column=0, sticky="nsew", padx=root.margin)
        self.employer_name_label_left["bg"] = self.occupation_label_left.master["bg"]

        self.employer_name_left = tk.StringVar()
        self.employer_name_field_left = tk.Entry(self.container_left, textvariable=self.employer_name_left)
        self.employer_name_field_left.grid(row=6, column=0, sticky="nsew", columnspan=3, padx=root.margin)


        self.employer_address_label_left = tk.Label(self.container_left, text="Your employer\'s address", anchor="w")
        self.employer_address_label_left.grid(row=7, column=0, sticky="nsew", padx=root.margin)
        self.employer_address_label_left["bg"] = self.occupation_label_left.master["bg"]

        self.employer_address_1_left = tk.StringVar()
        self.employer_address_field_1_left = tk.Entry(self.container_left, textvariable=self.employer_address_1_left)
        self.employer_address_field_1_left.grid(row=8, column=0, sticky="nsew", columnspan=3, padx=root.margin, pady=(0,10))

        self.employer_address_2_left = tk.StringVar()
        self.employer_address_field_2_left = tk.Entry(self.container_left, textvariable=self.employer_address_2_left)
        self.employer_address_field_2_left.grid(row=9, column=0, sticky="nsew", columnspan=3, padx=root.margin, pady=(0,10))

        self.employer_address_3_left = tk.StringVar()
        self.employer_address_field_3_left = tk.Entry(self.container_left, textvariable=self.employer_address_3_left)
        self.employer_address_field_3_left.grid(row=10, column=0, sticky="nsew", columnspan=1, padx=root.margin, pady=(0,10))

        self.employer_postcode_left = tk.StringVar()
        self.employer_postcode_field_left = tk.Entry(self.container_left, textvariable=self.employer_postcode_left)
        self.employer_postcode_field_left.grid(row=10, column=1, sticky="nsew", columnspan=2, padx=root.margin, pady=(0,10))


        self.current_working_time_label_left = tk.Label(self.container_left, text="How long have you worked for you current employer?", anchor="e")
        self.current_working_time_label_left.grid(row=11, column=0, sticky="ew", columnspan=1, pady=(0,10))
        self.current_working_time_label_left["bg"] = self.current_working_time_label_left.master["bg"]

        self.current_working_time_left = tk.StringVar()
        self.current_working_time_field_left = tk.Entry(self.container_left, textvariable=self.current_working_time_left)
        self.current_working_time_field_left.grid(row=11, column=2, sticky="ew", padx=root.margin, pady=(0,10))


        self.previous_working_time_label_left = tk.Label(self.container_left, text="How long did you work for you previous employer?", anchor="e")
        self.previous_working_time_label_left.grid(row=12, column=0, sticky="ew", columnspan=1, pady=(0,10))
        self.previous_working_time_label_left["bg"] = self.previous_working_time_label_left.master["bg"]

        self.previous_working_time_left = tk.StringVar()
        self.previous_working_time_field_left = tk.Entry(self.container_left, textvariable=self.previous_working_time_left)
        self.previous_working_time_field_left.grid(row=12, column=2, sticky="ew", padx=root.margin, pady=(0,10))


        self.pensionable_label_left = tk.Label(self.container_left, text="Is your employment pensionable?", anchor="e")
        self.pensionable_label_left.grid(row=13, column=0, sticky="ew", columnspan=1, pady=(0,10))
        self.pensionable_label_left["bg"] = self.previous_working_time_label_left.master["bg"]

        self.pensionable_value_left = tk.IntVar()
        self.pensionable_yes_left = tk.Radiobutton(self.container_left, variable=self.pensionable_value_left, value="yes", text="Yes")
        self.pensionable_no_left = tk.Radiobutton(self.container_left, variable=self.pensionable_value_left, value="no", text="No")
        self.pensionable_yes_left.grid(row=13, column=1, sticky="ew", pady=(0,10))
        self.pensionable_no_left.grid(row=13, column=2, sticky="ew", pady=(0,10))
        self.pensionable_yes_left["bg"] = self.pensionable_yes_left.master["bg"]
        self.pensionable_no_left["bg"] = self.pensionable_no_left.master["bg"]



       # Right

        self.customer_label_right = tk.Label(self.container_right, text="First customer", font=("Courier", 12, "bold"), anchor="w")
        self.customer_label_right.grid(row=0, column=0, padx=root.margin, pady=(10,0), columnspan=5, sticky="nsew")
        self.customer_label_right["bg"] = self.customer_label_right.master["bg"]

        self.please_fill_all = tk.Label(self.container_right, text="Please complete all sections of this form", anchor="w")
        self.please_fill_all.grid(row=1, column=0, padx=root.margin, pady=(10,0), sticky="nsew")
        self.please_fill_all["bg"] = self.please_fill_all.master["bg"]

        self.working_status_label_right = tk.Label(self.container_right, text="Are you working?", anchor="w")
        self.working_status_label_right.grid(row=2, column=0, sticky="nsew", padx=root.margin)
        self.working_status_label_right["bg"] = self.working_status_label_right.master["bg"]

        self.working_status_value_right = tk.IntVar()
        self.working_status_yes_right = tk.Radiobutton(self.container_right, text="Yes", variable=self.working_status_value_right, value="yes")
        self.working_status_no_right = tk.Radiobutton(self.container_right, text="No", variable=self.working_status_value_right, value="no")
        self.working_status_yes_right.grid(row=2, column=1, padx=root.margin)
        self.working_status_no_right.grid(row=2, column=2, padx=root.margin)
        self.working_status_yes_right["bg"] = self.working_status_yes_right.master["bg"]
        self.working_status_no_right["bg"] = self.working_status_no_right.master["bg"]
        self.working_status_yes_right["activebackground"] = self.working_status_yes_right.master["bg"]
        self.working_status_no_right["activebackground"] = self.working_status_no_right.master["bg"]

        self.occupation_label_right = tk.Label(self.container_right, text="Your occupation", anchor="w")
        self.occupation_label_right.grid(row=3, column=0, sticky="nsew", padx=root.margin)
        self.occupation_label_right["bg"] = self.occupation_label_right.master["bg"]

        self.occupation_right = tk.StringVar()
        self.occupation_field_right = tk.Entry(self.container_right, textvariable=self.occupation_right)
        self.occupation_field_right.grid(row=4, column=0, sticky="nsew", columnspan=3, padx=root.margin)


        self.employer_name_label_right = tk.Label(self.container_right, text="Your employer\'s name", anchor="w")
        self.employer_name_label_right.grid(row=5, column=0, sticky="nsew", padx=root.margin)
        self.employer_name_label_right["bg"] = self.occupation_label_right.master["bg"]

        self.employer_name_right = tk.StringVar()
        self.employer_name_field_right = tk.Entry(self.container_right, textvariable=self.employer_name_right)
        self.employer_name_field_right.grid(row=6, column=0, sticky="nsew", columnspan=3, padx=root.margin)


        self.employer_address_label_right = tk.Label(self.container_right, text="Your employer\'s address", anchor="w")
        self.employer_address_label_right.grid(row=7, column=0, sticky="nsew", padx=root.margin)
        self.employer_address_label_right["bg"] = self.occupation_label_right.master["bg"]

        self.employer_address_1_right = tk.StringVar()
        self.employer_address_field_1_right = tk.Entry(self.container_right, textvariable=self.employer_address_1_right)
        self.employer_address_field_1_right.grid(row=8, column=0, sticky="nsew", columnspan=3, padx=root.margin, pady=(0,10))

        self.employer_address_2_right = tk.StringVar()
        self.employer_address_field_2_right = tk.Entry(self.container_right, textvariable=self.employer_address_2_right)
        self.employer_address_field_2_right.grid(row=9, column=0, sticky="nsew", columnspan=3, padx=root.margin, pady=(0,10))

        self.employer_address_3_right = tk.StringVar()
        self.employer_address_field_3_right = tk.Entry(self.container_right, textvariable=self.employer_address_3_right)
        self.employer_address_field_3_right.grid(row=10, column=0, sticky="nsew", columnspan=1, padx=root.margin, pady=(0,10))

        self.employer_postcode_right = tk.StringVar()
        self.employer_postcode_field_right = tk.Entry(self.container_right, textvariable=self.employer_postcode_right)
        self.employer_postcode_field_right.grid(row=10, column=1, sticky="nsew", columnspan=2, padx=root.margin, pady=(0,10))


        self.current_working_time_label_right = tk.Label(self.container_right, text="How long have you worked for you current employer?", anchor="e")
        self.current_working_time_label_right.grid(row=11, column=0, sticky="ew", columnspan=1, pady=(0,10))
        self.current_working_time_label_right["bg"] = self.current_working_time_label_right.master["bg"]

        self.current_working_time_right = tk.StringVar()
        self.current_working_time_field_right = tk.Entry(self.container_right, textvariable=self.current_working_time_right)
        self.current_working_time_field_right.grid(row=11, column=2, sticky="ew", padx=root.margin, pady=(0,10))


        self.previous_working_time_label_right = tk.Label(self.container_right, text="How long did you work for you previous employer?", anchor="e")
        self.previous_working_time_label_right.grid(row=12, column=0, sticky="ew", columnspan=1, pady=(0,10))
        self.previous_working_time_label_right["bg"] = self.previous_working_time_label_right.master["bg"]

        self.previous_working_time_right = tk.StringVar()
        self.previous_working_time_field_right = tk.Entry(self.container_right, textvariable=self.previous_working_time_right)
        self.previous_working_time_field_right.grid(row=12, column=2, sticky="ew", padx=root.margin, pady=(0,10))


        self.pensionable_label_right = tk.Label(self.container_right, text="Is your employment pensionable?", anchor="e")
        self.pensionable_label_right.grid(row=13, column=0, sticky="ew", columnspan=1, pady=(0,10))
        self.pensionable_label_right["bg"] = self.previous_working_time_label_right.master["bg"]

        self.pensionable_value_right = tk.IntVar()
        self.pensionable_yes_right = tk.Radiobutton(self.container_right, variable=self.pensionable_value_right, value="yes", text="Yes")
        self.pensionable_no_right = tk.Radiobutton(self.container_right, variable=self.pensionable_value_right, value="no", text="No")
        self.pensionable_yes_right.grid(row=13, column=1, sticky="ew", pady=(0,10))
        self.pensionable_no_right.grid(row=13, column=2, sticky="ew", pady=(0,10))
        self.pensionable_yes_right["bg"] = self.pensionable_yes_right.master["bg"]
        self.pensionable_no_right["bg"] = self.pensionable_no_right.master["bg"]