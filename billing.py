from tkinter import *


class BillingApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Billing Software')
        self.root.geometry('560x400')
        self.root.state('zoomed')
        # self.root.iconbitmap('./icon.ico')

        headerTitle = Label(self.root, text="Retail Billing System", bg="purple", fg="white", font=('arial', 18, 'bold'), pady=10, bd=7, relief=GROOVE)
        headerTitle.place(x=0, y=0, relwidth=1,)
        # ==================
        Cframe = LabelFrame(self.root, text="Customer Information", font=('arial', 10, 'bold'), fg="gold", bd=5, bg="purple")
        Cframe.place(x=0, y=65, relwidth=1)
        # ==========
        CNameLbl = Label(Cframe, text="Customar Name:", font=('arial', 12), bg='white')
        CNameLbl.grid(row=0, column=0, padx=10, pady=5)
        CNameEntry = Entry(Cframe, width=20, font=('arial', 10), bd=5, relief=SUNKEN)
        CNameEntry.grid(row=0, column=1)
        # 
        CPhoneLbl = Label(Cframe, text="Customar Phone:", font=('arial', 12), bg='white')
        CPhoneLbl.grid(row=0, column=2, padx=10, pady=5)
        CPhoneEntry = Entry(Cframe, width=20, font=('arial', 10), bd=5, relief=SUNKEN)
        CPhoneEntry.grid(row=0, column=3)
        # 
        CBillLbl = Label(Cframe, text="Bill Number:", font=('arial', 12), bg='white')
        CBillLbl.grid(row=0, column=4, padx=10, pady=5)
        CBillEntry = Entry(Cframe, width=20, font=('arial', 10), bd=5, relief=SUNKEN)
        CBillEntry.grid(row=0, column=5)
        # 
        BillSearchBtn = Button(Cframe, text="Search Bill", font=('arial', 12, 'bold'), bg="skyblue", fg='#222222')
        BillSearchBtn.grid(row=0, column=6, padx=10, pady=5)
        # 
        ProFrame = LabelFrame(self.root, text="Product Section", bd=7, relief=GROOVE, bg="purple", font=('arial', 10, 'bold'), fg='gold')
        ProFrame.place(x=0, y=135, width=888, height=458)

        self.productList = [
            "--Select One--",
            "Rice",
            "Oil",
            "Juice",
            "Biscuit",
            "Hair Get",
            "Face wach",
            "Mustard oil"
        ]
        self.product1 = StringVar()
        self.product1.set(self.productList[0])
        
        self.product2 = StringVar()
        self.product2.set(self.productList[0])
        
        self.product3 = StringVar()
        self.product3.set(self.productList[0])
        
        self.product4 = StringVar()
        self.product4.set(self.productList[0])
        
        self.product5 = StringVar()
        self.product5.set(self.productList[0])
        
        self.product6 = StringVar()
        self.product6.set(self.productList[0])
        
        self.product7 = StringVar()
        self.product7.set(self.productList[0])
        
        self.product8 = StringVar()
        self.product8.set(self.productList[0])

        pro1 = OptionMenu(ProFrame,self.product1, *self.productList)
        pro1.grid(row=0, column=0, pady=10, padx=10, sticky='w')
        pro1.config(width=12)
        pro1Entry = Entry(ProFrame, width=15, font=('arial', 10, 'bold'), bd=5, relief=SUNKEN)
        pro1Entry.grid(row=0, column=1, pady=10, padx=10)

        pro2 = OptionMenu(ProFrame,self.product2, *self.productList)
        pro2.grid(row=1, column=0, pady=10, padx=10, sticky='w')
        pro2.config(width=12)
        pro2Entry = Entry(ProFrame, width=15, font=('arial', 10, 'bold'), bd=5, relief=SUNKEN)
        pro2Entry.grid(row=1, column=1, pady=10, padx=10)

        pro3 = OptionMenu(ProFrame,self.product3, *self.productList)
        pro3.grid(row=2, column=0, pady=10, padx=10, sticky='w')
        pro3.config(width=12)
        pro3Entry = Entry(ProFrame, width=15, font=('arial', 10, 'bold'), bd=5, relief=SUNKEN)
        pro3Entry.grid(row=2, column=1, pady=10, padx=10)

        pro4 = OptionMenu(ProFrame,self.product4, *self.productList)
        pro4.grid(row=3, column=0, pady=10, padx=10, sticky='w')
        pro4.config(width=12)
        pro4Entry = Entry(ProFrame, width=15, font=('arial', 10, 'bold'), bd=5, relief=SUNKEN)
        pro4Entry.grid(row=3, column=1, pady=10, padx=10)

        pro5 = OptionMenu(ProFrame,self.product5, *self.productList)
        pro5.grid(row=4, column=0, pady=10, padx=10, sticky='w')
        pro5.config(width=12)
        pro5Entry = Entry(ProFrame, width=15, font=('arial', 10, 'bold'), bd=5, relief=SUNKEN)
        pro5Entry.grid(row=4, column=1, pady=10, padx=10)

        pro6 = OptionMenu(ProFrame,self.product6, *self.productList)
        pro6.grid(row=5, column=0, pady=10, padx=10, sticky='w')
        pro6.config(width=12)
        pro6Entry = Entry(ProFrame, width=15, font=('arial', 10, 'bold'), bd=5, relief=SUNKEN)
        pro6Entry.grid(row=5, column=1, pady=10, padx=10)

        pro7 = OptionMenu(ProFrame,self.product7, *self.productList)
        pro7.grid(row=6, column=0, pady=10, padx=10, sticky='w')
        pro7.config(width=12)
        pro7Entry = Entry(ProFrame, width=15, font=('arial', 10, 'bold'), bd=5, relief=SUNKEN)
        pro7Entry.grid(row=6, column=1, pady=10, padx=10)

        pro8 = OptionMenu(ProFrame,self.product8, *self.productList)
        pro8.grid(row=7, column=0, pady=10, padx=10, sticky='w')
        pro8.config(width=12)
        pro8Entry = Entry(ProFrame, width=15, font=('arial', 10, 'bold'), bd=5, relief=SUNKEN)
        pro8Entry.grid(row=7, column=1, pady=10, padx=10)
        # 
        BillFrame = Frame(self.root, bd=7, relief=GROOVE)
        BillFrame.place(x=890, y=135, width=645, height=458)
        # 
        CustomarFrame = LabelFrame(self.root, text="Customar Area", bd=7, relief=GROOVE, bg="purple", font=('arial', 10, 'bold'), fg='gold')
        CustomarFrame.place(x=0, y=595, relwidth=1, relheight=1)

        totalLabel = Label(CustomarFrame, text="Total Bill", font=('arial', 10, "bold"), bg='purple', fg="white")
        totalLabel.grid(row=0, column=0, pady=5, padx=5)
        totalBillEntry = Entry(CustomarFrame, width=10, bd=5, relief=SUNKEN)
        totalBillEntry.grid(row=0, column=1)

        discountLabel = Label(CustomarFrame, text="Discount", font=('arial', 10, "bold"), bg='purple', fg="white")
        discountLabel.grid(row=1, column=0, pady=5, padx=5)
        discountBillEntry = Entry(CustomarFrame, width=10, bd=5, relief=SUNKEN)
        discountBillEntry.grid(row=1, column=1)

        netTotalLabel = Label(CustomarFrame, text="Net Total", font=('arial', 10, "bold"), bg='purple', fg="white")
        netTotalLabel.grid(row=0, column=2, pady=5, padx=5)
        netTotalEntry = Entry(CustomarFrame, width=10, bd=5, relief=SUNKEN)
        netTotalEntry.grid(row=0, column=3)

        CPayLabel = Label(CustomarFrame, text="Customar Pay", font=('arial', 10, "bold"), bg='purple', fg="white")
        CPayLabel.grid(row=1, column=2, pady=5, padx=5)
        CPayEntry = Entry(CustomarFrame, width=10, bd=5, relief=SUNKEN)
        CPayEntry.grid(row=1, column=3)

        CReturnLabel = Label(CustomarFrame, text="Customar Return", font=('arial', 10, "bold"), bg='purple', fg="white")
        CReturnLabel.grid(row=0, column=4, pady=5, padx=5)
        CReturnEntry = Entry(CustomarFrame, width=10, bd=5, relief=SUNKEN)
        CReturnEntry.grid(row=0, column=5)

        # 
        
        BtnFrame=Frame(CustomarFrame, bd=7, relief=GROOVE)
        BtnFrame.place(x=530, y=0, width=980, height=60)
        # 
        TotalCountBtn = Button(BtnFrame, text="Total", bg='skyblue', pady=5, padx=15)
        TotalCountBtn.grid(row=0, column=0, pady=5) 

        GenerateBillBtn = Button(BtnFrame, text="Generate Bill", bg='skyblue', pady=5, padx=15)
        GenerateBillBtn.grid(row=0, column=1, pady=5, padx=5) 

        ClearBtn = Button(BtnFrame, text="Clear", bg='skyblue', pady=5, padx=15)
        ClearBtn.grid(row=0, column=2, pady=5, padx=5) 

        PrintBtn = Button(BtnFrame, text="Print", bg='skyblue', pady=5, padx=15)
        PrintBtn.grid(row=0, column=3, pady=5, padx=5) 

        ExitBtn = Button(BtnFrame, text="Exit", bg='skyblue', pady=5, padx=15)
        ExitBtn.grid(row=0, column=4, pady=5, padx=5) 





root = Tk()
Obj = BillingApp(root)
root.mainloop()
