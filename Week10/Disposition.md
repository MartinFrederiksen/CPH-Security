# Week 11 - A1 SQL injection
Group: Martin Frederiksen(cph-mf237), Andreas Vikke(cph-av105).
    (Week4 - JuiceShop) (cd /mnt/c/Users/Bacon/Documents/GitHub/CPH-Business-Security/Week4/juice-shop/)

### Give an example of a SQL inject which will give all users in a user table
- Input: "Hans' or 1 = 1;--"
- SQL: "SELECT * FROM USERS WHERE name = '" + input + "'"
- Combined: SELECT * FROM USERS WHERE name = 'Hans' or 1 = 1; --'


### Explain how prepared statements prevent SQL injection
1. En forberedt sql statement bliver sendt til databasen og bliver klargjort(prepared) hvor den ikke har nogle values men ? istedet. Ex - INSERT INTO MyGuests VALUES(?, ?, ?)
2. Databasen parser, kompilere og optimisere sql statementet og gemmer det uden at eksekvere det.
3. Når sql statementet skal eksekveres binder applikationen værdierne til parameterne.
4. Ingen sql injection fordi vores parameter værdier bliver sendt efterføglende vha en anden protokol.(Escaping)


### Explain how to use placeholders in cases where prepared statements cannot do the job
For at bruge placeholders skal du erstatte placeholderen i strengen med dit input. Dette er ikke en god metode da sql injection kan opstå. 
1. DECLARE @query AS NVARCHAR(255) = N'SELECT * FROM dbo.Table';
2. SELECT @query AS query;


### Explain how logging could be used to monitor injection attempts
Ex. en server kan logge det input data der bliver sendt til den og derved kan der efterføglende ses i loggen om der er sql fragmenter i de inputs der blev sendt. Hvis der er sql fragmenter i input strengende er det med stor sandsynlighed injection forsøg.
