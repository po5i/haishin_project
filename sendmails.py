# -*- coding: utf-8 -*-
#import sendgrid
import requests
from django.utils.encoding import smart_str

class Email(object):
    @staticmethod
    def set_configuration(api_base_url,api_key, e_from, disablecss=False):
        Email.API_BASE_URL = api_base_url
        Email.API_KEY = api_key
        Email.FROM = e_from
        Email.DISABLECSS = disablecss

    @staticmethod
    def set_message_html(name, message):
        if Email.DISABLECSS:
            Email.HTML = smart_str(message)
        else:
            from premailer import transform
            Email.HTML = transform(('''
    <html>
        <head>
            <style type="text/css">
                body{
                    background:#f2f2f2;
                    background:#d9d9d9;
                }
                #e-body{
                    width:400px;
                    margin: 0 auto;
                }
                #e-content{
                    border:solid 1px #d9d9d8;
                    border-color:#cccccc;
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
            <div id="e-body">
                <div id="e-header">
                    <img src="http://delidelux.po5i.com/static/img/logo.png" alt="Delidelux"/>
                </div>
                <div id="e-content">
                    <div id="e-greetings">
                        <label>Hola, '''+ smart_str(name) +'''</label>
                    </div>
                    <div id="e-message">'''+ smart_str(message) +smart_str('''</div>
                </div>
                <div id="e-foot">
                    <p>
                        <b>Cláusula de confidencialidad:</b> La información contenida en el presente mensaje es confidencial y esta dirigida exclusivamente a su destinatario.<br/>
                        <b>Nota:</b> Este mensaje ha sido generado automáticamente, favor no responda a este e-mail.
                    </p> 
                </div>
            </div>
        </body>
    </html>''')).decode('utf8'))
       

    @staticmethod
    def send_test(to,name,subject,message):
        
        #sg = sendgrid.SendGridClient(Configuration.EMAIL_API_KEY)
        
        #message = sendgrid.Mail()
        #message.add_to(e_to)
        #message.set_subject(e_subject)
        #message.set_html(e_html)
        
        #status, msg = sg.send(message) 

        #if str(status) == "Error":
        #    return False
        #return True
        message = '<p>'+message+'</p>'
        set_message_html(name,message)

        requests.post(
        Email.API_BASE_URL+"/messages",
        auth=("api", Email.API_KEY),
        data={"from": Email.FROM,
              "to": to,
              "cc": 'jorlusal@gmail.com',
              "subject": subject,
              "html": Email.HTML})

    @staticmethod
    def notify_update_profile(user,profile):

        
        name = user.first_name + " " + user.last_name
        message = '<p>Se ha realizado una actualización de su información:</p>'

        if profile.birth_date: message += '<p> <b>Fecha de nacimiento: </b>'+profile.birth_date+'<br/>'
        if profile.country: message += smart_str('<b>País: </b>')+smart_str(profile.country)+'<br/>'
        if profile.city: message += '<b>Ciudad: </b>'+profile.city.decode('utf8')+'<br/>' 
        if profile.address: message += smart_str('<b>Dirección: </b>')+smart_str(profile.address) +'<br/>'
        if profile.phone: message += smart_str('<b>Teléfono: </b>')+profile.phone+'<br/></p>'

        message += '<p>Si usted no realizó esta acción, porfavor contactarse con nosotros.<br/>'
        message += 'Saludos, el equipo de DeliDelux.</p>'

        Email.set_message_html(name,message)

        requests.post(
        Email.API_BASE_URL+"/messages",
        auth=("api", Email.API_KEY),
        data={"from": Email.FROM,
              "to": user.email,
              "cc": 'jorlusal@gmail.com',
              "subject": "Actualización del perfil.",
              "html": smart_str(Email.HTML)}
        )
        
    @staticmethod
    def notify_business_new_job(job):

        
        name = job.business.admin.first_name + " " + job.business.admin.last_name
        message = '<p>Tienes un nuevo pedido para tu negocio.</p>'

        message += '<p> <b>Cliente: </b>'+job.user.first_name + " " + job.user.last_name+'<br/>'

        message += '<p>Para aceptar o rechazar el pedido vaya a DeliDelux.<br/>'
        message += 'Saludos, el equipo de DeliDelux.</p>'

        Email.set_message_html(name,message)

        requests.post(
        Email.API_BASE_URL+"/messages",
        auth=("api", Email.API_KEY),
        data={"from": Email.FROM,
              "to": job.user.email,
              "cc": 'jorlusal@gmail.com',
              "subject": "Nuevo pedido.",
              "html": smart_str(Email.HTML)}
        )

    @staticmethod
    def notify_client_job_accepted(job):

        name = job.user.first_name + " " + job.user.last_name

        message = '<p>Tu pedido en '+job.business.name+' se esta cocinando.<br/>'

        message += 'Saludos, el equipo de DeliDelux.</p>'

        Email.set_message_html(name,message)

        requests.post(
        Email.API_BASE_URL+"/messages",
        auth=("api", Email.API_KEY),
        data={"from": Email.FROM,
              "to": job.user.email,
              "cc": 'jorlusal@gmail.com',
              "subject": "Pedido aceptado.",
              "html": smart_str(Email.HTML)}
        )
    
        

