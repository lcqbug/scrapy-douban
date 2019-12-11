from scrapy import mail,middleware
from scrapy.downloadermiddlewares import *
abc = ...
print(abc)
print(type(abc))
# ellipsis

class xxx: ...
Ellipsis = ...  # type: ellipsis
# class xxx:
#     ...

x = xxx()
print(Ellipsis)
from scrapy.http.response.text import TextResponse
from scrapy.http.request import Request
from scrapy.http.response import Response
from six.moves.urllib.parse import urljoin
