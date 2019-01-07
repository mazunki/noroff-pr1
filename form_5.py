import tkinter as tk

class Form_5(tk.Frame):
    def __init__(self, root):
        super().__init__(root, height=root.height, background="#ebf4f2")
        root.master.update_idletasks()

    def add_buttons(self, root):
        self.next = tk.Button(self, text="Next page", width=35, height=3, command=self.master.layers[6].tkraise)
        self.next.place(relx=1, rely=1, anchor="se")

        self.prev = tk.Button(self, text="Back", width=35, height=3, command=self.master.layers[4].tkraise)
        self.prev.place(relx=0, rely=1, anchor="sw")

    def add_form(self, root):
        import focus_handler as focus

        self.text_label = tk.Label(self, text="Personal data")
        self.text_label.place(relx=0.5, rely=0, anchor="n")

        self.title_container = tk.Frame(self, background="#ebf4f2", height=40)
        self.title_container.grid(row=0, column=0, sticky="new", columnspan=2)
        #self.title_container.pack_propagate(0)

        self.title_number = tk.Label(self.title_container, background="#006e51", text="4", fg="white", font="-weight bold")
        self.title = tk.Label(self.title_container, background="#499a86", text="Your agreement with us", anchor="w", fg="white", font="-weight bold")
        self.title_number.pack(side="left", padx=(10,0), ipady=5, ipadx=20)
        self.title.pack(side="left", padx=(10,10), ipady=5, ipadx=5, fill="x", expand=True)
        

        self.container_left = tk.Frame(self, background="#ebf4f2")
        self.container_right = tk.Frame(self, background="#d9eae5")
        #self.container_left.grid_propagate(False)
        self.grid_columnconfigure(1, weight=1, uniform="group1")
        self.grid_columnconfigure(0, weight=1, uniform="group1")
        self.grid_rowconfigure(1, weight=1)
        self.container_left.grid_rowconfigure(0, weight=1)
        self.container_left.grid(row=1, column=0, sticky="nsew", ipadx=root.margin, ipady=35)
        self.container_right.grid(row=1, column=1, sticky="nsew", ipadx=root.margin, ipady=35)
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

        with open("agreement.txt", "r") as self.agreement_file:
            self.file_content = self.agreement_file.read()
        self.agreement_text = tk.Text(self.container_left)
        self.agreement_text.delete(1.0, "end")
        self.agreement_text.insert("end", self.file_content)
        self.agreement_text.config(wrap="word", bg = self.agreement_text.master["bg"], highlightthickness=0, borderwidth=0)
        self.agreement_text.grid(row=0, column=0, sticky="nsew")
        bold_it(self.file_content, self.agreement_text)

        self.wrapper = tk.Frame(self.container_left, height=56, width=1)
        self.wrapper.grid(row=1, column=0)
