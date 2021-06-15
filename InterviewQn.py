def find_max():
    count=0
    sum=11
    a=8
    b=3
    c=2
    bal=0

#Sample coding questions
    while(bal<sum):
        if count == 0:
            bal = sum
        if(bal==0 and count !=0):
            return count
        if bal-a < sum and bal >= a:
            if bal == a:
                count += 1
                return count
            bal = bal - a
            count += 1
        elif bal-b < sum and bal >= b:
            if bal == b:
                count += 1
                return count
            bal = bal - b
            count += 1
        elif bal-c < sum and bal >= c:
            if bal == c:
                count += 1
                return count
            bal = bal - c
            count += 1

if __name__== "__main__":
    times = find_max()
    print("number of counts ",times)
