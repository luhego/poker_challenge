from collections import Counter
from enum import Enum


class Result(Enum):
    WIN = 0
    LOSS = 1


def card_ranks(hand):
    """
    Return a list of the ranks, sorted with higher first.
    """
    ranks = ["--23456789TJQKA".index(rank) for rank, suit in hand]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if ranks == [14, 5, 4, 3, 2] else ranks


def royal_flush(ranks, hand):
    """
    Return True if it is a straight, a flush and the card ranks are [14, 13, 12, 11, 10].
    """
    return straight(ranks) and flush(hand) and ranks == [14, 13, 12, 11, 10]


def straight(ranks):
    """
    Return True if the ordered ranks form a 5-card straight.
    """
    return all([ranks[i] == ranks[i - 1] - 1 for i in range(1, len(ranks))])


def flush(hand):
    """
    Return True if all the cards have the same suit
    """
    return len(set(suit for rank, suit in hand)) == 1


def kind(n, ranks):
    """
    Return the first rank that this hand has exactly n of.
    Return None if there is no a n-of-a-kind in the hand.
    """
    counter = Counter(ranks)
    sorted_counter = sorted(counter.items(), reverse=True)
    for num, freq in sorted_counter:
        if freq == n:
            return num
    return None


def two_pair(ranks):
    """
    Check if there are a two pair. If so, return the two ranks as a tuple: (highest, lowest).
    Otherwise, return None.
    """
    highest = kind(2, ranks)
    lowest = kind(2, list(reversed(ranks)))
    if highest and lowest and highest != lowest:
        return highest, lowest
    return None


def hand_rank(hand):
    """
    Return a tuple indicating the ranking of a hand. The first values is the main ranking.
    If there is a tie, we use the remaining tuple elements.
    We will use this ranking to compare hands.
    """
    ranks = card_ranks(hand)
    if royal_flush(ranks, hand):                          # royal flush
        return 9,
    elif straight(ranks) and flush(hand):                 # straight flush
        return 8, max(ranks)
    elif kind(4, ranks):                                  # 4 of a kind
        return 7, kind(4, ranks), kind(1, ranks)
    elif kind(3, ranks) and kind(2, ranks):               # full house
        return 6, kind(3, ranks), kind(2, ranks)
    elif flush(hand):                                     # flush
        return 5, ranks
    elif straight(ranks):                                 # straight
        return 4, max(ranks)
    elif kind(3, ranks):                                  # 3 of a kind
        return 3, kind(3, ranks), ranks
    elif two_pair(ranks):                                 # 2 pair
        return 2, two_pair(ranks), ranks
    elif kind(2, ranks):                                  # kind
        return 1, kind(2, ranks), ranks
    else:                                                 # high card
        return 0, ranks


class PokerHand:
    def __init__(self, hand):
        self.hand = hand.split()
        self.ranking = hand_rank(self.hand)

    def compare_with(self, other_poker_hand):
        """
        We compare the current poker ranking hand with the given poker hand raking.
        If the current poker hand ranking is greater, we return Result.WIN.
        Otherwise, we return Result.LOSS.
        """
        return Result.WIN if self.ranking > other_poker_hand.ranking else Result.LOSS
