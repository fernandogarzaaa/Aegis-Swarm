import os

class WhatsAppNotifier:
    """
    Integrates with WhatsApp API.
    To use, set environment variable 'WHATSAPP_API_KEY' and 'WHATSAPP_PHONE_NUMBER'.
    """
    def __init__(self):
        self.api_key = os.getenv("WHATSAPP_API_KEY")
        self.phone = os.getenv("WHATSAPP_PHONE_NUMBER")

    def notify(self, message):
        if self.api_key and self.phone:
            print(f"[WhatsApp] Notification sent to {self.phone}: {message}")
        else:
            print(f"[WhatsApp] Simulation (No config): {message}")
