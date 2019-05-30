'''
判断用户是否处于登录状态
'''

class Login_status:
    def __init__(self, request):
        self.request = request
    def check(self):
        sessin_name = self.request.session.get('name', '')
        cookie_name = self.request.COOKIES.get('name', '')
        if sessin_name and sessin_name == cookie_name:
            return True
        else:
            return False

