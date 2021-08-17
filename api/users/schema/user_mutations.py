from .login_mutation import LoginMutation


class UserMutations:
    login = LoginMutation.Field(required=True)
