def finalValueAfterOperations(operations) -> int:
        X = 0
        for element in operations:
            if element == "++X" or element == "X++":
                X = X + 1
            else:
                X = X - 1
        return X

operations = ["--X","X++","X++"]
print(finalValueAfterOperations(operations))