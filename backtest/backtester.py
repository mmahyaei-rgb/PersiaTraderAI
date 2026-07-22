from domain.entities.trade import Trade


class BackTester:

    def __init__(self):

        self.trades = []

    def add_trade(

        self,

        symbol,

        entry,

        exit,

        quantity,

        signal

    ):

        profit = (exit - entry) * quantity

        self.trades.append(

            Trade(

                symbol,

                entry,

                exit,

                quantity,

                profit,

                signal

            )

        )

    def report(self):

        total = sum(t.profit for t in self.trades)

        wins = len([t for t in self.trades if t.profit > 0])

        losses = len(self.trades) - wins

        return {

            "Trades": len(self.trades),

            "Wins": wins,

            "Losses": losses,

            "Profit": total

        }
        