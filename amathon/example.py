'''
Created on 2012/01/13

@author: y42sora
@requires: Python 3.x
'''

"""
This is Example file.
The key is described on api_key.py
"""
import re

import api_key
from amathon import Amathon

# make api object
api = Amathon(AWSAccessKeyId=api_key.access_key, ASWSecretAccessKey=api_key.secret_key, AssociateTag=api_key.aa_id)

# lookup the Godel-Escher-Bach-Eternal-Golden ISBN: 0465026567
print(api.ItemLookup(ItemId="0465026567", ResponseGroup="ItemAttributes").decode("utf-8"))

# serath the Godel-Escher-Bach-Eternal-Golden
print(api.ItemSearch(SearchIndex="All", Keywords="Godel,Escher,Bach,Eternal,Golden").decode("utf-8"))

# create cart and add the Godel-Escher-Bach-Eternal-Golden
cart = api.CartCreate(AmathonParameterList=[("Item.1.ASIN","0465026567"), ("Item.1.Quantity",1)]).decode("utf-8")
print(cart)

# get needed data 
cart_id = re.search(r"<CartId>.*</CartId>", cart).group().replace("<CartId>","").replace("</CartId>","")
hmac = re.search(r"<HMAC>.*</HMAC>", cart).group().replace("<HMAC>","").replace("</HMAC>","")

# set proxy
api.set_proxy("http", api_key.proxy_url)

# add The Hitchhiker's Guide to the Galaxy
cart =api.CartAdd(HMAC=hmac,CartId=cart_id,AmathonParameterList=[("Item.1.ASIN", "0345391802"), ("Item.1.Quantity", 1)]).decode("utf-8")
print(cart)

# print purchese_url
purchase_url = re.search(r"<PurchaseURL>.*</PurchaseURL>", cart).group().replace("<PurchaseURL>","").replace("</PurchaseURL>","")
print(purchase_url)

# if you want to use amazon.com you should write like this
api = Amathon(
              AWSAccessKeyId=api_key.access_key,
              ASWSecretAccessKey=api_key.secret_key,
              AssociateTag=api_key.aa_id,
              API_URL="http://webservices.amazon.com/onca/xml"
              )
