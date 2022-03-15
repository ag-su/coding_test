id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

def solution(id_list, report, k):
    dic_report = {}
    for id_ in id_list: 
        dic_report[id_] = [set(), 0, 0]
        # [신고한 id집합, 신고 받은 횟수, 메일 받을 횟수 ]

    # 신고한 id 집합 생성 
    for id_id in report: 
        id_, report_ = id_id.split(' ')
        dic_report[id_][0].add(report_)

    # 신고 받은 횟수    
    for value in dic_report.values(): 
        set_id = value[0]
        for id_ in set_id: 
            dic_report[id_][1] += 1 

    # k번 이상 신고받은 id 리스트 생성         
    lst_id = []
    for id_ in id_list:
        cnt = dic_report[id_][1]
        if cnt >= k: 
            lst_id.append(id_) 

    # 신고 한 id 집합의 id들이 lst_id 안에 들어 있으면 +1         
    for key, val in dic_report.items():
        for set_id in val[0]: 
            if set_id in lst_id:
                dic_report[key][2] += 1

    answer = [i[2] for i in dic_report.values()]
    return answer




def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer


solution(id_list = id_list, report=report, k=k)