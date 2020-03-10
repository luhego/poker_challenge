import unittest


from poker import PokerHand, Result, card_ranks, royal_flush, straight, flush, kind, two_pair


class TestUtilFunctions(unittest.TestCase):
    def test_card_ranks(self):
        hand = ["TC", "TH", "5C", "5H", "KH"]
        self.assertEqual(card_ranks(hand), [13, 10, 10, 5, 5])

    def test_royal_flush(self):
        hand = ["TC", "QC", "KC", "AC", "JC"]
        ranks = card_ranks(hand)
        self.assertTrue(royal_flush(ranks, hand))

    def test_straight(self):
        hand = ["2C", "3H", "4C", "5H", "6C"]
        self.assertTrue(straight(card_ranks(hand)))

    def test_not_straight(self):
        hand = ["2C", "3H", "4C", "7H", "8C"]
        self.assertFalse(straight(card_ranks(hand)))

    def test_flush(self):
        hand = ["2C", "8C", "4C", "TC", "6C"]
        self.assertTrue(flush(hand))

    def test_not_flush(self):
        hand = ["2C", "8H", "4C", "TC", "6C"]
        self.assertTrue(flush(hand))

    def test_4_of_a_kind(self):
        hand = ["2C", "2H", "2C", "2S", "6C"]
        ranks = card_ranks(hand)
        self.assertEqual(kind(4, ranks), 2)

    def test_3_of_a_kind(self):
        hand = ["5C", "2H", "5C", "5S", "6C"]
        ranks = card_ranks(hand)
        self.assertEqual(kind(3, ranks), 5)

    def test_two_pair(self):
        hand = ["5C", "2H", "5C", "2S", "6C"]
        ranks = card_ranks(hand)
        self.assertEqual(two_pair(ranks), (2, 5))


class TestPoker(unittest.TestCase):
    def test_all_hands(self):
        self.assertTrue(
            PokerHand("TC TH 5C 5H KH").compare_with(PokerHand("9C 9H 5C 5H AC")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("TS TD KC JC 7C").compare_with(PokerHand("JS JC AS KC TD")) == Result.LOSS
        )
        self.assertTrue(
            PokerHand("7H 7C QC JS TS").compare_with(PokerHand("7D 7C JS TS 6D")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("5S 5D 8C 7S 6H").compare_with(PokerHand("7D 7S 5S 5D JS")) == Result.LOSS
        )
        self.assertTrue(
            PokerHand("AS AD KD 7C 3D").compare_with(PokerHand("AD AH KD 7C 4S")) == Result.LOSS
        )
        self.assertTrue(
            PokerHand("TS JS QS KS AS").compare_with(PokerHand("AC AH AS AS KS")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("TS JS QS KS AS").compare_with(PokerHand("TC JS QC KS AC")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("TS JS QS KS AS").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("AC AH AS AS KS").compare_with(PokerHand("TC JS QC KS AC")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("AC AH AS AS KS").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("TC JS QC KS AC").compare_with(PokerHand("QH QS QC AS 8H")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JC JS JD TH")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("4H 5H 9H TH JH")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("7H 8H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("JH JC JS JD TH").compare_with(PokerHand("4H 5H 9H TH JH")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("JH JC JS JD TH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("JH JC JS JD TH").compare_with(PokerHand("TS TH TD JH JD")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("JH JC JS JD TH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("7C 8S 9H TH JH")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.LOSS
        )
        self.assertTrue(
            PokerHand("4H 5H 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("TS TH TD JH JD")) == Result.LOSS
        )
        self.assertTrue(
            PokerHand("7C 8S 9H TH JH").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN
        )
        self.assertTrue(
            PokerHand("TS TH TD JH JD").compare_with(PokerHand("JH JD TH TC 4C")) == Result.WIN
        )


if __name__ == "__main__":
    unittest.main()
