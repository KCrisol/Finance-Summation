import turtle

#global variable
fswn = turtle.Screen()
global Name

#Financial Summation
def main():
    global Name
    #set window
    fswn.setup(width = 800,height = 400)
    fswn.title("Financial Summation")
    fswn.bgcolor("black")
    txt = turtle.Turtle()
    txt.color("white")
    Name = fswn.textinput("INTRO","What is your name?")
    txt.write("{}, Welcome to the Finance Program.\n\n".format(Name), align = "center", font = ("BookmanOldStyle",22))
    txt.write("Welcome!\n\n\n", align = "left", font = ("TimesNewRoman",25))
    txt.write("\nThe following is to approximate your financial earnings!\n", align = "center", font = ("TimesNewRoman",18))
    prompt = Type()
    Pay_Freq = Frequency(prompt)
    if prompt in ['H','h']:
        FinanceMenu(Pay_Freq)
    elif prompt in ['S','s']:
        AnnHrs = salHrs(Pay_Freq)
        AnnWks = salWks(Pay_Freq)
        salresult = salCalc(prompt,Pay_Freq,AnnHrs,AnnWks)

    again = fswn.textinput("BYE","Would you like to try again? (y/n)")
    if again in ['Y','y']:
        fswn.clear()
        return main()
    elif again in ['N','n']:
        fswn.clear()

def FinanceMenu(Pay_Freq):
    if Pay_Freq in ['WEEKLY','Weekly','weekly','wkly','w','W']:
        WklyWage = Wkly(Pay_Freq)
        Hrs = Hours(Pay_Freq)
        Tax = Search(Pay_Freq)
        wkresult = wkCalc(Pay_Freq,WklyWage,Hrs,Tax)
    elif Pay_Freq in ['BI-WEEKLY','Bi-Weekly','biweekly','biwkly','biw','bi-w']:
        BiWklyWage = BiWkly(Pay_Freq)
        Hrs = Hours(Pay_Freq)
        Tax = Search(Pay_Freq)
        biwkresult = biwkCalc(Pay_Freq,BiWklyWage,Hrs,Tax)
    elif Pay_Freq in ['MONTHLY','Monthly','monthly','mon','m']:
        MonthlyWage = Monthly(Pay_Freq)
        Hrs = Hours(Pay_Freq)
        Tax = Search(Pay_Freq)
        monresult = monCalc(Pay_Freq,MonthlyWage,Hrs,Tax)

#Getting user input for hourly or salary
def Type():
    prompt = fswn.textinput('Let us begin..',"Do you plan to be Hourly or Salary? (h/s)")
    if prompt in ['H','h','S','s']:
        return prompt
    else:
        return Type()

#Getting user hourly or salary pay
def Frequency(prompt):
    fswn.clear()
    fswn.setup(width = 450,height = 150)
    txt = turtle.Turtle()
    txt.color("black")
    Options = ['WEEKLY','Weekly','weekly','wkly','w','W',
               'BI-WEEKLY','Bi-Weekly','bi-weekly','Bi-Weekly','biwkly','biw','bi-w',
               'MONTHLY','Monthly','monthly','mon','m']
    while True:
        if prompt == 'H' or prompt == 'h':        
            txt.write("'Weekly', 'Bi-Weekly', 'Monthly'", align = "center", font = ("Arial",22))
            Pay_Freq = fswn.textinput('Question 2',"How often are you likely to be paid?")
            if Pay_Freq in Options:
                return Pay_Freq
        elif prompt == 'S' or prompt == 's':
            while True:
                fswn.clear()
                fswn.setup(width = 400,height = 200)
                fswn.bgcolor("grey")
                newText = turtle.Turtle()
                newText.color("white")
                try:
                    Pay_Freq = float(fswn.textinput('Question 2',"What is your annual wage? $"))
                    #if Pay_Freq > 0 and Pay_Freq < 50000000 or Pay_Freq < 0:
                        #newText.write("sorry, try again", align = "center", font = ("Arial",12))
                    if Pay_Freq > 0 and Pay_Freq < 40000:
                        newText.write("Nice, could do better.", align = "center", font = ("Arial",15))
                        break
                    elif Pay_Freq > 40000 and Pay_Freq < 80000:
                        newText.write("That's not bad at all.", align = "center", font = ("Arial",15))                        
                        break
                    elif Pay_Freq > 80000 and Pay_Freq < 100000:
                        newText.write("You're a good working American.", align = "center", font = ("Arial",15))
                        break
                    elif Pay_Freq > 100000 and Pay_Freq < 1000000:
                        newText.write("Okay, you're at that level", align = "center", font = ("Arial",15))
                        break
                except ValueError:
                    newText.write("sorry, try again", align = "center", font = ("Arial",12))
                    return Frequency(prompt)
                break
            return Pay_Freq

