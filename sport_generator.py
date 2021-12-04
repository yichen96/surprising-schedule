import random

def ceil_index(target, array):
    """
    find ceil index of target number in array using bisection
    
    Parameters
    ----------
    target: float
        a number that will be compared to items in input array.
    array : list of float
        
    Return
    ----------
    index: int
        the ceil index of target in the array 
    """
    start_ind = 0
    end_ind = len(array) - 1
    while start_ind < end_ind:
        mid = int((start_ind+end_ind) / 2)
        if target > array[mid]:
            start_ind = mid+1
        else:
            end_ind = mid
    return start_ind if array[start_ind] >= target else -1


class RandomCardio(object):
    # Values that may be returned by next_num()
    _random_nums = ["running","cycling","swimming"]
    # Probability of the occurence of random_nums
    _probabilities = [0.4,0.1,0.5]
    _cumulative_probs = [0.4,0.5,1]
    _prev = None
    def next(self):
        """
        Returns one of the randomNums. When this method is called
        multiple times over a long period, it should return the
        numbers roughly with the initialized probabilities.
        """
        ran_num = random.random()
        index = ceil_index(ran_num, self._cumulative_probs)
        next_activity = self._random_nums[index]
        if next_activity == "running" and self._prev == "running":
            return self.next()
        else:
            self._prev = next_activity
            return next_activity

class RandomBodyPart(object):
    # Values that may be returned by next_num()
    _random_nums = ["back","shoulder","legs","chest"]
    # Probability of the occurence of random_nums
    _probabilities = [0.3,0.3,0.2,0.1]
    _cumulative_probs = [0.3,0.6,0.8,1]
    _prev = None
    def next(self):
        """
        Returns one of the randomNums. When this method is called
        multiple times over a long period, it should return the
        numbers roughly with the initialized probabilities.
        """
        ran_num = random.random()
        index = ceil_index(ran_num, self._cumulative_probs)
        next_activity = self._random_nums[index]
        if next_activity is not None and self._prev == next_activity:
            return self.next()
        else:
            self._prev = next_activity
            return next_activity
