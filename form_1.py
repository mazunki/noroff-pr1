import tkinter as tk

class Form_1(tk.Frame):
    def __init__(self, root):
        super().__init__(root, background="yellow")
        root.master.update_idletasks()

    def add_buttons(self, root):
        self.next = tk.Button(self, text="Next page", width=35, height=3, command=self.master.layers[2].tkraise)
        self.next.place(relx=1, rely=1, anchor="se")

        self.prev = tk.Button(self, text="Back", width=35, height=3, command=self.master.layers[0].tkraise)
        self.prev.place(relx=0, rely=1, anchor="sw")
        pass


    def add_form(self, root):
        import focus_handler as focus

        self.text_label = tk.Label(self, text="Personal data")
        self.text_label.place(relx=0.5, rely=0, anchor="n")

        self.title_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_container.grid(row=0, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_number = tk.Label(self.title_container, background="#006e51", text="1", fg="white", font="-weight bold")
        self.title = tk.Label(self.title_container, background="#499a86", text="Your personal details", anchor="w", fg="white", font="-weight bold")
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

        def gray_out(*whats):
            for what in whats:
                    what["state"] = "disabled"
        def ungray(*whats):
            for what in whats:
                what["state"] = "normal"           
                


        # Left Side
        self.customer_label_left = tk.Label(self.container_left, text="First customer", font=("Courier", 12, "bold"), justify="left")
        self.customer_label_left.grid(row=0, column=0, padx=(10,0), pady=(10,0), columnspan=5)
        self.customer_label_left["bg"] = self.customer_label_left.master["bg"]

        self.existing_customer_label_left = tk.Label(self.container_left, text="Check if you're an existing\nLloyd Bank customer", font=("Courier", 8), justify="left")
        self.existing_customer_label_left.grid(row=1, column=0, padx=(10,0), pady=(10,0), columnspan=2)
        self.existing_customer_label_left["bg"] = self.existing_customer_label_left.master["bg"]

        self.existing_customer_left_value = tk.StringVar()
        #self.existing_customer_left_value.set("kartoffel")
        self.existing_customer_left = tk.Checkbutton(self.container_left, textvariable=self.existing_customer_left_value)
        self.existing_customer_left.grid(row=1, column=2, pady=(10,0))
        self.existing_customer_left["bg"] = self.existing_customer_left.master["bg"]

        print(type(self.existing_customer_left_value.get()))

        self.honorary_left = tk.IntVar()
        self.honorary_left.set("kartoffel")
        
        self.title_miss_left = tk.Radiobutton(self.container_left, text="Miss".ljust(5), font="TkFixedFont", variable=self.honorary_left, value="Miss", bg=self.container_left["bg"], command=lambda:gray_out(self.title_other_field_left), justify="left")
        self.title_miss_left.grid(row=2, column=0, padx=(10,0), pady=(10,0), sticky="we")
        self.title_mr_left = tk.Radiobutton(self.container_left, text="Mr.".ljust(5), font="TkFixedFont", variable=self.honorary_left, value="Mr", bg=self.container_left["bg"], command=lambda:gray_out(self.title_other_field_left), justify="left")
        self.title_mr_left.grid(row=2, column=1, padx=(10,0), pady=(10,0), sticky="we")
        self.title_mrs_left = tk.Radiobutton(self.container_left, text="Mrs.".ljust(5), font="TkFixedFont", variable=self.honorary_left, value="Mrs", bg=self.container_left["bg"], command=lambda:gray_out(self.title_other_field_left), justify="left")
        self.title_mrs_left.grid(row=2, column=2, padx=(10,0), pady=(10,0), sticky="we")
        self.title_ms_left = tk.Radiobutton(self.container_left, text="Ms.".ljust(5), font="TkFixedFont", variable=self.honorary_left, value="Ms", bg=self.container_left["bg"], command=lambda:gray_out(self.title_other_field_left), justify="left")
        self.title_ms_left.grid(row=3, column=0, padx=(10,0), pady=(10,0), sticky="we")
        self.title_other_left = tk.StringVar()
        self.title_other_field_left = tk.Entry(self.container_left, textvariable=self.title_other_left, fg="black", width=10, state="disabled")#, bg="#BBBBBB")
        self.title_other_field_left.insert(0, "...")
        self.title_other_field_left.grid(row=3, column=2, padx=(10,0), pady=(10,0), sticky="we")
        self.title_other_field_left.bind("<FocusIn>", focus.handle_focus_in)
        self.title_other_field_left.bind("<FocusOut>", focus.handle_focus_out)
        self.title_other_field_left.bind("<Configure>", lambda event:focus.check_load(self, self.title_other_field_left))
        self.title_other_radio_left = tk.Radiobutton(self.container_left, text="Other".ljust(5), font="TkFixedFont", variable=self.honorary_left, value="other", bg=self.container_left["bg"], command=lambda:ungray(self.title_other_field_left))
        self.title_other_radio_left.grid(row=3, column=1, padx=(10,0), pady=(10,0), sticky="we")


        self.last_name_label_left = tk.Label(self.container_left, text="Last name")
        self.last_name_label_left.grid(row=4, column=0, padx=(10,0), pady=(10,0))
        self.last_name_label_left["bg"] = self.last_name_label_left.master["bg"]
        
        self.last_name_left = tk.StringVar()
        self.last_name_space_left = tk.Entry(self.container_left, textvariable=self.last_name_left, fg="black")
        self.last_name_space_left.insert(0, "Smith")
        self.last_name_space_left.grid(row=4, column=1, padx=(5, 0), pady=(10,0), columnspan=5, sticky="ew")
        self.last_name_space_left.bind("<FocusIn>", lambda event:focus.handle_focus_in(event, "Smith", allow_hint=True))
        self.last_name_space_left.bind("<FocusOut>", lambda event:focus.handle_focus_out(event, "Smith", allow_hint=True))
        self.last_name_space_left.bind("<Configure>", lambda event:focus.check_load(self, self.last_name_space_left, value="Smith", allow_hint=True))

        self.first_name_label_left = tk.Label(self.container_left, text="First name")
        self.first_name_label_left.grid(row=5, column=0, padx=(10,0), pady=(10,0))
        self.first_name_label_left["bg"] = self.first_name_label_left.master["bg"]
        
        self.first_name_left = tk.StringVar()
        self.first_name_space_left = tk.Entry(self.container_left, textvariable=self.first_name_left, fg="black")
        self.first_name_space_left.grid(row=5, column=1, padx=(5, 0), pady=(10,0), columnspan=5, sticky="ew")
        self.first_name_space_left.insert(0, "Celestine")
        self.first_name_space_left.bind("<FocusIn>", lambda event:focus.handle_focus_in(event, "Celestine", allow_hint=True))
        self.first_name_space_left.bind("<FocusOut>", lambda event:focus.handle_focus_out(event, "Celestine", allow_hint=True))
        self.first_name_space_left.bind("<Configure>", lambda event:focus.check_load(self, self.first_name_space_left, value="Celestine", allow_hint=True))

        self.extra_name_label_left = tk.Label(self.container_left, text="Other name\n if applicable")
        self.extra_name_label_left.grid(row=6, column=0, padx=(10,0), pady=(10,0))
        self.extra_name_label_left["bg"] = self.extra_name_label_left.master["bg"]

        self.extra_name_left = tk.StringVar()
        self.extra_name_space_left = tk.Entry(self.container_left, textvariable=self.extra_name_left, fg="black")
        self.extra_name_space_left.grid(row=6, column=1, padx=(5, 0), pady=(10,0), columnspan=5, sticky="ew")
        self.extra_name_space_left.insert(0, "Jr.")
        self.extra_name_space_left.bind("<FocusIn>", lambda event:focus.handle_focus_in(event, "Jr.", allow_hint=True))
        self.extra_name_space_left.bind("<FocusOut>", lambda event:focus.handle_focus_out(event, "Jr.", allow_hint=True))
        self.extra_name_space_left.bind("<Configure>", lambda event:focus.check_load(self, self.extra_name_space_left, value="Jr.", allow_hint=True))

        self.date_of_birth_label_left = tk.Label(self.container_left, text="Date of birth")
        self.date_of_birth_label_left.grid(row=7, column=0, padx=(10,0), pady=(10,0))
        self.date_of_birth_label_left["bg"] = self.date_of_birth_label_left.master["bg"]

        self.date_of_birth_left = tk.StringVar()
        self.date_of_birth_space_left = tk.Entry(self.container_left, textvariable=self.date_of_birth_left, fg="black")
        self.date_of_birth_space_left.grid(row=7, column=1, padx=(5, 0), pady=(10,0), columnspan=5, sticky="ew")
        self.date_of_birth_space_left.insert(0, "yyyy-mm-dd")
        self.date_of_birth_space_left.bind("<FocusIn>", lambda event:focus.handle_focus_in(event, value="yyyy-mm-dd"))
        self.date_of_birth_space_left.bind("<FocusOut>", lambda event:focus.handle_focus_out(event, value="yyyy-mm-dd"))
        self.date_of_birth_space_left.bind("<Configure>", lambda event:focus.check_load(self, self.date_of_birth_space_left, value="yyyy-mm-dd"))

        self.employment_status_left = tk.IntVar()
        
        self.employment_employed_left = tk.Radiobutton(self.container_left, text="Employed".ljust(13), font="TkFixedFont", variable=self.employment_status_left, value="Employed", bg=self.container_left["bg"], command=lambda:gray_out(self.employment_other_field_left, self.if_unemployed_field_left), activebackground=self.container_left["bg"])
        self.employment_employed_left.grid(row=8, column=0, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_selfemployed_left = tk.Radiobutton(self.container_left, text="Self-employed".ljust(13), font="TkFixedFont", variable=self.employment_status_left, value="Self-employed", bg=self.container_left["bg"], command=lambda:gray_out(self.employment_other_field_left, self.if_unemployed_field_left), activebackground=self.container_left["bg"])
        self.employment_selfemployed_left.grid(row=8, column=1, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_part_time_left = tk.Radiobutton(self.container_left, text="Part-time".ljust(13), font="TkFixedFont", variable=self.employment_status_left, value="Part-time", bg=self.container_left["bg"], command=lambda:gray_out(self.employment_other_field_left, self.if_unemployed_field_left), activebackground=self.container_left["bg"])
        self.employment_part_time_left.grid(row=8, column=2, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_unemployed_left = tk.Radiobutton(self.container_left, text="Unemployed".ljust(13), font="TkFixedFont", variable=self.employment_status_left, value="Unemployed", bg=self.container_left["bg"], command=lambda:gray_out(self.employment_other_field_left) or ungray(self.if_unemployed_field_left), activebackground=self.container_left["bg"])
        self.employment_unemployed_left.grid(row=9, column=0, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_notworking_left = tk.Radiobutton(self.container_left, text="Not-working".ljust(13), font="TkFixedFont", variable=self.employment_status_left, value="Not-working", bg=self.container_left["bg"], command=lambda:gray_out(self.employment_other_field_left, self.if_unemployed_field_left), activebackground=self.container_left["bg"])
        self.employment_notworking_left.grid(row=9, column=1, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_seekingwork_left = tk.Radiobutton(self.container_left, text="Seeking work".ljust(13), font="TkFixedFont", variable=self.employment_status_left, value="Seeking work", bg=self.container_left["bg"], command=lambda:gray_out(self.employment_other_field_left, self.if_unemployed_field_left), activebackground=self.container_left["bg"])
        self.employment_seekingwork_left.grid(row=9, column=2, padx=(10,0), pady=(10,0), sticky="w")
        self.employment_retired_left = tk.Radiobutton(self.container_left, text="Retired".ljust(13), font="TkFixedFont", variable=self.employment_status_left, value="Retired", bg=self.container_left["bg"], command=lambda:gray_out(self.employment_other_field_left, self.if_unemployed_field_left), activebackground=self.container_left["bg"])
        self.employment_retired_left.grid(row=10, column=0, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_other_left = tk.StringVar()
        self.employment_other_field_left = tk.Entry(self.container_left, textvariable=self.employment_other_left, fg="black", width=10, state="disabled")#, bg="#BBBBBB")
        self.employment_other_field_left.insert(0, "...")
        self.employment_other_field_left.grid(row=10, column=2, padx=(10,0), pady=(10,0), sticky="ew")
        self.employment_other_field_left.bind("<FocusIn>", focus.handle_focus_in)
        self.employment_other_field_left.bind("<FocusOut>", focus.handle_focus_out)
        self.employment_other_field_left.bind("<Configure>", lambda event:focus.check_load(self, self.employment_other_field_left))
        self.employment_other_radio_left = tk.Radiobutton(self.container_left, text="Other".ljust(13), font="TkFixedFont", variable=self.employment_status_left, value=4, bg=self.container_left["bg"], command=lambda:ungray(self.employment_other_field_left) or gray_out(self.if_unemployed_field_left), activebackground=self.container_left["bg"])
        self.employment_other_radio_left.grid(row=10, column=1, padx=(10,0), pady=(10,0), sticky="e")
        self.if_unemployed_label_left = tk.Label(self.container_left, text="If unemployed, how long")#, justify="right")
        self.if_unemployed_label_left["bg"] = self.if_unemployed_label_left.master["bg"]
        self.if_unemployed_label_left.grid(row=11, column=0, padx=(10,0), pady=(10,0), sticky="e", columnspan=2)
        self.if_unemployed_left = tk.StringVar()
        self.if_unemployed_field_left = tk.Entry(self.container_left, textvariable=self.if_unemployed_left, fg="black", width=10, state="normal")
        self.if_unemployed_field_left.insert(0, "yy-mm")
        self.if_unemployed_field_left["state"] = "disabled"
        self.if_unemployed_field_left.grid(row=11, column=2, padx=(10,0), pady=(10,0), sticky="ew")
        self.if_unemployed_field_left.bind("<FocusIn>", lambda event:focus.handle_focus_in(event, value="yy-mm"))
        self.if_unemployed_field_left.bind("<FocusOut>", lambda event:focus.handle_focus_out(event, value="yy-mm"))
        self.if_unemployed_field_left.bind("<Configure>", lambda event:focus.check_load(self, self.if_unemployed_field_left, value="yy-mm"))



        self.country_of_birth_label_left = tk.Label(self.container_left, text="Country of birth")
        self.country_of_birth_label_left.grid(row=12, column=0, padx=(10,0), pady=(10,0))
        self.country_of_birth_label_left["bg"] = self.country_of_birth_label_left.master["bg"]

        self.country_of_birth_left = tk.StringVar()
        self.country_of_birth_space_left = tk.Entry(self.container_left, textvariable=self.country_of_birth_left, fg="black")
        self.country_of_birth_space_left.insert(0, "...")
        self.country_of_birth_space_left.grid(row=12, column=1, padx=(5, 0), pady=(10,0), columnspan=3, sticky="ew")
        self.country_of_birth_space_left.bind("<FocusIn>", focus.handle_focus_in)
        self.country_of_birth_space_left.bind("<FocusOut>", focus.handle_focus_out)
        self.country_of_birth_space_left.bind("<Configure>", lambda event:focus.check_load(self, self.country_of_birth_space_left, value="..."))


        self.city_of_birth_label_left = tk.Label(self.container_left, text="City/Town of birth")
        self.city_of_birth_label_left.grid(row=13, column=0, padx=(10,0), pady=(10,0))
        self.city_of_birth_label_left["bg"] = self.city_of_birth_label_left.master["bg"]

        self.city_of_birth_left = tk.StringVar()
        self.city_of_birth_space_left = tk.Entry(self.container_left, fg="black", textvariable=self.city_of_birth_left)
        self.city_of_birth_space_left.insert(0, "...")
        self.city_of_birth_space_left.grid(row=13, column=1, padx=(5, 0), pady=(10,0), columnspan=3, sticky="ew")
        self.city_of_birth_space_left.bind("<FocusIn>", focus.handle_focus_in)
        self.city_of_birth_space_left.bind("<FocusOut>", focus.handle_focus_out)
        self.city_of_birth_space_left.bind("<Configure>", lambda event:focus.check_load(self, self.city_of_birth_space_left, value="..."))


        self.additional_nationalities_label_left = tk.Label(self.container_left, text="Additional nationalities\n(if applicable, separated by newlines)")
        self.additional_nationalities_label_left.grid(row=14, column=0, padx=(10,0), pady=(10,0))
        self.additional_nationalities_label_left["bg"] = self.additional_nationalities_label_left.master["bg"]

        self.additional_nationalities_left = tk.StringVar()
        self.additional_nationalities_space_left = tk.Text(self.container_left, fg="black")
        self.additional_nationalities_space_left.insert("1.0", "...")
        self.additional_nationalities_space_left["width"] = self.additional_nationalities_space_left.master["width"]
        self.additional_nationalities_space_left["height"]= 3
        self.additional_nationalities_space_left.grid(row=14, column=1, padx=(5, 0), pady=(10,0), columnspan=3, sticky="ew")
        self.additional_nationalities_space_left.bind("<FocusIn>", focus.handle_focus_in)
        self.additional_nationalities_space_left.bind("<FocusOut>", focus.handle_focus_out)
        self.additional_nationalities_space_left.bind("<Configure>", lambda event:focus.check_load(self, self.additional_nationalities_space_left))



        self.country_of_residence_label_left = tk.Label(self.container_left, text="Country of residence")
        self.country_of_residence_label_left.grid(row=15, column=0, padx=(10,0), pady=(10,0))
        self.country_of_residence_label_left["bg"] = self.country_of_residence_label_left.master["bg"]

        self.country_of_residence_left = tk.StringVar()
        self.country_of_residence_space_left = tk.Entry(self.container_left, textvariable=self.country_of_residence_left, fg="black")
        self.country_of_residence_space_left.insert(0, "Norway")
        self.country_of_residence_space_left.grid(row=15, column=1, padx=(5, 0), pady=(10,0), columnspan=3, sticky="ew")
        self.country_of_residence_space_left.bind("<FocusIn>", lambda event: focus.handle_focus_in(event, value="Norway"))
        self.country_of_residence_space_left.bind("<FocusOut>", lambda event: focus.handle_focus_out(event, value="Norway", allow_hint=True))
        self.country_of_residence_space_left.bind("<Configure>", lambda event: focus.check_load(self, self.country_of_residence_space_left, value="Norway", allow_hint=True))



        self.tax_resident_label_left = tk.Label(self.container_left, text="Countries in which\n you're tax resident\n (separated by newlines)")
        self.tax_resident_label_left.grid(row=16, column=0, padx=(10,0), pady=(10,0))
        self.tax_resident_label_left["bg"] = self.tax_resident_label_left.master["bg"]

        self.tax_resident_left = tk.StringVar()
        self.tax_resident_space_left = tk.Text(self.container_left, fg="black")
        self.tax_resident_space_left.insert("1.0", "...")
        self.tax_resident_space_left["width"] = self.tax_resident_space_left.master["width"]
        self.tax_resident_space_left["height"]= 3
        self.tax_resident_space_left.grid(row=16, column=1, padx=(5, 0), pady=(10,0), columnspan=3, sticky="ew")
        self.tax_resident_space_left.bind("<FocusIn>", focus.handle_focus_in)
        self.tax_resident_space_left.bind("<FocusOut>", focus.handle_focus_out)
        self.tax_resident_space_left.bind("<Configure>", lambda event:focus.check_load(self, self.tax_resident_space_left))




 
        # Right Side
        self.customer_label_right = tk.Label(self.container_right, text="Second customer", font=("Courier", 12, "bold"), justify="left")
        self.customer_label_right.grid(row=0, column=0, padx=(10,0), pady=(10,0), columnspan=5)
        self.customer_label_right["bg"] = self.customer_label_right.master["bg"]

        self.existing_customer_label_right = tk.Label(self.container_right, text="Check if you're an existing\nLloyd Bank customer", font=("Courier", 8), justify="left")
        self.existing_customer_label_right.grid(row=1, column=0, padx=(10,0), pady=(10,0), columnspan=2)
        self.existing_customer_label_right["bg"] = self.existing_customer_label_right.master["bg"]

        self.existing_customer_right_value = tk.BooleanVar()
        self.existing_customer_right = tk.Checkbutton(self.container_right, variable=self.existing_customer_right_value)
        self.existing_customer_right.grid(row=1, column=2, pady=(10,0))
        self.existing_customer_right["bg"] = self.existing_customer_right.master["bg"]

        self.honorary_right = tk.IntVar()
        
        self.title_miss_right = tk.Radiobutton(self.container_right, text="Miss".ljust(5), font="TkFixedFont", variable=self.honorary_right, value=1, bg=self.container_right["bg"], command=lambda:gray_out(self.title_other_field_right), justify="left")
        self.title_miss_right.grid(row=2, column=0, padx=(10,0), pady=(10,0), sticky="we")
        self.title_mr_right = tk.Radiobutton(self.container_right, text="Mr.".ljust(5), font="TkFixedFont", variable=self.honorary_right, value=2, bg=self.container_right["bg"], command=lambda:gray_out(self.title_other_field_right), justify="left")
        self.title_mr_right.grid(row=2, column=1, padx=(10,0), pady=(10,0), sticky="we")
        self.title_mrs_right = tk.Radiobutton(self.container_right, text="Mrs.".ljust(5), font="TkFixedFont", variable=self.honorary_right, value=3, bg=self.container_right["bg"], command=lambda:gray_out(self.title_other_field_right), justify="left")
        self.title_mrs_right.grid(row=2, column=2, padx=(10,0), pady=(10,0), sticky="we")
        self.title_ms_right = tk.Radiobutton(self.container_right, text="Ms.".ljust(5), font="TkFixedFont", variable=self.honorary_right, value=4, bg=self.container_right["bg"], command=lambda:gray_out(self.title_other_field_right), justify="left")
        self.title_ms_right.grid(row=3, column=0, padx=(10,0), pady=(10,0), sticky="we")
        self.title_other_right = tk.StringVar()
        self.title_other_field_right = tk.Entry(self.container_right, textvariable=self.title_other_right, fg="black", width=10, state="disabled")#, bg="#BBBBBB")
        self.title_other_field_right.insert(0, "...")
        self.title_other_field_right.grid(row=3, column=2, padx=(10,0), pady=(10,0), sticky="we")
        self.title_other_field_right.bind("<FocusIn>", focus.handle_focus_in)
        self.title_other_field_right.bind("<FocusOut>", focus.handle_focus_out)
        self.title_other_field_right.bind("<Configure>", lambda event:focus.check_load(self, self.title_other_field_right))
        self.title_other_radio_right = tk.Radiobutton(self.container_right, text="Other".ljust(5), font="TkFixedFont", variable=self.honorary_right, value="5", bg=self.container_right["bg"], command=lambda:ungray(self.title_other_field_right))
        self.title_other_radio_right.grid(row=3, column=1, padx=(10,0), pady=(10,0), sticky="we")


        self.last_name_label_right = tk.Label(self.container_right, text="Last name")
        self.last_name_label_right.grid(row=4, column=0, padx=(10,0), pady=(10,0))
        self.last_name_label_right["bg"] = self.last_name_label_right.master["bg"]
        
        self.last_name_right = tk.StringVar()
        self.last_name_space_right = tk.Entry(self.container_right, textvariable=self.last_name_right, fg="black")
        self.last_name_space_right.insert(0, "Smith")
        self.last_name_space_right.grid(row=4, column=1, padx=(5, 0), pady=(10,0), columnspan=5, sticky="ew")
        self.last_name_space_right.bind("<FocusIn>", lambda event:focus.handle_focus_in(event, "Smith", allow_hint=True))
        self.last_name_space_right.bind("<FocusOut>", lambda event:focus.handle_focus_out(event, "Smith", allow_hint=True))
        self.last_name_space_right.bind("<Configure>", lambda event:focus.check_load(self, self.last_name_space_right, value="Smith", allow_hint=True))

        self.first_name_label_right = tk.Label(self.container_right, text="First name")
        self.first_name_label_right.grid(row=5, column=0, padx=(10,0), pady=(10,0))
        self.first_name_label_right["bg"] = self.first_name_label_right.master["bg"]
        
        self.first_name_right = tk.StringVar()
        self.first_name_space_right = tk.Entry(self.container_right, textvariable=self.first_name_right, fg="black")
        self.first_name_space_right.grid(row=5, column=1, padx=(5, 0), pady=(10,0), columnspan=5, sticky="ew")
        self.first_name_space_right.insert(0, "Celestine")
        self.first_name_space_right.bind("<FocusIn>", lambda event:focus.handle_focus_in(event, "Celestine", allow_hint=True))
        self.first_name_space_right.bind("<FocusOut>", lambda event:focus.handle_focus_out(event, "Celestine", allow_hint=True))
        self.first_name_space_right.bind("<Configure>", lambda event:focus.check_load(self, self.first_name_space_right, value="Celestine", allow_hint=True))

        self.extra_name_label_right = tk.Label(self.container_right, text="Other name\n if applicable")
        self.extra_name_label_right.grid(row=6, column=0, padx=(10,0), pady=(10,0))
        self.extra_name_label_right["bg"] = self.extra_name_label_right.master["bg"]

        self.extra_name_right = tk.StringVar()
        self.extra_name_space_right = tk.Entry(self.container_right, textvariable=self.extra_name_right, fg="black")
        self.extra_name_space_right.grid(row=6, column=1, padx=(5, 0), pady=(10,0), columnspan=5, sticky="ew")
        self.extra_name_space_right.insert(0, "Jr.")
        self.extra_name_space_right.bind("<FocusIn>", lambda event:focus.handle_focus_in(event, "Jr.", allow_hint=True))
        self.extra_name_space_right.bind("<FocusOut>", lambda event:focus.handle_focus_out(event, "Jr.", allow_hint=True))
        self.extra_name_space_right.bind("<Configure>", lambda event:focus.check_load(self, self.extra_name_space_right, value="Jr.", allow_hint=True))

        self.date_of_birth_label_right = tk.Label(self.container_right, text="Date of birth")
        self.date_of_birth_label_right.grid(row=7, column=0, padx=(10,0), pady=(10,0))
        self.date_of_birth_label_right["bg"] = self.date_of_birth_label_right.master["bg"]

        self.date_of_birth_right = tk.StringVar()
        self.date_of_birth_space_right = tk.Entry(self.container_right, textvariable=self.date_of_birth_right, fg="black")
        self.date_of_birth_space_right.grid(row=7, column=1, padx=(5, 0), pady=(10,0), columnspan=5, sticky="ew")
        self.date_of_birth_space_right.insert(0, "yyyy-mm-dd")
        self.date_of_birth_space_right.bind("<FocusIn>", lambda event:focus.handle_focus_in(event, value="yyyy-mm-dd"))
        self.date_of_birth_space_right.bind("<FocusOut>", lambda event:focus.handle_focus_out(event, value="yyyy-mm-dd"))
        self.date_of_birth_space_right.bind("<Configure>", lambda event:focus.check_load(self, self.date_of_birth_space_right, value="yyyy-mm-dd"))

        self.employment_status_right = tk.IntVar()
        
        self.employment_employed_right = tk.Radiobutton(self.container_right, text="Employed".ljust(13), font="TkFixedFont", variable=self.employment_status_right, value="Employed", bg=self.container_right["bg"], command=lambda:gray_out(self.employment_other_field_right, self.if_unemployed_field_right), activebackground=self.container_right["bg"])
        self.employment_employed_right.grid(row=8, column=0, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_selfemployed_right = tk.Radiobutton(self.container_right, text="Self-employed".ljust(13), font="TkFixedFont", variable=self.employment_status_right, value="Self-employed", bg=self.container_right["bg"], command=lambda:gray_out(self.employment_other_field_right, self.if_unemployed_field_right), activebackground=self.container_right["bg"])
        self.employment_selfemployed_right.grid(row=8, column=1, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_part_time_right = tk.Radiobutton(self.container_right, text="Part-time".ljust(13), font="TkFixedFont", variable=self.employment_status_right, value="Part-time", bg=self.container_right["bg"], command=lambda:gray_out(self.employment_other_field_right, self.if_unemployed_field_right), activebackground=self.container_right["bg"])
        self.employment_part_time_right.grid(row=8, column=2, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_unemployed_right = tk.Radiobutton(self.container_right, text="Unemployed".ljust(13), font="TkFixedFont", variable=self.employment_status_right, value="Unemployed", bg=self.container_right["bg"], command=lambda:gray_out(self.employment_other_field_right) or ungray(self.if_unemployed_field_right), activebackground=self.container_right["bg"])
        self.employment_unemployed_right.grid(row=9, column=0, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_notworking_right = tk.Radiobutton(self.container_right, text="Not-working".ljust(13), font="TkFixedFont", variable=self.employment_status_right, value="Not-working", bg=self.container_right["bg"], command=lambda:gray_out(self.employment_other_field_right, self.if_unemployed_field_right), activebackground=self.container_right["bg"])
        self.employment_notworking_right.grid(row=9, column=1, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_seekingwork_right = tk.Radiobutton(self.container_right, text="Seeking work".ljust(13), font="TkFixedFont", variable=self.employment_status_right, value="Seeking work", bg=self.container_right["bg"], command=lambda:gray_out(self.employment_other_field_right, self.if_unemployed_field_right), activebackground=self.container_right["bg"])
        self.employment_seekingwork_right.grid(row=9, column=2, padx=(10,0), pady=(10,0), sticky="w")
        self.employment_retired_right = tk.Radiobutton(self.container_right, text="Retired".ljust(13), font="TkFixedFont", variable=self.employment_status_right, value="Retired", bg=self.container_right["bg"], command=lambda:gray_out(self.employment_other_field_right, self.if_unemployed_field_right), activebackground=self.container_right["bg"])
        self.employment_retired_right.grid(row=10, column=0, padx=(10,0), pady=(10,0), sticky="e")
        self.employment_other_right = tk.StringVar()
        self.employment_other_field_right = tk.Entry(self.container_right, textvariable=self.employment_other_right, fg="black", width=10, state="disabled")#, bg="#BBBBBB")
        self.employment_other_field_right.insert(0, "...")
        self.employment_other_field_right.grid(row=10, column=2, padx=(10,0), pady=(10,0), sticky="ew")
        self.employment_other_field_right.bind("<FocusIn>", focus.handle_focus_in)
        self.employment_other_field_right.bind("<FocusOut>", focus.handle_focus_out)
        self.employment_other_field_right.bind("<Configure>", lambda event:focus.check_load(self, self.employment_other_field_right))
        self.employment_other_radio_right = tk.Radiobutton(self.container_right, text="Other".ljust(13), font="TkFixedFont", variable=self.employment_status_right, value=4, bg=self.container_right["bg"], command=lambda:ungray(self.employment_other_field_right) or gray_out(self.if_unemployed_field_right), activebackground=self.container_right["bg"])
        self.employment_other_radio_right.grid(row=10, column=1, padx=(10,0), pady=(10,0), sticky="e")
        self.if_unemployed_label_right = tk.Label(self.container_right, text="If unemployed, how long")#, justify="right")
        self.if_unemployed_label_right["bg"] = self.if_unemployed_label_right.master["bg"]
        self.if_unemployed_label_right.grid(row=11, column=0, padx=(10,0), pady=(10,0), sticky="e", columnspan=2)
        self.if_unemployed_right = tk.StringVar()
        self.if_unemployed_field_right = tk.Entry(self.container_right, textvariable=self.if_unemployed_right, fg="black", width=10, state="normal")
        self.if_unemployed_field_right.insert(0, "yy-mm")
        self.if_unemployed_field_right["state"] = "disabled"
        self.if_unemployed_field_right.grid(row=11, column=2, padx=(10,0), pady=(10,0), sticky="ew")
        self.if_unemployed_field_right.bind("<FocusIn>", lambda event:focus.handle_focus_in(event, value="yy-mm"))
        self.if_unemployed_field_right.bind("<FocusOut>", lambda event:focus.handle_focus_out(event, value="yy-mm"))
        self.if_unemployed_field_right.bind("<Configure>", lambda event:focus.check_load(self, self.if_unemployed_field_right, value="yy-mm"))



        self.country_of_birth_label_right = tk.Label(self.container_right, text="Country of birth")
        self.country_of_birth_label_right.grid(row=12, column=0, padx=(10,0), pady=(10,0))
        self.country_of_birth_label_right["bg"] = self.country_of_birth_label_right.master["bg"]

        self.country_of_birth_right = tk.StringVar()
        self.country_of_birth_space_right = tk.Entry(self.container_right, textvariable=self.country_of_birth_right, fg="black")
        self.country_of_birth_space_right.insert(0, "...")
        self.country_of_birth_space_right.grid(row=12, column=1, padx=(5, 0), pady=(10,0), columnspan=3, sticky="ew")
        self.country_of_birth_space_right.bind("<FocusIn>", focus.handle_focus_in)
        self.country_of_birth_space_right.bind("<FocusOut>", focus.handle_focus_out)
        self.country_of_birth_space_right.bind("<Configure>", lambda event:focus.check_load(self, self.country_of_birth_space_right, value="..."))


        self.city_of_birth_label_right = tk.Label(self.container_right, text="City/Town of birth")
        self.city_of_birth_label_right.grid(row=13, column=0, padx=(10,0), pady=(10,0))
        self.city_of_birth_label_right["bg"] = self.city_of_birth_label_right.master["bg"]

        self.city_of_birth_right = tk.StringVar()
        self.city_of_birth_space_right = tk.Entry(self.container_right, fg="black", textvariable=self.city_of_birth_right)
        self.city_of_birth_space_right.insert(0, "...")
        self.city_of_birth_space_right.grid(row=13, column=1, padx=(5, 0), pady=(10,0), columnspan=3, sticky="ew")
        self.city_of_birth_space_right.bind("<FocusIn>", focus.handle_focus_in)
        self.city_of_birth_space_right.bind("<FocusOut>", focus.handle_focus_out)
        self.city_of_birth_space_right.bind("<Configure>", lambda event:focus.check_load(self, self.city_of_birth_space_right, value="..."))


        self.additional_nationalities_label_right = tk.Label(self.container_right, text="Additional nationalities\n(if applicable, separated by newlines)")
        self.additional_nationalities_label_right.grid(row=14, column=0, padx=(10,0), pady=(10,0))
        self.additional_nationalities_label_right["bg"] = self.additional_nationalities_label_right.master["bg"]

        self.additional_nationalities_right = tk.StringVar()
        self.additional_nationalities_space_right = tk.Text(self.container_right, fg="black")
        self.additional_nationalities_space_right.insert("1.0", "...")
        self.additional_nationalities_space_right["width"] = self.additional_nationalities_space_right.master["width"]
        self.additional_nationalities_space_right["height"]= 3
        self.additional_nationalities_space_right.grid(row=14, column=1, padx=(5, 0), pady=(10,0), columnspan=3, sticky="ew")
        self.additional_nationalities_space_right.bind("<FocusIn>", focus.handle_focus_in)
        self.additional_nationalities_space_right.bind("<FocusOut>", focus.handle_focus_out)
        self.additional_nationalities_space_right.bind("<Configure>", lambda event:focus.check_load(self, self.additional_nationalities_space_right))



        self.country_of_residence_label_right = tk.Label(self.container_right, text="Country of residence")
        self.country_of_residence_label_right.grid(row=15, column=0, padx=(10,0), pady=(10,0))
        self.country_of_residence_label_right["bg"] = self.country_of_residence_label_right.master["bg"]

        self.country_of_residence_right = tk.StringVar()
        self.country_of_residence_space_right = tk.Entry(self.container_right, textvariable=self.country_of_residence_right, fg="black")
        self.country_of_residence_space_right.insert(0, "Norway")
        self.country_of_residence_space_right.grid(row=15, column=1, padx=(5, 0), pady=(10,0), columnspan=3, sticky="ew")
        self.country_of_residence_space_right.bind("<FocusIn>", lambda event: focus.handle_focus_in(event, value="Norway"))
        self.country_of_residence_space_right.bind("<FocusOut>", lambda event: focus.handle_focus_out(event, value="Norway", allow_hint=True))
        self.country_of_residence_space_right.bind("<Configure>", lambda event: focus.check_load(self, self.country_of_residence_space_right, value="Norway", allow_hint=True))



        self.tax_resident_label_right = tk.Label(self.container_right, text="Countries in which\n you're tax resident\n (separated by newlines)")
        self.tax_resident_label_right.grid(row=16, column=0, padx=(10,0), pady=(10,0))
        self.tax_resident_label_right["bg"] = self.tax_resident_label_right.master["bg"]

        self.tax_resident_right = tk.StringVar()
        self.tax_resident_space_right = tk.Text(self.container_right, fg="black")
        self.tax_resident_space_right.insert("1.0", "...")
        self.tax_resident_space_right["width"] = self.tax_resident_space_right.master["width"]
        self.tax_resident_space_right["height"]= 3
        self.tax_resident_space_right.grid(row=16, column=1, padx=(5, 0), pady=(10,0), columnspan=3, sticky="ew")
        self.tax_resident_space_right.bind("<FocusIn>", focus.handle_focus_in)
        self.tax_resident_space_right.bind("<FocusOut>", focus.handle_focus_out)
        self.tax_resident_space_right.bind("<Configure>", lambda event:focus.check_load(self, self.tax_resident_space_right))

