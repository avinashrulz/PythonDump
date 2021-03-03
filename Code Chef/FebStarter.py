T = int(input())
while T > 0:
    valueCoupon = 0
    valueDeliveryCharge = 0
    (D, C) = map(int, input().strip().split())
    (A1, A2, A3) = map(int, input().strip().split())
    (B1, B2, B3) = map(int, input().strip().split())
    valueDeliveryCharge = (A1+A2+A3) + (B1+B2+B3) + 2*D
    
    if (A1+A2+A3) < 150 and (B1+B2+B3) >= 150 :
        valueCoupon = (B1+B2+B3) + (A1+A2+A3) + D + C
    elif (B1+B2+B3) < 150 and (A1+A2+A3) >= 150:
        valueCoupon = (B1+B2+B3) + (A1+A2+A3) + D + C
    elif (B1+B2+B3) < 150 and (A1+A2+A3) < 150:
        valueCoupon = (B1+B2+B3) + (A1+A2+A3) + D + C + D
    else:
        valueCoupon = (A1+A2+A3) + (B1+B2+B3) + C
    #print(valueCoupon)
    #print(valueDeliveryCharge)
    if valueCoupon<valueDeliveryCharge:
        print("YES")
    else:
        print("NO")
    T -= 1