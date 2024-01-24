from constants import *
def squareRoot(num):
    return float(num**(1/2))

def round(num):
    num = int((num*100))/100
    return num

def euclideanDistance(x1, y1, x2, y2): 
    dx = x2 - x1 
    dy = y2 - y1 
    return round(squareRoot(dx*dx + dy*dy))

def findDistance(transDict1,transDict2):
    return euclideanDistance(transDict1[XCORDINATES],transDict1[YCORDINATES],transDict2[XCORDINATES],transDict2[YCORDINATES])
    
def distBetweenSameUserTrans(user_id, transaction_id_1, transaction_id_2, transactions):
    return findDistance(transactions[user_id][transaction_id_1],transactions[user_id][transaction_id_2])


def distBetweenDiffUserTrans(user_id_1, transaction_id_1, user_id_2, transaction_id_2, transactions):
    return findDistance(transactions[user_id_1][transaction_id_1],transactions[user_id_2][transaction_id_2])