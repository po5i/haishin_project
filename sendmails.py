# -*- coding: utf-8 -*-
#import sendgrid
import requests
from premailer import transform

# Authorization: "Basic <apiKeyId>:<apiSecretId>"
# Testing API KEYS:

class Configuration(object):
    @staticmethod
    def set_credentials(api_base_url,api_key, e_from, e_url_img):
        Configuration.EMAIL_API_BASE_URL = api_base_url
        Configuration.EMAIL_API_KEY = api_key
        Configuration.EMAIL_FROM = e_from
        Configuration.EMAIL_URL_IMG = e_url_img

    @staticmethod
    def headers():
        return {
            'Authorization': 'Basic %s' % ( Configuration.EMAIL_API_KEY)
        }
class Email(object):

    @staticmethod
    def send(e_to_email,e_to_name,e_subject,e_message):
        '''
        sg = sendgrid.SendGridClient(Configuration.EMAIL_API_KEY)
        
        message = sendgrid.Mail()
        message.add_to(e_to)
        #message.add_cc("jorlusal@gmail.com")
        message.set_subject(e_subject)
        message.set_html(e_html)

        status, msg = sg.send(message) 

        if str(status) == "Error":
            return False
        return True
        '''
        e_html= '''
<html>
    <head>
        <style type="text/css">
            body{
                background:#f2f2f2;

            }
            #e-content{
                width:400px;
                margin: 0 auto;
            }
            #e-body{
                border:solid 1px #d9d9d8;
                border-top:none;
                padding:15px;
                background: #FFFFFF;
            }
            #e-greetings{
                padding-bottom:10px;
                border-bottom:solid 1px #ff6600;
            }
            #e-message{
                padding-top:10px;
            }
            #e-header{
                padding-top:15px;
                border-bottom:solid 10px #ff6600;
            }
            #e-foot{
                font-size:10px;
                color:#91918d;
                padding-bottom:15px;
            }
        </style>
    </head>
    <body>
        <div id="e-content">
            <div id="e-header">
                <img src="'''+ Configuration.EMAIL_URL_IMG +'''/logo.png" alt="Delidelux"/>
            </div>
            <div id="e-body">
                <div id="e-greetings">
                    <label>Hola, '''+ e_to_name.decode('utf8') +'''</label>
                </div>
                <div id="e-message">
                    <p>
                        '''+ e_message.decode('utf8') +('''
                    </p>
                </div>
            </div>
            <div id="e-foot">
                <p>
                    <b>Cláusula de confidencialidad:</b> La información contenida en el presente mensaje es confidencial y esta dirigida exclusivamente a su destinatario.<br/>
                    <b>Nota:</b> Este mensaje ha sido generado automáticamente, favor no responda a este e-mail.
                </p> 
            </div>
        </div>
    </body>
</html>''').decode('utf8')
        
        e_html=transform(e_html)
        requests.post(
        Configuration.EMAIL_API_BASE_URL+"/messages",
        auth=("api", Configuration.EMAIL_API_KEY),
        data={"from": Configuration.EMAIL_FROM,
              "to": e_to_email.decode('utf8'),
              "cc": 'jorlusal@gmail.com',
              "subject": e_subject.decode('utf8'),
              "html": e_html})
        
