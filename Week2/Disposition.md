# Week 2 - A2-Broken Authentication, A5-Broken Access Control

## A2
### Explain about OWASP A2, and explain a number of the problems that would leave your application vulnerable to A2-problems
- OWASP A2 handler omkring at finde og udnytte Authentication metoder der er brug top en web application.
    1. Credential stuffing
    2. Brute force
    3. Default, weak or well-known passwords
    4. Exposed Session ID's (in URL)

### For each of the problems explained above, explain how this problem could have been prevented
1. Credential stuffing
    - Implementer multi-factor login.
2. Brute force
    - Implementer multi-factor login.
3. Default, weak or well-known passwords
    - Aldrig brug default password, især ikke på admin accounts. Implementer weak password check, imod et dataset af kendte passwords.
4. Exposed Session ID's (in URL)
    - Aldrig send session ID's over URL'en.

### Explain the idea behind the term Credential Stuffing
Credential Stuffing er en automatiseret injection, med kendte brugernavne og password kombinationer. Disse kombinationer bliver prøvet af på hjemmesiden indtil et match er fundet hvorefter hijakeren kan tage over.

### Demonstrate how you, in practice, have, or could, remove some of the vulnerabilities listed above
- Se password øvelse.

## A5
### Explain about OWASP A5, and explain a number of the problems that would leave your application vulnerable to A5-problems
- OWASP A5 handler omkring at udnytte andres access control til at få adgang til information som man ikke burde kunne få fat i.
    1. Modificere URL or HTML
    2. Tillade primary key at blive skiftet til en anden brugers.
    3. Elevation of privilege (Være bruger udne login, være admin som bruger)
    4. Fejlkonfiguration på CORS

### For each of the problems explained above, explain how this problem could have been prevented
1. Modificere URL or HTML
    - Aldrig have access control checket i browseren, check priviliger på server siden udfra JWT token.
2. Tillade primary key at blive skiftet til en anden brugers.
    - Check authentication a primary key hver gang.
3. Elevation of privilege (Være bruger uden login, være admin som bruger)
    - Altid check på server siden om brugerns token er gyldig
4. Fejlkonfiguration på CORS
    - Implementer access conmtrol mechanims en gang og genbrug dem så de ikke ændre sig.

### Demonstrate how you, in practice, have removed some of the vulnerabilities listed above
### Demonstrate at least one practical example of a A5 Vulnerability, and show how you have solved the problem (removed the vulnerability)
- http://dat-security.dk/a5demo/
- Øvelse a5demo
