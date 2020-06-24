# Week 13 - Crypto - 2
Group: Martin Frederiksen(cph-mf237), Andreas Vikke(cph-av105).

    (Localhost-Wire-Dump-TLS) (Filter: tcp.stream eq 0 && tls)

### Explain conceptually all the following terms, and how/why they are all needed for TLS/SSL 
- **Symmetric Encryption:** Er en algoritme for kryptografi der bruger den samme nøgle til at kryptering af "plaintext" og dekryptering af "ciphertext". Største ulempe ved det er at begge ender skal kende til nøglen.
- **Asymmetric Encryption:** Er en algoritme for kryptografi der bruger et par af nøgler; "public keys", som kan formidles til alle og "private keys" som kun kendes af ejeren.
- **Hashing and MAC:** Hashing er en metode der tager et input og retunere en fast-størrelse alfanumerisk streng. MAC er en metode der bygger videre på hasing og sikre autenticitet af beskeden, hvilket vil sige at den sikre at besked kommer fra serveren der har sendt den.
- **Digital Signatures and Certificates** Er data der fungere som et fysisk certificat. Den indeholder en public key, information om clienten såsom navn og id, og en eller flere digitale signature. Så i bund og grund er det en "public key" forbundet med 2 former af ID og et godkendelsesstempel fra en betroet tredje part.
- **Certificate Authorities and Certificate Trust Hierarchies:** Betroede certificat myndigheder er en tredje part som begge clinter kan betro, de certificerer integriteten af public keysne. Formatet for disse certifikater er standard X.509 or EMV.
- **Cipher Suites:** består af (1) nøgle udveksling (2) godkendelse (3) bulk kryptering (4) MAC-algoritme, og bruges til at få de 2 sider til at blive enige om en algoritme der skal bruges.
- **Diffie–Hellman key exchange:** etablere en delt hemmelig nøgle mellem 2 parter, som kan blive brugt til hemmelig kommunikation .

### How we use them for TLS/SSL
Kommunikationen starter med at clienten sender SSL version og Cipher Suites til serveren. Her efter sender severen Certificatet tilbage. Clientet generer en pre-master nøgle og kryptere den med public nøglen fra certificatet, dette bliver brugt til at lave MAC og secret key. Serveren motager pre-master nøglen og generere MAC og secret key. Nu kan clineten og serveren kommunikere sikkert.

![SSL](https://raw.githubusercontent.com/AndreasVikke/CPH-Business-Security/master/Week13/SSL.png "SSL")