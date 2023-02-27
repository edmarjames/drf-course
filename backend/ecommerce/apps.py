from django.apps import AppConfig


class EcommerceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecommerce'

    # The ready() method is called when the Django app is loaded, and is used to perform any necessary initialization or setup for the app.
    def ready(self):
        # it imports the signals module from the ecommerce app. Signals are a way to decouple the different parts of a Django app by allowing certain actions to be triggered in response to certain events (such as when a model is saved or deleted).

        # By importing the signals module in the ready() method, it ensures that the signals are registered and ready to be used when the app is loaded.
        
        import ecommerce.signals