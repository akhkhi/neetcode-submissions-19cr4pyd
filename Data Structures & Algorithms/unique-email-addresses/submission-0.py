class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails =set()

        for e in emails:
            name, domain = e.split("@")
            name = name.replace(".","")
            name = name.split("+")[0]
            unique_emails.add(name + "@" + domain)
        print(unique_emails)
        return len(unique_emails)



