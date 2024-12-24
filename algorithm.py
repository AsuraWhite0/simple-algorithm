# Those are 2 algorithms of the algorithms that using in the bot.
    def PastGame(self, safe_amount, mine_positions):
        if not mine_positions:
            return "None"
        if mine_positions:
            safespot = [mine for game in mine_positions for mine in game][:safe_amount]
            board = self.board(safespot=safespot)
        return board


     def Probability(self, safe_amount, mine_positions):
        if not mine_positions:
            return "None"
        mines = np.zeros(25)
        for locations in mine_positions:
            for mine in locations:
                mines[mine] += 1
        probabilities = mines / len(mine_positions)
        safespot = np.argsort(probabilities)[:safe_amount]
        board = self.board(safespot=safespot)
        return board

#Why use the past mineLocation?
#> past mineLocation is the location of the bombspot from a old game. Clicking on the past mineLocation is safer than other spots. With the modified algorithms (some using machine learning models), we can increase the accuracy of winning.
#> Some are use uncoverLocation which is a win-spot to train and find the unsafe or can be bombspot for the next game
