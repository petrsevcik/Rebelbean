# README example template #

### Description ###


#### Endpoints ####
#### Search page ####

Welcome page with input field for search in movie and actors

When you click on "Search" button you will be redirected to Search result page

`http://localhost:8080/`


## Architecture ##

#### Flaws of app ####

### All is ready to use via Dockerfile
#### Commands for docker startup
App run on **port 8080**. Run commands, when current location is repository:
```
docker build -t rebelbean:1.0 .
docker run -d -p 8080:8080 rebelbean:1.0
```