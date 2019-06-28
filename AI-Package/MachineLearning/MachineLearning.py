from math import *


class item:
    def __init__(self, age, prescription, astigmatic, tearRate, needLense):
        self.age = age
        self.prescription = prescription
        self.astigmatic = astigmatic
        self.tearRate = tearRate
        self.needLense = needLense


def getDataset():
    data = []
    labels = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0]
    data.append(item(0, 0, 0, 0, labels[0]))
    data.append(item(0, 0, 0, 1, labels[1]))
    data.append(item(0, 0, 1, 0, labels[2]))
    data.append(item(0, 0, 1, 1, labels[3]))
    data.append(item(0, 1, 0, 0, labels[4]))
    data.append(item(0, 1, 0, 1, labels[5]))
    data.append(item(0, 1, 1, 0, labels[6]))
    data.append(item(0, 1, 1, 1, labels[7]))
    data.append(item(1, 0, 0, 0, labels[8]))
    data.append(item(1, 0, 0, 1, labels[9]))
    data.append(item(1, 0, 1, 0, labels[10]))
    data.append(item(1, 0, 1, 1, labels[11]))
    data.append(item(1, 1, 0, 0, labels[12]))
    data.append(item(1, 1, 0, 1, labels[13]))
    data.append(item(1, 1, 1, 0, labels[14]))
    data.append(item(1, 1, 1, 1, labels[15]))
    data.append(item(1, 0, 0, 0, labels[16]))
    data.append(item(1, 0, 0, 1, labels[17]))
    data.append(item(1, 0, 1, 0, labels[18]))
    data.append(item(1, 0, 1, 1, labels[19]))
    data.append(item(1, 1, 0, 0, labels[20]))
    return data


class Feature:
    def __init__(self, name):
        self.name = name
        self.visited = -1
        self.infoGain = -1


