"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    # Return Rounds
    rounds = [number, number + 1, number + 2]
    return rounds


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    # Return Rounds Concatenated
    rounds = rounds_1 + rounds_2
    return rounds


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    # Check & Return Rounds Played
    if number in rounds:
        return True
    return False

def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    # Return Cards Average
    average = sum(hand) / len(hand)
    return average


def approx_average_is_average(hand):
    """Return if an average is using (first + last index values ) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    # Calculate Approximate Averages
    first_last = card_average([hand[0], hand[-1]])
    median = hand[len(hand) // 2]
    if first_last == card_average(hand) or median == card_average(hand):
        return True
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    # Check If Evens and Odds Averages Are Equal
    evens = [value for (index, value) in enumerate(hand) if index % 2 == 0]
    odds = [number for number in hand if number not in evens]
    if card_average(evens) == card_average(odds):
        return True
    return False 


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    # Double Jack Value In Hand
    if hand[-1] == 11:
        hand[-1] = 11 * 2
    return hand
    
