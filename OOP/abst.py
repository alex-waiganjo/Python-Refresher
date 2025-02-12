# Reduce complexity by hiding unecessary details

class EmailService:

    def _connect(self):
        print("Connecting...")

    def _authenticate(self):
        print("Authenticating...")

    def send_email(self):
        self._connect()
        self._authenticate()
        print("Sending Email")
        self._disconnect()

    def _disconnect(self):
        print('Disconnecting from Email Server')


email = EmailService()

email.send_email()
