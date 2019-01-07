import tkinter as tk

class Form_3(tk.Frame):
    def __init__(self, root):
        super().__init__(root, height=root.height, background="#ebf4f2")
        root.master.update_idletasks()

    def add_buttons(self, root):
        self.next = tk.Button(self, text="Next page", width=35, height=3, command=self.master.layers[4].tkraise)
        self.next.place(relx=1, rely=1, anchor="se")

        self.prev = tk.Button(self, text="Back", width=35, height=3, command=self.master.layers[2].tkraise)
        self.prev.place(relx=0, rely=1, anchor="sw")

    def add_form(self, root):
        import focus_handler as focus        
        def gray_out(*whats):
            for what in whats:
                    what["state"] = "disabled"
        def ungray(*whats):
            for what in whats:
                what["state"] = "normal"  

        # 1

        self.title_1_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_1_container.grid(row=0, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        
        self.container_1_left = tk.Frame(self, background="#ebf4f2")
        self.container_1_right = tk.Frame(self, background="#d9eae5")
        #self.container_2_left.grid_propagate(False)
        self.container_1_left.grid(row=1, column=0, sticky="nsew", ipadx=root.margin, ipady=15)
        self.container_1_right.grid(row=1, column=1, sticky="nsew", ipadx=root.margin, ipady=15)
        self.container_1_left.grid_columnconfigure(0, weight=1)
        self.container_1_right.grid_columnconfigure(0, weight=1)

        self.container_1_left.grid_columnconfigure(1, weight=1)
        self.container_1_right.grid_columnconfigure(1, weight=1)

        self.title_1_number = tk.Label(self.title_1_container, fg="#006e51", text="1.2", bg="white", font="-weight bold", bd=2, relief="solid")
        self.title_1 = tk.Label(self.title_1_container, background="#499a86", text="Your residential details", anchor="w", fg="white", font="-weight bold")
        self.title_1_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title_1.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)



        # Left 1
        self.home_address_label_left = tk.Label(self.container_1_left, text="Home address")
        self.home_address_label_left.grid(row=0, column=0)
        self.home_address_label_left["bg"] = self.home_address_label_left.master["bg"]

        self.h_address_1_left = tk.StringVar()
        self.home_address_1_left = tk.Entry(self.container_1_left, textvariable=self.h_address_1_left)
        self.home_address_1_left.grid(row=1, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)

        self.h_address_2_left = tk.StringVar()
        self.home_address_2_left = tk.Entry(self.container_1_left, textvariable=self.h_address_1_left)
        self.home_address_2_left.grid(row=2, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)

        self.h_address_3_left = tk.StringVar()
        self.home_address_3_left = tk.Entry(self.container_1_left, textvariable=self.h_address_2_left)
        self.home_address_3_left.grid(row=3, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)

        self.h_address_postcode_left = tk.StringVar()
        self.home_postcode_left = tk.Entry(self.container_1_left, textvariable=self.h_address_3_left)
        self.home_postcode_left.grid(row=4, column=0, sticky="nsew", padx=root.margin, pady=(3,3))

        self.h_address_postcountry_left = tk.StringVar()
        self.home_postcountry_left = tk.Entry(self.container_1_left, textvariable=self.h_address_postcountry_left)
        self.home_postcountry_left.grid(row=4, column=1, sticky="nsew", padx=root.margin, pady=(3,3))

        self.home_from_when_living_label_left = tk.Label(self.container_1_left, text="When did you start living at this address?")
        self.home_from_when_living_label_left.grid(row=5, column=0)
        self.home_from_when_living_label_left["bg"] = self.home_from_when_living_label_left.master["bg"]

        self.h_address_time_left = tk.StringVar()
        self.home_from_when_living_left = tk.Entry(self.container_1_left, textvariable=self.h_address_time_left)
        self.home_from_when_living_left.grid(row=5, column=1, sticky="nsew", padx=root.margin, pady=(3,3))




        self.previous_address_label_left = tk.Label(self.container_1_left, text="Previous address")
        self.previous_address_label_left.grid(row=6, column=0)
        self.previous_address_label_left["bg"] = self.previous_address_label_left.master["bg"]
        
        self.p_address_1_left = tk.StringVar()
        self.previous_address_1_left = tk.Entry(self.container_1_left, textvariable=self.p_address_1_left)
        self.previous_address_1_left.grid(row=7, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.p_address_2_left = tk.StringVar()
        self.previous_address_2_left = tk.Entry(self.container_1_left, textvariable=self.p_address_2_left)
        self.previous_address_2_left.grid(row=8, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.p_address_3_left = tk.StringVar()
        self.previous_address_3_left = tk.Entry(self.container_1_left, textvariable=self.p_address_3_left)
        self.previous_address_3_left.grid(row=9, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.p_address_postcode_left = tk.StringVar()
        self.previous_postcode_left = tk.Entry(self.container_1_left, textvariable=self.p_address_postcode_left)
        self.previous_postcode_left.grid(row=10, column=0, sticky="nsew", padx=root.margin, pady=(3,3))
        
        self.p_address_postcountry_left = tk.StringVar()
        self.previous_postcountry_left = tk.Entry(self.container_1_left, textvariable=self.p_address_postcountry_left)
        self.previous_postcountry_left.grid(row=10, column=1, sticky="nsew", padx=root.margin, pady=(3,3))

        self.previous_from_when_living_label_left = tk.Label(self.container_1_left, text="When did you start living at this address?")
        self.previous_from_when_living_label_left.grid(row=11, column=0)
        self.previous_from_when_living_label_left["bg"] = self.previous_from_when_living_label_left.master["bg"]
        
        self.p_address_time_left = tk.StringVar()
        self.previous_from_when_living_left = tk.Entry(self.container_1_left, textvariable=self.p_address_time_left)
        self.previous_from_when_living_left.grid(row=12, column=1, sticky="nsew", padx=root.margin, pady=(3,3))





        self.correspondence_address_label_left = tk.Label(self.container_1_left, text="Correspondence address")
        self.correspondence_address_label_left.grid(row=13, column=0)
        self.correspondence_address_label_left["bg"] = self.correspondence_address_label_left.master["bg"]
        
        self.c_address_1_left = tk.StringVar()
        self.correspondence_address_1_left = tk.Entry(self.container_1_left, textvariable=self.c_address_1_left)
        self.correspondence_address_1_left.grid(row=14, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.c_address_2_left = tk.StringVar()
        self.correspondence_address_2_left = tk.Entry(self.container_1_left, textvariable=self.c_address_2_left)
        self.correspondence_address_2_left.grid(row=15, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.c_address_3_left = tk.StringVar()
        self.correspondence_address_3_left = tk.Entry(self.container_1_left, textvariable=self.c_address_3_left)
        self.correspondence_address_3_left.grid(row=16, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.c_address_postcode_left = tk.StringVar()
        self.correspondence_address_left = tk.Entry(self.container_1_left, textvariable=self.c_address_postcode_left)
        self.correspondence_address_left.grid(row=17, column=0, sticky="nsew", padx=root.margin, pady=(3,3))
        
        self.c_address_postcountry_left = tk.StringVar()
        self.correspondence_address_left = tk.Entry(self.container_1_left, textvariable=self.c_address_postcountry_left)
        self.correspondence_address_left.grid(row=17, column=1, sticky="nsew", padx=root.margin, pady=(3,3))


        # Right 1
        self.home_address_label_right = tk.Label(self.container_1_right, text="Home address")
        self.home_address_label_right.grid(row=0, column=0)
        self.home_address_label_right["bg"] = self.home_address_label_right.master["bg"]

        self.h_address_1_right = tk.StringVar()
        self.home_address_1_right = tk.Entry(self.container_1_right, textvariable=self.h_address_1_right)
        self.home_address_1_right.grid(row=1, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)

        self.h_address_2_right = tk.StringVar()
        self.home_address_2_right = tk.Entry(self.container_1_right, textvariable=self.h_address_1_right)
        self.home_address_2_right.grid(row=2, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)

        self.h_address_3_right = tk.StringVar()
        self.home_address_3_right = tk.Entry(self.container_1_right, textvariable=self.h_address_2_right)
        self.home_address_3_right.grid(row=3, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)

        self.h_address_postcode_right = tk.StringVar()
        self.home_postcode_right = tk.Entry(self.container_1_right, textvariable=self.h_address_3_right)
        self.home_postcode_right.grid(row=4, column=0, sticky="nsew", padx=root.margin, pady=(3,3))

        self.h_address_postcountry_right = tk.StringVar()
        self.home_postcountry_right = tk.Entry(self.container_1_right, textvariable=self.h_address_postcountry_right)
        self.home_postcountry_right.grid(row=4, column=1, sticky="nsew", padx=root.margin, pady=(3,3))

        self.home_from_when_living_label_right = tk.Label(self.container_1_right, text="When did you start living at this address?")
        self.home_from_when_living_label_right.grid(row=5, column=0)
        self.home_from_when_living_label_right["bg"] = self.home_from_when_living_label_right.master["bg"]

        self.h_address_time_right = tk.StringVar()
        self.home_from_when_living_right = tk.Entry(self.container_1_right, textvariable=self.h_address_time_right)
        self.home_from_when_living_right.grid(row=5, column=1, sticky="nsew", padx=root.margin, pady=(3,3))




        self.previous_address_label_right = tk.Label(self.container_1_right, text="Previous address")
        self.previous_address_label_right.grid(row=6, column=0)
        self.previous_address_label_right["bg"] = self.previous_address_label_right.master["bg"]
        
        self.p_address_1_right = tk.StringVar()
        self.previous_address_1_right = tk.Entry(self.container_1_right, textvariable=self.p_address_1_right)
        self.previous_address_1_right.grid(row=7, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.p_address_2_right = tk.StringVar()
        self.previous_address_2_right = tk.Entry(self.container_1_right, textvariable=self.p_address_2_right)
        self.previous_address_2_right.grid(row=8, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.p_address_3_right = tk.StringVar()
        self.previous_address_3_right = tk.Entry(self.container_1_right, textvariable=self.p_address_3_right)
        self.previous_address_3_right.grid(row=9, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.p_address_postcode_right = tk.StringVar()
        self.previous_postcode_right = tk.Entry(self.container_1_right, textvariable=self.p_address_postcode_right)
        self.previous_postcode_right.grid(row=10, column=0, sticky="nsew", padx=root.margin, pady=(3,3))
        
        self.p_address_postcountry_right = tk.StringVar()
        self.previous_postcountry_right = tk.Entry(self.container_1_right, textvariable=self.p_address_postcountry_right)
        self.previous_postcountry_right.grid(row=10, column=1, sticky="nsew", padx=root.margin, pady=(3,3))

        self.previous_from_when_living_label_right = tk.Label(self.container_1_right, text="When did you start living at this address?")
        self.previous_from_when_living_label_right.grid(row=11, column=0)
        self.previous_from_when_living_label_right["bg"] = self.previous_from_when_living_label_right.master["bg"]
        
        self.p_address_time_right = tk.StringVar()
        self.previous_from_when_living_right = tk.Entry(self.container_1_right, textvariable=self.p_address_time_right)
        self.previous_from_when_living_right.grid(row=12, column=1, sticky="nsew", padx=root.margin, pady=(3,3))





        self.correspondence_address_label_right = tk.Label(self.container_1_right, text="Correspondence address")
        self.correspondence_address_label_right.grid(row=13, column=0)
        self.correspondence_address_label_right["bg"] = self.correspondence_address_label_right.master["bg"]
        
        self.c_address_1_right = tk.StringVar()
        self.correspondence_address_1_right = tk.Entry(self.container_1_right, textvariable=self.c_address_1_right)
        self.correspondence_address_1_right.grid(row=14, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.c_address_2_right = tk.StringVar()
        self.correspondence_address_2_right = tk.Entry(self.container_1_right, textvariable=self.c_address_2_right)
        self.correspondence_address_2_right.grid(row=15, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.c_address_3_right = tk.StringVar()
        self.correspondence_address_3_right = tk.Entry(self.container_1_right, textvariable=self.c_address_3_right)
        self.correspondence_address_3_right.grid(row=16, column=0, sticky="nsew", padx=root.margin, pady=(3,3), columnspan=2)
        
        self.c_address_postcode_right = tk.StringVar()
        self.correspondence_address_right = tk.Entry(self.container_1_right, textvariable=self.c_address_postcode_right)
        self.correspondence_address_right.grid(row=17, column=0, sticky="nsew", padx=root.margin, pady=(3,3))
        
        self.c_address_postcountry_right = tk.StringVar()
        self.correspondence_address_right = tk.Entry(self.container_1_right, textvariable=self.c_address_postcountry_right)
        self.correspondence_address_right.grid(row=17, column=1, sticky="nsew", padx=root.margin, pady=(3,3))







        # Debit stuff

        self.title_2_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_2_container.grid(row=2, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_2_number = tk.Label(self.title_2_container, background="#006e51", text="2", fg="white", font="-weight bold")
        self.title_2 = tk.Label(self.title_2_container, background="#499a86", text="Your debit card details", anchor="w", fg="white", font="-weight bold")
        self.title_2_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title_2.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)


        self.container_2_left = tk.Frame(self, background="#ebf4f2")
        self.container_2_right = tk.Frame(self, background="#d9eae5")
        #self.container_left.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_rowconfigure(3, weight=1)
        self.container_2_left.grid(row=3, column=0, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_2_right.grid(row=3, column=1, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_2_left.grid_columnconfigure(0, weight=1)
        self.container_2_right.grid_columnconfigure(0, weight=1)

        # Left
        self.apply_for_debit_card_label_left = tk.Label(self.container_2_left, justify="left", text= "I would like to apply for a debit card\n"+\
                                                                                              "The type of card we give you depends on our assessment of your personal circumstances.")
        self.apply_for_debit_card_label_left.grid(row=0, column=0, sticky="nsew")
        self.apply_for_debit_card_label_left["bg"] = self.apply_for_debit_card_label_left.master["bg"]

        self.apply_for_debit_card_value_left = tk.IntVar()
        self.apply_for_debit_card_box_left = tk.Checkbutton(self.container_2_left, variable=self.apply_for_debit_card_value_left)
        self.apply_for_debit_card_box_left.grid(row=0, column=1, sticky="nsew")
        self.apply_for_debit_card_box_left["bg"] = self.apply_for_debit_card_box_left.master["bg"]

        self.customer_on_card_label_left = tk.Label(self.container_2_left, justify="left", text="Customer name to appear on card")
        self.customer_on_card_label_left.grid(row=1, column=0, sticky="nsew", columnspan=2)
        self.customer_on_card_label_left["bg"] = self.customer_on_card_label_left.master["bg"]

        self.customer_on_card_left = tk.StringVar()
        self.customer_on_card_entry_left = tk.Entry(self.container_2_left, textvariable=self.customer_on_card_left)
        self.customer_on_card_entry_left.grid(row=2, column=0, sticky="nsew", columnspan=2, padx=(10,0))


        self.mother_prev_name_label_left = tk.Label(self.container_2_left, justify="left", text="Mother\'s previous name (new debit card customers only)")
        self.mother_prev_name_label_left.grid(row=3, column=0, sticky="nsew", columnspan=2)
        self.mother_prev_name_label_left["bg"] = self.mother_prev_name_label_left.master["bg"]

        self.mother_prev_name_left = tk.StringVar()
        self.mother_prev_name_entry_left = tk.Entry(self.container_2_left, textvariable=self.mother_prev_name_left)
        self.mother_prev_name_entry_left.grid(row=4, column=0, sticky="nsew", columnspan=2, padx=(10,0))


        self.date_of_birth_label_left = tk.Label(self.container_2_left, justify="left", text="Date of birth")
        self.date_of_birth_label_left.grid(row=5, column=0, sticky="nsew", columnspan=2)
        self.date_of_birth_label_left["bg"] = self.date_of_birth_label_left.master["bg"]

        self.date_of_birth_left = tk.StringVar()
        self.date_of_birth_entry_left = tk.Entry(self.container_2_left, textvariable=self.date_of_birth_left)
        self.date_of_birth_entry_left.grid(row=6, column=0, sticky="nsew", columnspan=2, padx=(10,0))


        #Right
        self.apply_for_debit_card_label_right = tk.Label(self.container_2_right, justify="left", text= "I would like to apply for a debit card\n"+\
                                                                                              "The type of card we give you depends on our assessment of your personal circumstances.")
        self.apply_for_debit_card_label_right.grid(row=0, column=0, sticky="nsew")
        self.apply_for_debit_card_label_right["bg"] = self.apply_for_debit_card_label_right.master["bg"]

        self.apply_for_debit_card_value_right = tk.IntVar()
        self.apply_for_debit_card_box_right = tk.Checkbutton(self.container_2_right, variable=self.apply_for_debit_card_value_right)
        self.apply_for_debit_card_box_right.grid(row=0, column=1, sticky="nsew")
        self.apply_for_debit_card_box_right["bg"] = self.apply_for_debit_card_box_right.master["bg"]

        self.customer_on_card_label_right = tk.Label(self.container_2_right, justify="left", text="Customer name to appear on card")
        self.customer_on_card_label_right.grid(row=1, column=0, sticky="nsew", columnspan=2)
        self.customer_on_card_label_right["bg"] = self.customer_on_card_label_right.master["bg"]

        self.customer_on_card_right = tk.StringVar()
        self.customer_on_card_entry_right = tk.Entry(self.container_2_right, textvariable=self.customer_on_card_right)
        self.customer_on_card_entry_right.grid(row=2, column=0, sticky="nsew", columnspan=2, padx=(10,0))


        self.mother_prev_name_label_right = tk.Label(self.container_2_right, justify="left", text="Mother\'s previous name (new debit card customers only)")
        self.mother_prev_name_label_right.grid(row=3, column=0, sticky="nsew", columnspan=2)
        self.mother_prev_name_label_right["bg"] = self.mother_prev_name_label_right.master["bg"]

        self.mother_prev_name_right = tk.StringVar()
        self.mother_prev_name_entry_right = tk.Entry(self.container_2_right, textvariable=self.mother_prev_name_right)
        self.mother_prev_name_entry_right.grid(row=4, column=0, sticky="nsew", columnspan=2, padx=(10,0))


        self.date_of_birth_label_right = tk.Label(self.container_2_right, justify="left", text="Date of birth")
        self.date_of_birth_label_right.grid(row=5, column=0, sticky="nsew", columnspan=2)
        self.date_of_birth_label_right["bg"] = self.date_of_birth_label_right.master["bg"]

        self.date_of_birth_right = tk.StringVar()
        self.date_of_birth_entry_right = tk.Entry(self.container_2_right, textvariable=self.date_of_birth_right)
        self.date_of_birth_entry_right.grid(row=6, column=0, sticky="nsew", columnspan=2, padx=(10,0))