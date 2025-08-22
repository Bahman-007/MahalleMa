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
# This is a simple age checker program
# Version 1 - ارسال برای بررسی و تکميل برنامه
