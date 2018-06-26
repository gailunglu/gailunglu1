import msg,display
msg.msg_method()
display.display_method()
n=input("Enter your expression ");
print "The evaluated expression is ", n

prn=int(raw_input("Enter Principal"))
r=int(raw_input("Enter Rate"))
t=int(raw_input("Enter Time"))
si=(prn*r*t)/100
print "Simple Interest is ",si