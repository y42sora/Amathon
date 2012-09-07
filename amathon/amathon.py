'''
Created on 2012/01/09

@author: y42sora
@requires: Python 3.x

Amazon Product Advertising API for Python 3.x
'''
import re

from amathon.binder import bind_api

class Amathon(object):
    """ Amazon Product Advertising API for Python 3.x

    This is a amazon api wrapper for Python 3.x.

    This libraries make you easier to care for requesting amazon api.

    First you must make Amathon object, this object need api_keys and assocciate ID.
    api = Amathon(AWSAccessKeyId=api_key.access_key, ASWSecretAccessKey=api_key.secret_key, AssociateTag=api_key.aa_id)

    If you want to use proxy, you can set it.
    api.set_proxy("http", api_key.proxy_url)

    The libraries don't save other parameters.

    Afterwards you can call method with parameters.
    print(api.ItemLookup(ItemId="0465026567", ResponseGroup="ItemAttributes").decode("utf-8"))

    This libraries use amazon.co.jp default,  if you want to use amazon.com you should write like this
    api = Amathon(
              AWSAccessKeyId=api_key.access_key,
              ASWSecretAccessKey=api_key.secret_key,
              AssociateTag=api_key.aa_id,
              API_URL="http://webservices.amazon.com/onca/xml"
              )

    If you want to other example you see the example.py.

    All method name is same operation name which described on API reference.
    en : http://docs.amazonwebservices.com/AWSECommerceService/2011-08-01/DG/CHAP_ApiReference.html
    jp : https://images-na.ssl-images-amazon.com/images/G/09/associates/paapi/dg/CHAP_ApiReference.html

    """

    def __init__(self,AWSAccessKeyId, ASWSecretAccessKey, AssociateTag, API_URL="http://webservices.amazon.co.jp/onca/xml"):
        """
        initalized method

        Args:
            AWSAccesKeyId : your access key.
            AWASecretAccessKey : your secret access key.
            AssociateTag : amazon associate tag.
            API_URL : api_url. the amazon japan url is default.
                    if you want to another country's amazon, you should set the url.
        """        
        self.access_key = AWSAccessKeyId
        self.secret_key = ASWSecretAccessKey
        self.aa_tag = AssociateTag
        self.api_url = API_URL
        self.proxy_flag = False
        self.proxy = dict([])
        self.get_url = re.search(r"//.+?/", API_URL).group()[2:-1]        
        
        
    def set_proxy(self,protocol, url):
        """ set proxy url and port
        """
        self.proxy[protocol] = url
        self.proxy_flag = True

    BrowseNodeLookup = bind_api("BrowseNodeLookup")
    ItemLookup = bind_api("ItemLookup")
    ItemSearch = bind_api("ItemSearch")
    CartAdd = bind_api("CartAdd")
    CartClear = bind_api("CartClear")
    CartCreate = bind_api("CartCreate")
    CartGet = bind_api("CartGet")
    CartModify = bind_api("CartModify")
    SimilarityLookup = bind_api("SimilarityLookup")
