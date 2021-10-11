def negative_vs_positive(*args):
    sum_negative = 0
    sum_positive = 0
    for x in args:
        if x > 0:
            sum_positive += x
        else:
            sum_negative += x
    print(sum_negative)
    print(sum_positive)
    if sum_positive > abs(sum_negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")
    return


numbers = [int(x) for x in input().split()]
negative_vs_positive(*numbers)
