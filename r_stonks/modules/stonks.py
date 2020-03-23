class UserRequest():

    def __new__(cls, user_message):

        def is_valid_request(user_message):
            if user_message.count("$") >=2:
                first_index = user_message.find("$")
                second_index = user_message.find("$", first_index + 1)
                request = user_message[first_index:second_index + 1]
            else:
                return False

            parameters = request.split()

            if (len(parameters) == 3
                and parameters[0][0] == "$"
                and parameters[2][0].upper() == "X"
                and parameters[2][-1] == "$"):
                    return True
            else:
                return False

        if is_valid_request(user_message):
            return super(UserRequest, cls).__new__(cls)


    def __init__(self, user_message):

        first_index = user_message.find("$")
        second_index = user_message.find("$", first_index + 1)
        request = user_message[first_index:second_index + 1]

        parameters = request.split()

        self.action = parameters[0].upper()
        self.ticker = parameters[1].upper()
        self.volume = int(parameters[2][1:-1])
