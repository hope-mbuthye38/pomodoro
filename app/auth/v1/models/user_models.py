class UserModels:
    '''
    class for user operations
    '''
    users = {}

    def __init__(self,username, password, confirm_password,work,worktimer,breaktime):
        '''
        Initialising the user model
        '''
        self.id = len(UserModels.users)
        self.username = username
        self.password = password
        self.confirm_password = confirm_password
        self.work=work
        self.worktimer=worktimer
        self.breaktime=breaktime
    def save_user(self):
        '''
        Method to register a user ins
        '''
     
        user_record = dict(
            id = self.id,
            email = self.username,
            password = self.password,
            confirm_password = self.confirm_password,
            work = self.work,
            worktimer = self.worktimer,
            breaktimer = self.breaktimer
            )
        self.users.update({
            self.id: user_record
    })
         

     