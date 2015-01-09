# fish
Simple website for a fish shop

<h3>Introduction</h3>
************

This is basically a little website to allow our customer's cliens to place orders online and to view basic information
about the business. 

<h3>Of Interest</h3>
************

Inside the gem_soft folder is a script to run an asynchronous process in the background. On the main page is a button
which, when clicked, sends a message to the process in the background. Currently, the flow of information is only one
way. This will potentially allow our server to respond to long running requests (such as back-ups, sending bulk email,
etc) without the page freezing, since they are carried out in the background. The background process is currently
being started by supervisord (but could be run from the terminal manually and should still work).
