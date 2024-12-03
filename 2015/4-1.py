import hashlib

input_string = "iwrupvqb"
print(hashlib.md5(str.encode("abcdef609043")).hexdigest())

for i in range(10000000000000000000):
    to_convert  = f"{input_string}{i}"
    result = hashlib.md5(str.encode(to_convert))
    
    digested = result.hexdigest()
    if digested[:5]=='00000':
        print(i)
        break