
author_first=input("Enter the authors first name:\n")
author_second=input("Enter the authors second name:\n")
quote=input("Enter the authors quote:\n")

author_first=author_first.title().strip() + " "
author_second=author_second.title().strip() + " "
quote='"'+quote.strip()+'"'

print(author_first + author_second + "once said, " + quote)


