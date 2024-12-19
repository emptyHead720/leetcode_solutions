# we should use dynamic array as never need to insert or remove from in between yeah?
# and we need to access elements at certain indices
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.all_url = [homepage]
        self.current_index = 0
        self.last_valid_index = 0

        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        if self.current_index + 1 >= len(self.all_url):
            self.all_url.append(url)
            self.current_index += 1
            self.last_valid_index = self.current_index
        else:
            self.current_index += 1
            self.last_valid_index = self.current_index
            self.all_url[self.current_index] = url


    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if steps > self.current_index:
            self.current_index = 0
            return self.all_url[self.current_index]
        else:
            self.current_index = self.current_index - steps
            return self.all_url[self.current_index]

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        if self.current_index + steps > self.last_valid_index:
            self.current_index = self.last_valid_index
            return self.all_url[self.current_index]
        self.current_index = self.current_index + steps
        return self.all_url[self.current_index]
        


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory(homepage)
obj.visit(url)
param_2 = obj.back(steps)
param_3 = obj.forward(steps)
