a,b= map(int, input().split())
if a <=1000 and b<=1000:
    print("{} + {} = {}".format(a,b,a+b))
    print("{} * {} = {}".format(a,b,a*b))
    print("{} - {} = {}".format(a,b,a-b))
    print("{} / {} = {}...{}".format(a,b,a//b,a%b))
else:
    print("input must be smaller or equal to 1000")