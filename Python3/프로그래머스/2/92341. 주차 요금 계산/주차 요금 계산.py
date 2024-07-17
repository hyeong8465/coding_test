def price(fees, time_val):
    time_base, fee_base, time_unit, fee_unit = fees
    if time_val <= time_base:
        return fee_base
    else:
        if (time_val-time_base) % time_unit == 0:
            price = fee_base + (time_val-time_base)/time_unit * fee_unit
        else:
            price = fee_base + ((time_val-time_base)//time_unit+1) * fee_unit
        return price
    
def solution(fees, records):
    in_dic = {}
    out_dic = {}
    time_dic = {}
    price_dic = {}
    count_dic = {}
    for i in records:
        temp = i.split(' ')
        if temp[-1] == 'IN':
            time_temp = temp[0].split(':')
            time = int(time_temp[0])*60 + int(time_temp[1])
            car_num = temp[1]
            in_dic[car_num] = time
            if car_num not in time_dic:
                time_dic[car_num] = 0
                count_dic[car_num] = 0
            count_dic[car_num] += 1
        else:
            time_temp = temp[0].split(':')
            time = int(time_temp[0])*60 + int(time_temp[1])
            car_num = temp[1]
            out_dic[car_num] = time
            
            time_val = out_dic[car_num] - in_dic[car_num]
            time_dic[car_num] += time_val
            count_dic[car_num] += 1
            
    for i in list(count_dic.keys()):
        if count_dic[i] % 2 != 0:
            time_dic[i] += 23*60+59 - in_dic[i]

    temp2 = []
    for i in records:
        temp = i.split(' ')
        if temp[-1] == 'IN':
            if temp[1] not in temp2:
                temp2.append(temp[1])
    temp2.sort()
    answer = []
    for i in temp2:
        answer.append(price(fees, time_val = time_dic[i]))
    
    return answer