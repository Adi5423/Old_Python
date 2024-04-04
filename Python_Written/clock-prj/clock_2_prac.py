import time
sec_2 = 0.0 
sec = 0.0 
aar : float 
aar = 0.0
tr = input("Enter The Time!! in Hours or Minutes=")
if 'hr' in tr:
    re = tr.rstrip("hr")
    rr = float(re)
    rr += 0
    ser = rr*60
    print("In Hours = " , rr, "\n" , "In Minutes = " ,  ser , "\n")
    time.sleep(1.5)
    print("Ohkh!! You Will be ALERTED after " ,int(re), "Hours!! or" , int(ser), " Minutes!! \n" )
    sec = float(ser/60)
    time.sleep(sec)
    print("Time Out user!! Completed " , ser ,"Minutes!!\n")
    print("Wake Up Buddy!!")
elif 'min' in tr:
    ae = tr.rstrip("min")
    aer = float(ae)
    if aer == 60.0 or aer > 60.0:
       aer += 0
       aar = aer/60
       print("In Minutes = " , ae , "\n" , "In Hours = " ,  str(aar) , "\n")
       time.sleep(1.5)
       print("Ohkh!! You Will be ALERTED after " ,int(ae), "Minutes!! or " , int(aar), "Hours!!\n" )
       sec2 = float(aer/60)
       time.sleep(sec2)
       print("Time Out user!! Completed " , aar ,"Hours!!\n")
       print("Wake Up Buddy!!")
    else:
       print("In Minutes = " , ae, "\n")
       time.sleep(1.5)
       print("Ohkh!! You Will be ALERTED after " ,int(ae), "Minutes!! \n" )
       sec_2 = float(ae*60)
       time.sleep(sec_2)
       print("Time Out user!! Completed " , ae ,"Minutes!!\n")
       print("Wake Up Buddy!!")