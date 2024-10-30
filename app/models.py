class PriceData:
    def __init__(self, time, price_usd):
        self.time = time
        self.price_usd = price_usd
        
    def __repr__(self):
        return f"<PriceData time={self.time}, USD={self.price_usd}>"