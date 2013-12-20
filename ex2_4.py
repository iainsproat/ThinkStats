import Pmf

def RemainingLifetime(original, cutoff):
    new = original.Copy()
    for key in original.d.keys():
        if key < cutoff:
            new.Remove(key)
    new.Normalize()
    return new



pmf = Pmf.MakePmfFromList([1, 2, 2, 3, 5])
new = RemainingLifetime(pmf, 3);
print(new.Prob(5))