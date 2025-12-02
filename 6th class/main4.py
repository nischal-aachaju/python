
url = input("Enter url :").strip().lower()  # strip remove extra space 
url = url.replace("https://", "")
url = url.replace("http://", "")
url = url.replace("www.", "")

clean_url = url
domain = clean_url.split("/", 1)[1]

print("Clean URL:", clean_url)
print("Domain:",domain)




