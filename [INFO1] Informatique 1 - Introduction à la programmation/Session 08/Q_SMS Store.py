class SMSStore:
    def __init__(self):
        self.messages = []

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.messages.append((False, from_number, time_arrived, text_of_SMS))

    def message_count(self):
        return len(self.messages)

    def get_unread_indexes(self):
        unread = []
        for message in range(len(self.messages)):
            if self.messages[message][0] == False:
                unread.append(message)
        return unread

    def get_message(self, i):
        try:
            list(self.messages[i])[0] = True
            self.messages[i] = tuple(self.messages[i])
            return (self.messages[i][1], self.messages[i][2], self.messages[i][3])
        except IndexError:
            return None

    def delete(self, i):
        self.messages.remove(self.messages[i])

    def clear(self):
        self.messages = []