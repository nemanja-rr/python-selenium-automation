
class Page:

    def click(self):
        print('Clicking...')

    def verify_text(self):
        print('Verifying...')

    def input_text(self, text):
        print(f'Inputting text, {text}')


class LoginPage(Page):

    pass

login_page = LoginPage
login_page.click()