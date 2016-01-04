from collections import defaultdict

from smtp_usage.sender import send_email

class MailingList:
    "Manage groups of email addresses to send emails."

    def __init__(self):
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        self.email_map[email].add(group)

    def email_in_groups(self, *groups):
        groups = set(groups)
        return [e for (e, g) in self.email_map.items() if g & groups]

    def send_mailing(self, subject, message, from_addr, *groups, **kwargs):
        emails = self.email_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, **kwargs)
