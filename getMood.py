import pandas as pd
import os

z1moodlist = []
z2moodlist = []
deltalist = []
    
def calculateMood (z11, z12, z21, z22, z31, z32, gf, gm, filename):
    cwd = os.getcwd()
    df = pd.read_csv(cwd + filename)
    mem = df['mem'].to_list()
    pr = df['pr'].to_list()
    nic = df['nic'].to_list()
    length = len(mem)
    i = 0
    z13 = 1 - (z11 + z12)
    z23 = 1 - (z21 + z22)
    z33 = 1 - (z31 + z32)
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

def saveToList (z1mood, z2mood, delta):
    z1moodlist.append(z1mood)
    z2moodlist.append(z2mood)
    deltalist.append(delta)

if ( __name__ == '__main__' ):
    z11 = 0
    z12 = 0
    z21 = 0.6
    z22 = 0.2
    z31 = 0.5
    z32 = 0.3
    gf = 0.9
    gm = 0.9
    #TODO : 8 loops for all coeficients above
    while(z11 < 1):
        z12 = 0
        while(z12 <1):
            if (z11 + z12) > 1: break
            #print("z11: " + str(z11) + ", z12: " + str(z12))
            z1mood = calculateMood(z11, z12, z21, z22, z31, z32, gf, gm, "/Z1.csv")
            z2mood = calculateMood(z11, z12, z21, z22, z31, z32, gf, gm, "/Z2.csv")
            delta = (abs(z1mood - z2mood)) / z1mood * 100
        
            saveToList(z1mood, z2mood, delta)
            z12 = z12 + 0.1
        z11 = z11 + 0.1
    
    dict = {'z1mood': z1moodlist, 'z2mood': z2moodlist, 'delta': deltalist} 
    df = pd.DataFrame(dict) 
    df.to_csv('test.csv')
    

    