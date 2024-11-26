from django.apps import AppConfig

class MyThemeConfig(AppConfig):
    name = "mytheme"  # This should be 'mytheme' if that's your app name
    tailwind = True  # This enables the app as a Tailwind app
