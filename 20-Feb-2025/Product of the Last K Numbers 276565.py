# Problem: Product of the Last K Numbers - https://leetcode.com/problems/product-of-the-last-k-numbers/description/

class ProductOfNumbers:

    def __init__(self):
        self.nums = []
        self.prefix_products = [1] 

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]
            self.nums.append(num)
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)
            self.nums.append(num)

    def getProduct(self, k: int) -> int:
        n = len(self.prefix_products) - 1  #
        if k > n:
            return 0
       
        if 0 in self.nums[-k:]:
            return 0
        
        return self.prefix_products[-1] // self.prefix_products[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)