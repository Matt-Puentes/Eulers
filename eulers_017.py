import sys
ones = ["","one","two","three","four","five","six","seven","eight","nine"]
teens = ["ten", "eleven", "twelve", "thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens = ["","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
past = ["hundred","thousand"]

megaString = ""
for num in range(1,1000+1):
    output = ""
    numIterate = [i for i in str(num)]
    numIterate = numIterate[::-1]
    index = len(numIterate)-1
    while index >= 0:
        n = int(numIterate[index])
        if index == 3:
            output = output + ones[n]+past[n]
        if index == 2:
            if not n == 0:
                output = output + ones[n]+past[0]
                if not (int(numIterate[0])==0 and int(numIterate[1])==0):
                    output = output + "and"
        if index == 1:
            if n == 1:
                output = output + teens[int(numIterate[index-1])]
            else:
                output = output + tens[n]
        if index == 0:
            if len(numIterate)<2:
                output = output + ones[n]
            else:
                if not (int(numIterate[1])==1):
                    output = output + ones[n]
        index-=1
    print(str(num)+" "+output)
    megaString = megaString + output
print(megaString)
print(len(megaString))
