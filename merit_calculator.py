x = int(input("Matric: "))
y = int(input("FSc: "))
z = int(input("NET: "))

percent_matric = x/11
percent_fsc = y/5.2
percent_net = z/2

agg_matric = percent_matric*0.1
agg_fsc = percent_fsc*0.15
agg_net = percent_net*0.75

aggregate = agg_fsc + agg_matric + agg_net

print(aggregate)