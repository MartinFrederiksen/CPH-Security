# Week 8 - Authentication/login- strategies


### Java’s declarative authentication and authorization features
#### Pros
* Framework der er blevet bygget og bliver opdateret
* Det kan bruges på både desktop applikations og web-applikations i en browser. Spootify kan genbruge auth model.
* Du kan bestemme hvad der skal kræves login på. Ex api metoder.
* Du sender kun login en gang. Java session id bliver genbrugt(kinda token).

#### Cons
* Jaas er baseret på HVEM der køre koden og ikke HVAD der bliver kørt i koden.
* Byg ovenpå et allerede eksisterende framework.
* Kræver lidt opsætning - Basic auth er hurtigere at sætte op og kræver ikke db.


### Basic HTTP-authentication
#### Pros
* Nemt at sætte op kræver ikke ex. cookies, sessions.
* State er holdt af HTTP clienten.(Username/Pw)
* På HTTPS vil SSL gøre det mere sikkert i forhold til man in the middle attacks.
* Kun et request - (! token fra api -> der hvor du vil hen)

#### Cons
* Username/Pw bliver sendt ved hvert request.
* Sårbart til man in the middle attacks.
* "Grim" login box.
* Password og username bliver ikke hashet eller krypteret men bliver encoded med base64.
* Brugeren kan ikke logge ud før browser lukkes
* Der kan ikke inkluderes andre informationer end username og password.
* Udsat for bruteforce kan gøres noget på server side.


### Form-based authentication
#### Pros
* Selv lavet login box/side.
* Egen redirect/ forskellige redirects pr bruger(kan ændre siden efter login) side.
* Egen error side.
* Sender ikke login info hver gang der laves en request.
* Kan sende flere ting med.
* Robotbeskyttelse i form af reCaptcha.
* Mulighed for kryptering på form.(Man in the middle)
* Fuld kontrol over authentication code.

#### Cons
* Selv lavet login box/side.
* Skal logge ind hver gang da browseren ikke gemmer info. Uden token.
* Database(admin/program) - Oplysninger skal gemmes og gemmes sikkert.
* Man in the middle - SSL
* Fuld kontrol over authentication code (Vedligeholdelse).


### Token Based authentication
#### Pros
* Stateless
* Payload indeholder alt the nødvendige data om brugeren og derved undgår vi at tilgå serveren mere end en gang.
* Underskrevet vi kan verificere brugeren.
* Skalerbart(nemt).
* Kan deles imellem mange enheder.
* Kan bruges af stort set alle teknologier/Sprog.

#### Cons
* Når en token er underskrevet er den gyldig indtil udløbs tidspunkt.
* Log ud ved at slette token på client siden men token er stadig gyldig. -> Server performance issues hvis vi vælger at blackliste.
* Hvis signerings sikkerheden bliver bragt i fare, vil alle tokens potentielt være i fare.
