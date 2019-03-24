from django_cron import CronJobBase, Schedule
from datetime import date, datetime, timedelta
from .utils import *
from .models import *


class DailyTask(CronJobBase):
    RUN_EVERY_DAY = 120 #run every 2hrs
    schedule = Schedule(run_every_mins=RUN_EVERY_DAY)
    code = 'bill.task'

    def daily(self):
        client = cycle.objects.filter(type="daily", status="NO")
        for i in client:
            created = i.created
            today = date.today()
            if created == today:
                a = "This is to remind you for the payment of this following products"
                msg = a + "    " + i.item
                email = EmailHandler(
                    email_subject='BILLING REMINDER',
                    email_to=i.user.email,
                    email_reply_to='sales@mul-t-lock.com.ng',
                    email_msg=msg,
                )
                try:
                    email.send_mail()
                except:
                    pass
                new_date = today + timedelta(1)
                new = cycle.objects.get(id=i.id)
                new.created = new_date
                new.status = "YES"
                new.save()


class DailyUndoTask(CronJobBase):
    RUN_EVERY_DAY = 1440
    schedule = Schedule(run_every_mins=RUN_EVERY_DAY)
    code = 'bill.task1'

    def undaily(self):
        client = cycle.objects.filter(type="daily", status="YES")
        for i in client:
            new = cycle.objects.get(id=i.id)
            new.status = "NO"
            new.save()


class WeeklyTask(CronJobBase):
    RUN_EVERY_DAY = 10080
    schedule = Schedule(run_every_mins=RUN_EVERY_DAY)
    code = 'bill.task'

    def daily(self):
        client = cycle.objects.filter(type="weekly", status="NO")
        for i in client:
            created = i.created
            today = date.today()
            if created == today:
                a = "This is to remind you for the payment of this following products"
                msg = a + "    " + i.item
                email = EmailHandler(
                    email_subject='BILLING REMINDER',
                    email_to=i.user.email,
                    email_reply_to='sales@mul-t-lock.com.ng',
                    email_msg=msg,
                )
                try:
                    email.send_mail()
                except:
                    pass
                new_date = today + timedelta(7)
                new = cycle.objects.get(id=i.id)
                new.created = new_date
                new.status = "YES"
                new.save()


class WeeklyUndoTask(CronJobBase):
    RUN_EVERY_DAY = 1440
    schedule = Schedule(run_every_mins=RUN_EVERY_DAY)
    code = 'bill.task1'

    def undaily(self):
        client = cycle.objects.filter(type="weekly", status="YES")
        for i in client:
            new = cycle.objects.get(id=i.id)
            new.status = "NO"
            new.save()


class MonthlyTask(CronJobBase):
    RUN_EVERY_DAY = 43200
    schedule = Schedule(run_every_mins=RUN_EVERY_DAY)
    code = 'bill.task'

    def daily(self):
        client = cycle.objects.filter(type="monthly", status="NO")
        for i in client:
            created = i.created
            today = date.today()
            if created == today:
                a = "This is to remind you for the payment of this following products"
                msg = a + "    " + i.item
                email = EmailHandler(
                    email_subject='BILLING REMINDER',
                    email_to=i.user.email,
                    email_reply_to='sales@mul-t-lock.com.ng',
                    email_msg=msg,
                )
                try:
                    email.send_mail()
                except:
                    pass
                new_date = today + timedelta(30)
                new = cycle.objects.get(id=i.id)
                new.created = new_date
                new.status = "YES"
                new.save()


class MonthlyUndoTask(CronJobBase):
    RUN_EVERY_DAY = 43200
    schedule = Schedule(run_every_mins=RUN_EVERY_DAY)
    code = 'bill.task1'

    def undaily(self):
        client = cycle.objects.filter(type="weekly", status="YES")
        for i in client:
            new = cycle.objects.get(id=i.id)
            new.status = "NO"
            new.save()


class YearlyTask(CronJobBase):
    RUN_EVERY_DAY = 120
    schedule = Schedule(run_every_mins=RUN_EVERY_DAY)
    code = 'bill.task'

    def daily(self):
        client = cycle.objects.filter(type="yearly", status="NO")
        for i in client:
            created = i.created
            today = date.today()
            if created == today:
                a = "This is to remind you for the payment of this following products"
                msg = a + "    " + i.item
                email = EmailHandler(
                    email_subject='BILLING REMINDER',
                    email_to=i.user.email,
                    email_reply_to='sales@mul-t-lock.com.ng',
                    email_msg=msg,
                )
                try:
                    email.send_mail()
                except:
                    pass
                new_date = today + timedelta(365)
                new = cycle.objects.get(id=i.id)
                new.created = new_date
                new.status = "YES"
                new.save()


class YearlyUndoTask(CronJobBase):
    RUN_EVERY_DAY = 120
    schedule = Schedule(run_every_mins=RUN_EVERY_DAY)

    def undaily(self):
        client = cycle.objects.filter(type="yearly", status="YES")
        for i in client:
            new = cycle.objects.get(id=i.id)
            new.status = "NO"
            new.save()
