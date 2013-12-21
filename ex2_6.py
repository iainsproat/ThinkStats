import sys
import Pmf
from ex1_3 import GetData, PartitionFirstBornFromSubsequentBorn

def ProbEarly(pmfObject):
   return ProbInLimits(pmfObject, 0, 38)
 
def ProbOnTime(pmfObject):
    return ProbInLimits(pmfObject, 38, 41)

def ProbLate(pmfObject):
    return ProbInLimits(pmfObject, 41, 9999)

def ProbInLimits(pmfObject, lowerLimit, upperLimit):
    cumulative = 0
    for k, v in pmfObject.d.items():
        if k >= lowerLimit and k < upperLimit:
            cumulative += v
    return cumulative

def MakePmfOfAttributeFromObjects(list, attr):
    attrList = [getattr(x, attr) for x in list]
    return Pmf.MakePmfFromList(attrList)
    
def Main(name):
    records = GetData()
    firstBorn, subsequentBorn = PartitionFirstBornFromSubsequentBorn(records)
    liveBorn = firstBorn + subsequentBorn
    firstBornPmf = MakePmfOfAttributeFromObjects(firstBorn, 'prglength')
    subsequentBornPmf = MakePmfOfAttributeFromObjects(subsequentBorn, 'prglength')
    liveBornPmf = MakePmfOfAttributeFromObjects(liveBorn, 'prglength')
    print ("Early first born :        ", ProbEarly(firstBornPmf))
    print ("On time first born :      ", ProbOnTime(firstBornPmf))
    print ("Late first born :         ", ProbLate(firstBornPmf))
    print ("Early subsequent born :   ", ProbEarly(subsequentBornPmf))
    print ("On time subsequent born : ", ProbOnTime(subsequentBornPmf))
    print ("Late subsequent born :    ", ProbLate(subsequentBornPmf))
    print ("Early all live born :     ", ProbEarly(liveBornPmf))
    print ("On time all live born :   ", ProbOnTime(liveBornPmf))
    print ("Late all live born :      ", ProbLate(liveBornPmf))
    print ("Relative risk first born are early : ", ProbEarly(firstBornPmf) - ProbEarly(subsequentBornPmf))
    print ("Relative risk first born are late  : ", ProbLate(firstBornPmf) - ProbLate(subsequentBornPmf))

if __name__ == '__main__':
    Main(*sys.argv)