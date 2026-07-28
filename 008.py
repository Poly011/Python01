medida = float(input(' Me de uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m corresponde a {}cm, e a {}mm, alem de que tambem pode ser {}dam, {}hm e {}km'.format(medida, cm, mm, dam, hm, km))
