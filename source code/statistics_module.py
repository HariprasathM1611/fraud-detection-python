from constants import *

def squareRoot(num):
    return float(num**(1/2))

def round(num):
    num = int((num*100))/100
    return num

def getTransAmount(transDict):
    amountList = []
    for transactionId in transDict.keys():
                amountList.append(transDict[transactionId][TRANSACTIONAMOUNT])
    return amountList

def getAmountList(transactions, userId=None):
    if userId: 
        if userId in transactions: 
            transAmountList = getTransAmount(transactions[userId]) 
        else: 
            return None 
    else: 
        transAmountList = [] 
        for userTransactions in transactions.values(): 
            transAmountList.extend(getTransAmount(userTransactions)) 
    return transAmountList

def findMode(transAmountList):
    freq_dict = {}
    for item in transAmountList:
        if item in freq_dict:
            freq_dict[item] += 1
        else:
            freq_dict[item] = 1 
    mode = None 
    max_freq = 0 
    for key, value in freq_dict.items(): 
        if value > max_freq:
            mode = key 
            max_freq = value
    return mode

def modeTransaction(transactions,userId = None):
    transAmountList = getAmountList(transactions,userId)
    return findMode(transAmountList)
            

def averageTransaction(transactions, userId=None):
    transAmountList = getAmountList(transactions,userId)
    totalAmount = 0.0
    for eachAmount in transAmountList:
        totalAmount = totalAmount + eachAmount
    return round(totalAmount/len(transAmountList))
        
