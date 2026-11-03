class TimeMap:

    def __init__(self):
        self._map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self._map:
            self._map[key] = [[timestamp, value]]
            return

        self._map[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        
        arr = self._map.get(key, [])
        l, r = 0, len(arr) - 1

        output = ""
        while l <= r:
            i = l + ((r - l) // 2)

            if arr[i][0] <= timestamp:
                output = arr[i][1]
                l = i + 1
            else:
                r = i - 1

        return output


        
