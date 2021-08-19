# -*- coding:utf8 -*-

def main(s):
    master_string = s[0]
    for i in range(1,len(s)):
        if s[i-1] == s[i] and master_string:
            continue
        else:
            master_string += s[i]

    num_of_zero = master_string.count("0")
    num_of_one = master_string.count("1")
    if num_of_one > num_of_zero:
        return num_of_zero
    else:
        return num_of_one

def solution(data):
    count0 = 0 #전부 0으로 바꾸는 경우
    count1 = 0 #전부 1로 바꾸는 경우
    if data[0] == "1":
        count0 +=1
    else:
        count1 += 1

    for i in range(len(data)-1):
        if data[i] != data[i+1]:
            if data[i+1] == "1":
                count0 +=1
            else:
                count1 += 1

    return min(count0, count1)

if __name__ =="__main__":
    s = input()
    result = main(s)
    print(result)