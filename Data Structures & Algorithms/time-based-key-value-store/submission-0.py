class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store.setdefault(key, []).append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        value_pair = self.store.get(key)
        if not value_pair:
            return res
        l, r = 0, len(value_pair) -1
        while l<=r:
            m = (l+r) //2
            if timestamp == value_pair[m][1]:
                return value_pair[m][0]
            if timestamp > value_pair[m][1]:
                res = value_pair[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        
