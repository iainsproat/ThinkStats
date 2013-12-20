import math
import sys
from datetime import timedelta
import survey
import thinkstats
from ex1_3 import GetData, Mean, PartitionFirstBornFromSubsequentBorn

def Variance(records, attrName, mean=None):
    if mean == None:
        numRecords, mean = Mean(records, attrName)
    
    itemVariances = [(getattr(record, attrName) - mean)**2 for record in records]
    variance = thinkstats.Mean(itemVariances)
    return numRecords, mean, variance

def StandardDeviationFromVariance(variance):
    return math.sqrt(variance)

def StandardDeviation(records, mean=None):
    numRecords, mean, variance = Variance(records, mean)
    standardDeviation = StandardDeviationFromVariance(variance)
    return numRecords, mean, standardDeviation, variance

def Main(name):
    records = GetData()
    firstBorn, subsequentBorn = PartitionFirstBornFromSubsequentBorn(records)
    numberFirstBorn, meanFirstBornPrgLength, varianceFirstBornPrgLength = Variance(firstBorn, 'prglength')
    numberSubsequentBorn, meanSubsequentBornPrgLength, varianceSubsequentBornPrgLength = Variance(subsequentBorn, 'prglength')
    print("Variance in first born pregnancy length :            ", varianceFirstBornPrgLength)
    print("Variance in second and later born pregnancy length : ", varianceSubsequentBornPrgLength)
    print("Standard Deviation in first born pregnancy length :            ", timedelta(weeks = StandardDeviationFromVariance(varianceFirstBornPrgLength)))
    print("Standard Deviation in second and later born pregnancy length : ", timedelta(weeks = StandardDeviationFromVariance(varianceSubsequentBornPrgLength)))

if __name__ == '__main__':
    Main(*sys.argv)