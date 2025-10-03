class MovieRentingSystem(object):

    def __init__(self, n, entries):
        """
        :type n: int
        :type entries: List[List[int]]
        """
        self.avail = defaultdict(dict)
        self.prices = defaultdict(dict)
        self.rented = []
        
        for s, m, p in entries:
            self.avail[m][s] = p
            self.prices[m][s] = p


    def search(self, movie):
        shop_inventory = self.avail[movie]
        if len(shop_inventory) == 0:
            return [] 
    
        return [m[0] for m in sorted(shop_inventory.items(), key=lambda(k,v): (v,k))][:5]
        

    def rent(self, shop, movie):
        price = self.avail[movie][shop]
        self.avail[movie].pop(shop)
        
        self.rented.append([price, shop, movie])
        

    def drop(self, shop, movie):
        price = self.prices[movie][shop]
        
        self.rented.remove([price, shop, movie])
        self.avail[movie][shop] = price
        

    def report(self):
        sorted_output = sorted(self.rented)[:5]
        return map(lambda x: x[-2:], sorted_output)
