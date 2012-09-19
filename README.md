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
>   &lt;p&gt;I'm going mobile!&lt;/p&gt;
> {% endif %} 

The specific device capabilities are easily configured in the context
processor.  The remote ip address is added, as well.

There is a template loader for the Jinja2 templates that allows them to be used side-by-side with the standard Django templates.  Just put them the the jinja_templates directory, at the project or application level.

GETTING THE AMI
---------------
This application is really just a starting point for people using the AMI.
To get the AMI id, just fill out the form in the application or send an
email to gisdemo-AT-numenet-DOT-com.  It's free!  It's what we use at
Numenet as a starting point for mobile web application backends.

RUNNING DEMO
------------
Check out the [demo][1] with your mobile device or web browser.

MORE INFORMATION
----------------
Go to [Numenet][2] for more information.

[1]: http://demo.numenet.com/
[2]: http://www.numenet.com/
