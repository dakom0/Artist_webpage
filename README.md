# Artist Webpage
-----


#### Coldplay

This app is based on the popular band [Coldplay](http://coldplay.com/). This app retrieves song and image data from Twitter and Genius' API. Every refresh displays a random song and a random quote from Twitter. There is an image of the band, image of the song, song's name and random quotes about Coldplay on the page.

### Search theme

  The quotes I searched for was 'Coldplay'. I used a url from twitter where I sorted the quotes by popularity and in English only.
  
For the song image and title, I searched for 'Coldplay' on Genius' API and parsed the json to get the image and title in the result block.

### Known Issues

The project was mostly operational. I did have some issues before completing the app. These were:

* When deploying to Heroku there was an error that the server was unavailable. The issue was, I didnt push every file to github, specifically the html file. This meant that Heroku couldnt read the html file that I linked app.py to. Once I pushed all files and folders to the github repo, the app was running without errors.





**Click [here](https://warm-savannah-67240.herokuapp.com/) to see the App!**

