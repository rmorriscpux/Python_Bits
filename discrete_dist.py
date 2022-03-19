import random, math

class DiscreteDist:
    def __init__(self, arr):
        # Type Check
        if (not (isinstance(arr, list) or isinstance(arr, tuple))):
            raise TypeError("Parameter must be a list or tuple.")
        
        self._weights = tuple(arr)

        self._sum = 0
        self._cum_weights = [] # Potentially refactor this as a property. For now I'd rather just calculate this once.

        for weight in self._weights:
            # Check each item is a positive integer.
            if (not (isinstance(weight, int) and weight > 0)):
                raise TypeError("All values in the parameter must be positive integers.")
            
            # Add the cumulative weight (current sum) to the list, then add to the sum.
            self._cum_weights.append(self._sum)
            self._sum = self._sum + weight

    def __str__(self):
        return str(self._weights)

    def GetRandomIndex(self):
        def _rGetRandomIndex(raw_random, begin_index, end_index):
            if (begin_index == end_index): # We have traced it down to the final index.
                return begin_index

            # Get the middle index, rounded down.
            pivot_index = math.floor((begin_index + end_index) / 2)

            # Determine if we're in the right spot. This will be if we're greater than or equal to the value in the pivot_index and less than the value in the next index.
            if (raw_random >= self._cum_weights[pivot_index] and raw_random < self._cum_weights[pivot_index + 1]): # We're here. Return.
                return pivot_index
            elif (raw_random < self._cum_weights[pivot_index]): # raw_random is lower, go to the lower bound.
                return _rGetRandomIndex(raw_random, begin_index, pivot_index - 1)
            else: # raw_random is higher, go to the upper bound
                return _rGetRandomIndex(raw_random, pivot_index + 1, end_index)

            return None # Should never get here.

        # Get random integer 
        raw_random = random.randrange(0, self._sum)
        # Do recursive function.
        return _rGetRandomIndex(raw_random, 0, len(self._cum_weights)-1)


if __name__ == "__main__":
    dd1 = DiscreteDist([1, 2, 3, 4])
    dd2 = DiscreteDist((5, 6, 7, 8))
    print(dd1, dd2)

    output = []
    for i in range(0, 20):
        output.append(dd1.GetRandomIndex())
    print(output)