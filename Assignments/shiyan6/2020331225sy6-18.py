s="语文:80,数学:82,英语:90,物理:85,化学:88,美术:80"
lst_score=[]
for x in s.split(","):
    i=x.index(":")+1
    score=int(x[i:])
    lst_score.append(score)
sum_score=sum(lst_score)
print("总分为：{}\n平均分为：{:.1f}".format(sum_score,sum_score/len(lst_score)))