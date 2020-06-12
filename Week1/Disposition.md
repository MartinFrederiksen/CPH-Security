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
* Afsløring - Hvad er sandsynligheden for at udnyttelsen af sårbarheden bliver opdaget.

<table align="center">
    <tbody>
        <tr>
            <td align="center">0 < 3</td>
            <td align="center">3 < 6</td>
            <td align="center">6 < 10</td>
        </tr>
        <tr>
            <td align="center">Low</td>
            <td align="center">Medium</td>
            <td align="center">High</td>
        </tr>
    </tbody>
</table>

<table align="center">
    <thead>
        <tr>
            <th align="center", colspan="8">Sandsynligheds udregning</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">Erfaring</td>
            <td align="center">Motiv</td>
            <td align="center">Mulighed</td>
            <td align="center">Størrelse</td>
            <td align="center">Opdage</td>
            <td align="center">Udnytte</td>
            <td align="center">Opmærksomhed</td>
            <td align="center">Afsløring</td>
        </tr>
        <tr>
            <td align="center">5</td>
            <td align="center">9</td>
            <td align="center">4</td>
            <td align="center">9</td>
            <td align="center">3</td>
            <td align="center">3</td>
            <td align="center">4</td>
            <td align="center">8</td>
        </tr>
        <tr>
            <td align="center", colspan="4" >Sandsynlighed</td>
            <td align="center">5.625</td>
            <td align="center", colspan="3" >Medium</td>
        </tr>
    </tbody>
</table>



| Sandsynlighed	|
|-----	|-----	|-----	|-----	|-----	|-----	|-----	|-----	|
|Erfaring|Motiv|Mulighed|Størrelse|Opdage|Udnytte|Opmærksomhed|Afsløring|
|   5	|   9	|   4	|   9	|   3	|   3	|   4	|   8	|
|   Sandsynlighed	|   5.625	|   Medium	|

### Give some examples of how you can change those parameters - for example for MySQL servers.


### Explain how security risks are rated in OWASP.


### Argue whether OWASP gives the complete picture of security risks on an application.
