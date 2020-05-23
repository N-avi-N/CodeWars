# Test cases for name sort by last name
from unittest import TestCase

class Test(TestCase):

    def test_sort_reindeer(self):
        from Sort_Santa_Reindeer import sort_reindeer
        self.assertTrue(sort_reindeer(['aa bb']) == ['aa bb'])

    def test_sort_reindeer_2(self):
        from Sort_Santa_Reindeer import sort_reindeer
        self.assertTrue(sort_reindeer(['aa bb', 'bb aa', 'cc dd', '']) == ['', 'bb aa', 'aa bb', 'cc dd'])

    def test_sort_reindeer_3(self):
        from Sort_Santa_Reindeer import sort_reindeer
        self.assertTrue(sort_reindeer(["Dasher Tonoyan", "Dancer Moore", "Prancer Chua", "Vixen Hall", "Comet Karavani", "Cupid Foroutan", "Donder Jonker", "Blitzen Claus"]) ==
                                        ["Prancer Chua", "Blitzen Claus", "Cupid Foroutan", "Vixen Hall", "Donder Jonker", "Comet Karavani", "Dancer Moore", "Dasher Tonoyan"])
