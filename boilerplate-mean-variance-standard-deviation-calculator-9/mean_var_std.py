import numpy as np

def calculate(list):

  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
  else:
    np_array = np.array(list)
    print(np_array)

    mean1 = [np_array[[0,1,2]].mean(),np_array[[3,4,5]].mean(),np_array[[6,7,8]].mean()]

    mean2 = [np_array[[0,3,6]].mean(),np_array[[1,4,7]].mean(),np_array[[2,5,8]].mean()]
    
    variance1 =[np_array[[0,3,6]].var(),np_array[[1,4,7]].var(),np_array[[2,5,8]].var()]

    variance2 = [np_array[[0,1,2]].var(),np_array[[3,4,5]].var(),np_array[[6,7,8]].var()]

    sd1 = [np_array[[0,3,6]].std(),np_array[[1,4,7]].std(),np_array[[2,5,8]].std()]

    sd2 =  [np_array[[0,1,2]].std(),np_array[[3,4,5]].std(),np_array[[6,7,8]].std()]


    amax1 =  [np_array[[0,3,6]].max(),np_array[[1,4,7]].max(),np_array[[2,5,8]].max()]

    amax2 = [np_array[[0,1,2]].max(),np_array[[3,4,5]].max(),np_array[[6,7,8]].max()]

    amin1 =  [np_array[[0,3,6]].min(),np_array[[1,4,7]].min(),np_array[[2,5,8]].min()]

    amin2 = [np_array[[0,1,2]].min(),np_array[[3,4,5]].min(),np_array[[6,7,8]].min()]

    sum1 = [np_array[[0,3,6]].sum(),np_array[[1,4,7]].sum(),np_array[[2,5,8]].sum()]

    sum2 = [np_array[[0,1,2]].sum(),np_array[[3,4,5]].sum(),np_array[[6,7,8]].sum()]
    return{
      'mean': [mean2,mean1,np_array.mean()],
      'variance': [variance1, variance2 , np_array.var()],
      'standard deviation': [sd1 , sd2 , np_array.std()],
      'max': [amax1 , amax2 , np_array.max()],
      'min': [amin1 , amin2 , np_array.min()],
      'sum': [sum1 , sum2 , np_array.sum()]
    }