from email.mime.image import MIMEImage

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class EmailHandler:
    def __init__(self, email_subject=None, email_to=None, email_cc=None,
                 email_bcc=None, email_reply_to=None, email_msg=None):
        self.email_subject = email_subject
        self.email_to = email_to
        self.email_cc = email_cc
        self.email_bcc = email_bcc
        self.email_reply_to = email_reply_to
        self.email_msg = email_msg

    def send_mail(self):
        email = EmailMessage()
        if self.email_subject:
            email.subject = self.email_subject
        if self.email_to:
            email.to = [x.strip() for x in self.email_to.split(',')]
        if self.email_cc:
            email.cc = [x.strip() for x in self.email_cc.split(',')]
        if self.email_bcc:
            email.bcc = [x.strip() for x in self.email_bcc.split(',')]
        if self.email_reply_to:
            email.reply_to = [x.strip() for x in self.email_reply_to.split(',')]
        if self.email_msg:
            email.body = self.email_msg

        return email.send(fail_silently=False)

    def send_email_attachment(self, files):
        email = EmailMessage()
        if self.email_subject:
            email.subject = self.email_subject
        if self.email_to:
            email.to = [x.strip() for x in self.email_to.split(',')]
        if self.email_cc:
            email.cc = [x.strip() for x in self.email_cc.split(',')]
        if self.email_bcc:
            email.bcc = [x.strip() for x in self.email_bcc.split(',')]
        if self.email_reply_to:
            email.reply_to = [x.strip() for x in self.email_reply_to.split(',')]
        if self.email_msg:
            email.body = self.email_msg
        for file in files:
            email.attach(file.name, file.read(), file.content_type)

        return email.send(fail_silently=False)

    def send_email_html(self, template, context):
        html_content = render_to_string(template, context)
        text_content = strip_tags(html_content).strip()
        email = EmailMultiAlternatives()
        if self.email_subject:
            email.subject = self.email_subject
        if self.email_to:
            email.to = [x.strip() for x in self.email_to.split(',')]
        if self.email_cc:
            email.cc = [x.strip() for x in self.email_cc.split(',')]
        if self.email_bcc:
            email.bcc = [x.strip() for x in self.email_bcc.split(',')]
        if self.email_reply_to:
            email.reply_to = [x.strip() for x in self.email_reply_to.split(',')]
        # if self.email_msg:
        #     email.body = msg

        email.body = html_content
        email.attach_alternative(text_content, 'text/plain')

        email.content_subtype = "html"
        email.mixed_subtype = 'related'

        fp = open('static/image/logo.png', 'rb')
        msg_img1 = MIMEImage(fp.read())
        fp.close()
        msg_img1.add_header('Content-ID', '<{}>'.format("logo.png"))
        email.attach(msg_img1)

        fp = open(context['order'].door_image.image.url.replace('/', '', 1), 'rb')
        msg_img2 = MIMEImage(fp.read())
        fp.close()
        msg_img2.add_header('Content-ID', '<{}>'.format("door.png"))
        email.attach(msg_img2)

        fp = open(context['order'].frame_image.image.url.replace('/', '', 1), 'rb')
        msg_img3 = MIMEImage(fp.read())
        fp.close()
        msg_img3.add_header('Content-ID', '<{}>'.format("frame.png"))
        email.attach(msg_img3)

        fp = open(context['order'].handle.image.url.replace('/', '', 1), 'rb')
        msg_img4 = MIMEImage(fp.read())
        fp.close()
        msg_img4.add_header('Content-ID', '<{}>'.format("handle.png"))
        email.attach(msg_img4)

        return email.send(fail_silently=True)

