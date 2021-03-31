def solution(participant, completion):
    hash = {index : 0 for index in participant}
    for item in hash.keys():
        if item not in completion:
            return item

    for i in hash:
        if participant.count(i) > 1:
            return i




print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))

