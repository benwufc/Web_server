# Web-server-POC
using python's library flask to build client.py and server.py and make sure it can be connected with each other.
## Example of usage
**run server.py:**
``python server.py``
and it will show as following:
```
 * Serving Flask app "server" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:6000/ (Press CTRL+C to quit)
```
**run client.py:**
there are three argument should input: --a, --b, --o.
a and b are integer; o is string, you should input "add" or "minus"

```
python client.py --a 69 --b 78 --o minus
```
it will return -9.

```
python client.py --a 69 --b 78 -- add
```
it will return 147.
