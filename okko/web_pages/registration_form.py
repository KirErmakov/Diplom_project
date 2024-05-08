from selene import be, have
from selene.support.shared.jquery_style import s
import allure


class RegistrationForm:

    @allure.step('Registration with email')
    def register_with_email(self, email, email_valid=True):
        s('[test-id="sign_input"]').should(be.blank).type(email)
        continue_button = s('[test-id="continue_btn"]')

        if email_valid:
            continue_button.should(be.clickable)
        else:
            continue_button.should(have.attribute('disabled'))


registration_from = RegistrationForm()
