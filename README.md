#Amazon Product Advertising API for Python 3.x**

This is a amazon api wrapper for Python 3.x.  
This libraries make you easier to care for requesting amazon api.  
The license is LGPL.

First you must make Amathon object, this object need api_keys and assocciate ID.  
`api = Amathon(AWSAccessKeyId=api_key.access_key, ASWSecretAccessKey=api_key.secret_key, AssociateTag=api_key.aa_id)`

If you want to use proxy, you can set it.  
`api.set_proxy("http", api_key.proxy_url)`  
The libraries don't save other parameters.

Afterwards you can call method with parameters.  
`print(api.ItemLookup(ItemId="0465026567", ResponseGroup="ItemAttributes").decode("utf-8"))`

This libraries use amazon.co.jp default,  if you want to use amazon.com you should write like this  
<pre>
api = Amathon(
			AWSAccessKeyId=api_key.access_key,
            ASWSecretAccessKey=api_key.secret_key,
            AssociateTag=api_key.aa_id,
            API_URL="http://webservices.amazon.com/onca/xml"
			)
</pre>

*If you want to other example you see the example.py.*

'All method name is same operation name which described on API reference.'  
*en : [API Reference - Product Advertising API](http://docs.amazonwebservices.com/AWSECommerceService/2011-08-01/DG/CHAP_ApiReference.html "API Reference - Product Advertising API")  
*jp : [Product Advertising API](https://images-na.ssl-images-amazon.com/images/G/09/associates/paapi/dg/CHAP_ApiReference.html "Product Advertising API")



