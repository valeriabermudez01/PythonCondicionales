def poblacionmayor(paisA, paisB,año):
  while paisA > paisB:
    paisA+=paisA*0.02
    paisB+=paisB*0.03 
    año+=1
  return año
