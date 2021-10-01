a, b =map(int, input().split())
if b==1:
    print("{:.2f}".format((a-80)*0.7))
elif b==2:
    print("{:.2f}".format((a-70)*0.6))
else:
    print("1 for boy 2 for girl")
