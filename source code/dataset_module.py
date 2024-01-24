from constants import *
def transactionsDict(filename):
    userTransactions = {}
    try:
        file = open(filename,"r")
    except:
        print("Something went wrong in opening the file")
        return userTransactions
    for line in file:
        transDict = {}
        line = line.strip()
        if not line:
            continue;
        values = line.split(":")
        userId = int(values[0])
        transactionId = int(values[1])
        description = values[2]
        transactionAmount = float(values[3])
        transactionXaxis = float(values[4])
        transactionYaxis = float(values[5])
        fraudTransaction = str(values[6])
        if fraudTransaction == "true":
            fraudTrans = True
        elif fraudTransaction == "false":
            fraudTrans = False
        transDict = {
            DESCRIPTION: description,
            TRANSACTIONAMOUNT: transactionAmount,
            XCORDINATES: transactionXaxis,
            YCORDINATES: transactionYaxis,
            FRAUDTRANSACTION: fraudTrans
        }
        if userId in userTransactions:
            userTransactions[userId][transactionId] = transDict
        else:
            userTransactions[userId] = {transactionId:transDict}
    return userTransactions