class ID3:
    def __init__(self, features):
        self.features = features

    def calcEntropy(self, numOf0, numOf1, total):
        # to handel log0
        if numOf0 == 0:
            return ((numOf1 / total) * log2(numOf1 / total))
        if numOf1 == 0:
            return ((numOf0 / total) * log2(numOf0 / total))

        return (-(numOf0 / total) * log2(numOf0 / total)) + (-(numOf1 / total) * log2(numOf1 / total))

    def calcGain(self, totalEntropy, Total1, Total2, Entropy1, Entropy2, tempDataset):
        infoGain = totalEntropy - (((Total1 / len(tempDataset)) * Entropy1) + ((Total2 / len(tempDataset)) * Entropy2))
        return infoGain

    def getNewData(self, index, inputValue, tempDataset):
        newData = []
        for x in range(len(tempDataset)):
            #####################Age####################
            if index == 0 and inputValue == 0 and tempDataset[x].age == 0:
                newData.append(tempDataset[x])
            elif index == 0 and inputValue == 1 and tempDataset[x].age == 1:
                newData.append(tempDataset[x])

            ################Prescription#################
            elif index == 1 and inputValue == 0 and tempDataset[x].prescription == 0:
                newData.append(tempDataset[x])
            elif index == 1 and inputValue == 1 and tempDataset[x].prescription == 1:
                newData.append(tempDataset[x])

            ################Astigmatic####################
            elif index == 2 and inputValue == 0 and tempDataset[x].astigmatic == 0:
                newData.append(tempDataset[x])
            elif index == 2 and inputValue == 1 and tempDataset[x].astigmatic == 1:
                newData.append(tempDataset[x])

            #################TearRate####################
            elif index == 3 and inputValue == 0 and tempDataset[x].tearRate == 0:
                newData.append(tempDataset[x])
            elif index == 3 and inputValue == 1 and tempDataset[x].tearRate == 1:
                newData.append(tempDataset[x])
        return newData

    def getMaxGain(self, input, newDataset):
        # da hayb2a fe function lwa7do a3tkd
        tempData = newDataset.copy()
        # forTotalEntropy
        noLense, needLense = 0, 0

        # age
        youngTotal, youngNoLense, youngNeedLense, adultTotal, adultNoLense, adultNeedLense = 0, 0, 0, 0, 0, 0

        # prescription
        myopeTotal, myopeNoLense, myopeNeedLense, hyperTotal, hyperNoLense, hyperNeedLense = 0, 0, 0, 0, 0, 0

        # astigmatic
        astigmaticNoTotal, astigmaticNONoLense, astigmaticNONeedLense, astigmaticYesTotal, astigmaticYesNoLense, astigmaticYesNeedLense = 0, 0, 0, 0, 0, 0

        # tearRate
        normalTotal, normalNoLense, normalNeedLense, reducedTotal, reducedNoLense, reducedNeedLense = 0, 0, 0, 0, 0, 0

        for x in range(len(newDataset)):
            ###############totalEntropy#################
            if newDataset[x].needLense == 0:
                noLense += 1
            elif newDataset[x].needLense == 1:
                needLense += 1
            #####################Age####################
            if newDataset[x].age == 0 and features[0].visited == -1:
                youngTotal += 1
                if newDataset[x].needLense == 0:
                    youngNoLense += 1
                else:
                    youngNeedLense += 1
            elif newDataset[x].age == 1 and features[0].visited == -1:
                adultTotal += 1
                if newDataset[x].needLense == 0:
                    adultNoLense += 1
                else:
                    adultNeedLense += 1
            ################Prescription#################
            if newDataset[x].prescription == 0 and features[1].visited == -1:
                myopeTotal += 1
                if newDataset[x].needLense == 0:
                    myopeNoLense += 1
                else:
                    myopeNeedLense += 1
            elif newDataset[x].prescription == 1 and features[1].visited == -1:
                hyperTotal += 1
                if newDataset[x].needLense == 0:
                    hyperNoLense += 1
                else:
                    hyperNeedLense += 1
            ################Astigmatic####################
            if newDataset[x].astigmatic == 0 and features[2].visited == -1:
                astigmaticNoTotal += 1
                if newDataset[x].needLense == 0:
                    astigmaticNONoLense += 1
                else:
                    astigmaticNONeedLense += 1
            elif newDataset[x].astigmatic == 1 and features[2].visited == -1:
                astigmaticYesTotal += 1
                if (newDataset[x].needLense == 0):
                    astigmaticYesNoLense += 1
                else:
                    astigmaticYesNeedLense += 1
            #################TearRate####################
            if newDataset[x].tearRate == 0 and features[3].visited == -1:
                normalTotal += 1
                if newDataset[x].needLense == 0:
                    normalNoLense += 1
                else:
                    normalNeedLense += 1
            elif newDataset[x].tearRate == 1 and features[3].visited == -1:
                reducedTotal += 1
                if newDataset[x].needLense == 0:
                    reducedNoLense += 1
                else:
                    reducedNeedLense += 1
        ############################################################
        ageGain = prescriptionGain = astigmaticGain = tearRateGain = -1  # ba set el gain b -1 3shan lw mat7sbsh may5dhosh maximum mn kemto el adema

        totalEntropy = self.calcEntropy(noLense, needLense, noLense + needLense)

        if features[0].visited == -1:
            youngEntropy = self.calcEntropy(youngNoLense, youngNeedLense, youngTotal)
            adultEntropy = self.calcEntropy(adultNoLense, adultNeedLense, adultTotal)
            ageGain = self.calcGain(totalEntropy, youngTotal, adultTotal, youngEntropy, adultEntropy, tempData)
        if features[1].visited == -1:
            myopeEntropy = self.calcEntropy(myopeNoLense, myopeNeedLense, myopeTotal)
            hyperEntropy = self.calcEntropy(hyperNoLense, hyperNeedLense, hyperTotal)
            prescriptionGain = self.calcGain(totalEntropy, myopeTotal, hyperTotal, myopeEntropy, hyperEntropy, tempData)
        if features[2].visited == -1:
            astigmaticNOEntropy = self.calcEntropy(astigmaticNONoLense, astigmaticNONeedLense, astigmaticNoTotal)
            astigmaticYesEntropy = self.calcEntropy(astigmaticYesNoLense, astigmaticYesNeedLense, astigmaticYesTotal)
            astigmaticGain = self.calcGain(totalEntropy, astigmaticNoTotal, astigmaticYesTotal, astigmaticNOEntropy,
                                           astigmaticYesEntropy, tempData)
        if features[3].visited == -1:
            normalEntropy = self.calcEntropy(normalNoLense, normalNeedLense, normalTotal)
            reducedEntropy = self.calcEntropy(reducedNoLense, reducedNeedLense, reducedTotal)
            tearRateGain = self.calcGain(totalEntropy, normalTotal, reducedTotal, normalEntropy, reducedEntropy,
                                         tempData)

        # ba set el values ele f class feature b el gain  bta3 kol wa7da
        self.features[0].infoGain = ageGain
        self.features[1].infoGain = prescriptionGain
        self.features[2].infoGain = astigmaticGain
        self.features[3].infoGain = tearRateGain

        maximumGain = max(self.features[0].infoGain, self.features[1].infoGain, self.features[2].infoGain,
                          self.features[3].infoGain)

        for i in range(len(newDataset)):
            if self.features[0].infoGain == maximumGain and (
                    youngTotal == youngNoLense or youngTotal == youngNeedLense) and input[0] == 0:
                return newDataset[i].needLense
            elif self.features[0].infoGain == maximumGain and (
                    adultTotal == adultNoLense or adultTotal == adultNeedLense) and input[0] == 1:
                return newDataset[i].needLense
            elif self.features[1].infoGain == maximumGain and (
                    myopeTotal == myopeNoLense or myopeTotal == myopeNeedLense) and input[1] == 0:
                return newDataset[i].needLense
            elif self.features[1].infoGain == maximumGain and (
                    hyperTotal == hyperNoLense or hyperTotal == hyperNeedLense) and input[1] == 1:
                return newDataset[i].needLense

            elif self.features[2].infoGain == maximumGain and (
                    astigmaticNoTotal == astigmaticNONoLense or astigmaticNoTotal == astigmaticNONeedLense) and input[
                2] == 0:
                return newDataset[i].needLense
            elif self.features[2].infoGain == maximumGain and (
                    astigmaticYesTotal == astigmaticYesNoLense or astigmaticYesTotal == astigmaticYesNeedLense) and \
                    input[2] == 1:
                return newDataset[i].needLense

            elif self.features[3].infoGain == maximumGain and (
                    normalTotal == normalNoLense or normalTotal == normalNeedLense) and input[3] == 0:
                return newDataset[i].needLense
            elif self.features[3].infoGain == maximumGain and (
                    reducedTotal == reducedNoLense or reducedTotal == reducedNeedLense) and input[3] == 1:
                return newDataset[i].needLense

        ################### bnshuf el max gain lw msh pure sa3tha h-recursive w a5leeh visited#############
        newDataset = []
        if features[0].infoGain == maximumGain:
            features[0].visited = 1
            newDataset = self.getNewData(0, input[0], tempData)
            return self.getMaxGain(input, newDataset)
        elif features[1].infoGain == maximumGain:
            features[1].visited = 1
            newDataset = self.getNewData(1, input[1], tempData)
            return self.getMaxGain(input, newDataset)
        elif features[2].infoGain == maximumGain:
            features[2].visited = 1
            newDataset = self.getNewData(2, input[2], tempData)
            return self.getMaxGain(input, newDataset)
        elif features[3].infoGain == maximumGain:
            features[3].visited = 1
            newDataset = self.getNewData(3, input[3], tempData)
            return self.getMaxGain(input, newDataset)

    def classify(self, input):
        # takes an array for the features ex. [0, 0, 1, 1]
        # should return 0 or 1 based on the classification
        features[0].infoGain = features[1].infoGain = features[2].infoGain = features[3].infoGain = -1
        features[0].visited = features[1].visited = features[2].visited = features[3].visited = -1

        return self.getMaxGain(input, dataset)


dataset = getDataset()
features = [Feature('age'), Feature('prescription'), Feature('astigmatic'), Feature('tearRate')]
id3 = ID3(features)
cls = id3.classify([0, 0, 1, 1])  # should print 1
print('testcase 1: ', cls)
cls = id3.classify([1, 1, 0, 0])  # should print 0
print('testcase 2: ', cls)
cls = id3.classify([1, 1, 1, 0])  # should print 0
print('testcase 3: ', cls)
cls = id3.classify([1, 1, 0, 1])  # should print 1
print('testcase 4: ', cls)
