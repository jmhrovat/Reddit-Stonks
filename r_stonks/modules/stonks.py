

class UserRequest():

    def __init__(self, user_message):
        self.user_message = user_message

        def is_valid_request(self):
            parameters = self.user_message.split()
            if (len(parameters) == 3
                and parameters[0][0] == "$"
                and parameters[2][0].upper() == "X"
                and parameters[2][-1] == "$"):
                    return True
            else:
                return False

        try:
            if is_valid_request(self):
                parameters = self.user_message.split()
                self.action = parameters[0].upper()
                self.ticker = parameters[1].upper()
                self.quantity = int(parameters[2][1:-1])
            else:
                raise ValueError
        except ValueError:
            print('''The message provided by the user does not match the format.
            Please double check your entry and make sure you follow the format $ACTION TICKER X###$''')
