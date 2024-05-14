from selene import be, have
from selene.support.shared.jquery_style import s, ss
import allure


class RegistrationForm:

    @allure.step('Enter email into the field')
    def enter_email(self, email):
        s('[test-id="sign_input"]').should(be.blank).type(email)
        s('[test-id="continue_btn"]').click()

    @allure.step('Verify registration')
    def check_registration_result(self, email_valid=True):

        if email_valid:
            s('[test-id="sliding_panel"]').should(be.visible)
        else:
            s('[test-id="sign_input"]+div').should(have.exact_text('Неверный формат'))


registration_form = RegistrationForm()
