# A6: Security Misconfiguration + A9: Components with Known Vulnerabilities

This [link points](http://sec-dat-demo.surge.sh/) to an extremely simple Single Page Application, providing a login page and, after a successful login, a page using a single protected REST-endpoint.

See whether you can discover the following properties of the application (not all are necessary security-problems). Use the GUI provided by the application (as a start), Postman, nmap and obviously your browser's Developer Tools, when probing the app:

**Q:** OS?
  - **A:** Linux/Ubuntu

**Q:** Server Architecture (Come up with a “guess” and provide arguments for your suggestion)
  - **A:** nginx - tomcat

**Q:** Server(s)
  - **A:** Linux, Nginx, Tomcat

**Q:** Programming Language
  - **A:** Frontend -> React/Javascript
  - **A:** Backend -> Java

**Q:** Important packages, classes used by the Programming Language
  - **A:** JAX-RS

**Q:** Can you see “what kind of pages” logged-in users will see, without having a way to log in?
  - **A:** Yes trhough looking at the JavaScript more spcific looking in the App.js file from React

**Q:** Can you discover the client technologies used
  - **A:** React can be seen in node modules under debug

**Q:** Default users and Passwords = the ability to login
  - **A:** user, admin -> passwords begge test

**Q:** If you can make a successful login, can you: discover the algorithm used to “protect” the token, the lifetime of the token, the role, assigned to you by the system?
  - **A:** Secret base64, alg: hs256, Life-time 30min - Roles: user, admin

**Q:** How/where is the token stored by the client
  - **A:** In the lcoal storage of the browser

**Q:** Can you determine/guess(must be qualified) whether front-end, REST back-end and Database is running on the same or on different servers?
- **A   :** They are running on different servers, Front-end is runnung on surge and backend is running on digitalocean

**Q:** Can you determine which database is used by the backend?
  - **A:** MySQL v8.0.19

**Q:** Have you discovered any unnecessary features which are enabled or installed (e.g. unnecessary ports, services, pages, accounts, or privileges)
  - **A:** 3306 is open for mysql, this should be closed as the only thing that should be able to call it is a local API

**Q:** Who owns the domain used for the server?
  - **A:** Lars Åke Mortensen - Running on Digital Ocean
    
**Q:** Is the server hosted “privately”, by a cloud provider, or …..?
  - **A:** The server is hosted on digital ocean, can be seen by the nameserver ex. at dkhostmaster

**Q:** Open developer tools, and the network-tab. Enter this URL (exactly as given) http://studypoints.info
Explain the first two requests, you monitor. Is this a problem, could this have been done better” (this probably require that you have read the suggested readings related to security-headers)
  - **A:** The first request redirects you from http to https trough a 301 Status. The second requests the https site.


# A6, Security Headers

#### X-Frame-Options: 
    Disallowes making the site to an <íframe> on another site

#### X-Content-Type-Options:
    nosniff means that it's not allowed to try and guess what the response content type is. So if the sites return json but as text it is showend as text in the browser
    - [Site with json as text](https://security-headers.dat-security.dk/api/json)
    - [Site with json as json](https://security-headers.dat-security.dk/api/jsonwithcontenttype)

#### X-Download-Options:
    noopen, instructs the browser not to try and download the file but instead show it in the browser

#### X-XXS-Protection:
    configures the cross-site scripting filter, which is build into most browsers

#### Content-Security-Policy:
    effective measure to protect site from XSS attacks, by whitelisting sources of approved content.
    - default-src 'self'; style-src 'self' maxcdn.bootstrapcdn.com; font-src 'self'  https: data: