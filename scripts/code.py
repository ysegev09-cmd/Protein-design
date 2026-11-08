import random
def next_indo(protin,lenf):
    hydrophobs=["A", "V", "L", "I", "P", "F", "M", "W", "G", "C"]
    poli_protin=["N", "Q", "S", "T", "Y"]
    postive=["K", "R", "H"]
    negtive=["D", "E"]
    next=""
    if lenf<75:
        next= random.choice(hydrophobs)
    if lenf>75 and i<120:
        next= random.choice(poli_protin)
    if lenf>120 and i<135:
        next= random.choice(postive)
    if lenf >135 and i<150:
        next= random.choice(negtive)
    return next
    
def protin_C(protin,protin_amunt):
    file_a=open('results/Out_RandProtSeq.txt', 'w')
    lenf=len(protin)
    for p in range(protin_amunt+1):
        for i in range(150):
           next=next_indo(protin,lenf)
           if lenf<=1:
              protin=protin + next 
           if lenf<1:
              index = random.randint(2, len(protin) - 1)
              left_part = protin[:index]
              right_part = protin[index:]
              protin=left_part + next + right_part
        file_a.write("Rand_Prot "+str(p)+"\n" )
        file_a.write(protin+"\n" )


protin_amunt =int(input("Please indicate how many random protein sequences you need (1-1000)?"))
protin="M"
protin_maker=protin_C(protin,protin_amunt)