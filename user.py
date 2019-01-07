
class User():
    def __init__(self, username="0"):
        self.user_name = username
        self.private_dict_data = {

        "existing_customer": "kartoffel",
        "honorary": "kartoffel",
        "honorary_other": "kartoffel",
        "last_name": "kartoffel",
        "first_names": "kartoffel",
        "other_names": "kartoffel",
        "date_of_birth": "kartoffel",
        "employment_status": "kartoffel",
        "unemployed_time": "kartoffel",
        "employment_other": "kartoffel",
        "country_birth": "kartoffel",
        "city_birth": "kartoffel",
        "nationalities": "kartoffel",
        "country_residence": "kartoffel",
        "countries_tax_resident": "kartoffel",

        "tin1": "kartoffel",
        "tin2": "kartoffel",
        "tin3": "kartoffel",


        "home_number": "kartoffel",
        "mobile_number": "kartoffel",
        "work_number": "kartoffel",
        "email": "kartoffel",


        "home_address_1": "kartoffel",
        "home_address_2": "kartoffel",
        "home_address_3": "kartoffel",
        "home_address_code": "kartoffel",
        "home_addreess_country": "kartoffel",
        "home_address_time": "kartoffel",
        "previous_address_1": "kartoffel",
        "previous_address_2": "kartoffel",
        "previous_address_3": "kartoffel",
        "previous_address_code": "kartoffel",
        "previous_addreess_country": "kartoffel",
        "previous_address_time": "kartoffel",
        "correspondence_address_1": "kartoffel",
        "correspondence_address_2": "kartoffel",
        "correspondence_address_3": "kartoffel",
        "correspondence_address_code": "kartoffel",
        "correspondence_addreess_country": "kartoffel",

        }

        self.dict_data = {

        "apply_debit": "kartoffel",
        "name_on_card": "kartoffel",
        "mother_name": "kartoffel",
        "card_date_of_birth": "kartoffel",


        "marketing_internet_banking": "kartoffel",
        "marketing_email": "kartoffel",
        "marketing_post": "kartoffel",
        "marketing_device_messaging": "kartoffel",
        "marketing_text_messages": "kartoffel",
        "marketing_phone": "kartoffel",


        "currently_working": "kartoffel",
        "occupation": "kartoffel",
        "employer_name": "kartoffel",
        "employer_address_1": "kartoffel",
        "employer_address_2": "kartoffel",
        "employer_address_3": "kartoffel",
        "employer_postcode": "kartoffel",
        "employer_time": "kartoffel",
        "previous_employment_time": "kartoffel",
        "employmnet_pensionable": "kartoffel",


        "income_salary": "kartoffel",
        "income_salary_frequency": "kartoffel",
        "income_salary_method": "kartoffel",
        "income_benefits": "kartoffel",
        "income_benefits_frequency": "kartoffel",
        "income_benefits_method": "kartoffel",
        "income_pension": "kartoffel",
        "income_pension_frequency": "kartoffel",
        "income_pension_method": "kartoffel",
        "income_investments": "kartoffel",
        "income_investments_frequency": "kartoffel",
        "income_investments_method": "kartoffel",
        "income_other": "kartoffel",
        "income_other_frequency": "kartoffel",
        "income_other_method": "kartoffel",
        "income_other_explanation": "kartoffel",
        "income_total": "kartoffel",
        "expected_through_account": "kartoffel",


        "mortage": "kartoffel",
        "other_loans": "kartoffel",
        "lloyd_loans": "kartoffel",
        "total_loans": "kartoffel",


        "type_savings": "kartoffel",
        "total_savings": "kartoffel",


        "type_account": "kartoffel",


        "facilities": "kartoffel",
        "banked_time": "kartoffel",
        "account_to_be_closed": "kartoffel",
        "account_to_be_closed_explanation": "kartoffel",
        "transfer_account": "kartoffel",


        "hold_credit_card": "kartoffel",
        "credit_card_quantity": "kartoffel",
        "hold_lloyd_credit_card": "kartoffel",
        "lloyd_credit_card_limit": "kartoffel",
        "other_cards": "kartoffel",
        "other_cards_specification": "kartoffel",


        "have_mortage": "kartoffel",
        "mortage_with_lloyd": "kartoffel",
        "balance_mortage": "kartoffel",
        "value_house": "kartoffel" ,
}


    def load_user(self, layers, side, loading_user):
        #print(loading_user)
        if side == "left":
            # 1
            def check_value(object, newvalue):
                try:
                    if newvalue.lower() not in ["none", 0, None, ""]:
                        object.set(newvalue)
                        object["fg"] = "black"
                    else:
                        if object.winfo_class().lower() in ["entry", "text"]:
                            object["fg"] = "#888888"
                        return False
                except:
                    return False


            check_value(layers[1].existing_customer_left_value, loading_user["existing_customer"])
            check_value(layers[1].honorary_left, loading_user["honorary"])
            check_value(layers[1].title_other_left, loading_user["honorary_other"])
            check_value(layers[1].last_name_left, loading_user["last_name"])
            check_value(layers[1].first_name_left, loading_user["first_names"])
            check_value(layers[1].extra_name_left, loading_user["other_names"])
            check_value(layers[1].date_of_birth_left, loading_user["date_of_birth"])
            check_value(layers[1].employment_status_left, loading_user["employment_status"])
            check_value(layers[1].employment_other_left, loading_user["employment_other"])
            check_value(layers[1].if_unemployed_left, loading_user["unemployed_time"])
            check_value(layers[1].country_of_birth_left, loading_user["country_birth"])
            check_value(layers[1].city_of_birth_left, loading_user["city_birth"])
            check_value(layers[1].additional_nationalities_left, loading_user["nationalities"])
            check_value(layers[1].country_of_residence_left, loading_user["country_residence"])
            check_value(layers[1].tax_resident_left, loading_user["countries_tax_resident"])

            
            check_value(layers[2].taxpayer_identification_number_1_left, loading_user["tin1"])
            check_value(layers[2].taxpayer_identification_number_2_left, loading_user["tin2"])
            check_value(layers[2].taxpayer_identification_number_3_left, loading_user["tin3"])

            # 1.1
            check_value(layers[2].tel_1_left, loading_user["home_number"])
            check_value(layers[2].tel_2_left, loading_user["mobile_number"])
            check_value(layers[2].tel_3_left, loading_user["work_number"])
            check_value(layers[2].emailaddress_left, loading_user["email"])

            # 1.2
            check_value(layers[3].h_address_1_left, loading_user["home_address_1"])
            check_value(layers[3].h_address_2_left, loading_user["home_address_2"])
            check_value(layers[3].h_address_3_left, loading_user["home_address_3"])
            check_value(layers[3].h_address_postcode_left, loading_user["home_address_code"])
            check_value(layers[3].h_address_postcountry_left, loading_user["home_addreess_country"])
            check_value(layers[3].h_address_time_left, loading_user["home_address_time"])

            check_value(layers[3].p_address_1_left, loading_user["previous_address_1"])
            check_value(layers[3].p_address_2_left, loading_user["previous_address_2"])
            check_value(layers[3].p_address_3_left, loading_user["previous_address_3"])
            check_value(layers[3].p_address_postcode_left, loading_user["previous_address_code"])
            check_value(layers[3].p_address_postcountry_left, loading_user["previous_addreess_country"])
            check_value(layers[3].p_address_time_left, loading_user["previous_address_time"])

            check_value(layers[3].c_address_1_left, loading_user["correspondence_address_1"])
            check_value(layers[3].c_address_2_left, loading_user["correspondence_address_2"])
            check_value(layers[3].c_address_3_left, loading_user["correspondence_address_3"])
            check_value(layers[3].c_address_postcode_left, loading_user["correspondence_address_code"])
            check_value(layers[3].c_address_postcountry_left, loading_user["correspondence_addreess_country"])

            # 2
            check_value(layers[3].apply_for_debit_card_value_left, loading_user["apply_debit"])
            check_value(layers[3].customer_on_card_left, loading_user["name_on_card"])
            check_value(layers[3].mother_prev_name_left, loading_user["mother_name"])
            check_value(layers[3].date_of_birth_left, loading_user["card_date_of_birth"])

            # 3
            check_value(layers[4].internet_banking_first_value, loading_user["marketing_internet_banking"])
            check_value(layers[4].email_first_value, loading_user["marketing_email"])
            check_value(layers[4].post_first_value, loading_user["marketing_post"])
            check_value(layers[4].device_messaging_first_value, loading_user["marketing_device_messaging"])
            check_value(layers[4].text_messages_first_value, loading_user["marketing_text_messages"])
            check_value(layers[4].phone_first_value, loading_user["marketing_phone"])

            # 5
            check_value(layers[6].working_status_value_left, loading_user["currently_working"])
            check_value(layers[6].occupation_left, loading_user["occupation"])
            check_value(layers[6].employer_name_left, loading_user["employer_name"])
            check_value(layers[6].employer_address_1_left, loading_user["employer_address_1"])
            check_value(layers[6].employer_address_2_left, loading_user["employer_address_2"])
            check_value(layers[6].employer_address_3_left, loading_user["employer_address_3"])
            check_value(layers[6].employer_postcode_left, loading_user["employer_postcode"])
            check_value(layers[6].current_working_time_left, loading_user["employer_time"])
            check_value(layers[6].previous_working_time_left, loading_user["previous_employment_time"])
            check_value(layers[6].pensionable_value_left, loading_user["employmnet_pensionable"])

            # 6
            check_value(layers[7].salary_checkbox_value_top, loading_user["income_salary"])
            check_value(layers[7].salary_top, loading_user["income_salary_frequency"])
            check_value(layers[7].benefits_checkbox_value_top, loading_user["income_benefits"])
            check_value(layers[7].benefits_top, loading_user["income_benefits_frequency"])
            check_value(layers[7].pension_checkbox_value_top, loading_user["income_pension"])
            check_value(layers[7].pension_top, loading_user["income_pension_frequency"])
            check_value(layers[7].investments_checkbox_value_top, loading_user["income_investments"])
            check_value(layers[7].investments_top, loading_user["income_investments_frequency"])
            check_value(layers[7].other_checkbox_value_top, loading_user["income_other"])
            check_value(layers[7].other_top, loading_user["income_other_frequency"])
            check_value(layers[7].other_explain_top, loading_user["income_other_explanation"])
            check_value(layers[7].total_net_top, loading_user["income_total"])
            check_value(layers[7].salary_type_top, loading_user["income_salary_method"])
            check_value(layers[7].benefits_type_top, loading_user["income_benefits_method"])
            check_value(layers[7].pension_type_top, loading_user["income_pension_method"])
            check_value(layers[7].investment_type_top, loading_user["income_investments_method"])
            check_value(layers[7].other_type_top, loading_user["income_other_method"])
            check_value(layers[7].expected_month_top, loading_user["expected_through_account"])

            # 6.1
            check_value(layers[8].mortage_left, loading_user["mortage"])
            check_value(layers[8].other_loans_left, loading_user["other_loans"])
            check_value(layers[8].lloyd_loans_left, loading_user["lloyd_loans"])
            check_value(layers[8].total_left, loading_user["total_loans"])

            # 7
            check_value(layers[8].type_of_savings_value_left, loading_user["type_savings"])
            check_value(layers[8].total_savings_left, loading_user["total_savings"])

            # 8
            check_value(layers[9].personal_or_business_value_left, loading_user["type_account"])

            # 8.1
            check_value(layers[9].facilities_value_left, loading_user["facilities"])
            check_value(layers[9].banking_time_left, loading_user["banked_time"])
            check_value(layers[9].to_be_closed_value_left, loading_user["account_to_be_closed"])
            check_value(layers[9].to_be_closed_left, loading_user["account_to_be_closed_explanation"])
            check_value(layers[9].transfer_value_left, loading_user["transfer_account"])

            # 8.2 
            check_value(layers[10].hold_credit_card_value_left, loading_user["hold_credit_card"])
            check_value(layers[10].how_many_credit_card_left, loading_user["credit_card_quantity"])
            check_value(layers[10].credit_lloyd_banks_value_left, loading_user["hold_lloyd_credit_card"])
            check_value(layers[10].credit_lloyd_bank_limit_left, loading_user["lloyd_credit_card_limit"])
            check_value(layers[10].other_cards_value_left, loading_user["other_cards"])
            check_value(layers[10].other_cards_left, loading_user["other_cards_specification"])

            # 8.3
            check_value(layers[10].have_mortage_value_left, loading_user["have_mortage"])
            check_value(layers[10].mortage_with_lloyd_value_left, loading_user["mortage_with_lloyd"])
            check_value(layers[10].balance_mortage_left, loading_user["balance_mortage"])
            check_value(layers[10].value_house_left, loading_user["value_house"])

            for i in range(11):
                #layers[i].config(pady=10)
                layers[i].update()

    def save_user(self, layers, side, saving_user):
        if side == "left":

            print(layers[1].existing_customer_left_value.get())

            print(get())
            return
           
            saving_user.private_dict_data["existing_customer"] = str(layers[1].existing_customer_left_value.get())
            saving_user.private_dict_data["honorary"] = layers[1].honorary_left.get()
            saving_user.private_dict_data["honorary_other"] = layers[1].title_other_left.get()
            saving_user.private_dict_data["last_name"] = layers[1].last_name_left.get()
            saving_user.private_dict_data["first_names"] = layers[1].first_name_left.get()
            saving_user.private_dict_data["other_names"] = layers[1].extra_name_left.get()
            saving_user.private_dict_data["date_of_birth"] = layers[1].date_of_birth_left.get()
            saving_user.private_dict_data["employment_status"] = layers[1].employment_status_left.get()
            saving_user.private_dict_data["employment_other"] = layers[1].employment_other_left.get()
            saving_user.private_dict_data["unemployed_time"] = layers[1].if_unemployed_left.get()
            saving_user.private_dict_data["country_birth"] = layers[1].country_of_birth_left.get()
            saving_user.private_dict_data["city_birth"] = layers[1].city_of_birth_left.get()
            saving_user.private_dict_data["nationalities"] = layers[1].additional_nationalities_left.get()
            saving_user.private_dict_data["country_residence"] = layers[1].country_of_residence_left.get()
            saving_user.private_dict_data["countries_tax_resident"] = layers[1].tax_resident_left.get()
            saving_user.private_dict_data["tin1"] = layers[2].taxpayer_identification_number_1_left.get()
            saving_user.private_dict_data["tin2"] = layers[2].taxpayer_identification_number_2_left.get()
            saving_user.private_dict_data["tin3"] = layers[2].taxpayer_identification_number_3_left.get()
            
            saving_user.private_dict_data["home_number"] = layers[2].tel_1_left.get()
            saving_user.private_dict_data["mobile_number"] = layers[2].tel_2_left.get()
            saving_user.private_dict_data["work_number"] = layers[2].tel_3_left.get()
            saving_user.private_dict_data["email"] = layers[2].emailaddress_left.get()
            
            saving_user.private_dict_data["home_address_1"] = layers[3].h_address_1_left.get()
            saving_user.private_dict_data["home_address_2"] = layers[3].h_address_2_left.get()
            saving_user.private_dict_data["home_address_3"] = layers[3].h_address_3_left.get()
            saving_user.private_dict_data["home_address_code"] = layers[3].h_address_postcode_left.get()
            saving_user.private_dict_data["home_addreess_country"] = layers[3].h_address_postcountry_left.get()
            saving_user.private_dict_data["home_address_time"] = layers[3].h_address_time_left.get()
            saving_user.private_dict_data["previous_address_1"] = layers[3].p_address_1_left.get()
            saving_user.private_dict_data["previous_address_2"] = layers[3].p_address_2_left.get()
            saving_user.private_dict_data["previous_address_3"] = layers[3].p_address_3_left.get()
            saving_user.private_dict_data["previous_address_code"] = layers[3].p_address_postcode_left.get()
            saving_user.private_dict_data["previous_addreess_country"] = layers[3].p_address_postcountry_left.get()
            saving_user.private_dict_data["previous_address_time"] = layers[3].p_address_time_left.get()
            saving_user.private_dict_data["correspondence_address_1"] = layers[3].c_address_1_left.get()
            saving_user.private_dict_data["correspondence_address_2"] = layers[3].c_address_2_left.get()
            saving_user.private_dict_data["correspondence_address_3"] = layers[3].c_address_3_left.get()
            saving_user.private_dict_data["correspondence_address_code"] = layers[3].c_address_postcode_left.get()
            saving_user.private_dict_data["correspondence_addreess_country"] = layers[3].c_address_postcountry_left.get()
            
            saving_user.dict_data["apply_debit"] = layers[3].apply_for_debit_card_value_left.get()
            saving_user.dict_data["name_on_card"] = layers[3].customer_on_card_left.get()
            saving_user.dict_data["mother_name"] = layers[3].mother_prev_name_left.get()
            saving_user.dict_data["card_date_of_birth"] = layers[3].date_of_birth_left.get()
            
            saving_user.dict_data["marketing_internet_banking"] = layers[4].internet_banking_first_value.get()
            saving_user.dict_data["marketing_email"] = layers[4].email_first_value.get()
            saving_user.dict_data["marketing_post"] = layers[4].post_first_value.get()
            saving_user.dict_data["marketing_device_messaging"] = layers[4].device_messaging_first_value.get()
            saving_user.dict_data["marketing_text_messages"] = layers[4].text_messages_first_value.get()
            saving_user.dict_data["marketing_phone"] = layers[4].phone_first_value.get()
            
            saving_user.dict_data["currently_working"] = layers[6].working_status_value_left.get()
            saving_user.dict_data["occupation"] = layers[6].occupation_left.get()
            saving_user.dict_data["employer_name"] = layers[6].employer_name_left.get()
            saving_user.dict_data["employer_address_1"] = layers[6].employer_address_1_left.get()
            saving_user.dict_data["employer_address_2"] = layers[6].employer_address_2_left.get()
            saving_user.dict_data["employer_address_3"] = layers[6].employer_address_3_left.get()
            saving_user.dict_data["employer_postcode"] = layers[6].employer_postcode_left.get()
            saving_user.dict_data["employer_time"] = layers[6].current_working_time_left.get()
            saving_user.dict_data["previous_employment_time"] = layers[6].previous_working_time_left.get()
            saving_user.dict_data["employmnet_pensionable"] = layers[6].pensionable_value_left.get()
            
            saving_user.dict_data["income_salary"] = layers[7].salary_checkbox_value_top.get()
            saving_user.dict_data["income_salary_frequency"] = layers[7].salary_top.get()
            saving_user.dict_data["income_benefits"] = layers[7].benefits_checkbox_value_top.get()
            saving_user.dict_data["income_benefits_frequency"] = layers[7].benefits_top.get()
            saving_user.dict_data["income_pension"] = layers[7].pension_checkbox_value_top.get()
            saving_user.dict_data["income_pension_frequency"] = layers[7].pension_top.get()
            saving_user.dict_data["income_investments"] = layers[7].investments_checkbox_value_top.get()
            saving_user.dict_data["income_investments_frequency"] = layers[7].investments_top.get()
            saving_user.dict_data["income_other"] = layers[7].other_checkbox_value_top.get()
            saving_user.dict_data["income_other_frequency"] = layers[7].other_top.get()
            saving_user.dict_data["income_other_explanation"] = layers[7].other_explain_top.get()
            saving_user.dict_data["income_total"] = layers[7].total_net_top.get()
            saving_user.dict_data["income_salary_method"] = layers[7].salary_type_top.get()
            saving_user.dict_data["income_benefits_method"] = layers[7].benefits_type_top.get()
            saving_user.dict_data["income_pension_method"] = layers[7].pension_type_top.get()
            saving_user.dict_data["income_investments_method"] = layers[7].investment_type_top.get()
            saving_user.dict_data["income_other_method"] = layers[7].other_type_top.get()
            saving_user.dict_data["expected_through_account"] = layers[7].expected_month_top.get()
            
            saving_user.dict_data["mortage"] = layers[8].mortage_left.get()
            saving_user.dict_data["other_loans"] = layers[8].other_loans_left.get()
            saving_user.dict_data["lloyd_loans"] = layers[8].lloyd_loans_left.get()
            saving_user.dict_data["total_loans"] = layers[8].total_left.get()
            
            saving_user.dict_data["type_savings"] = layers[8].type_of_savings_value_left.get()
            saving_user.dict_data["total_savings"] = layers[8].total_savings_left.get()
            
            saving_user.dict_data["type_account"] = layers[9].personal_or_business_value_left.get()
            
            saving_user.dict_data["facilities"] = layers[9].facilities_value_left.get()
            saving_user.dict_data["banked_time"] = layers[9].banking_time_left.get()
            saving_user.dict_data["account_to_be_closed"] = layers[9].to_be_closed_value_left.get()
            saving_user.dict_data["account_to_be_closed_explanation"] = layers[9].to_be_closed_left.get()
            saving_user.dict_data["transfer_account"] = layers[9].transfer_value_left.get()
            
            saving_user.dict_data["hold_credit_card"] = layers[10].hold_credit_card_value_left.get()
            saving_user.dict_data["credit_card_quantity"] = layers[10].how_many_credit_card_left.get()
            saving_user.dict_data["hold_lloyd_credit_card"] = layers[10].credit_lloyd_banks_value_left.get()
            saving_user.dict_data["lloyd_credit_card_limit"] = layers[10].credit_lloyd_bank_limit_left.get()
            saving_user.dict_data["other_cards"] = layers[10].other_cards_value_left.get()
            saving_user.dict_data["other_cards_specification"] = layers[10].other_cards_left.get()
            
            saving_user.dict_data["have_mortage"] = layers[10].have_mortage_value_left.get()
            saving_user.dict_data["mortage_with_lloyd"] = layers[10].mortage_with_lloyd_value_left.get()
            saving_user.dict_data["balance_mortage"] = layers[10].balance_mortage_left.get()
            saving_user.dict_data["value_house"] = layers[10].value_house_left.get()            


    def login_button(self, user1, user2, pass1, pass2, origin, wish=1):
        import json
        def encrypt(raw_string:str="Hello,World", password:int=b"4")->str:
            encrypted_string = ""
            for letter in raw_string:
                encrypted_letter = chr(ord(letter)+int(pasword))
                encrypted_string = encrypted_string + encrypted_letter
            return encrypted_string
        def decrypt(coded_string:str, password:int=b"4")->str:
            raw_string = ""
            for letter in raw_string:
                raw_letter = chr(ord(letter)-int(password))
                raw_string = raw_string + raw_letter
            return raw_string


        self.user1_acc = User(user1)
        self.user2_acc = User(user2)

        if wish==1:
            try:
                with open("./users/"+self.user1_acc.user_name+".json", "r") as file:
                    self.user1_acc.user1_content = json.load(file)
                    print("loaded file:", self.user1_acc.user1_content)
            except Exception as e:
                print(e)
            else:
                self.load_user(origin.master.layers, "left", self.user1_acc.user1_content)
                #print("\n\n")
                #print(self.dict_data)

            try:
                with open("./users/"+self.user2_acc.user_name+".json", "r") as file:
                    self.user2_acc.user2_content = json.load(file)
            except FileNotFoundError:
                pass
            else:
                self.load_user(origin.master.layers, "right", self.user1_acc)

        if wish==2:
            print("saving to file: ", self.user1_acc)
    
            # try:
            self.save_user(origin.master, "left", self.user1_acc.dict_data)
            # except Exception as e:
                # print(e)


            #print("saving file with", self.user1_acc.user_name)
            with open("./users/"+self.user1_acc.user_name+".json", "w") as file:
                json.dump(self.user1_acc.dict_data, file, indent=4)

            with open("./users/"+self.user2_acc.user_name+".json", "w") as file:
               json.dump(self.user2_acc.dict_data, file, indent=4)