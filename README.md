# Looking-Glass
Looking Glass utlity serverside component

Requires gunicorn and Python3.7 or higher

Run ``start.sh`` after installing gunicorn and installing dependencies.

### Usage
#### Looking-Glass uses URL paramaters in order to process the request
###### The paramaters are defined here, we'll use `https://lhr.zt-e.tech` as our example domain. (This is currently active, so you can try this out for yourself!)

```
https://lhr.zt-e.tech/ip=<IP or Hostname here>/op=<operation code, defined below>

Example:

https://lhr.zt-e.tech/ip=1.1.1.1/op=1

This will perform 4 pings to cloudflare's 1.1.1.1 DNS service.
```
  
###### Operation Codes (op=)
 - 1 - Ping IPv4
 - 2 - Ping IPv6
 - 3 - Traceroute IPv4
 - 4 - Traceroute IPv6
 - 5 - MTR IPv4
 - 6 - MTR IPv6
