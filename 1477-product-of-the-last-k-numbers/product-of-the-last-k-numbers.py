class ProductOfNumbers:

    def __init__(self):
        self.numbers = []
        self.prefix_product = [1]
        self.length = 0 

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_product = [1]
            self.length = 0
        else:
            self.numbers.append(num)
            self.prefix_product.append(self.prefix_product[-1] * num)
            self.length += 1

    def getProduct(self, k: int) -> int:
        if self.length < k:
            return 0
        else:
            return self.prefix_product[-1] // self.prefix_product[-k-1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)