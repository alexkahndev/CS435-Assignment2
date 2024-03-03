import random


def generate_random_preferences(n):
    # Generate a list of preferences for each man and woman in the range n
    men_preferences = [random.sample(range(n), n) for _ in range(n)]
    women_preferences = [random.sample(range(n), n) for _ in range(n)]
    return men_preferences, women_preferences


def is_stable(men_engaged, men_preferences, women_preferences):
    # Iterate over each man and his engaged woman
    for man, woman in enumerate(men_engaged):
        # Find the position of the current man in this woman's preference list
        i = women_preferences[woman].index(man)
        # Get all men who are preferred by this woman over the current man
        preferred_men = women_preferences[woman][:i]
        # Iterate over each preferred man
        for preferred_man in preferred_men:
            # Check if the preferred man also prefers this woman over his current partner
            if women_preferences[men_engaged[preferred_man]].index(
                preferred_man
            ) < women_preferences[men_engaged[preferred_man]].index(
                man
            ) and men_preferences[
                preferred_man
            ].index(
                woman
            ) < men_preferences[
                preferred_man
            ].index(
                men_engaged[preferred_man]
            ):
                # If so, the matching is not stable
                return False
    # If no unstable pairs found, the matching is stable
    return True
