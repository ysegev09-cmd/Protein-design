import random
def next_indo(protin):
    hydrophobs=["A", "V", "L", "I", "P", "F", "M", "W", "G", "C"]
    poli_protin=["N", "Q", "S", "T", "Y"]
    postive=["K", "R", "H"]
    negtive=["D", "E"]
     len=len(protin)
     next=""
     if len<75:
        next= random.choice(hydrophobs)
     if len>75 and i<120:
        next= random.choice(poli_protin)
     if len>120 and i<135:
        next= random.choice(postive)
     if len >135 and i<150:
        next= random.choice(negtive)
     return next
    
def protin_C(protin,protin_amunt):
    list=[hydrophobs,poli_protin,postive,negtive]
    for p in range(protin_amunt+1):
        for i in range(150):
           next=
        if len<=1:
            protin=protin + next 
        if len<1:
            index = random.randint(1, len(protin) - 1)
            left_part = protin[:index]
            right_part = protin[index:]
            protin=left_part + next + right_part
    


protin_amunt =int(input("Please indicate how many random protein sequences you need (1-1000)?"))
protin="M"
protin_maker=protin_C(protin,protin_amunt)