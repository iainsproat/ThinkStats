import Pmf

def PmfMean(t):
    mean = 0
    for k, v in t.d.items():
        mean += v * k
    return mean

def PmfVariance(t, mean=None):
    if mean == None:
        mean = PmfMean(t)
    
    variance = 0
    for k, v in t.d.items():
        variance += v * (k - mean)**2
    
    return variance

pmf = Pmf.MakePmfFromList([1, 2, 2, 3, 5])
print ('PmfMean : ', PmfMean(pmf))
print ('Mean : ', pmf.Mean())
print ('PmfVariance : ', PmfVariance(pmf))
print ('Variance : ', pmf.Var())