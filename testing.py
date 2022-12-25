def email_list(domains):
	emails = []
	for users in domains:
	  for user in users:
	    emails.append("{}{}".format(users, users[user]))
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))