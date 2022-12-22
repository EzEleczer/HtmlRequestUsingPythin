import cgi
print ("Content-type: text/html\n\n")
 

form = cgi.FieldStorage()

# username = form.getvalue("UserName")
# if "name" not in form or "addr" not in form:
#     print("<H1>Error</H1>")
#     print("Please fill in the name and addr fields.")
# return

print("<p>Name:", form["UserName"].value)
