import pandas as pd
import os

z1moodlist = []
z2moodlist = []
deltalist = []
gflist = []
gmlist = []
    
def calculateMood (z11, z12, z13, z21, z22, z23, z31, z32, z33, gf, gm, filename):
    cwd = os.getcwd()
    df = pd.read_csv(cwd + filename)
    mem = df['mem'].to_list()
    pr = df['pr'].to_list()
    nic = df['nic'].to_list()
    length = len(mem)
    i = 0
    #z13 = 1 - (z11 + z12)
    #z23 = 1 - (z21 + z22)
    #z33 = 1 - (z31 + z32)
    f1 = 0
    f2 = 0
    f3 = 0
    m = 0
    k = gf
    while i < length:
        #print(mem[i])
        f1 = k * f1 + (1 - k) * (mem[i] * z11 + nic[i] * z12 + pr[i] * z13)
        f2 = k * f2 + (1 - k) * (mem[i] * z21 + nic[i] * z22 + pr[i] * z23)
        f3 = k * f3 + (1 - k) * (mem[i] * z31 + nic[i] * z32 + pr[i] * z33)
        k = gf / (1 + m)
        m = gm * m + (1 - gm) / 3 * (f1 + f2 + f3)
        i += 1
    return(m)

def saveToList (z1mood, z2mood, delta, gf, gm):
    z1moodlist.append(z1mood)
    z2moodlist.append(z2mood)
    deltalist.append(delta)
    gflist.append(gf)
    gmlist.append(gm)

if ( __name__ == '__main__' ):
    z11 = 0.05
    z12 = 0.1
    z13 = 0.85
    z21 = 0.05
    z22 = 0.1
    z23 = 0.85
    z31 = 0.05
    z32 = 0.1
    z33 = 0.85
    #gf = 0.9
    gm = 0.05
    
    while(gm < 1):
        gf = 0.05
        while(gf < 1):
            z1mood = calculateMood(z11, z12, z13, z21, z22, z23, z31, z32, z33, gf, gm, "/Z1.csv")
            z2mood = calculateMood(z11, z12, z13, z21, z22, z23, z31, z32, z33, gf, gm, "/Z2.csv")
            delta = (abs(z1mood - z2mood)) / z1mood * 100
        
            saveToList(z1mood, z2mood, delta, gf, gm)
            gf = gf + 0.1
        gm = gm + 0.1
    
    dict = {'z1mood': z1moodlist, 'z2mood': z2moodlist, 'delta': deltalist, 'gf': gflist, 'gm': gmlist} 
    df = pd.DataFrame(dict) 
    df.to_csv('outputGama.csv')

