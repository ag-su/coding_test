import re

def solution(new_id):
    answer = ''
    # 1단계: 대문자 -> 소문자 
    if not(new_id.islower()):
        new_id = new_id.lower()

    # 2단계: 소문자, -, _, . 제외한 문자 제거 
    if len(re.sub('[^0-9a-z-_.]', '', new_id)) > 0:
        new_id = re.sub('[^0-9a-z-_.]', '', new_id)

    # 3단계: 연속된 . 제거 
    if '..' in new_id: 
        new_id = re.sub('(([.])\\2{1,})', '.', new_id)

    # 4단계: 마침표 처음과 끝 제거
    if (new_id.startswith('.')) or new_id.endswith('.'): 
        new_id = new_id[0].replace('.', '') + new_id[1:-1]+new_id[-1].replace('.', '')

    # 5단계: 빈 문자열? 
    if len(new_id) == 0: 
        new_id = 'a'

    # 6단계: 길이가 16 이상 -> 첫 15개의 문자 제외 나머지 문자들 모두 제거 
    if len(new_id) >= 16: 
        if new_id[:15].endswith('.'):
            new_id = new_id[:14]
        else:
            new_id = new_id[:15]

    # 7단계: new_id 길이 2자 이하 -> 마지막 문자를 길이가 3이 될 때까지 반복
    if len(new_id) <= 2: 
        n = 3 - len(new_id)
        new_id = new_id + new_id[-1]*n

    return new_id