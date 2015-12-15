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
            import pynliner
            #from premailer import transform
            #Email.HTML = transform(('''
            Email.HTML = pynliner.fromString(('''
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
              "subject": "Nuevo pedido.",
              "html": smart_str(Email.HTML)}
        )

    @staticmethod
    def notify_client_job_accepted(job):

        name = job.user.first_name + " " + job.user.last_name

        message = smart_str('<p>Tu pedido en ')+smart_str(job.business.name)+smart_str(' se está cocinando.<br/>')

        message += 'Saludos, el equipo de DeliDelux.</p>'

        Email.set_message_html(name,message)

        requests.post(
        Email.API_BASE_URL+"/messages",
        auth=("api", Email.API_KEY),
        data={"from": Email.FROM,
              "to": job.user.email,
              "subject": "Pedido aceptado.",
              "html": smart_str(Email.HTML)}
        )

    @staticmethod
    def notify_client_job_rejected(job):

        name = job.user.first_name + " " + job.user.last_name

        message = '<p>Lamentamos informarte que tu pedido en '+job.business.name+' ha sido rechazado por el siguiente motivo.<br/>'
        message = '<br/>'+job.rejected_message+'<br/>'

        message += 'Saludos, el equipo de DeliDelux.</p>'

        Email.set_message_html(name,message)

        requests.post(
        Email.API_BASE_URL+"/messages",
        auth=("api", Email.API_KEY),
        data={"from": Email.FROM,
              "to": job.user.email,
              "subject": "Pedido rechazado.",
              "html": smart_str(Email.HTML)}
        )

    @staticmethod
    def notify_client_job_shipped(job):

        name = job.user.first_name + " " + job.user.last_name

        message = smart_str('<p>En pocos minutos tu pedido de ')+smart_str(job.business.name)+smart_str(' llegará a su destino.<br/>')

        message += 'Saludos, el equipo de DeliDelux.</p>'

        Email.set_message_html(name,message)

        requests.post(
        Email.API_BASE_URL+"/messages",
        auth=("api", Email.API_KEY),
        data={"from": Email.FROM,
              "to": job.user.email,
              "subject": "Pedido enviado.",
              "html": smart_str(Email.HTML)}
        )

    @staticmethod
    def notify_client_job_completed(job):

        name = job.user.first_name + " " + job.user.last_name

        message = '<p>Tu pedido de '+job.business.name+' ha llegado a su destino..<br/>'
        message = '<br/>Muchas gracias por confiar en nosotros.<br/>'

        message += 'Saludos, el equipo de DeliDelux.</p>'

        Email.set_message_html(name,message)

        requests.post(
        Email.API_BASE_URL+"/messages",
        auth=("api", Email.API_KEY),
        data={"from": Email.FROM,
              "to": job.user.email,
              "subject": "Pedido completado.",
              "html": smart_str(Email.HTML)}
        )

    @staticmethod
    def notify_payment_change(job, previous_status, current_status):

        #name = job.user.first_name + " " + job.user.last_name
        name = job.business.admin.first_name + " " + job.business.admin.last_name

        message = '<p>Hay un cambio en el estado del pago del pedido ' + str(job.id) + '.<br/><br/>'
        message += '<b>Cliente: </b>'+job.user.first_name + " " + job.user.last_name+'<br/>'
        message += '<b>Estado anterior: </b>' + str(previous_status) + '.<br/>'
        message += '<b>Estado actual: </b>' + str(current_status) + '.<br/><br/>'
        message += 'Saludos, el equipo de DeliDelux.</p>'

        Email.set_message_html(name,message)

        requests.post(
        Email.API_BASE_URL+"/messages",
        auth=("api", Email.API_KEY),
        data={"from": Email.FROM,
              "to": job.user.email,
              "bcc": "carlos.po5i@gmail.com",
              "subject": "Cambio de estado en el pago.",
              "html": smart_str(Email.HTML)}
        )
