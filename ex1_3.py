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

def GetData():
    table = survey.Pregnancies()
    table.ReadRecords()
    return table.records

def Sum(records, attrName):
    sumPrgLengths = 0
    for record in records:
        sumPrgLengths += getattr(record, attrName)
    return sumPrgLengths

def Mean(records, attrName):
    numberRecords = len(records)
    sumRecordAttributes = Sum(records, attrName)
    meanRecordAttributes = float(sumRecordAttributes / numberRecords)
    return numberRecords, meanRecordAttributes

def Main(name):
    records = GetData()
    print ('Number of pregnancies', len(records))

    firstBorn, subsequentBorn = PartitionFirstBornFromSubsequentBorn(records)
    
    numberFirstBorn, meanFirstBornPrgLength = Mean(firstBorn, 'prglength')
    numberSubsequentBorn, meanSubsequentBornPrgLength = Mean(subsequentBorn, 'prglength')
    numberLiveBirths = numberFirstBorn + numberSubsequentBorn
    
    meanFirstBornPrgLength= timedelta(weeks = meanFirstBornPrgLength)
    meanSubsequentBornPrgLength = timedelta(weeks = meanSubsequentBornPrgLength)
    diffFirstBornToSubsequentBornPrgLength = meanFirstBornPrgLength - meanSubsequentBornPrgLength

    print ('Number of live births:               ', numberLiveBirths)
    print ('Number of live first born:           ', numberFirstBorn)
    print ('Number of live second or later born: ', numberSubsequentBorn)
    print ('Average pregnancy length of first born:           ', meanFirstBornPrgLength)
    print ('Average pregnancy length of second or later born: ', meanSubsequentBornPrgLength)
    print ('Difference in pregnancy length between first born and later born: ', diffFirstBornToSubsequentBornPrgLength)


if __name__ == '__main__':
    Main(*sys.argv)