#1)
# შექმენით ფუნქცია, რომელსაც გადაეცემა სტრინგი და დააბრუნეთ
# ეს სტრინგდი შებრუნებულ + დიდი ასოებით (reversed / upper).
# test_case = ("VaNo MoTiashvili) ---> "ILIVHSAITOM ONAV"

def transfer(name):
    for i in name:
        return name.upper() 
    
print(transfer("VaNo MoTiashvili"))

#2)
# შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან ---> 
#(["vano" , "nika" , "bubazi" , "zauri"....)],
# დამატებით შექმენით ორი სია odd = [] და even = [], გადაუარეთ 
#ორიგინალ სიას for ციკლით და გაიგეთ რომელი ელემენტი შედგება 
#კენტი ასოებისგან და რომელი ლუწი, საბოლოოდ ჩაამატეთ შესაბამისი
# სტრინგები შესაბამის სიებში (odd / even) დიდ ასოებათ (upper) და ბოლოს დაბეჭდეთ.
# test_case = (["vano" , "davit" , "zuka" , "yiyliyo"]) ---> odd = 
#["davit" , "yiyliyo"] / even = ["vano" , "zuka"]


def list_with_str():
    list = ["vano" , "nika" , "bubazi" , "zauri", "saba", "luka"]
    odd = []
    even = []
    for i in list:
        if ''%2 == 0:
            odd.append
        return odd 
    else:
        even.append
        return even

print(list_with_str())        
       
#3)
# შექმენით ფუნქცია რომელსაც გადაეცემა სია შემდგარი სტრინგებისგან,
#  გადაუარეთ ამ სიას და შეამოწმეთ თუ მისი characterების რაოდენობა 
# არის ლუწი, ჩაამატეთ ეს კონკრეტული სიის ელემენტი ახალ ცარიელ სიაში 
# და გადააკეთეთ იგი upper ფუნქციით, თუ იქნება ამ სტრინგის ასოების 
# რაოდენობა კენტი, ჩაამატეთ ეს ელემენტი ახალ სიაში რომელსაც პირველი 
# character ექნება გადიდებული, დანარჩენი პატარა. საბოლოოდ გამოიტანეთ ეს სია.
# test_case = (["goa_best" , "vano" , "nesvi" , "tskhVarAdzE"]) ---> 
# result = ["GOA_BEST" , "VANO" , "Nesvi" , "Tskhvaradze"]
 
            


    