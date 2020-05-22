import operator


def repayment_calculations(bills):
    result = []
    while sorted(bills.items(), key=operator.itemgetter(1), reverse=True)[0][1] > 0.001:
        sorted_bills = sorted(bills.items(), key=operator.itemgetter(1), reverse=True)
        diff_highest_lowest = sorted_bills[0][1] + sorted_bills[-1][1]
        if diff_highest_lowest > 0:  # In this case the lowest amount can't fill the highest amount
            result.append({"payer": sorted_bills[-1][0], "receiver": sorted_bills[0][0], "amount": str(
                abs(sorted_bills[-1][1]))})
            bills[sorted_bills[-1][0]] = 0  # The lowest bill is done paying!
            bills[sorted_bills[0][
                0]] = diff_highest_lowest  # The person with the most amount of money still needs to receive money
        else:  # The highest amount gets completely paid off.
            result.append({"payer": sorted_bills[-1][0], "receiver": sorted_bills[0][0], "amount": str(
                abs(sorted_bills[0][1]))})
            bills[sorted_bills[-1][0]] = diff_highest_lowest  # The lowest person still has to pay
            bills[sorted_bills[0][0]] = 0  # The richest person got all of his money
    return result
