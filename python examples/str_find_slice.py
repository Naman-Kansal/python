text = "X-DSPAM-Confidence:    0.8475";

index=text.find(':')
length=len(text)
num=float(text[index+1:length+1])
print(num)
