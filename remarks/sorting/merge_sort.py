def merge(left, right):
    result = []
    while len(left)> 0 or len(right) > 0 :
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left= left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


def merge_sort(list):
    #배열의 길이가 1이 될 떄 까지 리스트를 쪼갠다.
    if len(list) <= 1:
        return list

    mid = len(list)//2
    left_list= list[:mid]
    right_list= list[mid:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    # 쪼갠 다음 merge함수로 두개 리스트를 크기 순으로 정렬 한다.
    return merge(left_list, right_list)