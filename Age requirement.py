# برنامه شرط سني (Age requirement)
#START
while True:
    try :
        age = input ("Please enter your age:")
        if int(age) >= 18 :
            print ("You can register for certification.")
        else:
            print ("You can't register for certification.")
    except ValueError:
        print ("Error: Input is not a number! Please enter a number.")
#END
# سلام ، برنامه رو ساده نوشتم تا ببينم هر کدام از اعضاي تيم ، چه تغييرات اصلاحي رو پيشنهاد ميدن!
# Version 1 - ارسال برای بررسی و تکميل برنامه

