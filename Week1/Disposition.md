# Week-01 OWASP Rating Methodology


### Explain the two sets of Factors - Threat Agents and Vulnerability.
#### Risk = Likelihood ∗ Impact
* Truslen der er involveret.
* Angrebet der vil blive brugt.
* Sårbarhed involveret.
* Indvirkningen af en succesfuldt udnyttelse af virksomheden.

#### Trussel(Hacker gruppen) og sårbarhed = sandsynligheden(likelihood)
##### Trussel
* Erfaring - Hvor teknisk erfarne er gruppen.
* Motiv - Hvor motiveret er gruppen til at finde og udnytte sårbarheden.
* Mulighed - Hvilke muligheder og ressourcer er krævet for gruppen for at finde og udnytte sårbarheden.
* Størrelse - Hvor stor er gruppen.

##### Sårbarhed
* Opdage - Hvor nemt er det for gruppen at opdage sårbarheden.
* Udnytte - Hvor nemt er det for gruppen at udnytte sårbarheden.
* Opmærksomhed - Hvor kendt er sårbarheden for gruppen.
* Afsløring af indtrængen - Hvad er sandsynligheden for at udnyttelsen af sårbarheden bliver opdaget.

| Are           |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |



|   0 < 3	|   Low	|
|   3 < 6	|   Medium	|
|   6 < 10	|   High	|

| Sandsynlighed	|
|-----	|-----	|-----	|-----	|-----	|-----	|-----	|-----	|
|Erfaring|Motiv|Mulighed|Størrelse|Opdage|Udnytte|Opmærksomhed|Afsløring af indtrængen|
|   5	|   9	|   4	|   9	|   3	|   3	|   4	|   8	|
|   Sandsynlighed	|   5.625	|   Medium	|

### Give some examples of how you can change those parameters - for example for MySQL servers.


### Explain how security risks are rated in OWASP.


### Argue whether OWASP gives the complete picture of security risks on an application.
