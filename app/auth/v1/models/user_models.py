class UserModels:
    '''
    class for user operations
    '''
    users = {}

    def __init__(self,email, password, confirm_password):
        '''
        Initialising the user model
        '''
        self.id = len(UserModels.users)
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def save_user(self):
        '''
        Method to register a user ins
        '''