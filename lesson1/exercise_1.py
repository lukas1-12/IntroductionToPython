#Definition der Werte, Variablen, Konstanten
m = 1500
u = 0.015
g = 9.81
v = 80/3.6
c_w = 0.31
A = 1.97
p = 1.204

#Berechnungen

F_r = m * g * u
F_l = c_w * A * p * v * v * 0.5
F = F_r + F_l

P = F * v /1000

print(round(P,2), "kW")
