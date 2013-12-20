import survey
import sys
from datetime import timedelta

def IsLiveBirth(self):
    return self.outcome == 1

def IsFirstBorn(self):
    return self.birthord == 1

def MonkeyPatch():
    global IsLiveBirth
    global IsFirstBorn
    survey.Pregnancy.IsLiveBirth = IsLiveBirth
    survey.Pregnancy.IsFirstBorn = IsFirstBorn

def CleanupMonkeyPatching():
    global IsLiveBirth
    global IsFirstBorn
    del(IsLiveBirth)
    del(IsFirstBorn)

def PartitionFirstBornFromSubsequentBorn(records):
    MonkeyPatch()
    firstBorn = []
    subsequentBorn = []
    for record in records:
        if not record.IsLiveBirth():
            continue
            
        if record.IsFirstBorn():
            firstBorn.append(record)
        else:
            subsequentBorn.append(record)
                
    CleanupMonkeyPatching()
    return firstBorn, subsequentBorn

def SumPregnancyLength(records):
    sumPrgLengths = 0
    for record in records:
        sumPrgLengths += record.prglength
    return sumPrgLengths

def main(name):

    table = survey.Pregnancies()
    table.ReadRecords()
    print ('Number of pregnancies', len(table.records))

    firstBorn, subsequentBorn = PartitionFirstBornFromSubsequentBorn(table.records)
    
    numberFirstBorn = len(firstBorn)
    numberSubsequentBorn = len(subsequentBorn)
    numberLiveBirths = numberFirstBorn + numberSubsequentBorn
    
    sumFirstBornPrgLength = SumPregnancyLength(firstBorn)
    sumSubsequentBornPrgLength = SumPregnancyLength(subsequentBorn)

    avgFirstBornPrgLength = timedelta(weeks = (sumFirstBornPrgLength / numberFirstBorn))
    avgSubsequentBornPrgLength = timedelta(weeks = (sumSubsequentBornPrgLength / numberSubsequentBorn))

    diffFirstBornToSubsequentBornPrgLength = avgFirstBornPrgLength - avgSubsequentBornPrgLength

    print ('Number of live births:               ', numberLiveBirths)
    print ('Number of live first born:           ', numberFirstBorn)
    print ('Number of live second or later born: ', numberSubsequentBorn)
    print ('Average pregnancy length of first born:           ', avgFirstBornPrgLength)
    print ('Average pregnancy length of second or later born: ', avgSubsequentBornPrgLength)
    print ('Difference in pregnancy length between first born and later born: ', diffFirstBornToSubsequentBornPrgLength)


if __name__ == '__main__':
    main(*sys.argv)