import sys
import Pmf

def TruncatePmf(original, cutoff):
    new = original.Copy()
    for key in original.d.keys():
        if key < cutoff:
            new.Remove(key)
    new.Normalize()
    return new


def Main(name):
    pmf = Pmf.MakePmfFromList([1, 2, 2, 3, 5])
    new = TruncatePmf(pmf, 3);
    print(new.Prob(5))

if __name__ == '__main__':
    Main(*sys.argv)