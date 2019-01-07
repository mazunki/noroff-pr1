import tkinter as tk

class Form_4(tk.Frame):
    def __init__(self, root):
        super().__init__(root, height=root.height, background="#ebf4f2")
        root.master.update_idletasks()

    def add_buttons(self, root):
        self.next = tk.Button(self, text="Next page", width=35, height=3, command=self.master.layers[5].tkraise)
        self.next.place(relx=1, rely=1, anchor="se")

        self.prev = tk.Button(self, text="Back", width=35, height=3, command=self.master.layers[3].tkraise)
        self.prev.place(relx=0, rely=1, anchor="sw")


    def add_form(self, root):
        import focus_handler as focus

        self.text_label = tk.Label(self, text="Personal data")
        self.text_label.place(relx=0.5, rely=0, anchor="n")

        self.title_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_container.grid(row=0, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_number = tk.Label(self.title_container, background="#006e51", text="3", fg="white", font="-weight bold")
        self.title = tk.Label(self.title_container, background="#499a86", text="How we process your personal information", anchor="w", fg="white", font="-weight bold")
        self.title_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)
        

        self.container_left = tk.Frame(self, background="#ebf4f2")
        self.container_right = tk.Frame(self, background="#d9eae5")
        #self.container_left.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_rowconfigure(1, weight=1)
        self.container_left.grid(row=1, column=0, sticky="nsew", ipadx=root.margin)
        self.container_left.grid_rowconfigure(0, weight=1)
        self.container_right.grid(row=1, column=1, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_left.grid_columnconfigure(0, weight=1)
        self.container_right.grid_columnconfigure(0, weight=1)

        def gray_out(*whats):
            for what in whats:
                    what["state"] = "disabled"
        def ungray(*whats):
            for what in whats:
                what["state"] = "normal"  
        def bold_it(string, text):
            self.start_pos = "1.0"
            for _ in range(int(string.count("*")/2)):
                self.pos =  text.search("*", self.start_pos, stopindex="end")
                text.delete(self.pos)
                self.pos2 = text.search("*", self.pos, stopindex="end")
                text.delete(self.pos2)
                text.tag_add("bold", self.pos, self.pos2)
                text.insert(self.pos+"-1c", "\n")

                self.start_pos = self.pos2+"+1c"
            text.tag_configure("bold", font="-weight bold")
            text.config(state="disabled")

        with open("policy.txt", "r") as self.policy_file:
            self.file_content = self.policy_file.read()
        self.policy_text = tk.Text(self.container_left)
        self.policy_text.delete(1.0, "end")
        self.policy_text.insert("end", self.file_content)
        self.policy_text.grid(row=0, column=0, sticky="nsew")
        self.policy_text.config(wrap="word", bg = self.policy_text.master["bg"], highlightthickness=0, borderwidth=0)
        bold_it(self.file_content, self.policy_text)



        self.wrapper = tk.Frame(self.container_left, height=56, width=1)  # Apparently the height of the button due to the font size
        self.wrapper.grid(row=1, column=0)


        self.marketing_label = tk.Label(self.container_right, text =  "*Your marketing choices*\n"+\
                                                                      "We would like to keep you up to date on products and offers that may be of interest to you. \n"+\
                                                                      "Please select how you would like to hear from us below. These choices won’t affect any \n"+\
                                                                      "necessary information we need to send you such as statements and, don’t worry, you can \n"+\
                                                                      "change your mind and update your preferences at any time", justify="left")
        self.marketing_label.grid(row=0, column=0, sticky="nsew", columnspan=5)
        self.marketing_label["bg"] = self.marketing_label.master["bg"]

        self.first_customer = tk.Label(self.container_right, text="First customer")
        self.first_customer.grid(row=1, column=1, sticky="nsew", columnspan=2)
        self.first_customer["bg"] = self.first_customer.master["bg"]

        self.second_customer = tk.Label(self.container_right, text="Second customer")
        self.second_customer.grid(row=1, column=3, sticky="nsew", columnspan=2)
        self.second_customer["bg"] = self.second_customer.master["bg"]


        self.first_customer = tk.Label(self.container_right, text="Yes")
        self.first_customer.grid(row=2, column=1, sticky="nsew")
        self.first_customer["bg"] = self.first_customer.master["bg"]


        self.second_customer = tk.Label(self.container_right, text="No")
        self.second_customer.grid(row=2, column=2, sticky="nsew")
        self.second_customer["bg"] = self.second_customer.master["bg"]

        self.first_customer = tk.Label(self.container_right, text="Yes")
        self.first_customer.grid(row=2, column=3, sticky="nsew")
        self.first_customer["bg"] = self.first_customer.master["bg"]


        self.second_customer = tk.Label(self.container_right, text="No")
        self.second_customer.grid(row=2, column=4, sticky="nsew")
        self.second_customer["bg"] = self.second_customer.master["bg"]


        self.internet_banking_label = tk.Label(self.container_right, text = "Internet Banking")
        self.internet_banking_label.grid(row=3, column=0, sticky="nsew")
        self.internet_banking_label["bg"] = self.internet_banking_label.master["bg"]

        self.internet_banking_first_value = tk.IntVar()
        self.internet_banking_second_value = tk.IntVar()
        self.internet_banking_first_yes = tk.Radiobutton(self.container_right, variable=self.internet_banking_first_value, value="yes")
        self.internet_banking_first_no  = tk.Radiobutton(self.container_right, variable=self.internet_banking_first_value, value="yes")
        self.internet_banking_second_yes = tk.Radiobutton(self.container_right, variable=self.internet_banking_second_value, value="no")
        self.internet_banking_second_no  = tk.Radiobutton(self.container_right, variable=self.internet_banking_second_value, value="no")
        self.internet_banking_first_yes.grid(row=3, column=1 , sticky="nsew")
        self.internet_banking_first_no.grid(row=3, column=2 , sticky="nsew")
        self.internet_banking_second_yes.grid(row=3, column=3 , sticky="nsew")
        self.internet_banking_second_no.grid(row=3, column=4 , sticky="nsew")
        self.internet_banking_first_yes["bg"] = self.internet_banking_first_yes.master["bg"]
        self.internet_banking_first_no["bg"] = self.internet_banking_first_no.master["bg"]
        self.internet_banking_second_yes["bg"] = self.internet_banking_second_yes.master["bg"]
        self.internet_banking_second_no["bg"] = self.internet_banking_second_no.master["bg"]
        self.internet_banking_first_yes["activebackground"] = self.internet_banking_first_yes.master["bg"]
        self.internet_banking_first_no["activebackground"] = self.internet_banking_first_no.master["bg"]
        self.internet_banking_second_yes["activebackground"] = self.internet_banking_second_yes.master["bg"]
        self.internet_banking_second_no["activebackground"] = self.internet_banking_second_no.master["bg"]


        self.email_label = tk.Label(self.container_right, text = "Email")
        self.email_label.grid(row=4, column=0, sticky="nsew")
        self.email_label["bg"] = self.email_label.master["bg"]

        self.email_first_value = tk.IntVar()
        self.email_second_value = tk.IntVar()
        self.email_first_yes = tk.Radiobutton(self.container_right, variable=self.email_first_value, value="yes")
        self.email_first_no  = tk.Radiobutton(self.container_right, variable=self.email_first_value, value="no")
        self.email_second_yes = tk.Radiobutton(self.container_right, variable=self.email_second_value, value="yes")
        self.email_second_no  = tk.Radiobutton(self.container_right, variable=self.email_second_value, value="no")
        self.email_first_yes.grid(row=4, column=1 , sticky="nsew")
        self.email_first_no.grid(row=4, column=2 , sticky="nsew")
        self.email_second_yes.grid(row=4, column=3 , sticky="nsew")
        self.email_second_no.grid(row=4, column=4 , sticky="nsew")
        self.email_first_yes["bg"] = self.email_first_yes.master["bg"]
        self.email_first_no["bg"] = self.email_first_no.master["bg"]
        self.email_second_yes["bg"] = self.email_second_yes.master["bg"]
        self.email_second_no["bg"] = self.email_second_no.master["bg"]
        self.email_first_yes["activebackground"] = self.email_first_yes.master["bg"]
        self.email_first_no["activebackground"] = self.email_first_no.master["bg"]
        self.email_second_yes["activebackground"] = self.email_second_yes.master["bg"]
        self.email_second_no["activebackground"] = self.email_second_no.master["bg"]


        self.post_label = tk.Label(self.container_right, text = "Post")
        self.post_label.grid(row=5, column=0, sticky="nsew")
        self.post_label["bg"] = self.post_label.master["bg"]

        self.post_first_value = tk.IntVar()
        self.post_second_value = tk.IntVar()
        self.post_first_yes = tk.Radiobutton(self.container_right, variable=self.post_first_value, value="yes")
        self.post_first_no  = tk.Radiobutton(self.container_right, variable=self.post_first_value, value="no")
        self.post_second_yes = tk.Radiobutton(self.container_right, variable=self.post_second_value, value="yes")
        self.post_second_no  = tk.Radiobutton(self.container_right, variable=self.post_second_value, value="no")
        self.post_first_yes.grid(row=5, column=1 , sticky="nsew")
        self.post_first_no.grid(row=5, column=2 , sticky="nsew")
        self.post_second_yes.grid(row=5, column=3 , sticky="nsew")
        self.post_second_no.grid(row=5, column=4 , sticky="nsew")
        self.post_first_yes["bg"] = self.post_first_yes.master["bg"]
        self.post_first_no["bg"] = self.post_first_no.master["bg"]
        self.post_second_yes["bg"] = self.post_second_yes.master["bg"]
        self.post_second_no["bg"] = self.post_second_no.master["bg"]
        self.post_first_yes["activebackground"] = self.post_first_yes.master["bg"]
        self.post_first_no["activebackground"] = self.post_first_no.master["bg"]
        self.post_second_yes["activebackground"] = self.post_second_yes.master["bg"]
        self.post_second_no["activebackground"] = self.post_second_no.master["bg"]


        self.device_messaging_label = tk.Label(self.container_right, text = "Device messaging")
        self.device_messaging_label.grid(row=6, column=0, sticky="nsew")
        self.device_messaging_label["bg"] = self.device_messaging_label.master["bg"]

        self.device_messaging_first_value = tk.IntVar()
        self.device_messaging_second_value = tk.IntVar()
        self.device_messaging_first_yes = tk.Radiobutton(self.container_right, variable=self.device_messaging_first_value, value="yes")
        self.device_messaging_first_no  = tk.Radiobutton(self.container_right, variable=self.device_messaging_first_value, value="no")
        self.device_messaging_second_yes = tk.Radiobutton(self.container_right, variable=self.device_messaging_second_value, value="yes")
        self.device_messaging_second_no  = tk.Radiobutton(self.container_right, variable=self.device_messaging_second_value, value="no")
        self.device_messaging_first_yes.grid(row=6, column=1 , sticky="nsew")
        self.device_messaging_first_no.grid(row=6, column=2 , sticky="nsew")
        self.device_messaging_second_yes.grid(row=6, column=3 , sticky="nsew")
        self.device_messaging_second_no.grid(row=6, column=4 , sticky="nsew")
        self.device_messaging_first_yes["bg"] = self.device_messaging_first_yes.master["bg"]
        self.device_messaging_first_no["bg"] = self.device_messaging_first_no.master["bg"]
        self.device_messaging_second_yes["bg"] = self.device_messaging_second_yes.master["bg"]
        self.device_messaging_second_no["bg"] = self.device_messaging_second_no.master["bg"]
        self.device_messaging_first_yes["activebackground"] = self.device_messaging_first_yes.master["bg"]
        self.device_messaging_first_no["activebackground"] = self.device_messaging_first_no.master["bg"]
        self.device_messaging_second_yes["activebackground"] = self.device_messaging_second_yes.master["bg"]
        self.device_messaging_second_no["activebackground"] = self.device_messaging_second_no.master["bg"]


        self.text_messages_label = tk.Label(self.container_right, text = "Text messages")
        self.text_messages_label.grid(row=7, column=0, sticky="nsew")
        self.text_messages_label["bg"] = self.text_messages_label.master["bg"]

        self.text_messages_first_value = tk.IntVar()
        self.text_messages_second_value = tk.IntVar()
        self.text_messages_first_yes = tk.Radiobutton(self.container_right, variable=self.text_messages_first_value, value="yes")
        self.text_messages_first_no  = tk.Radiobutton(self.container_right, variable=self.text_messages_first_value, value="no")
        self.text_messages_second_yes = tk.Radiobutton(self.container_right, variable=self.text_messages_second_value, value="yes")
        self.text_messages_second_no  = tk.Radiobutton(self.container_right, variable=self.text_messages_second_value, value="no")
        self.text_messages_first_yes.grid(row=7, column=1 , sticky="nsew")
        self.text_messages_first_no.grid(row=7, column=2 , sticky="nsew")
        self.text_messages_second_yes.grid(row=7, column=3 , sticky="nsew")
        self.text_messages_second_no.grid(row=7, column=4 , sticky="nsew")
        self.text_messages_first_yes["bg"] = self.text_messages_first_yes.master["bg"]
        self.text_messages_first_no["bg"] = self.text_messages_first_no.master["bg"]
        self.text_messages_second_yes["bg"] = self.text_messages_second_yes.master["bg"]
        self.text_messages_second_no["bg"] = self.text_messages_second_no.master["bg"]
        self.text_messages_first_yes["activebackground"] = self.text_messages_first_yes.master["bg"]
        self.text_messages_first_no["activebackground"] = self.text_messages_first_no.master["bg"]
        self.text_messages_second_yes["activebackground"] = self.text_messages_second_yes.master["bg"]
        self.text_messages_second_no["activebackground"] = self.text_messages_second_no.master["bg"]


        self.phone_label = tk.Label(self.container_right, text = "Phone")
        self.phone_label.grid(row=8, column=0, sticky="nsew")
        self.phone_label["bg"] = self.phone_label.master["bg"]

        self.phone_first_value = tk.IntVar()
        self.phone_second_value = tk.IntVar()
        self.phone_first_yes = tk.Radiobutton(self.container_right, variable=self.phone_first_value, value="yes")
        self.phone_first_no  = tk.Radiobutton(self.container_right, variable=self.phone_first_value, value="no")
        self.phone_second_yes = tk.Radiobutton(self.container_right, variable=self.phone_second_value, value="yes")
        self.phone_second_no  = tk.Radiobutton(self.container_right, variable=self.phone_second_value, value="no")
        self.phone_first_yes.grid(row=8, column=1 , sticky="nsew")
        self.phone_first_no.grid(row=8, column=2 , sticky="nsew")
        self.phone_second_yes.grid(row=8, column=3 , sticky="nsew")
        self.phone_second_no.grid(row=8, column=4 , sticky="nsew")
        self.phone_first_yes["bg"] = self.phone_first_yes.master["bg"]
        self.phone_first_no["bg"] = self.phone_first_no.master["bg"]
        self.phone_second_yes["bg"] = self.phone_second_yes.master["bg"]
        self.phone_second_no["bg"] = self.phone_second_no.master["bg"]
        self.phone_first_yes["activebackground"] = self.phone_first_yes.master["bg"]
        self.phone_first_no["activebackground"] = self.phone_first_no.master["bg"]
        self.phone_second_yes["activebackground"] = self.phone_second_yes.master["bg"]
        self.phone_second_no["activebackground"] = self.phone_second_no.master["bg"]

        self.marketing_label = tk.Label(self.container_right, text ="By saying yes you are giving consent for Lloyds Bank to use your personal information to \n"+\
                                                                    "send you relevant offers and products. Lloyds Bank includes the following legal entities: \n"+\
                                                                    "Lloyds Bank plc; Lloyds Bank Insurance Services Ltd; and Halifax Share Dealing Limited.\n\n"+\
                                                                    "Occasionally we will send you selected offers from other companies within Lloyds Banking \n"+\
                                                                    "Group that may be relevant to you.", justify="left")
        self.marketing_label.grid(row=9, column=0, sticky="nsew", columnspan=5)
        self.marketing_label["bg"] = self.marketing_label.master["bg"]