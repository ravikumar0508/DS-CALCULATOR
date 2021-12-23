import math as m
import sympy as sym
import statistics as s



#Add check:
def add_function(val1, val2):
    return val1 + val2



#Multiply check:
def multiply(val1, val2):
    return val1 * val2



#subraction check:
def subraction(val1,val2):
    return val1 - val2



#division Check:
def division(val1,val2):
    return val1 / val2



#Modulus check:
def modulus (val1,val2):
    return val1 % val2



#exponention check:
def exponention(val1,val2):
    return val1 ** val2


#Floor division check:
def floor_division(val1,val2):
    return val1 // val2

#odd or even check:
def odd_or_even(val1):
    if val1 % 2==0:
        print("it is a even")
    else:
        print("its odd")
        
        

#positve or negative checck:
def positive_or_negative(val1):
    if val1 >0:
        return "its a pos number"
    elif val1 <0:
        return "its  a negative number"
    else:
        return "its a zero"
    
    
    
#Palindrome check
def ispalindrome(val1):
    if val1 ==val1[::-1]:
        print("its a plaindrome")
    else:
        print("its not a palindrome")
        
        
        
#list creation
def list_create():
    a =int(input("enter lem "))
    b =[]
    for i in range(0,a):
        c = int(input("enter num"))
        b.append(c)
    return(b)



#Set creation
def set_create():
    a =int(input("enter your integer"))
    b =set()
    for i in range(0,a):
        c =int(input("enter the elemnts need to added to set"))
        b.add(c)
    return b



#Dictionary creation
def dictionary_create():
    a =int(input("enter your integer"))
    b ={}
    for i in range(0,a):
        keys =int(input("enter the keys added to dictionary"))
        values=int(input("enter the values added to dictionary"))
        b[keys]=values
    return b


#Tuple Creation:
def Tuple_create():
    a =int(input("enter len"))
    b =[]
    for i in range(0,a):
        c =int(input("enter the numbers added into the tuples"))
        b.append(c)
    return tuple(b)

print('''
Welcome to Calculator

Please select any one data strucuture to proceed 
1) Int
2) String
3) List
4) set
5) Dictionary
6) tuple
''')
user_input = int(input("Please enter a value between 1-7: "))
if user_input == 1:
    print("""select any one operation from below
    1) add_function
    2) multiply
    3) subraction
    4) division
    5) modulus
    6) exponention
    7) floor_division
    8) Facctorial 
    9) cos
    10) odd or even
    11) positive or negative
    12) prime or not
    13) sin
    14) ceil
    15) log
    16)fibanocci series
    17)armstrong number
    """)
    int_user_input =int(input("please select any one numbers form 1-15"))
    if int_user_input == 1:
        val1 =int(input("plesae enter 1st value"))
        val2 =int(input("please enter 2nd value"))
        print(add_function(val1,val2))
    elif int_user_input ==2:
        val1 =int(input("plesae enter 1st value"))
        val2 =int(input("please enter 2nd value"))
        print(multiply(val1,val2))
    elif int_user_input ==3:
        val1 =int(input("plesae enter 1st value"))
        val2 =int(input("please enter 2nd value"))
        print(subraction(val1,val2))
    elif int_user_input==4:
        val1 =int(input("plesae enter 1st value"))
        val2 =int(input("please enter 2nd value"))
        print(division(val1,val2))
    elif int_user_input==5:
        val1 =int(input("plesae enter 1st value"))
        val2 =int(input("please enter 2nd value"))
        print(modulus(val1,val2))
    elif int_user_input ==6:
        val1 =int(input("plesae enter 1st value"))
        val2 =int(input("please enter 2nd value"))
        print(exponention(val1,val2))
    elif int_user_input ==7:
        val1 =int(input("plesae enter 1st value"))
        val2 =int(input("please enter 2nd value"))
        print(floor_division(val1,val2))
    elif int_user_input==8:
        val1 =int(input("plesae enter the value"))
        print(m.factorial(val1))
    elif int_user_input==9:
        val1 =int(input("plesae enter the value"))
        print(m.cos(val1))
    elif int_user_input==10:
        val1 =int(input("enter your number"))
        print(odd_or_even(val1))
    elif int_user_input==11:
        val1 = int(input("enterr your number"))
        print(positive_or_negative(val1))
    elif int_user_input ==12:
        val1 = int(input("enterr your number"))
        print(sym.isprime(val1))
    elif int_user_input==13:
        val1 =int(input("enterr your number"))
        print(m.sin(val1))
    elif int_user_input==14:
        val1 =int(input("enterr your number"))
        print(m.ceil(val1))
    elif int_user_input==15:
        val1 =int(input("enterr your number"))
        print(m.log(val1))
    else:
        print("you are choosing wrong number please choose numbers between 1 to 15")
