from unittest import TestCase

class Test(TestCase):
    def test_ranges(self):
        from Stat_Ath_Assoc import ranges
        self.assertTrue(ranges([1, 2, 3, 4]) == 3)

    def test_means(self):
        from Stat_Ath_Assoc import means
        self.assertTrue(means([1, 2, 3, 4]) == 2)

    def test_medians(self):
        from Stat_Ath_Assoc import medians
        self.assertTrue(medians([1, 2, 3, 4]) == 2)

    def test_time_convert(self):
        from Stat_Ath_Assoc import time_convert
        self.assertTrue(time_convert(5554) == '01|32|34')

    def test_stat(self):
        from Stat_Ath_Assoc import stat
        self.assertTrue(stat("01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17") == 'Range: 00|47|18 Average: 01|35|15 Median: 01|32|34')