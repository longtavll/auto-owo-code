from pickle import TRUE
import requests
import time
import random
import discord

id_channel = 'ID CHANNEL'

url = f'https://discord.com/api/v9/channels/{id_channel}/messages'

auth = {'Authorization':'YOUR TOKEN HERE'}

msg = {'content':'owo h'}
msg2 = {'content':'owo b'}

msgg1 = {'content':'owo use 051 065 072'}
msgg3 = {'content':'owo use 053 067 074'}
msgg4 = {'content':'owo use 054 068 075'}
msgg5 = {'content':'owo use 055 069 076'}
msgg2 = {'content':'owo use 052 066 073'}
msgg6 = {'content':'owo lb all'}
msgg7 = {'content':'owo crate all'}

msgg = [msgg1,msgg2,msgg3,msgg4,msgg5,msgg6,msgg7]

while True:
    delay = random.uniform(13,18)
    delay2 = random.uniform(1,3)
    delay3 = random.uniform(1,3)
    
    time.sleep(delay)
    requests.post(url, headers = auth, data = msg)
    time.sleep(delay2)
    requests.post(url, headers = auth, data = msg2)
    time.sleep(delay3)
    requests.post(url, headers = auth, data = random.choice(msgg))