elif user_input == 2:
    print("""select any one operation from below
    1) count
    2) casefold
    3) upper
    4) is_ascii
    5) split
    6) swapcase
    7) zfill
    8) ispalindrome
    9) concatenation
    10) isalnum
    11) isdecimal
    12) isdigit
    13) capitalize
    14) index
    15) encode
    16)chr and ord
    17)special_character_removal
    18)strip
    """)
    str_user_input =int(input("enter your choice from 1-15"))
    if str_user_input ==1:
        over_all_text =input("enter your over all string")
        print(over_all_text.count(input("enter your specified string to count")))
    elif str_user_input ==2:
        str1 =input("enter your string")
        print(str1.casefold())
    elif str_user_input==3:
        str1 =input("enter your string")
        print(str1.upper())
    elif str_user_input==4:
        str1 =input("enter your string")
        print(str1.isascii())
    elif str_user_input==5:
        str1 =input("enter your string")
        print(str1.split())
    elif str_user_input==6:
        str1 =input("enter your string")
        print(str1.swapcase())
    elif str_user_input==7:
        str1 =input("enter your string")
        print(str1.zfill(int(input("enter your value"))))
    elif str_user_input==8:
        val1 = input("enter your string")
        print(ispalindrome.val1)
    elif str_user_input==9:
        str1 =input("enter your string")
        str2 =input("enter your string")
        print(str1 + str2)
    elif str_user_input==10:
        str1 =input("enter your string")
        print(str1.isalnum())
    elif str_user_input==11:
        str1 =input("enter your string")
        print(str1.isdecimal())
    elif str_user_input==12:
        str1 =input("enter your string")
        print(str1.isdigit())
    elif str_user_input==13:
        str1 =input("enter your string")
        print(str1.capitalize())
    elif str_user_input==14:
        str1 =input("enter your string")
        print(str1.index(int(input("enter which string index u need"))))
    elif str_user_input==15:
        str1 =input("enter your string")
        print(str1.encode())
    else:
        print("please choose any number in between 1 to 15")
elif user_input==3:
    print("""select any one operation from below
    1) mean
    2) median
    3) counter
    4) geo_metric_mean
    5) harmonic_mean
    6) median_high
    7) median_low
    8) sum
    9) remove
    10) sort#(ascending or descending)
    11) append
    12) clear
    13) copy
    14) index
    15) count
    16) del
    17) duplicate removal
    18) reversed
    19) concatination
    """)
    li_user_input =int(input("please select any one numbers form 1-15"))
    if li_user_input==1:
        list1 =list_create()
        print(s.mean(list1))
    elif li_user_input==2:
        list1 = list_create()
        print(s.median(list1))
    elif li_user_input==3:
        list1 =list_create()
        print(s.Counter(list1))
    elif li_user_input==4:
        list1 =list_create()
        print(s.geometric_mean(list1))
    elif li_user_input==5:
        list1 =list_create()
        print(s.harmonic_mean(list1))
    elif li_user_input==6:
        list1 =list_create()
        print(s.median_high(list1))
    elif li_user_input==7:
        list1 =list_create()
        print(s.median_low(list1))
    elif li_user_input==8:
        list1 =list_create()
        print(sum(list1))
    elif li_user_input ==9:
        list1 =list_create()
        (list1.remove(int(input("enter number to remove"))))
        print(list1)
    elif li_user_input ==10:
        list1 =list_create()
        (list1.sort())
        print(list1)
    elif li_user_input==11:
        list1 =list_create()
        list1.remove(10)
        print(list1)
    elif li_user_input==12:
        list1 =list_create()
        list1.clear()
        print(list1)
    elif li_user_input==13:
        list1 =list_create()
        list1.copy()
        print(list1)
    elif li_user_input==13:
        list1=list_create()
        print(list1.index(int(input("enter the interger u want to find indexing"))))
    elif li_user_input==14:
        list1=list_create()
        print(list1.pop(int(input("enter the interger u want to pop"))))
        print(list1)
    elif li_user_input==14:
        list1=list_create()
        print(list1)
        list1.reverse()
        print(list1)
    elif li_user_input==15:
        list1=list_create()
        print(list1.count(int(input("enter the value to be count"))))
