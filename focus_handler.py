def handle_focus_in(event, value="...", allow_hint=False):
    global string
    type_widget = event.widget.winfo_class().lower()
    if type_widget == "entry":
        string = event.widget.get()
    elif type_widget == "text":
        string = event.widget.get("1.0", "end")[:-1]  # Removing a newline
    hint_checker = True if event.widget["fg"] == "#888888" else False  # Using font colour to check if input was written manually
    print("in:", string)
    event.widget["fg"] = "#000000"
    if type_widget == "entry" and hint_checker == True:
        if string == value or string == "None":
            event.widget.delete(0, "end")
            event.widget.insert(0, "")
    elif type_widget == "text" and hint_checker == True:
        if string == value or string == "None":
            event.widget.delete("1.0", "end")
            event.widget.insert("1.0", "")

def handle_focus_out(event, value="...", allow_hint=False):
    current_year = 2019
    validity = False
    print(event, value, allow_hint)
    try:
        item=event.widget
    except:
        item=event
    global string
    type_widget = item.winfo_class().lower()
    if type_widget == "entry":
        string = item.get()
    elif type_widget == "text":
        string = item.get("1.0", "end")
    print(string+"\n")
    if value == "yyyy-mm-dd":
        try:
            year = string[0:4]
            month = string[5:7]
            date = string[8:10]
            try:
                if (1900 < int(year) <= current_year):
                    if (1 <= int(month) <= 12):
                        if (1 <= int(date) <= 31):
                            validity = True
            except ValueError:
                validity = False
        except IndexError:
            validity = False
    elif value == "yy-mm":
        try:
            years = string[0:2]
            months = string[3:5]
            try:
                if string[2] == "-" and len(string) == 5:
                    if (1 <= int(years) <= 99) and (1 <= int(months) <= 12):
                        validity = True
                else:
                    validity = False
            except ValueError:
                validity = False
        except IndexError:
            validity = False
    elif string == "" or string in ["\r", "\n", "none", "none\n"]:
        validity = False
    else:
        validity = True
    if validity == False and allow_hint == False:
        if type_widget == "entry":
            item.delete(0, "end")
            item.insert(0, value)
        elif type_widget == "text":
            item.delete("1.0", "end")
            item.insert("1.0", value)
        item["fg"] = "#888888"
    elif validity == False and allow_hint == True:
        if string in ["", "\n", "\r"]:
            if type_widget == "entry":            
                item.delete(0, "end")
                item.insert(0, value)
            elif type_widget == "text":
                item.delete("1.0", "end")
                item.insert("1.0", value)
            item["fg"] = "#888888"

def check_load(event, item, *bonus, **kwargs):
    #print(event,item,bonus,kwargs)
    try:
        string = bonus
    except:
        string = "..."
    if str(string) == "()":
        string = "..."
    try:
        for key, values in kwargs.items():
            if key == "value":
                string = values
    except:
        pass
    if item.winfo_class().lower() == "entry":
        if len(item.get())<2 or item.get().lower() in ["\n", "\r", string.lower(), "...", "...\n", "none"]:
            item.delete(0, "end")
            item.insert(0, string)
            item["fg"] = "#888888"
        else:
            item["fg"] = "black"
    elif item.winfo_class().lower() == "text":
        if item.get("1.0", "end") in ["\n", "\r", string, "...", "...\n", "none"]:
            item.delete("1.0", "end")
            item.insert("1.0", string)
            item["fg"] = "#888888"
        else:
            item["fg"] = "black"