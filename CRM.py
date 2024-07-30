import sys
import random

class Customer:
    def __init__(self, name, id, ph_no, address):
        self.name = name
        self.id = id
        self.ph_no = ph_no
        self.address = address
        
    def customer_data(self):
        self.name = input("Enter the name of the customer: ")
        self.id = input("Enter the email-id: ")
        self.ph_no = input("Enter the phone number: ")
        self.address = input("Enter the address with city: ")
        print()

    def display_details(self):
        print("Name:", self.name)
        print("Email-id:", self.id)
        print("Phone number:", self.ph_no)
        print("Address:", self.address)
        print()

    def take_review(self, product_name, rating, feedback):
        print(f"Thank you, {self.name}! Your review for {product_name} has been recorded.")
        print(f"Rating: {rating}")
        print(f"Feedback: {feedback}")
        print()

class Review:
    def __init__(self, customer, product, rating, feedback):
        self.customer = customer
        self.product = product
        self.rating = rating
        self.feedback = feedback

class CRMSystem:
    def __init__(self):
        self.reviews = []
        self.customer_ids = {}

    def generate_customer_id(self):
        return str(random.randint(1000, 9999))

    def take_review(self, customer, rating, feedback):
        o2 = Review(customer, "", rating, feedback)  
        self.reviews.append(o2)
        print("Thank you,Your review for product has been recorded.") 
        print()

    def store_customer_id(self, customer):
        customer_id = self.generate_customer_id()
        self.customer_ids[customer_id] = customer
        print(f"Your customer ID is: {customer_id}") 
        print()
        
    def lead_score(self):
        ts = 0
        if not self.reviews:
            print("No reviews available.Be the first customer to provide review!")
            return
        for review in self.reviews:
            score = int(review.rating)
            ts = ts + score
        average_score = ts / len(self.reviews)
        print(f"Lead Score:{average_score}")
        print()
        
    def lead_score1(self, product_name):
        ts = 0
        if not self.reviews:
            print("No reviews available.Be the first customer to provide review!")
            return
        for review in self.reviews:
            score = int(review.rating)
            ts = ts + score
        average_score = ts / len(self.reviews)
        print(f"Lead score for {product_name}: {average_score}")
        print()
        
    def schedule_followup(self, customer_id, date): 
        if customer_id in self.customer_ids:
            global m, n, w
            print(f"Follow-up scheduled for customer {customer_id} on {date}")
            print("How was the product?")
            print("1.Not good 2.Average 3.Good 4.Excellent 5.Outstanding")
            m = int(input("Enter the choice: "))
            print()
            n = input("Is the product worthy? (y/n): ").upper()
            print()
            w = input("Would you want to give any suggestions? ")
            self.generate_lead_score()
            print() 
        else:
            print(f"Customer {customer_id} not found in the CRM system. Cannot schedule follow-up.")
    
    def main():
        customer_id = input("Enter customer ID: ")
        followup_date = input("Enter follow-up date (YYYY-MM-DD): ")
        o1.schedule_followup(customer_id, followup_date)
        print()
        
    def generate_lead_score(self):
        if m in range(1, 6):
            print(f"Lead Score: {m}")
        else:
            print("Invalid rating.")
        print()

def review():
    r = input("Do you want to give a review? y/n: ").upper()
    if r == 'Y':
        i = input("Enter your customer-id: ")
        if i in o1.customer_ids:
            rating = input("Rate the product (1-5): ")
            feedback = input("Provide feedback: ")
            o1.take_review(o1.customer_ids[i], rating, feedback)
            print()
        else:
            print("Invalid customer id!")
            print()
    elif r == 'N':
        print("Thank You!")

o1 = CRMSystem()

