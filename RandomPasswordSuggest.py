import random
import string

password_len = 8

char_merge = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(char_merge) for i in range(password_len)])

print("Suggested Password:", password)