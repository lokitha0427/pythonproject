#make _out_word
out="<<>>"
word="yay"
make=out[:2]+word+out[-2:]
print(make)
