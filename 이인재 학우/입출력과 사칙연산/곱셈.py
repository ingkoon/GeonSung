inputA = int(input())
inputB = int(input())

if inputA > 100 and inputB >100:
    thB = int((inputB)/100)
    huB = int((inputB%100)/10)
    onB = int((inputB%10))
    
    cnt3 = (inputA) * onB
    cnt2 = (inputA) * huB
    cnt1 = (inputA) * thB

    print("%d\n%d\n%d" %(cnt3,cnt2,cnt1))
    
    result = cnt3 + cnt2 * 10 + cnt1 * 100

    print(result) 