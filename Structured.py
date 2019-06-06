import pickle
import pandas as pd

with open('datax_header.pickle','rb') as f:
    header = pickle.load(f)
countryba_list = [i for i in header if i.startswith('countryba_')]
sic_list = [i for i in header if i.startswith('sic_')]
stprba_list = [i for i in header if i.startswith('stprba_')]
# 'sic_0100' , 't_2001q1','countryba_AE' , 'stprba_AB', 'afs_1-LAF'

def getX(sic,countryba,stprba,afs):
    t_list= ['2009q4']+[str(y)+'q'+str(q+1) for y in range(2010,2019) for q in range(4)]
    d = {'const':[1]*len(t_list)}
    for c,t in enumerate(t_list):
        temp = [0]*len(t_list)
        temp[c] = 1
        d['t_'+t] = temp
    if countryba == 'Other':
        for country in countryba_list:
            d[country] = [1/84]*len(t_list)
    elif countryba == 'AE':
        pass
    else:
        d['countryba_'+countryba] = [1]*len(t_list)
    
    if stprba == 'AB':
        pass
    else:
        if (countryba == 'CA') | (countryba == 'US'):       
            d['stprba_'+stprba] = [1]*len(t_list)
        else: pass
      
    if afs == 'afs_1-LAF':
        pass
    else:
        d[afs] = [1]*len(t_list)
        
    if sic == '0100':
        pass
    else:
        d['sic_'+sic] = [1]*len(t_list)  
    return pd.DataFrame(data = d,columns = header).fillna(0)