elif user_input==4:
    print("""select any one operation from below
    1) mean
    2) median
    3) add
    4) remove
    5) pop
    6) clear
    7) discard
    8) Counter
    9) sum
    10) median_low
    11)union
    12)intersection
    13)difference
    14)symmetric_difference
    15)is disjoint
    16)set to list & set to tuple
    """)
    set_input =int(input("please select any one numbers form 1-15"))
    if set1_input==1:
        set1==set_create()
        print(s.mean(set1))
    elif set_input==2:
        set1==set_create()
        print(s.median(set1))
    elif set_input==3:
        set1==set_create()
        set1.add(int(input("enter the integer you want to add")))
        print(set1)
    elif set1_input==4:
        set1 =set_create()
        set1.remove(int(input("the element u need to remove from set")))
        print(set1)
    elif set1_input==5:
        set1 =set_create()
        set1.pop()
        print(set1)
    elif set1_input==6:
        set1=set_create()
        set1.clear()
        print(set1)
    elif set1_input==7:
        set1=set_create()
        set1.discard(int(input("enter the integer you want to discard")))
        print(set1)
    elif set1_input==8:
        set1=set_create()
        print(s.Counter(set1))
    elif set1_input==9:
        set1=set_create()
        print(sum(set1))
    elif set1_input==10:
        set1=set_create()
        print(s.median_low(set1))
    else:
        print("you are choosing wrong number pls select anything in between 1-10")
elif user_input==5:
    print("""select any one operation from below
    1) clear
    2) copy
    3) from keys
    4) get
    5) items
    6) keys
    7) pop
    8) popitem
    9) update
    10) values
    """)
    dict_user_input=int(input("enter any operarations from 1-10"))
    if dict_user_input==1:
        dict1 = dictionary_create()
        print(dict1)
        dict1.clear()
        print(dict1)
    elif dict_user_input==2:
        dict1 = dictionary_create()
        print(dict1)
        b = dict1.copy()
        print(b)
    elif dict_user_input==3:
        list1=list_create()
        list2 =list_create()
        dict1 =dict.fromkeys(list1,list2)
        print(dict1)
    elif dict_user_input==4:
        dict1 = dictionary_create()
        print(dict1)
        d =dict1.get(int(input("enter the key you need to get from dict1 ")))
        print(d)
    elif dict_user_input==5:
        dict1 = dictionary_create()
        print(dict1)
        d =dict1.items()
        print(d)
    elif dict_user_input==6:
        dict1 = dictionary_create()
        print(dict1)
        d =dict1.keys()
        print(d)
    elif dict_user_input==7:
        dict1 = dictionary_create()
        print(dict1)
        d =dict1.pop(int(input("enter the element u need to pop from the list")))
        print(dict1)
    elif dict_user_input==8:
        dict1 = dictionary_create()
        print(dict1)
        d =dict1.popitem()
        print(d)
    elif dict_user_input==9:
        dict1 = dictionary_create()
        print(dict1)
        dict2 =dictionary_create()
        print(dict2)
        dict1.update(dict2)
        print(dict1)
    elif dict_user_input==10:
        dict1 = dictionary_create()
        print(dict1)
        d =dict1.values()
        print(d)
elif user_input==6:
    print("""select any one operation from below
    1) tuple creation
    2) index
    3) concatenate
    4) count
    5) tuple_conversion
    """)
    tuple_user_input=int(input("enter any operarations from 1-10"))
    if tuple_user_input==1:
        tuple1 = Tuple_create()
        print(tuple1)
    elif tuple_user_input==2:
        tuple1 =Tuple_create()
        print(tuple1)
        d =tuple1.index(int(input("enter the numbers tuples")))
        print(d)
    elif tuple_user_input==3:
        tuple1 =Tuple_create()
        tuple2 =Tuple_create()
        tuple3 =tuple1 + tuple2
        print(tuple3)
    elif tuple_user_input==4:
        tuple1 =Tuple_create()
        print(tuple1.count(int(input("enter the count element for tuples"))))
    elif tuple_user_input==5:
        tuple1 =Tuple_create()
        print(tuple1)
        b =input("what you need to convert list or set")
        if b =="list":
            c =list(tuple1)
            print(c)
        elif b =="set":
            d =set(tuple1)
            print(d)
    else:
        print("you are entering wrong number please choose numbers between 1-5")
else:
    print("you are entering wrong number please choose numbers between 1-6")
                