#Getting user salary hours
def salHrs(Pay_Freq):
    while True:
        try:
            AnnHrs = float(fswn.textinput('Question 3',"How many predicted hours will you work per week?"))
            if AnnHrs < 0:
                print("Sorry, must be positive hours.")
                continue
            break
        except ValueError:
            print("Wrong input.")
    return AnnHrs

#Getting salary work weeks
def salWks(Pay_Freq):
    txt = turtle.Turtle()
    fswn.setup(width = 400,height = 200)
    while True:
        try:
            fswn.clear()
            AnnWks = float(fswn.textinput('Question 4',"How many weeks will you work in the year?"))
            if AnnWks < 0:
                print("Sorry, must be actual weeks.")
                continue
            break
        except ValueError:
            print("Wrong input")
    return AnnWks

def Wkly(Pay_Freq):
    if Pay_Freq in ['WEEKLY','Weekly','weekly','wkly','w','W']:
        while True:
            try:
                fswn.clear()
                WklyWage = float(fswn.textinput('Question 3',"What is your hourly wage? $"))
                if WklyWage < 0 or WklyWage > 200:
                    print("Wrong input")
                    continue
                break
            except ValueError:
                print("Wrong input")
        return WklyWage

def BiWkly(Pay_Freq):
    if Pay_Freq in ['BI-WEEKLY','Bi-Weekly','biweekly','biwkly','biw','bi-w']:
        while True:
            try:
                fswn.clear()
                BiWklyWage = float(fswn.textinput('Question 3',"What is your hourly wage? $"))
                if BiWklyWage < 0 or BiWklyWage > 200:
                    print("Wrong input")
                    continue
                break
            except ValueError:
                print("Wrong input")
        return BiWklyWage

def Monthly(Pay_Freq):
    if Pay_Freq in ['MONTHLY','Monthly','monthly','mon','m']:
        while True:
            try:
                fswn.clear()
                MonthlyWage = float(fswn.textinput('Question 4',"What is your hourly wage? $"))
                if MonthlyWage < 0 or MonthlyWage > 200:
                    print("Wrong input")
                    continue
                break
            except ValueError:
                print("Wrong input")
        return MonthlyWage

def Hours(Wage_Freq):
    while True:
        try:
            Hrs = float(fswn.textinput('Question 4',"How many predicted hours will you work weekly?"))
            if Hrs < 0:
                print("Wrong input")
                continue
            break
        except ValueError:
            print("Wrong input")
    return Hrs
    
def Search(Pay_Frequency):
    States = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado',
              'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
              'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
              'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
              'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada',
              'New Hampshire', 'New Jersey', 'New Mexico', 'New York',
              'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
              'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota',
              'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Washington',
              'West Virginia', 'Wisconsin', 'Wyoming']

    IncomeTaxes = ['2%-5%','No Income Tax','2.59%-4.54%','0.9%-6.9%','1%-13.3%','4.63%',
                   '3%-6.99%','2.2%-6.6%','No Income Tax','1%-6%','1.4%-8.25%','1.6%-7.4%',
                   '3.75%','3.3%','0.36%-8.98%','2.9%-5.2%','2%-6%','2%-6%','5.8%-7.15%',
                   '2%-5.75%','5.1%','4.25%','5.35%-9.85%','3%-5%','1.5%-6%','1%-6.9%',
                   '2.46%-6.84%','No Income Tax','5%','1.4%-8.97%','1.7%-4.9%','4%-8.82%',
                   '5.75%','1.1%-2.9%','0.5%-5%','0.5%-5%','5%-9.9%','3.07%','3.75%-5.99%',
                   '0%-7%','No Income Tax','5%','No Income Tax','5%','3.55%-8.95%','2%-5.75%',
                   'No Income Tax','3%-6.5%','4%-7.65%','No Income Tax']
    
    Abbr = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI',
            'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI',
            'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC',
            'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
            'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
    state = fswn.textinput('State Search',"What state are you from?\n"
                                          "(Please provide full state name or abbr.)")
    state.upper()

    for x in range(50):
        if States[x].upper() == state.upper() or Abbr[x] == state.upper(): #Next time do .lower or .upper for Search of state
            printres = turtle.Turtle()
            printres.color("black")
            #print("test")
            printres.write(States[x] + " income tax:" + IncomeTaxes[x], align = "center", font = ("TimesNewRoman",15))
            #print(States[x], "tax is:", Taxes[x])
    while True:
        try:
            Tax = float(fswn.textinput('Tax Search',"What is your State income tax percent?\n"
                                                  "(Please provide decimal notation)"))
            if Tax < 0:
                print("Wrong input")
                continue
            break
        except ValueError:
            print("Wrong input")
    return Tax

