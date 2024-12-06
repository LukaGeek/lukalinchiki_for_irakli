""" იტერატორად(ობიექტი) გარდაქმნა """
# next() მეთოდით შეგვეძლება list_1-ის იტერატორად გარდაქმნილ list'ს შიგნით წავიკითხოთ პირველი ელემენტი

""" list_1  = ['a','b','c']
iterr = iter(list_1) # იტერატორი

print(next(iterr)) # შედეგი: a
print(next(iterr)) # შედეგი: b
print(next(iterr)) # შედეგი: c """

# ალტერნატიული გზა for ციკლით:
"""
 for el in iterr :
    print(el) """ # შედეგი a b c

print("---------------")

""" comprehensions """
"""
 # List
list_compr = [el for el in range(5)]
print("List:",list_compr)
# Set
set_compr = {el for el in range(5)}
print("Set:",set_compr)
# Dict
dict_compr = {el:el**5 for el in range(5)}
print("Dict:",dict_compr)
# Tuple(იგივე generator'ის გამოსახულება)
tuple_compr = (el for el in range(5))
print("Tuple:",tuple_compr) # არ გვაქვს tuple'ს comprehension, გვიბრუნებს გენერატორის ადგილს მეხსიერებაში <generator object <genexpr> at 0x000001D49E3B4B80>
# რომ ავამუშაოთ უნდა გამოვიყენოთ for ციკლი აქაც:
for el in tuple_compr :
    print(el) # შედეგი 0 1 2 3 4
"""

""" Return-მა გაწყვიტა პროცესი და გამოიტანა 1 """
""" 
def get_list() :
    for el in [1,2,3,4,5] :
        return el
    
print(get_list()) # შედეგი: 1
"""

""" Yield """
def get_list() :
    for el in [1,2,3,4,5] :
        yield el
a = get_list()

print(get_list()) # ფუნქცია გადაიქცა გენერატორის ფუნქციად, რომლისთვისაც საჭიროა next()
print(next(a))
print(next(a))
print(next(a))