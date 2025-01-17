# მუშაობა ფაილურ სისტემასთან

"""
1. თუ გვინდა რომ ფაილი გავხსნათ და წავიკითხოთ შიგნით რა წერია
უნდა გამოვიყენოთ ეს კოდი
"""

# file = open("my_file.txt", 'r', encoding="utf-8")
#                             ↑
# 'r' აღნიშნავს Reading Mode(default). შეგვიძლია მასში მხოლოდ ინფომაციის წაკითხვა
# 'w' აღნიშნავს Writing Mode. შიგნით შეგვიძლია შევიტანოთ ინფორმაცია კოდის დახმარებით
# 'b' აღნიშნავს Binary Mode
# 't' აღნიშნავს Text Mode(default) 
# 'a' აღნიშნავს და გადაიტანს მაუსის კურსორს ტექსტის გვერდით და არა ქვემოთ
# 'a+' აღნიშნავს
# '+' აღნიშნავს Updating(reading and writing)

# ფაილის წასაკითხად ვიყენებთ .readlines მეთოდს

""" lines = file.readlines()
print("1.", lines)
print("---------------") """
"""
თუკი კოდი არასწორად დავწერეთ, გამოგვიტანა Error, მაგრამ გვინდა რომ კოდის კითხვა
გააგრძელოს დასრულებამდე ჩვენ გვჭირდება რაღაც ფუნქცია ან მეთოდი, რომელიც
გაუმკლავდემა ამ Error'ს და ჩვენ გვაქვს try/except/finally მეთოდი. 
"""
# try - ჯერ ვწერთ ამ ბლოკს პირველად, აქ ვწერთ ეგრეთწოდებულ კრიტიკულ კოდს, რაშიც შეიძლება იყოს შეცდომა.
# except - ეს ბლოკი იჭერს ამ გამონაკლისს და რაიმეს მოიმოქმედებს კოდის არასწორობის დროს.
# finally - რაც არ უნდა მოხდეს, ამ ბლოკში ჩაწერილი კოდი ნებისმიერ შემთხვევაში უნდა გაიშვას მიუხედავად რაიმე Error ისა.

""" try:
    file = open("my_file.txt", 'r', encoding="utf-8")
    try:
        s = int(file.readlines()) # კითხულობს ყველა ხაზს
        print(s) # გამოვიტანოთ შედეგი
    finally:
        print(file.closed)
        file.close() # ვხურავთ ფაილს 
        print(file.closed)
except FileNotFoundError: 
    print("2. File not found.")
    print("---------------")
except:
    print("2-1. Error occured while working on file.") """

# with ... as ის დახმარებით:  

""" try:
    with open("my_fil.txt", 'r', encoding="utf-8") as file :
        s = file.readlines()
        int(s)
        print("2-2.", s)
except FileNotFoundError:
    print("Can't Open File.")
except:
    print("Error Occured.")
finally:
    print(file.closed) """

# Write მეთოდი
""" file = open("out.txt", "w")
file.seek(1000)
file.write("Hello World!")
file.close() """

""" try :
    with open("out.txt", 'a') as file :
        file.write("Hello1\n")
        file.write("Hello2\n")
        file.write("Hello3\n")
except :
    print("დაფიქსირდა შეცდომა") """

""" try :
    with open("out.txt", "a+") as file :
        file.seek(0)
        file.write("Hello")
        s = file.readline()
        print(s)
except :
    print("Error!") """