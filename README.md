DESCRIPTION
-----------
This is a simple Django demo that uses HTML5 and...
* TeraWurfl to identify the mobile device accessing the web application.
* Jinja2 templates.
* jQueryMobile in the templates to provide a mobile device "look and feel."
* Google Maps to display user's location

For convenience, the mobile device parameters are made available in the
Django RequestContext, so they can be easily accessed in the template.
This allows the template designer to write something like
> {% if device.is_wireless_device %}
>   <p>I'm going mobile!</p>
> {% endif %} 
The specific device capabilities are easily configured in the context
processor.  The remote ip address is added, as well.

GETTING THE AMI
---------------
This application is really just a starting point for people using the AMI.
To get the AMI id, just fill out the form in the application or send an
email to gisdemo-AT-numenet-DOT-com.  It's free!  It's what we use at
Numenet as a starting point for mobile web application backends.

RUNNING DEMO
------------
Check out the [running demo][2] with your mobile device or web browser.

MORE INFORMATION
----------------
Go to [Numenet][1] for more information.

[1]: http://www.numenet.com/	"Numenet, Inc."
[2]: http://demo.numenet.com/	"The demo"
