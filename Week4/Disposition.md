# Week 5 - Security+Penetration-Testing, Tools + how to practice 

### Explain briefly about the concept of Security Testing, and more thoroughly about Penetration Testing
Security Testing er en metode til altid at teste systemer undervejs i forløbet, "Test Early and Test Often".
    - Manuel inspection og anmeldelser
    - Threat Modeling
    - Code Review
    - Penetration Testing

En af metoderne der kan bruges er Penetration Testing, hvor en attacker for et bruger loggin og skal derfra finde en vej ind i systemet. Attackeren kender ikke til hvordan programmet virker (black box) men prøver at finde vulnerabilities ved at agere som en hacker.

### Explain the pros & cons related to Penetration Testing
#### Pros
- Det er hurtigt og derved billigt
- Kræver mindre skill-set end source code review.
- Koden der bliver testet er koden der vil udsat

#### Cons
- Det sker for sent i SDLC (Systems development life cycle)
- Tester kun fra fronten

### Explain a few (one or two) of the tools meant for Penetration Testing
- NMAP (netdiscover)
    - Kan scanne netværker, finde åbne porte eller gætte OS brugt.
- WireShark
    - Network Protocol analyzer, bruges til at catche indgående og udgående traffik på systemet. HTTP, DNS, IP osv.
- BurpSuite
    - Tool til at intercepte requests, og ændre på dem inden de bliver sent
- Postman
    - Tool til at sende custom HTTP requests med

### Explain the purpose of NMap and what can be discovered with the tool, using one or more prepared samples
1. NMAP kan finde åbne porte på et netværk.
    - nc -lvp 2222
    - nmap 127.0.0.1
<table align="center">
    <thead>
        <tr>
            <th>PORT</th>
            <th>STATE</th>
            <th>SERVICE</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">21/tcp</td>
            <td align="center">filtered</td>
            <td align="center">ftp</td>
        </tr>
        <tr>
            <td align="center">53/tcp</td>
            <td align="center">open</td>
            <td align="center">domain</td>
        </tr>
        <tr>
            <td align="center">80/tcp</td>
            <td align="center">filtered</td>
            <td align="center">http</td>
        </tr>
        <tr>
            <td align="center">3333/tcp</td>
            <td align="center">open</td>
            <td align="center">dec-notes</td>
        </tr>
        <tr>
            <td align="center">5555/tcp</td>
            <td align="center">filtered</td>
            <td align="center">freeciv</td>
        </tr>
    </tbody>
</table>

2. NMAP kan også finde hvilket OS systemt kører
    - nmap 91.100.104.27 -O
<table align="center">
    <tbody>
        <tr>
            <th align="center">Running:</th>
            <td align="center">Linux 2.6.X</td>
        </tr>
        <tr>
            <th align="center">OS CPE:</th>
            <td align="center">cpe:/o:linux:linux_kernel:2.6</td>
        </tr>
        <tr>
            <th align="center">OS details:</th>
            <td align="center">Linux 2.6.9 - 2.6.27</td>
        </tr>
    </tbody>
</table>

### Explain “ways” to legally practice Penetration Tester Skills
Der er mange sider såsom TryHackMe.com som udbyder maskiner du kan lave penetration test på, udover dette findes der test enviroment som man selv kan sætte op, såsom Metasploitable 2 og Juice Shop

### Explain the concepts (where do they fit in) Kali Linux, Metasploitable 2 (and 3) OWASP Juice Shop.
#### Kali Linux
Er et Linux build lavet til hacking, det kommer med stort set alle programmer installeret, så man nemt bare kan komme igang.

#### Metasploitable 2
Er en server med fejl som man kan prøve at finde genne Pen-testing, f.eks. er Tomcat 5.5 installeret som har kom med et default password til admin login som var tomcat.

#### Juice Shop
Er en hjemmeside med et scoreboard, hvor det gælder om at finde flest mulige fejl som kan udnyttes.

### Explain a possible test-setup using Kali Linux and Metasploitable x (or similar) and why testing/practising in this way “makes sense”
