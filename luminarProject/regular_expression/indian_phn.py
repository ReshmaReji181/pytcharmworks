import re
rule='[+][9][1][ ][0-9]{10}'
phn=input("enter phone number")
matcher=re.fullmatch(rule,phn)
if matcher is not None:
    print("valid")
else:
    print("invalid")