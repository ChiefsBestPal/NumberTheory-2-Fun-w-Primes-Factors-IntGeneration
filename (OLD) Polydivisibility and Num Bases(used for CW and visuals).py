from functools import reduce #!ONE DAY ILL MAKE AN AI THAT CAN DETECT WHICH BASE IS BEEING USED W/ A CONFIDENCE PARAMETER, AND MAYBE THE SAME THING WITH MORE IMPOSING ENCRYPTION SYSTEMS
def baseConvert(num, base):  #base 10 to other base (num_b:10 -> b:other)
    chars = "".join([chr(i) for i in range(48,58)] + [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)])
    if num < 0:
        return ("-" + baseConvert(-num, base))
    else:
        return (("" if num < base else baseConvert(num//base, base)) + chars[num % base])

def tob10(s,b):
    chars = "".join([chr(i) for i in range(48,58)] + [chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)])
    arr = [(int(chars.index(i)) * b**int((len(s)-c-1))) for c,i in enumerate(s)]
    b10 = reduce(lambda a,b : a+b,arr)
    return str(b10)

def baseConvert64(num, base = 64):  
    chars = "".join([chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]+[chr(i) for i in range(48,58)] + ["+","/"])
    if num < 0:
        return ("-" + baseConvert(-num, base))
    else:
        return (("" if num < base else baseConvert(num//base, base)) + chars[num % base])
def tob1064(s,b = 64):
    chars = "".join([chr(i) for i in range(65,91)] + [chr(i) for i in range(97,123)]+[chr(i) for i in range(48,58)] + ["+","/"])
    arr = [(int(chars.index(i)) * b**int((len(s)-c-1))) for c,i in enumerate(s)]
    b10 = reduce(lambda a,b : a+b,arr)
    return str(b10)
#print(baseConvert64(23452))

#print(tob1064())

def is_polydivisible(s,b):
    t = "" #if s.isdigit():
    for n in range(len(s)):
        if int(tob10(s[0:(n+1)],b)) % (n+1) == 0: 
            t += s[n]
            continue
        else:
            t = ""
            break
    if t == s:
        return True
    return False
print(is_polydivisible("123220",10))
print(tob10("123432",15)) #!MAKE KATA ON HOW TO CONVERT BASES !!!!!!!!!!!!!!!!

def get_polydivisible(n,b):
    c = 0
    for i in range(100000): #while len(condition) < n: better but range(1000) it is for the meme kek
        if is_polydivisible(str(i),b) or len(str(baseConvert(i,b))) == 1:
            #print(i,str(baseConvert(i,b)).rjust(5,'*'))             
            c+=1
        if c == n:
            return baseConvert(i,b)

#!print(is_polydivisible("123220", 5))
print(get_polydivisible(22,10))

#██████╗░██████╗░██╗░░░██╗██╗░░██╗
#██╔══██╗██╔══██╗██║░░░██║██║░░██║
#██████╦╝██████╔╝██║░░░██║███████║
#██╔══██╗██╔══██╗██║░░░██║██╔══██║
#██████╦╝██║░░██║╚██████╔╝██║░░██║
#╚═════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝

