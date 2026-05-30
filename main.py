import random
import string

def check_strength(pass_string):
    length = len(pass_string)
    has_digit = False
    has_symbol = False
    
    for char in pass_string:
        if char in string.digits:
            has_digit = True
        if char in string.punctuation:
            has_symbol = True
            
    if length < 8:
        return "WEAK 🔴 (Keep it 8+ characters for safety)"
    elif length >= 10 and has_digit and has_symbol:
        return "STRONG 🟢 (Excellent and secure!)"
    elif length >= 8 and has_digit:
        return "MEDIUM 🟡 (Pretty good, but missing symbols)"
    else:
        return "WEAK 🔴"

def pass_maker():
    password = [] 
    
    a = input("Want To add Symbols in your password? : ")
    for _ in range(6):
        alphabet = random.choice(string.ascii_letters)
        password.append(alphabet)
        
    if "yes" in a.lower():
        print("Sure..\n")
        for _ in range(2):
            Symbols = random.choice(string.punctuation)
            password.append(Symbols)
    else:
        print("OK, lets Move Ahead!\n")
        
    b = input("Want To add Digits in your password? : ")
    if "yes" in b.lower():
        print("Sure\n")
        for _ in range(4):
            Num = random.choice(string.digits)
            password.append(Num)
    
    print("OK, Here is your Password")
            
    passs = "".join(password)
    print(f"Here Is Your Password : {passs}")
    
    strength = check_strength(passs)
    print(f"Strength: {strength}")
    
    with open("passmaker.txt", "a") as f:
        f.write(f"Password: {passs} | Strength: {strength}\n")
    
    print("-" * 40)
    
    c = input("\nWant Another Password? : ")
    if "yes" in c.lower():
        print("Ok, I'm Up!\n")
        pass_maker()
    else:
        print("Sure, Visit Again")

if __name__ == "__main__":
    pass_maker()
