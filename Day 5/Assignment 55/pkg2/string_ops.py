def str_rev(str):
    return str[::-1]

def vowelcount(str1):
    str2=str1.lower()
    str3=str2.replace(" ","")
    length=len(str3)
    vowelcount=0
    for i in range(length):
        if(str3[i]=='o'or str3[i]=='i'or str3[i]=='e'or str3[i]=='u'or str3[i]=='a'):
            vowelcount+=1
    return vowelcount