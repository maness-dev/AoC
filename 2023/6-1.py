import re

DATA = [
    "Time:        41     96     88     94",
    "Distance:   214   1789   1127   1055"
]

times = [int(a) for a in re.findall(r"\d+",DATA[0])]
dist = [int(a) for a in re.findall(r"\d+",DATA[1])]

race_inds = 1
ind_succ  = []
for ind, time in enumerate(times):
    ind_succ = []
    for sec in range(time+1):
        diff = time-sec
        if sec * diff > dist[ind]:
            ind_succ.append(sec)

    race_inds = race_inds*len(ind_succ)

print(race_inds)
