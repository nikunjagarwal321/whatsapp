# whatsapp

Steps to run the service:

From developer side:

1. Clone this repo : https://github.com/nikunjagarwal321/whatsapp
2. Run python app.py   -- to start the service  {This service is running on http://127.0.0.1:5000/}.
3. In the second terminal run ngrok http 5000  to allocate a temporary public domain that redirects HTTP requests to our local port 5000. On Mac OS ru ./ngrok http 5000.
4. The public URL would be created for forwarding. Copy this and paste this in Twilio WhatsApp SandBox settings.
5. The user can now test the service with whatsApp on this number +14155238886. 


From user side :
1. Users can send/receive messages from WhatsApp number : +14155238886. 
2. Initiate the message with “join pour-vast”.
3. Reply “help” to get any help.
4. To leave the sandbox service any time reply with “stop”.