def findMedian(transAmountList): 
    sortedTrans = sorted(transAmountList) 
    length = len(sortedTrans) 
    if length % 2 == 0: 
        median = (sortedTrans[length // 2 - 1] + sortedTrans[length // 2]) / 2 
    else: 
        median = sortedTrans[length // 2] 
    return median 

def medianTransaction(transactions, userId=None): 
    transAmountList = getAmountList(transactions,userId) 
    return round(findMedian(transAmountList))

def interquartileRangeTransaction(transactions, userId=None):
    transAmountList = getAmountList(transactions,userId) 
    sortedTrans = sorted(transAmountList) 
    n = len(sortedTrans)  
    if n % 2 == 0: 
        lower_half = sortedTrans[:n // 2] 
        upper_half = sortedTrans[n // 2:] 
    else: 
        lower_half = sortedTrans[:n // 2] 
        upper_half = sortedTrans[n // 2 + 1:] 
    q1 = findMedian(lower_half) 
    q3 = findMedian(upper_half) 
    iqr = q3 - q1 
    return round(iqr)

def getTransLocation(transDict):
    locationList = []
    for transactionId in transDict.keys():
                cordinates = [0.0,0.0]
                cordinates[0] = transDict[transactionId][XCORDINATES]
                cordinates[1] = transDict[transactionId][YCORDINATES]
                locationList.append(cordinates)
    return locationList

def getLocationList(transactions, userId=None):
    if userId: 
        if userId in transactions: 
            transAmountList = getTransLocation(transactions[userId]) 
        else: 
            return None 
    else: 
        transAmountList = [] 
        for userTransactions in transactions.values():
            transAmountList.extend(getTransLocation(userTransactions)) 
    return transAmountList

def centroidTransaction(transactions, userId = None):
    transLocationList = getLocationList(transactions,userId)
    x_value = 0.0
    y_value = 0.0
    for each in transLocationList:
        x_value = x_value + each[0]
        y_value = y_value + each[1]
    centroid = [ round(x_value/len(transLocationList)),round(y_value/len(transLocationList))]
    return centroid

def standardDeviation(transactions, userId= None):
    transAmountList = getAmountList(transactions,userId)
    mean = averageTransaction(transactions,userId)
    standardDeviation = 0.0
    for x in transAmountList:
        standardDeviation = standardDeviation + ((x - mean) ** 2)
    variance = standardDeviation/(len(transAmountList)-1)
    stdev = round(squareRoot(variance))
    return stdev

def getFraudTrans(transDict):
    fraudList = []
    for transactionId in transDict.keys():
        if transDict[transactionId][FRAUDTRANSACTION] == True:
            fraudList.append({transactionId:transDict[transactionId]})
    return fraudList      

def fraudTransaction(transactions, userId=None):
    if userId: 
        if userId in transactions: 
            fraudTrans = getFraudTrans(transactions[userId]) 
        else: 
            return None 
    else: 
        fraudTrans = [] 
        for userTransactions in transactions.values():
            fraudTrans.extend(getFraudTrans(userTransactions)) 
    return fraudTrans

def getabnormalTrans(transDict):
    abnormalTransactionList = []
    transAmountList = getTransAmount(transDict) 
    sortedTrans = sorted(transAmountList) 
    n = len(sortedTrans)  
    if n % 2 == 0: 
        lower_half = sortedTrans[:n // 2] 
        upper_half = sortedTrans[n // 2:] 
    else: 
        lower_half = sortedTrans[:n // 2] 
        upper_half = sortedTrans[n // 2 + 1:] 
    q1 = findMedian(lower_half) 
    q3 = findMedian(upper_half)
    for transactionId in transDict.keys():
        if transDict[transactionId][TRANSACTIONAMOUNT] < q1 or transDict[transactionId][TRANSACTIONAMOUNT] > q3:
            abnormalTransactionList.append({transactionId:transDict[transactionId]})
    return abnormalTransactionList

def abnormalTransaction(transactions, userId):
    if userId in transactions:
        abnormalTrans = getabnormalTrans(transactions[userId]) 
    else: 
        return None
    return abnormalTrans

def getDesc(transaction):
    descList = []
    for transactionId in transaction.keys():
        descList.append(transaction[transactionId][DESCRIPTION])
    return descList

def getDescList(transactions):
    transDescList = []
    for userTransactions in transactions.values(): 
        transDescList.extend(getDesc(userTransactions)) 
    return transDescList

def frequencyTransaction(transactions, description):
    frequency = 0
    getAllTrans = getDescList(transactions)
    for desc in getAllTrans:
        if desc == description:
            frequency = frequency + 1
    return frequency

def nthPercentile(transactions,N,userId = None):
    transAmountList = getAmountList(transactions,userId)
    transAmountList = sorted(transAmountList)
    index = int(((N/100)*len(transAmountList)*100) // 100)
    return transAmountList[index]

def zscore(transactions, userId=None):
    zscoreList = []
    transAmountList = getAmountList(transactions,userId)
    mean = averageTransaction(transactions, userId)
    stdev = standardDeviation(transactions, userId)
    for amount in transAmountList:
        zscore = (amount - mean) / stdev
        zscoreList.append(round(zscore))
    return zscoreList
def getLocationIqr(locationList, x ):
    if x == "X":
        index = 0
    elif x == "Y":
        index = 1
    cordlist = []
    for each in locationList:
        cordlist.append(each[index])
    n = len(cordlist)  
    if n % 2 == 0: 
        lower_half = cordlist[:n // 2] 
        upper_half = cordlist[n // 2:] 
    else: 
        lower_half = cordlist[:n // 2] 
        upper_half = cordlist[n // 2 + 1:] 
    q1 = findMedian(lower_half) 
    q3 = findMedian(upper_half) 
    iqr = q3 - q1 
    return iqr,q1,q3
    


def outliers(transactions, userId, threshold=1.5):
    outlierTransactions =  []
    locationList = getLocationList(transactions,userId)
    xiqr,xq1,xq3 = getLocationIqr(locationList,"X")
    yiqr,yq1,yq3 = getLocationIqr(locationList,"Y")
    xlowerthreshold = xq3 + (threshold * xiqr)
    xupperthreshold = xq1 - (threshold * xiqr)
    ylowerthreshold = yq3 + (threshold * yiqr)
    yupperthreshold = yq1 - (threshold * yiqr)
    for transactionId in transactions[userId].keys():
        x_coord = transactions[userId][transactionId][XCORDINATES]
        y_coord = transactions[userId][transactionId][YCORDINATES]
        if(x_coord < xlowerthreshold or x_coord > xupperthreshold) and (y_coord < ylowerthreshold or y_coord > yupperthreshold):
            outlierTransactions.append({transactionId : transactions[userId][transactionId]})
    return outlierTransactions

