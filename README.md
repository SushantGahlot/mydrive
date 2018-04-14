#### mydrive
***
#### To build this project, following libraries and plugins have been used-

* jQuery
* jQuery Autocomplete
* Bootstrap
* jQuery Noty
* jQuery File Upload
* Django
* Django Celery
***
#### Usage for these are explained below with screenshots of the project-

* Landing Page or Home Page


![img](https://github.com/SushantGahlot/mydrive/blob/master/docs/Screenshot%20from%202018-04-14%2016-55-27.png)


* To Upload Files, click on the "Upload" button on the navbar and a modal will pop-up


![img](https://github.com/SushantGahlot/mydrive/blob/master/docs/Screenshot%20from%202018-04-14%2016-55-41.png)


* From this modal, we choose the file to be uploaded along with the category and click the "Save Changes" button


![img](https://github.com/SushantGahlot/mydrive/blob/master/docs/Screenshot%20from%202018-04-14%2017-24-05.png)


* The file is then uploaded to the server and on successful upload, it shows up on the home page
* To search a file, we click on the search bar on the navbar, this is where jQuery autocomplete helps

![img](https://github.com/SushantGahlot/mydrive/blob/master/docs/Screenshot%20from%202018-04-14%2016-55-58.png)


* After selecting a file, we are redirected to the individual file page where we can either delete the file or change the category of the file

![img](https://github.com/SushantGahlot/mydrive/blob/master/docs/Screenshot%20from%202018-04-14%2016-56-03.png)
![img](https://github.com/SushantGahlot/mydrive/blob/master/docs/Screenshot%20from%202018-04-14%2016-56-10.png)

##### To delete files in the background and not block the request, I have used celery so that if a file is large that needs to be deleted, user is not timed-out while waiting for the file to be deleted or request to be completed.
