def find_max_min (seq):
    """ returns in an array containing the min and max number, respectively"""
    org_len = len(seq)
    unique_set = sorted(set(seq))
 
    length = len(unique_set)
 
    if length > 1:
      return [unique_set[0], unique_set[length-1]]
     
    return [org_len]