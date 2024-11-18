import csv

def register():
    with open("database.csv", mode ="a", newline ="") as f:
        writer = csv.writer(f, delimiter = ",")
        print ("Please enter the following information")
        fname = input ("First Name: ")
        lname = input ("Last Name: ")
        street = input ("Street Address: ")
        city=input("City: ")
        postalcode=input("Postal Code: ")
        phone=input ("Phone: ")
        emailaddress = input("Email: ")
        password = input("Password: ")
        secondpassword = input("Reenter Password: ")
        if password == secondpassword:
            writer.writerow([fname, lname, street, city, postalcode,
                             phone, emailaddress, password])
            print ("Registration complete! Thank you")
        else:
            print("Passwords do not match. Please try again")

def login():
    print("Login Page")
    email = input("Email: ")
    password = input("Password: ")
    with open("database.csv", mode = "r") as f:
        readlines = csv.reader(f, delimiter = ",")
        for row in readlines:
            if row[6]==emailaddress and row[7]==password:
                print("Login successful")
    print("Login unsuccessful, please try again")

def main():
    logged_in = False
    interested=True
    while interested == True:
        if logged_in == False:
            ans = input("Would you like to [A] login, [B]register, [C]quit? ")
            if ans == 'a' or ans== 'A' or ans=='[A]':
                login()
            elif ans == 'B' or ans== 'b' or ans=='[B]':
                register()
            elif ans == 'c' or ans== 'c' or ans=='[C]':
                interested = False
                print ("You are now logged out")
            else:
                print("Wrong input, please try again from our choices A, B, or C")

main()
            
                
