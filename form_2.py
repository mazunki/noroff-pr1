import tkinter as tk

class Form_2(tk.Frame):
    def __init__(self, root):
        super().__init__(root, background="gray")
        root.master.update_idletasks()

    def add_buttons(self, root):
        self.next = tk.Button(self, text="Next page", width=35, height=3, command=self.master.layers[3].tkraise)
        self.next.place(relx=1, rely=1, anchor="se")

        self.prev = tk.Button(self, text="Back", width=35, height=3, command=self.master.layers[1].tkraise)
        self.prev.place(relx=0, rely=1, anchor="sw")
        pass

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
        #self.container_1_left.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_columnconfigure(0, weight=1, uniform="group1")

        self.container_1_left.grid(row=1, column=0, sticky="nsew", ipadx=root.margin, ipady=15)
        self.container_1_right.grid(row=1, column=1, sticky="nsew", ipadx=root.margin, ipady=15)
        self.container_1_left.grid_columnconfigure(0, weight=1)
        self.container_1_right.grid_columnconfigure(0, weight=1)

        self.title_number = tk.Label(self.title_1_container, background="#006e51", text="1", fg="white", font="-weight bold")
        self.title = tk.Label(self.title_1_container, background="#499a86", text="Your personal details", anchor="w", fg="white", font="-weight bold")
        self.title_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)
        

        # Left 1
        self.customer_label_left = tk.Label(self.container_1_left, text="First customer", font=("Courier", 12, "bold"), justify="left")
        self.customer_label_left.grid(row=0, column=0, padx=(10,0), pady=(10,0), columnspan=2, sticky="nsew")
        self.customer_label_left["bg"] = self.customer_label_left.master["bg"]

        self.taxpayer_identification_number_label_left = tk.Label(self.container_1_left, text="If you have a Taxpayer Identification Number (TIN)\n for other countries, please provide details below")
        self.taxpayer_identification_number_label_left.grid(row=1, column=0, padx=(10,0), pady=(10,0), sticky="nsew")
        self.taxpayer_identification_number_label_left["bg"] = self.taxpayer_identification_number_label_left.master["bg"]


        self.taxpayer_identification_number_1_left = tk.StringVar()
        self.taxpayer_identification_number_field_1_left = tk.Entry(self.container_1_left, textvariable=self.taxpayer_identification_number_1_left)
        self.taxpayer_identification_number_field_1_left.grid(row=2, column=0, sticky="ew", padx=root.margin, pady=(3,3))

        self.taxpayer_identification_number_2_left = tk.StringVar()
        self.taxpayer_identification_number_field_2_left = tk.Entry(self.container_1_left, textvariable=self.taxpayer_identification_number_2_left)
        self.taxpayer_identification_number_field_2_left.grid(row=3, column=0, sticky="ew", padx=root.margin, pady=(3,3))

        self.taxpayer_identification_number_3_left = tk.StringVar()
        self.taxpayer_identification_number_field_3_left = tk.Entry(self.container_1_left, textvariable=self.taxpayer_identification_number_3_left)
        self.taxpayer_identification_number_field_3_left.grid(row=4, column=0, sticky="ew", padx=root.margin, pady=(3,3))

        # self.taxpayer_identification_number_4_left = tk.Entry(self.container_1_left)
        # self.taxpayer_identification_number_4_left.grid(row=5, column=0, sticky="ew", padx=root.margin, pady=(3,3))

        # self.taxpayer_identification_number_5_left = tk.Entry(self.container_1_left)
        # self.taxpayer_identification_number_5_left.grid(row=6, column=0, sticky="ew", padx=root.margin, pady=(3,3))

        # self.taxpayer_identification_number_6_left = tk.Entry(self.container_1_left)
        # self.taxpayer_identification_number_6_left.grid(row=7, column=0, sticky="ew", padx=root.margin, pady=(3,3))



        # Right 1
        self.customer_label_right = tk.Label(self.container_1_right, text="Second customer", font=("Courier", 12, "bold"), justify="left")
        self.customer_label_right.grid(row=0, column=0, padx=(10,0), pady=(10,0), columnspan=2, sticky="nsew")
        self.customer_label_right["bg"] = self.customer_label_right.master["bg"]

        self.taxpayer_identification_number_label_right = tk.Label(self.container_1_right, text="If you have a Taxpayer Identification Number (TIN)\n for other countries, please provide details below")
        self.taxpayer_identification_number_label_right.grid(row=1, column=0, padx=(10,0), pady=(10,0), sticky="nsew")
        self.taxpayer_identification_number_label_right["bg"] = self.taxpayer_identification_number_label_right.master["bg"]

        self.taxpayer_identification_number_1_right = tk.StringVar()
        self.taxpayer_identification_number_1_right = tk.Entry(self.container_1_right, textvariable=self.taxpayer_identification_number_1_right)
        self.taxpayer_identification_number_1_right.grid(row=2, column=0, sticky="ew", padx=root.margin, pady=(3,3))

        self.taxpayer_identification_number_2_right = tk.StringVar()
        self.taxpayer_identification_number_2_right = tk.Entry(self.container_1_right, textvariable=self.taxpayer_identification_number_2_right)
        self.taxpayer_identification_number_2_right.grid(row=3, column=0, sticky="ew", padx=root.margin, pady=(3,3))

        self.taxpayer_identification_number_3_right = tk.StringVar()
        self.taxpayer_identification_number_3_right = tk.Entry(self.container_1_right, textvariable=self.taxpayer_identification_number_3_right)
        self.taxpayer_identification_number_3_right.grid(row=4, column=0, sticky="ew", padx=root.margin, pady=(3,3))

        # self.taxpayer_identification_number_4_right = tk.Entry(self.container_1_right)
        # self.taxpayer_identification_number_4_right.grid(row=5, column=0, sticky="ew", padx=root.margin, pady=(3,3))

        # self.taxpayer_identification_number_5_right = tk.Entry(self.container_1_right)
        # self.taxpayer_identification_number_5_right.grid(row=6, column=0, sticky="ew", padx=root.margin, pady=(3,3))

        # self.taxpayer_identification_number_6_right = tk.Entry(self.container_1_right)
        # self.taxpayer_identification_number_6_right.grid(row=7, column=0, sticky="ew", padx=root.margin, pady=(3,3))



        # 2

        self.title_2_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_2_container.grid(row=2, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        
        self.container_2_left = tk.Frame(self, background="#ebf4f2")
        self.container_2_right = tk.Frame(self, background="#d9eae5")
        #self.container_2_left.grid_propagate(False)
        #self.grid_rowconfigure(3, weight=1)
        self.container_2_left.grid(row=3, column=0, sticky="nsew", ipadx=root.margin)
        self.container_2_right.grid(row=3, column=1, sticky="nsew", ipadx=root.margin)
        self.container_2_left.grid_columnconfigure(1, weight=1)
        self.container_2_right.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.title_2_number = tk.Label(self.title_2_container, fg="#006e51", text="1.1", bg="white", font="-weight bold", bd=2, relief="solid")
        self.title_2 = tk.Label(self.title_2_container, background="#499a86", text="Your contact details", anchor="w", fg="white", font="-weight bold")
        self.title_2_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title_2.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)


        # Left 2
        self.telephone_label_left = tk.Label(self.container_2_left, text="Home number")
        self.telephone_label_left.grid(row=0, column=0)
        self.telephone_label_left["bg"] = self.telephone_label_left.master["bg"]

        self.tel_1_left = tk.StringVar()
        self.telephone_1_left = tk.Entry(self.container_2_left, textvariable=self.tel_1_left)
        self.telephone_1_left.grid(row=0, column=1, sticky="nsew", padx=root.margin, pady=(3,3))


        self.telephone_label_left = tk.Label(self.container_2_left, text="Mobile number")
        self.telephone_label_left.grid(row=1, column=0)
        self.telephone_label_left["bg"] = self.telephone_label_left.master["bg"]

        self.tel_2_left = tk.StringVar()
        self.telephone_2_left = tk.Entry(self.container_2_left, textvariable=self.tel_2_left)
        self.telephone_2_left.grid(row=1, column=1, sticky="nsew", padx=root.margin, pady=(3,3))


        self.telephone_label_left = tk.Label(self.container_2_left, text="Work number")
        self.telephone_label_left.grid(row=2, column=0)
        self.telephone_label_left["bg"] = self.telephone_label_left.master["bg"]

        self.tel_3_left = tk.StringVar()
        self.telephone_3_left = tk.Entry(self.container_2_left, textvariable=self.tel_3_left)
        self.telephone_3_left.grid(row=2, column=1, sticky="nsew", padx=root.margin, pady=(3,3))


        self.email_left_label = tk.Label(self.container_2_left, text="Your email address")
        self.email_left_label.grid(row=3, column=0)
        self.email_left_label["bg"] = self.email_left_label.master["bg"]

        self.emailaddress_left = tk.StringVar()
        self.email_left = tk.Entry(self.container_2_left, textvariable=self.emailaddress_left)
        self.email_left.grid(row=3, column=1, sticky="nsew", padx=root.margin, pady=(3,3))


        # Right 2
        self.telephone_label_right = tk.Label(self.container_2_right, text="Home number")
        self.telephone_label_right.grid(row=0, column=0)
        self.telephone_label_right["bg"] = self.telephone_label_right.master["bg"]

        self.tel_1_right = tk.StringVar()
        self.telephone_1_right = tk.Entry(self.container_2_right, textvariable=self.tel_1_right)
        self.telephone_1_right.grid(row=0, column=1, sticky="nsew", padx=root.margin, pady=(3,3))


        self.telephone_label_right = tk.Label(self.container_2_right, text="Mobile number")
        self.telephone_label_right.grid(row=1, column=0)
        self.telephone_label_right["bg"] = self.telephone_label_right.master["bg"]

        self.tel_2_right = tk.StringVar()
        self.telephone_2_right = tk.Entry(self.container_2_right, textvariable=self.tel_2_right)
        self.telephone_2_right.grid(row=1, column=1, sticky="nsew", padx=root.margin, pady=(3,3))


        self.telephone_label_right = tk.Label(self.container_2_right, text="Work number")
        self.telephone_label_right.grid(row=2, column=0)
        self.telephone_label_right["bg"] = self.telephone_label_right.master["bg"]

        self.tel_3_right = tk.StringVar()
        self.telephone_3_right = tk.Entry(self.container_2_right, textvariable=self.tel_3_right)
        self.telephone_3_right.grid(row=2, column=1, sticky="nsew", padx=root.margin, pady=(3,3))


        self.email_right_label = tk.Label(self.container_2_right, text="Your email address")
        self.email_right_label.grid(row=3, column=0)
        self.email_right_label["bg"] = self.email_right_label.master["bg"]

        self.emailaddress_right = tk.StringVar()
        self.email_right = tk.Entry(self.container_2_right, textvariable=self.emailaddress_right)
        self.email_right.grid(row=3, column=1, sticky="nsew", padx=root.margin, pady=(3,3))
