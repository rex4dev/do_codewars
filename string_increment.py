# 문자열을 리스트에 넣는다
# 리스트를 탐색하여 숫자이면 계산할 숫자 변수에 넣는다. 이 때 리스트의 다음 값이 숫자가 아니면 숫자 변수를 초기화 시킨다.
# 숫자가 포함되어 있지 않으면 문자열의 끝에 1을 붙인다.
# 0만 포함되어 있으면

def increment_string(strng):
    incr = ""
    for s in list(strng):
        if s.isnumeric() and s != "0":
            incr = incr + s
        else:
            incr = ""
    if incr == "" and strng.count("0") == 0:
        strng = strng + "1"
    elif incr != "" and strng.count("0") > 0:
        if len(str(int(incr) + 1)) > len(incr):
            strng = strng[:len(strng) - len(incr)-1] + str(int(incr) + 1)
        else:
            strng = strng[:len(strng) - len(incr)]  + str(int(incr) + 1)
    elif incr == "" and strng.count("0") > 0:
        strng = strng[:len(strng)-1] + "1"
    else:
        strng = strng[:len(strng) - len(incr)] + str(int(incr) + 1)
    return strng

def best_increment_string(strng):
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    if tail == "": return strng+"1"
    return head + str(int(tail) + 1).zfill(len(tail))


aa = "foo99"
bb = "bar099"
cc = "foobar00"
dd = "3NSG459498(Q!|j891A=C2o3600000004799"
print(increment_string(aa))
print(increment_string(bb))
print(increment_string(cc))
print(increment_string(dd))

