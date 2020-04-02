# Import for custom tasks
from __future__ import absolute_import, unicode_literals
from celery import shared_task

# Import library for saving data
import requests
from django.utils.dateparse import parse_datetime
from bs4 import BeautifulSoup

# Import library for sending mail
from . models import Article
from django.template.loader import render_to_string
from django.core.mail import send_mail
from crawlweb.settings import EMAIL_HOST_USER

requests.packages.urllib3.disable_warnings()


@shared_task
def remove_article():
    old_article = Article.objects.all().delete()


@shared_task
def crawl_new_article():
    session = requests.Session()

    session.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36"}

    url = "https://cafef.vn/"

    content = session.get(url, verify=False ).content

    soup = BeautifulSoup(content,'html.parser')

    posts = soup.find_all('li',{'class':'tlitem clearfix'})

    for i in posts:
        # Find the content in web
        link = i.find('a')
        img = i.find('img')
        time = i.find('span',{'class':'time'})

        # Modify the content
        title_article = link['title']
        link_article = "https://cafef.vn/" + link['href']
        img_src = img['src']
        time_convert = parse_datetime(time['title'])

        # Create new Table and add data to db
        new_article = Article()
        new_article.title = title_article
        new_article.link = link_article
        new_article.img_src = img_src
        new_article.time = time_convert
        new_article.save()


# Create context for templates display
top_article = Article.objects.all()[0]
article1 = Article.objects.all()[1:3]
article2 = Article.objects.all()[3:5]
last_article = Article.objects.all()[5:8]
context = {
    'top_article': top_article,
    'article1': article1,
    'article2': article2,
    'last_article': last_article,
}

msg_plain = render_to_string('index/email_templates.txt')
msg_html = render_to_string('index/email_template.html', context)
subject = "NEWS"


# Sending the email to UserMail
@shared_task
def auto_send_email():
    users_mail = UserMail.objects.all()
    for each_user in users_mail:
        if each_user.auto_send_mail:
            recepient = each_user.user_mail
            send_mail(subject, msg_plain, EMAIL_HOST_USER, [recepient], html_message=msg_html, fail_silently=False)


# Make function to run a specific time
@shared_task
def sending_email(recepient):
    recepient = recepient
    send_mail(subject, msg_plain, EMAIL_HOST_USER, [recepient], html_message=msg_html, fail_silently=False)

