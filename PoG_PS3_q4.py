import math, random

Agroup = list()
Bgroup = list()
Cgroup = list()
sample = list()
totalAM = 0
totalOM = 0
totalD1 = 0
totalD2 = 0

for i in range(20):
  Dtrue = random.randint(70, 90)
  Mabs = round(random.triangular(4.48, 5.08, 4.78), 2)
  Mobs = round(Mabs + 5*(math.log10(Dtrue/10)),2)
  Mapp = round(Mabs + 5*(math.log10(80/10)),2)
  listy = [Dtrue, Mabs, Mobs, Mapp]
  Agroup.append(listy)
  
for i in range(20):
  Dtrue = random.randint(90, 110)
  Mabs = round(random.triangular(4.48, 5.08, 4.78), 2)
  Mobs = round(Mabs + 5*(math.log10(Dtrue/10)),2)
  Mapp = round(Mabs + 5*(math.log10(100/10)),2)
  listy = [Dtrue, Mabs, Mobs, Mapp]
  Bgroup.append(listy)
  
for i in range(20):
  Dtrue = random.randint(110, 130)
  Mabs = round(random.triangular(4.48, 5.08, 4.78), 2)
  Mobs = round(Mabs + 5*(math.log10(Dtrue/10)),2)
  Mapp = round(Mabs + 5*(math.log10(120/10)),2)
  listy = [Dtrue, Mabs, Mobs, Mapp]
  Cgroup.append(listy)

print("First 10 A group stars: \nno., Dtrue, Mabs, Mapp, Mw/D=80")
for i in range(10):
  print(i+1, Agroup[i])
  

print("\nFirst 10 B group stars: \nno., Dtrue, Mabs, Mapp, Mw/D=100")
for i in range(10):
  print(i+1, Bgroup[i])
  

print("\nFirst 10 C group stars: \nno., Dtrue, Mabs, Mapp, Mw/D=120")
for i in range(10):
  print(i+1, Cgroup[i])

for i in range(20):
  if Agroup[i][2] <= 10:
    sample.append(Agroup[i])
    totalD2 += 80
  if Bgroup[i][2] <= 10:
    sample.append(Bgroup[i])
    totalD2 += 100
  if Cgroup[i][2] <= 10:
    sample.append(Cgroup[i])
    totalD2 += 120

print("\nThe sample has", len(sample), "stars with mV <= 10 mag from 60 stars.")

for i in range(len(sample)):
  totalAM += sample[i][1]
  totalD1 += sample[i][0]
  totalOM += sample[i][3]

print("\nThe average absolute magnitude of the sample is", round(totalAM/float(len(sample)), 2), "and this is brighter than the mean absolute magnitude of all stars because the fainter stars are not included in the sample." )

print("\nThe average distance of the stars in the sample is", round(totalD2/float(len(sample)), 2), "(or", round(totalD1/float(len(sample)), 2),  "from the actual distance values).")

avgOM = totalOM/float(len(sample))
avgAM = totalAM/float(len(sample))
D = round(10*(10**((avgOM-avgAM)/5)), 2)

print("\nThe average distance calculated from the apparent magnitude is", D, "and this is different because we considered the average distance of the stars in group A, B, and C to be 80, 100, and 120 respectively but this is not exactly accurate.")