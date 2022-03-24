# https-github.com-itmo-wad-itmo316326-hw2
Login monitoring method:
Listen to the submit request of the login form.
Get the submitted username and password if requested.
Return a count value by querying MongoDB.
If count has a value, it means that the user has registered and the user name is added to the session. Then jump to the user information page.
If count has no value, it means that every time the user has registered, the login fails. Return to the login page and prompt the message information.
Register listener method:
Listen to the submit request of the register form.
Get the user's session. If the user has logged in, the session has a value. So jump directly to the user information page. Avoid double registration.
Otherwise start registration. after request to form data.
Use the insert method of manggoDB to insert the username and password into the user collection. A hash value is returned if the insertion is successful.
Check if there is a hash value. If there is a description of successful registration. By the way, put the username into the session. And jump to the user information page.
If the registration fails, the hash value is empty. And pass the information to the registration page when the page returns to the registration page.
