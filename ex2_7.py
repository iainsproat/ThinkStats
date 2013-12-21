import sys
from ex2_4 import TruncatePmf
from ex2_6 import ProbEarly, ProbOnTime, ProbLate, MakePmfOfAttributeFromObjects
from ex1_3 import GetData, PartitionFirstBornFromSubsequentBorn

def Main(name):
    records = GetData()
    firstBorn, subsequentBorn = PartitionFirstBornFromSubsequentBorn(records)
    liveBorn = firstBorn + subsequentBorn
    firstBornPmf = MakePmfOfAttributeFromObjects(firstBorn, 'prglength')
    subsequentBornPmf = MakePmfOfAttributeFromObjects(subsequentBorn, 'prglength')
    liveBornPmf = MakePmfOfAttributeFromObjects(liveBorn, 'prglength')
    
    currentTime = 38 #weeks
    cutoff = currentTime + 1
    firstBornPmf = TruncatePmf(firstBornPmf, cutoff)
    subsequentBornPmf = TruncatePmf(subsequentBornPmf, cutoff)
    liveBornPmf = TruncatePmf(liveBornPmf, cutoff)
    
    print("Probability first pregnancy not delivered by 38 weeks will be delivered by 39 weeks : ", firstBornPmf.Prob(39))
    print("Probability subsequent pregnancy not delivered by 38 weeks will be delivered by 39 weeks : ", subsequentBornPmf.Prob(39))
    print("Probability pregnancy not delivered by 38 weeks will be delivered by 39 weeks : ", liveBornPmf.Prob(39))

if __name__ == '__main__':
    Main(*sys.argv)