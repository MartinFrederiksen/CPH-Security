# Week-09 SSH + Crypto-1

### Explain conceptually all the following terms, and how/why they are needed for SSH and TLS/SSL.
* Symmetric Encryption
    - En algoritme for kryptografi som bruger en kryptografiske nøgle for at enkryptere en plain tekst og dekryptering af en chifferskrift(cipher tekst).
    - Use case: Ex bluetooth.
* Asymmetric Encryption
    - En algoritme for kryptografi som bruger et par af kryptografiske nøgler for at kunne enkryptere en plain tekst og dekryptere en cipher tekst. Den offentlige nøgle(public) er kendt af mange og den private nøgle(private) er kun kendt af egeren(ham der laver nøglen/kryptere teksten)
    - Use case: Ex SSH / Dankort systemer.
* Hashing
    - En særlig funktion som bruges til at omdanne data fra en stor definitionsmængde til en mindre værdimængde. Har så få kollisioner som muligt, En kollision er når to forskellige inddata giver samme funktionsværdi. Det er kun muligt at gå den ene vej.
    - Use case: Sortering af nøgle/værdier(key/value) par i en database.


### Explain what it takes to safely log in to an SSH server, without having to provide a password.
Dette kræver en offentlig nøgle(public key) og en privat nøgle(private key) og en ip. Offentlig nøgle ligger på serveren du skal oprette forbindelse til og med din private nøgle kryptere du dataen du vil sende til serveren og serveren kan så dekryptere dataen med sin offentlige nøgle. Asymmetrisk kryptering.

Eks: A ønsker at kunne modtage en hemmelig leverance fra B. En tredjepart C må ikke kunne få fat i den hemmelige leverance, og når først den er afsendt, må B heller ikke kunne få fat i leverancen. A sender en hængelås(Public key) til B, men beholder nøglen(Private key). B låser leverancen nede i en kasse og sender den til A. A åbner kassen med sin nøgle. 


### Explain the term SSH-tunnel, and provide a practical example for its use.
Secure shell tunneling er en krypteret tunnel til at overføre ikke krypteret traffik. Når en server og en client har godkendt hinanden vha. offentlig/privat nøglepar(public/private key pairs) bliver der etableret en SSH-tunnel til at kryptere alt data mellem client og server så offentlig/privat nøgleparrene ikke længere skal bruges.


### Explain conceptually the purpose of Symmetrical Encryption, Asymmetrical Encryption and hashing for an SSH-connection.
- Symmetrisk kryptering bruges af SSH-tunnelen til at kryptere dataen der skal sendes imellem clienten og serveren.
- Asymmetrisk kryptering bruges til at oprette SSH-tunnelen, ved at sende den Symmetriske nøgle med de asymetriske nøgler til begge parter.
- Hashing bruges af SSH-tunnelen for at minimere datamangden der skal krypteres. Ex client sender plain tekst hashed og sender tekst krypteret for at server kan dekryptere tekst og hashe teksten for at se om det er det samme som clients hashed tekst.



### Explain the steps you have to go through to set up a server with MySQL,  as secure as possible →
* How can we limit the client IP's that can connect
    - Vi kan begrænse clientens IP's der kan forbinde ved at tilføje ip'erne til serveren firewall og give tilladelse til at bruge port 3306 til den givne ip.
* If set up to allow only localhost and a firewall that deny 3306, can we still connect “safely” from a remote server 
    - Ja igennem en SSH-tunnel
* how to set up an SSL connection that anyone can use
    - Ved at tilføje mysqld med require_secure_transport=ON i /etC/mysql/my.cnf, og generere mysql ssl rsa nøgler
* Demonstrate a client application (Java or whatever you prefer) running on a separate server that access the Database using SSL
    - Vis øvelserne fra denne uge!