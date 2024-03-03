import random


def gale_shapley(men_pref, women_pref):
    # Number of men (or women)
    n = len(men_pref)

    # All men are initially free
    free_men = list(range(n))

    # No woman is initially engaged
    engaged_women = [None] * n

    # No man is initially engaged
    engaged_men = [None] * n

    # Copy men's preferences because we'll modify them (removing women from men's lists)
    men_pref_copy = [list(men) for men in men_pref]

    # While there's a free man who still has a woman to propose to
    while free_men:
        # Choose such a man
        man = free_men[0]

        # The highest ranked woman in man's list
        woman = men_pref_copy[man][0]

        # If the woman is free
        if engaged_women[woman] is None:
            # Engage her with the man (best-valid-friend for man)
            engaged_women[woman] = man
            engaged_men[man] = woman
            free_men.remove(man)
        else:
            # The woman is not free
            current_man = engaged_women[woman]

            # If the woman prefers this man over her current engagement
            if women_pref[woman].index(man) < women_pref[woman].index(current_man):
                # Engage her with this man (worst-valid-friend for woman)
                engaged_women[woman] = man
                engaged_men[man] = woman
                free_men.remove(man)

                # The dumped man becomes free
                free_men.append(current_man)

        # The man removes the woman from his list, moving on to propose to his next most preferred woman
        men_pref_copy[man].remove(woman)

    # Return the final engagements
    return engaged_men
