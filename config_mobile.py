import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from utils import path
from appium.options.android import UiAutomator2Options

load_dotenv()


class Config(BaseSettings):
    USER_NAME: str = os.getenv('USER_NAME')
    ACCESS_KEY: str = os.getenv('ACCESS_KEY')
    TIMEOUT: float = float(os.getenv('TIMEOUT', '10'))
    REMOTE_URL: str = os.getenv('REMOTE_URL')
    PLATFORM_NAME: str = os.getenv('PLATFORM_NAME')
    PLATFORM_VERSION: str = os.getenv('PLATFORM_VERSION', '')
    DEVICE_NAME: str = os.getenv('DEVICE_NAME')
    APP: str = os.getenv('APP')

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'bstack':
            options.set_capability('remote_url', self.REMOTE_URL)
            options.set_capability('deviceName', self.DEVICE_NAME)
            options.set_capability('platformName', self.PLATFORM_NAME)
            options.set_capability('platformVersion', self.PLATFORM_VERSION)
            options.set_capability('app', self.APP)
            options.set_capability(
                'bstack:options',
                {
                    "projectName": "First Python models",
                    "buildName": "browserstack-build-1",
                    "sessionName": "BStack first_test",
                    "userName": self.USER_NAME,
                    "accessKey": self.ACCESS_KEY,
                },
            )

        elif context == 'emulator_local':
            options.set_capability('remote_url', self.REMOTE_URL)
            options.set_capability('platformName', self.PLATFORM_NAME)
            options.set_capability('app', path.relative_from_root(self.APP))

        return options


config_app = Config()
