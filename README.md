# One Piece Grabber
One piece Grabber (OPG) is a python webscraping script made to grab one piece chapters for convenient reading.
Made since I was tired of all the annoying ads on different manga sites and wanted a cleaner experience.

## Dependencies needed
1. pip install beautifulsoup4
2. pip install requests
3. pip install Pillow

## How it works
It scrapes a manga website by using the request and beautiful soup library. Once it does this, it'll show the 5 most recent chapters and prompt the user for the chapter they'd like to request. Once the chapter is given, it'll create a folder on the system with the chapter number as it's name and start downloading the manga pages. Once complete, it'll use the downloaded pages and combine them into a pdf document for frictionless reading. 

## Steps

Run the python script and enter the One Piece chapter number you would like to download. 
![image](https://user-images.githubusercontent.com/25711110/232199257-8c7e51a0-fb61-4107-a039-37c739b87679.png)


### Results:
Preliminary results: Images of the chapter are downloaded to a folder.

![image](https://user-images.githubusercontent.com/25711110/231508430-8aeb989e-da2f-4f6d-bbeb-76e7a1a5a81f.png)

Final results: A single PDF with all the pages of the manga chapter.

![image](https://user-images.githubusercontent.com/25711110/232199529-72b4d7b8-e9d7-41bf-bc3f-136e2810622b.png)

## Update:
Instead of individual images, produces a pdf of the manga chapter for convenience. 






