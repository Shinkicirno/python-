import random
def hongbao(amount, number):
    # amount 总金额
    # number 红包个数
    picked_list = []
    total = amount * 100
    for idx in range(0, number-1):
        print('idx', idx)

        for_one_person = random.randrange(1, total // (number - len(picked_list)) * 2 + 1)

        total=total-for_one_person#从剩余总金额中减去本次领取的金额
        picked_list.append(for_one_person / 100)#把本次领取的金额加入到领取列表中
    picked_list.append(total / 100)
    return picked_list
if __name__ == '__main__':
        amount = 5
        number = 4
        hb_ls = hongbao(5,4)
        print(hb_ls)