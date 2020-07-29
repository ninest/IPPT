from static import Station, get_score

s_score = get_score(Station.situp, 18, 40)
p_score = get_score(Station.pushup, 18, 20)

print(s_score)
print(p_score)