def wkCalc(Pay_Freq,WklyWage,Hrs,Tax):
    global Name
    wkresult = turtle.Turtle()
    wkresult.color("gold")
    if Pay_Freq in ['WEEKLY','Weekly','weekly','wkly','w','W']:
        fswn.clear()
        fswn.setup(width = 600,height = 250)
        WklyWage = (WklyWage * Hrs)
        WklyWagee = round(WklyWage,2)
        WklyTax = WklyWagee - (WklyWagee * (Tax + 0.12)) #12% is the single tax bracket income over $9700, under $39,475
        WklyTaxx = round(WklyTax,2)
        wkresult.write(("{}, you would be making: $" + str(WklyWagee) + "\nApproximately $" + str(WklyTaxx) + "\nafter federal and state income taxes.").format(Name), align = "center", font = ("TimesNewRoman",20))
    return wkresult

def biwkCalc(Pay_Freq,BiWklyWage,Hrs,Tax):
    global Name
    biwkresult = turtle.Turtle()
    biwkresult.color("gold")
    if Pay_Freq in ['BI-WEEKLY','Bi-Weekly','biweekly','biwkly','biw','bi-w']:
        fswn.clear()
        fswn.setup(width = 600,height = 300)
        fswn.bgcolor("black")
        BiWklyWage = (BiWklyWage * Hrs) * 2
        BiWklyWagee = round(BiWklyWage,2)
        BiWklyTax = BiWklyWagee - (BiWklyWagee * (Tax + 0.12)) #12% is the single tax bracket income over $9700, under $39,475
        BiWklyTaxx = round(BiWklyTax,2)
        biwkresult.write(("{}, you would be making: $" + str(BiWklyWagee) +"\nevery two weeks." + "\nApproximately $" + str(BiWklyTaxx) + "\nafter federal and state income taxes.").format(Name), align = "center", font = ("TimesNewRoman",20))
    return biwkresult

def monCalc(Pay_Freq,MonthlyWage,Hrs,Tax):
    global Name
    monresult = turtle.Turtle()
    monresult.color("gold")
    if Pay_Freq in ['MONTHLY','Monthly','monthly','mon','m']:
        fswn.clear()
        fswn.setup(width = 600,height = 300)
        fswn.bgcolor("black")
        MonthlyWage = (MonthlyWage * Hrs) * 4
        MonthlyWagee = round(MonthlyWage,2)
        MonthlyTax = MonthlyWagee - (MonthlyWagee * (Tax + 0.12)) #12% is the single tax bracket income over $9700, under $39,475
        MonthlyTaxx = round(MonthlyTax,2)
        monresult.write(("{}, you would be making: $" + str(MonthlyWagee) +"\nevery monthly." + "\nApproximately $" + str(MonthlyTaxx) + "\nafter federal and state income taxes.").format(Name), align = "center", font = ("TimesNewRoman",20))
    return monresult

def salCalc(prompt,Pay_Freq,AnnHrs,AnnWks):
    global Name
    salresult = turtle.Turtle()
    salresult.color("gold")
    if prompt in ['SALARY','Salary','SAL','Sal','S','s']:
        fswn.clear()
        fswn.setup(width = 750,height = 300)
        fswn.bgcolor("black")
        SalWage = (Pay_Freq / (AnnHrs * AnnWks))
        SalWagee = round(SalWage,2)
        salresult.write(("{}, you would be making: $" + str(SalWagee) + " an hour.").format(Name), align = "center", font = ("TimesNewRoman",20))
main()