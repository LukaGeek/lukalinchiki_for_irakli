# 1 დან 6-ის ჩათვლით რიცხვების კვადრატები:
n1 = 6
result1 = [0]*6
str1 = "1:"

for i in range(1, n1+1) :
    result1[i-1] = i**2
print("------------------------------------------")
print(str1, result1)

## List comprehension-ის გამოყენებით:
str2 = "1.1:"
result2 = [i**2 for i in range(1, i+1)]
print(str2, result2)

""" ------------------------------------------ """

# 5 ცალი 1იანის გამოტანა List Comperhension-ის დახმარებით:
n2 = 5
str3 = "2:"
result3 = [1 for _ in range(5)]
print("------------------------------------------")
print(str3, result3)

""" ------------------------------------------ """

# 3-ზე გაყოფისას მიღებული ნაშთების გამოტანა List Comperhension-ის დახმარებით:
numb_list1 = [15,23,75,35,26,87]
str4 = "3:"
result4 = [i%3 for i in numb_list1]
print("------------------------------------------")
print(str4, result4)

## 3-ზე გაყოფისას მიღებული ნაშთების გამოტანა boolean ტიპით:
numb_list2 = [15,23,75,35,26,87]
str5 = "3.1:"
result5 = [i%3 == 0 for i in numb_list2]
print(str5, result5)

### 3-ზე გაყოფისას მიღებული ნაშთების გამოტანა პირობის დამატებით:
numb_list3 = [15,23,75,35,26,87]
str6 = "3.2:"
result6 = [i for i in numb_list3 if i%3 == 0]
print(str6, result6)
print("------------------------------------------")

""" ------------------------------------------ """

# სიტყვის Split-ით დაყოფა

print("separate".split("s"))
print("separate".split("e"))
print("separate".split("p"))
print("separate".split("a"))
print("separate".split("r"))
print("separate".split("a"))
print("separate".split("t"))
print("separate".split("e"))
print("------------------------------------------")
print("s eparate".split(" "))
print("s e parate".split(" "))
print("s e p arate".split(" "))
print("s e p a rate".split(" "))
print("s e p a r ate".split(" "))
print("s e p a r a te".split(" "))
print("s e p a r a t e".split(" "))
print("------------------------------------------")

""" ------------------------------------------ """

# input-ში ჩაწერილი რიცხვების string-ად დაბრუნება:

""" inp = input("Input your numbers with spaces: ") """
""" result = [int(i) for i in inp.split(' ')] """
""" print(result)
print("------------------------------------------") """

""" ------------------------------------------ """

# 2-ის ან 3-ის ჯერადის გამოტანა: 
str7 = "4:"
result7 = [x for x in range(100,200) if x%2 or x%3]
print(str7, result7)
print("------------------------------------------")

""" ------------------------------------------ """

# ლუწ-კენტის გამოტანა:
str8 = "5:"
numb = [12,43,52,64,32,87,2,63,99]
result8 = [f'{x} is even'
           if x%2 == 0 
           else f'{x} is odd' 
           for x in numb
           ]
print(str8, result8)
print("------------------------------------------")

""" ------------------------------------------ """

# რიცხვების დაკავშირება:
list1 = [1,2,3]
list2 = [11,12,13]
str9 = "6:"
result = [(i,j)
            for i in list1
            for j in list2
            ]
print(str9, result)