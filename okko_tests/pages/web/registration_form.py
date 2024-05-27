from selene import be, have
from selene.support.shared.jquery_style import s, ss
import allure


class RegistrationForm:

    def __init__(self):
        self.sign_input = s('[test-id="sign_input"]')
        self.continue_button = s('[test-id="continue_btn"]')
        self.sliding_panel = s('[test-id="sliding_panel"]')
        self.info_message = s('[test-id="sign_input"]+div')

    @allure.step('Enter email into the field')
    def enter_email(self, email):
        self.sign_input.should(be.blank).type(email)
        self.continue_button.click()

    @allure.step('Verify registration')
    def check_registration_result(self, email_valid=True):

        if email_valid:
            self.sliding_panel.should(be.visible)
        else:
            self.info_message.should(have.exact_text('Неверный формат'))


registration_form = RegistrationForm()
