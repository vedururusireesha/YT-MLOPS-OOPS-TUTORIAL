class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.menu()
    def menu(self):
        user_input=input("""welcome to chatbook!! how would u like to proceed
                         1. press 1 to signup
                         2. press 2 to signin
                         3. press 3 to write a post
                         4. press aby other key to exit""")
        if user_input=="1":
            self.signup()
        if user_input=="2":
            self.signin()
        if user_input=="3":
            self.my_post()
        if user_input=="4":
            self.sendmsg()
        else:
            exit()
    def signup(self):
        email=input("enter ur email")
        pwd=input("enter ur pwd")
        self.username=email
        self.password=pwd
        print("u have signed in successfully")
        print("\n")
        self.menu()
    def signin(self):
        if self.username=='' and self.password=='':
            print("please signup first by pressing 1 in the main menu")
        else:
            uname=input("enter username")
            pwd=input("enter password")
            if self.username==uname and self.password==pwd:
                print("signin successful")
                self.loggedin=True
            else:
                print("pls enter correct credentials")
                print("\n")
                self.menu()
    def my_post(self):
        if self.loggedin==True:
            txt=input("enter ur message")
            print("following content has been posted {txt}")
        else:
            print("you need to signin first to post something")
            print("\n")
            self.menu()
    def sendmsg(self):
        if self.loggedin==True:
            txt=input("enter ur message")
            frnd=input("whom to send the message")
            print(f"your message has been sent to ur {frnd}")
        else:
            print("you need to signin first to post something")
            print("\n")
            self.menu()


user1=chatbook()
        