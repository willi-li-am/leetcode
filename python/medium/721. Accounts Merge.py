class UnionFind:
    def __init__(self, n):
        self.graph = [i for i in range(n)]

    def find(self, x):
        if x != self.graph[x]:
            self.graph[x] = self.find(self.graph[x])
        
        return self.graph[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        self.graph[x] = y

class Solution:
    """
    1. Unionize sets of emails with Union Find
    2. We map through every email to it's parent index in the Union Find
    3. We add the email to the accountList
    4. We append the accountList to the result using the index to find the account name
    """
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        union = UnionFind(len(accounts))
        email_to_union = {}

        for i, account in enumerate(accounts):
            emails = account[1:]
            for email in emails:
                if email in email_to_union:
                    union.union(email_to_union[email], i)
                else:
                    email_to_union[email] = i


        accountList = defaultdict(list)
        for email in email_to_union:
            index = union.find(email_to_union[email])
            accountList[index].append(email)

        res = []

        for index in accountList:
            res.append([accounts[index][0]] + sorted(accountList[index]))

        return res
