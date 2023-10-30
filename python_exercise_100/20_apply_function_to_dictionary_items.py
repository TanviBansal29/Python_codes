d = {"a": 1, "b": 2, "c": 3}
ans=0

for item in d:
    ans+=d[item]

print(ans)

print(sum(d.values()))