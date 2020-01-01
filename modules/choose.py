class Choose:
    def __init__(self, lists):
        self.lists = lists

    def anime(self):
        global send
        lists = self.lists
        num = 0
        for key in lists:
            def send():
                return f'{num}) --> {lists[num]}'
            num = num + 1
            # return f'{num}) --> {lists[key]}'
        for i in range(1, num):
            send()
