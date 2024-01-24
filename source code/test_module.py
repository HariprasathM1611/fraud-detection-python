import dataset_module
import distance_module as dm
import statistics_module as sm
option=['1=Distance_module','2=Statistics_module']
for i in option:
    print(i)
n=input("Choose option from above:")
case=n
data = dataset_module.transactionsDict(r"/Users/haripotter/Downloads/Assignment1_dataset 5/transaction.txt")
match case:
    case "1":
        n=int(input("select the operation to perform \n1-Distance Between Same User 2-Distance Between Different User: "))
        if(n==1):
          userid=int(input("enter the UserId: "))
          TransId_1=int(input("enter the TransId_1: "))
          TransId_2=int(input("enter the TransId_2: "))
          a=data
          sameuser=dm.distBetweenSameUserTrans(userid,TransId_1,TransId_2,a)
          print("Distance Between Transaction is: ",sameuser)
        elif(n==2):
          userid_1=int(input("enter the UserId_1: "))
          userid_2=int(input("enter the UserId_2: "))
          TransId_1=int(input("enter the TransId_1: "))
          TransId_2=int(input("enter the TransId_2: "))
          a=data
          diffuser=dm.distBetweenDiffUserTrans(userid_1,TransId_1,userid_2,TransId_2,a)
          print("Distance Between Transaction is:",diffuser)
        else:
           print("Wrong input")
            
    case "2":
        stat_option=['1 - Average Transaction','2 - Mode transaction','3 - Median Transaction', '4 - Inter Quartile Range Transaction','5 - Location Centroid Transaction','6 - Standart Deviation Transaction','7 - Fraud Transaction','8 - Abnormal Transaction','9 - Z Score Transaction','10 - Frequency Transaction','11 - Outlier Transaction','12 - Nth Percentiles Transaction']
        for i in stat_option:
           print(i)
        n=input("Choose option from above:")
        statoption=n 
        match statoption:
          case "1":
            n=int(input("select the operation to perform 1-With UserId  2-Without UserId: "))
            if(n==1):
               userid=int(input("enter the UserId: "))
               a=data
               avg=sm.averageTransaction(a,userid)
               print("Average Transaction is:",avg)
            elif(n==2):
               a=data
               avg=sm.averageTransaction(a)
               print("Average Transaction is:",avg)
            else:
               print("Wrong input")
               
          case "2":
              n=int(input("select the operation to perform 1-With UserId  2-Without UserId: "))
              if(n==1):
               userid=int(input("enter the UserId: "))
               a=data
               mde=sm.modeTransaction(a,userid,)
               print("Mode Transaction is:",mde)
              elif(n==2):
               a=data
               mde=sm.modeTransaction(a)
               print("Mode Transaction is:",mde)
              else:
               print("Wrong input")
            
            
          case "3":
            n=int(input("select the operation to perform 1-With UserId  2-Without UserId: "))
            if(n==1):
               userid=int(input("enter the UserId: "))
               a=data
               median=sm.medianTransaction(a,userid)
               print("Median Transaction is:",median)
            elif(n==2):
               a=data
               median=sm.medianTransaction(a)
               print("Median Transaction is:",median)
            else:
               print("Wrong input")
          case "4":
            n=int(input("select the operation to perform 1-With UserId  2-Without UserId: "))
            if(n==1):
               userid=int(input("enter the UserId: "))
               a=data
               iqr=sm.interquartileRangeTransaction(a,userid)
               print("Inter Quartile Range of Transaction is:",iqr)
            elif(n==2):
               a=data
               iqr=sm.interquartileRangeTransaction(a)
               print("Inter Quartile Range of Transaction is:",iqr)
            else:
               print("Wrong input")
          case "5":
            n=int(input("select the operation to perform 1-With UserId  2-Without UserId: "))
            if(n==1):
               userid=int(input("enter the UserId: "))
               a=data
               loccen=sm.centroidTransaction(a,userid)
               print("Centroid of Transaction is:",loccen)
            elif(n==2):
               a=data
               loccen=sm.centroidTransaction(a)
               print("Centroid of Transaction is:",loccen)
            else:
               print("Wrong input")
          case "6":
            n=int(input("select the operation to perform 1-With UserId  2-Without UserId: "))
            if(n==1):
               userid=int(input("enter the UserId: "))
               a=data
               stddev=sm.standardDeviation(a,userid)
               print("Standard Deviation of Transaction is:",stddev)
            elif(n==2):
               a=data
               stddev=sm.standardDeviation(a)
               print("Standard Deviation of Transaction is:",stddev)
            else:
               print("Wrong input")
          case "7":
            n=int(input("select the operation to perform 1-With UserId  2-Without UserId: "))
            if(n==1):
               userid=int(input("enter the UserId: "))
               a=data
               b=sm.fraudTransaction(a,userid)
               print("Fraud Transactions are:",b)
            elif(n==2):
               a=data
               b=sm.fraudTransaction(a)
               print("Fraud Transactions are:",b)
            else:
               print("Wrong input")
          case "8":
            n=int(input("select the operation to perform 1-With UserId  2-Without UserId: "))
            if(n==1):
               userid=int(input("enter the UserId: "))
               a=data
               b=sm.abnormalTransaction(a,userid)
               print("Abnormal Transactions are: ",b)
            elif(n==2):
               a=data
               b=sm.abnormalTransaction(a)
               print("Abnormal Transactions are: ",b)
            else:
               print("Wrong input")
          case "9":
            n=int(input("select the operation to perform 1-With UserId  2-Without UserId: "))
            if(n==1):
               userid=int(input("enter the UserId: "))
               a=data
               b=sm.zscore(a,userid)
               print("Z Score of Transactions are: ",b)
            elif(n==2):
               a=data
               b=sm.zscore(a)
               print("Z Score of Transactions are: ",b)
            else:
               print("Wrong input")
          case "10":
            n=int(input("select the operation to perform 1-With Descrption  2-Without Description: "))
            if(n==1):
               desc=str(input("enter the UserId: "))
               a=data
               b=sm.frequencyTransaction(a,desc)
               print("frequency of Transactions are: ",b)
            elif(n==2):
               a=data
               b=sm.frequencyTransaction(a)
               print("Frequency of Transactions are: ",b)
            else:
               print("Wrong input")
          case "11":
            n=int(input("press 1 to continue: "))
            if(n==1):
               userid=int(input("enter the UserId: "))
               a=data
               b=sm.outliers(a,userid)
               print("outliers of Transactions are: ",b)
            else:
               print("Wrong input")
          case "12":
            n=int(input("select the operation to perform 1-With UserId  2-Without UserId: "))
            if(n==1):
               userid=int(input("enter the UserId: "))
               a=data
               N=int(input("Enter the N Value"))
               b=sm.nthPercentile(a,N,userid)
               print("Z Score of Transactions are: ",b)
            elif(n==2):
               a=data
               b=sm.zscore(a)
               print("Z Score of Transactions are: ",b)
            else:
               print("Wrong input")
          case _:
            print("Code not found")
        
    case _:
        print("Code not found")