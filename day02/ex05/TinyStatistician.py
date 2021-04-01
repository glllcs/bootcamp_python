from typing import List, Union
from functools import reduce
from math import sqrt


class TinyStatistician:
    @staticmethod
    def mean(nbr_list: List = None) -> Union[float, None]:
        """
        Computes the mean of a given non-empty array nbr_list and returns the
        mean as a float, otherwise None if nbr_list is an empty array.
        """
        if nbr_list == None:
            return None
        nbr_sum = reduce(lambda x, y: x + y, nbr_list)
        return nbr_sum / len(nbr_list)

    @staticmethod
    def median(nbr_list: List = None) -> Union[float, None]:
        """
        Computes the median, also called the 50th percentile, of a given
        non-empty darray nbr_list and returns the median as a float,
        otherwise None if nbr_list is an empty array.
        """
        if nbr_list == None:
            return None
        nbr_list.sort()
        len_nbr_list = len(nbr_list)
        if len_nbr_list % 2 != 0:
            return nbr_list[len_nbr_list // 2]
        else:
            middle = len_nbr_list // 2
            return (nbr_list[middle] + nbr_list[middle - 1]) / 2

    @staticmethod
    def quartile(nbr_list: List = None,
                 percentile: int = 0) -> Union[float, None]:
        """
        Computes the 1st and 3rd quartiles, also called the 25th percentile and
        the 75th percentile, of a given non-empty array nbr_list and
        returns the quartile as a float, otherwise None if nbr_list is an empty
        array.
        The first parameter is the array and the second parameter is the 
        expected percentile.
        """
        if nbr_list == None:
            return None
        nbr_list.sort()
        return (float(nbr_list[int(percentile / 100 * len(nbr_list))]))

    def var(self, nbr_list: List = None) -> Union[float, None]:
        """
        Computes the variance of a given non-empty array nbr_list and
        returns the variance as a float, otherwise None if nbr_list is an
        empty array.
        """
        if nbr_list == None:
            return None
        mean = self.mean(nbr_list)

        var = 0
        for nbr in nbr_list:
            var += pow((nbr - mean), 2)

        return var / len(nbr_list)

    def std(self, nbr_list: List = None) -> Union[float, None]:
        """
        Computes the standard deviation of a given non-empty array nbr_list and
        returns the standard deviation as a float, otherwise None if nbr_list
        is an empty array.
        """
        if nbr_list == None:
            return None
        var = self.var(nbr_list)

        return sqrt(var)