while True:
    o = Customer("", "", "", "")
    print("1.Order 2.Review 3.Lead score 4.Schedule_up 5.Exit")
    choice = int(input("Enter the choice: "))
    print()
    if choice == 1:
        ans = input("Do you want to purchase any item? y/n: ")
        print()
        if ans.upper() == 'Y':
            print("The items that are available on our website are:")
            print("1. Mobiles 2. Laptops 3. Digital Watches 4. Airpods 5. Exit")
            ch = int(input("Enter the choice: "))
            print()
            if ch == 1:
                mobiles = {'Samsung': {'Galaxy M51': 25000, 'Galaxy M31': 20000},
                           'iphone': {'iphone 14': 70999, 'iphone 14 pro': 108999, 'iphone 15': 164000},
                           'Oneplus': {'Onplus 9': 28000, 'oneplus 9R': 40000, 'oneplus 9 pro': 69000},
                           'Realme': {'realme 6i': 12999, 'realme narzo': 10999, 'realme C53': 9999},
                           'Poco': {'poco x2': 17000, 'poco x3 pro': 13499, 'poco C3': 7499}
                           }
                for i, j in mobiles.items():
                    print(i, j)
                print()
                s = input("Enter the brand you want to purchase: ")
                if s == 'Samsung':
                    print("1.Galaxy M51:25000 2.Galaxy M31:20000")
                    ch1 = int(input("Enter the choice: "))
                    if ch1 == 1:
                        j = input("Do you want to check the score for the product? y/n: ").upper()
                        if j == 'Y':
                            o1.lead_score()
                            k = input("Do you want continue ordering? y/n: ").upper()
                            if k == 'Y':
                                print("Enter your details: ")
                                o.customer_data()
                                o.display_details() 
                                print("Your product Galaxy M51 of cost 25000 has been successfully ordered!")
                                o1.store_customer_id(o)
                                print()
                            else:
                                print("Thank You!")
                                print()
                        elif j == 'N':   
                            print("Enter your details: ")
                            o.customer_data()
                            o.display_details() 
                            print("Your product Galaxy M51 of cost 25000 has been successfully ordered!")
                            o1.store_customer_id(o)
                            print()         
                    elif ch1 == 2:
                        j = input("Do you want to check the score for the product? y/n: ").upper()
                        if j == 'Y':
                            o1.lead_score()
                            k = input("Do you want continue ordering? y/n: ").upper()
                            if k == 'Y':
                                print("Enter your details: ")
                                o.customer_data()
                                o.display_details() 
                                print("Your product Galaxy M31 of cost 20000 has been successfully ordered!")
                                o1.store_customer_id(o)
                                print()
                            else:
                                print("Thank You!")
                                print()
                        elif j == 'N':   
                            print("Enter your details: ")
                            o.customer_data()
                            o.display_details() 
                            print("Your product Galaxy M31 of cost 20000 has been successfully ordered!")
                            o1.store_customer_id(o)
                            print()
                elif s == 'iphone':
                    print("1.iphone 14:70999,2.iphone 14 pro:108999,3.iphone 15:164000")
                    ch2 = int(input("Enter your choice: "))
                    if ch2 == 1:
                        j = input("Do you want to check the score for the product? y/n: ").upper()
                        if j == 'Y':
                            o1.lead_score()
                            k = input("Do you want continue ordering? y/n: ").upper()
                            if k == 'Y':
                                print("Enter your details: ")
                                o.customer_data()
                                o.display_details() 
                                print("Your product iphone 14 of cost 70999 has been successfully ordered!")
                                o1.store_customer_id(o)
                            else:
                                print("Thank You!")
                        elif j == 'N':   
                            print("Enter your details: ")
                            o.customer_data()
                            o.display_details() 
                            print("Your product iphone 14 of cost 70999 has been successfully ordered!")
                            o1.store_customer_id(o)       
                    elif ch2 == 2:
                        j = input("Do you want to check the score for the product? y/n: ").upper()
                        if j == 'Y':
                            o1.lead_score()
                            k = input("Do you want continue ordering? y/n: ").upper()
                            if k == 'Y':
                                print("Enter your details: ")
                                o.customer_data()
                                o.display_details() 
                                print("Your product iphone 14 pro of cost 108999 has been successfully ordered!")
                                o1.store_customer_id(customer='')
                            else:
                                        print("Thank You!")
                        elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product iphone 14 pro of cost 108999 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                    elif ch2==3:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product iphone 15 of cost 164000 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product iphone 15 of cost 164000 has been successfully ordered!")
                                    o1.store_customer_id(customer='')           
                elif s=='Oneplus' or 'Oneplus'==s.upper():
                            print("1.Oneplus 9:28000 2.Oneplus 9R:40000 3.Oneplus 9pro:69000")
                            ch3=int(input("enter your choice:"))
                            if ch3==1:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Oneplus 9 of cost 28000 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Oneplus 9 of cost 28000 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                            elif ch3==2:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Oneplus 9R of cost 40000 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Oneplus 9R of cost 40000 has been successfully ordered!")
                                    o1.store_customer_id(customer='')   
                            elif ch3==3:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Oneplus 9 Pro of cost 69000 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Oneplus 9 Pro of cost 69000 has been successfully ordered!")
                                    o1.store_customer_id(customer='')       
                elif s=='Realme' or 'Realme'==s.upper():
                            print("1.Realme 6i:12999 2.Realme Narzo:10999 3.Realme C53:74999")
                            ch4=int(input("enter your choice:"))
                            if ch4==1:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Realme 6i of cost 12999 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Realme 6i of cost 12999 has been successfully ordered!")
                                    o1.store_customer_id(customer='')  
                            elif ch4==2:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Realme Narzo of cost 10999 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Realme Narzo of cost 10999 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                            elif ch4==3:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Realme C53 of cost 9999 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Realme C53 of cost 9999 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                elif s=='Poco' or 'Poco'==s.upper():
                            print("1.Poco x2:17000 2.Poco x3 Pro:13499 3.Poco c3:7499")
                            ch5=int(input("enter your choice:"))
                            if ch5==1:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Poco x2 of cost 17000 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Poco x2 of cost 17000 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                            elif ch5==2:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Poco x3 of cost 13499 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Poco x3 of cost 13499 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                            elif ch5==3:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Poco c3 of cost 7499 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Poco c3 of cost 7499 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
            elif ch == 2:
                laptops = {'Lenovo': 22000, 'hp': 36000, 'Asus': 30700, 'Dell': 36300}

                for i,j in laptops.items():
                    print(f"{i}\t{j}")
                
                c = input("Enter the brand you want to purchase: ")
                
                if c == 'Lenovo':
                        j=input("Do u want to check the score for the product? y/n: ").upper()
                        if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Lenovo of cost 22000 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                        elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Lenovo of cost 22000 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                elif c=='hp':
                        j=input("Do u want to check the score for the product? y/n: ").upper()
                        if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product hp of cost 36000 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                        elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product hp of cost 36000 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                        
                elif c=='Asus':
                        j=input("Do u want to check the score for the product? y/n: ").upper()
                        if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Asus of cost 30700 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                        elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Asus of cost 30700 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                        
                elif c=='Dell':
                        j=input("Do u want to check the score for the product? y/n: ").upper()
                        if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Dell of cost 36300 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                        elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Dell of cost 36300 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                        
            elif ch == 3:
                digital_watches = {'Boat': {'Boat Wave': 1499, 'Boat Storm Call': 1600, 'Boat Utlima Call': 1299},
                                'Noise': {'Noise Color Fit': 3999, 'Noise Color Fit Icon plus': 1299},
                                'Fire Boltt': {'Fire Boltt Epic': 999, 'Fire Boltt Ultimate': 1799}}

                for i,j in digital_watches.items():
                    print(i,j)

                s1 = input("Enter the brand you want to purchase: ")

                if s1 == 'Boat':
                    print("1.Boat Wave:1499 2.Boat Storm Call:1600 3.Boat Utlima Call:1299")
                    c2=int(input("Enter the choice: "))
                    if c2==1:
                            j=input("Do u want to check the score for the product? y/n: ").upper()
                            if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Boat Wave of cost 1499 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                            elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Boat Wave of cost 1499 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                    elif c2==2:
                            j=input("Do u want to check the score for the product? y/n: ").upper()
                            if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Boat Storm Call of cost 1600 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                            elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Boat Storm Call of cost 1600 has been successfully ordered!")
                                    o1.store_customer_id(customer='')                           
                    elif c2==3:
                            j=input("Do u want to check the score for the product? y/n: ").upper()
                            if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Boat Ultima Call of cost 1299 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                            elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Boat Ultima Call of cost 1299 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                elif s1=='Noise' or 'Noise'==s1.upper():
                            print("1.Noise Color Fit:3999 2.Noise Color Fit Icon plus:1299")
                            c3=int(input("enter your choice:"))
                            if c3==1:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Noise Color Fit of cost 3999 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Noise Color Fit of cost 3999 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                                
                            elif c3==2:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Noise Color Fit Icon Plus of cost 1299 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Noise Color Fit Icon Plus of cost 1299 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                                
                elif s1=='Fire Boltt' or 'Fire Boltt'==s1.upper():
                            print("1.Fire Boltt Epic:999 2.Fire Boltt Ultimate:1799")
                            c4=int(input("enter your choice:"))
                            if c4==1:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Fire Boltt Epic of cost 999 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Fir Boltt Epic of cost 999 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                            elif c4==2:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Fire Boltt Ultimate of cost 1799 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Fire Boltt Ultimate of cost 1799 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
            elif ch == 4:
                airpods = {'Boat': {'Boat Airpods 131': 999, 'Boat Airpods 148': 1199},
                        'Realme': {'realme Buds Air 5': 3699, 'realme Buds 3 Neo': 1999},
                        'Oneplus': {'Oneplus Nord Buds 2': 2999, 'Oneplus Nord Buds 2r': 2199}
                        }
                for i,j in airpods.items():
                    print(i,j)
                s2 = input("Enter the brand you want to purchase: ").capitalize()
                if s2 == 'Boat':
                    print("1.Boat Airpods 131:999 2.Boat Airpods 148:1199")
                    c3=int(input("Enter the choice: "))
                    if c3==1:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Boat Airpods 131 of cost 999 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Boat Airpods 131 of cost 999 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                                
                    elif c3==2:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Boat Airpods 148 of cost 1199 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Boat Airpods 148 of cost 1199 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                elif s2=='Realme' or 'Realme'==s2.upper():
                            print("1.realme Buds 131:999 2.realme Buds 3 Neo:1199")
                            c3=int(input("enter your choice:"))
                            if c3==1:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Realme Buds Air 5 of cost 3699 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Realme Buds Air 5 of cost 3699 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                            elif c3==2:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Realme Buds 3 Neo of cost 1999 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Realme Buds 3 Neo of cost 1999 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                elif s2=='Oneplus' or 'Oneplus'==s2.upper():
                            print("1.Oneplus Nord Buds:2999 2.Oneplus Nord Buds 2r:2199")
                            c3=int(input("enter your choice:"))
                            if c3==1:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Oneplus Nord Buds 2 of cost 2999 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Oneplus Nord Buds 2 of cost 2999 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
                            elif c3==2:
                                j=input("Do u want to check the score for the product? y/n: ").upper()
                                if j=='Y':
                                    o1.lead_score()
                                    k=input("Do u want continue ordering? y/n: ").upper()
                                    if k=='Y':
                                        print("Enter your details: ")
                                        o.customer_data()
                                        o.display_details() 
                                        print("Your product Oneplus Nord Buds 2r of cost 2199 has been successfully ordered!")
                                        o1.store_customer_id(customer='')
                                    else:
                                        print("Thank You!")
                                elif j=='N':   
                                    print("Enter your details: ")
                                    o.customer_data()
                                    o.display_details() 
                                    print("Your product Oneplus Nord Buds 2r of cost 2199 has been successfully ordered!")
                                    o1.store_customer_id(customer='')
        elif ans.upper() == 'N':
            print("Terminated Successfully")
            sys.exit(0)
    elif choice == 2:
        review()   
    elif choice == 3:
        product_name = input("Enter the product name for lead scoring: ")
        o1.lead_score1(product_name)
    elif choice == 4:
       CRMSystem.main()
    elif choice == 5:
        sys.exit(0)
    else:
        print("Invalid choice")
