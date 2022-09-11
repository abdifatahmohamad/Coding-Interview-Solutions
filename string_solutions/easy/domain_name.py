'''
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

'''

def domain_name(url):
    headers = ["http://", "https://", "www."]
    for h in headers:
        url = url.replace(h, "")

#     for i in range(len(url)):
#         if url[i] == '.':
#             return url[0 : i]


    # Or shorter way:
    return url.split('.')[0]
  
  
print(domain_name("https://www.cnet.com"))
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"
