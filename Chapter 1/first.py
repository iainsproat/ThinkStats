import survey
from datetime import timedelta

def isLiveBirth(self):
    return self.outcome == 1

def isFirstBorn(self):
    return self.birthord == 1

#monkey patch
survey.Pregnancy.isLiveBirth = isLiveBirth
survey.Pregnancy.isFirstBorn = isFirstBorn

table = survey.Pregnancies()
table.ReadRecords()
print ('Number of pregnancies', len(table.records))
liveBirths = 0
firstBorn = 0
notFirstBorn = 0
sumFirstBornPrgLength = 0
sumNotFirstBornPrgLength = 0

for rec in table.records:
    if rec.isLiveBirth():
        liveBirths += 1
        if rec.isFirstBorn():
            firstBorn += 1
            sumFirstBornPrgLength += rec.prglength
        else:
            notFirstBorn += 1
            sumNotFirstBornPrgLength += rec.prglength

avgFirstBornPrgLength = timedelta(weeks = (sumFirstBornPrgLength / firstBorn))
avgNotFirstBornPrgLength = timedelta(weeks = (sumNotFirstBornPrgLength / notFirstBorn))

diff = avgFirstBornPrgLength - avgNotFirstBornPrgLength

print ('Number of live births', liveBirths)
print ('Number of live first born', firstBorn)
print ('Number of live second or later born', notFirstBorn)
print ('Average pregnancy length of first born', avgFirstBornPrgLength)
print ('Average pregnancy length of second or later born', avgNotFirstBornPrgLength)
print ('Difference in pregnancy length between first born and later born', diff)

del(isLiveBirth)
del(isFirstBorn)