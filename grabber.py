import requests, bs4, os, shutil
from pathlib import Path
from PIL import Image


if __name__=="__main__":
    base_link="https://onepiecechapters.com" #base url to attach to the hrefs we grab
    onepiece_manga_link="https://onepiecechapters.com/mangas/5/one-piece" # url for the actual manga. Onepiecemanga site stores multiples mangas, not just one piece
    chapter_list_page=requests.get(onepiece_manga_link); 


    if chapter_list_page.status_code==requests.codes.ok:
        chapter_list_soup = bs4.BeautifulSoup(chapter_list_page.text, 'html.parser')
        chapter_containers=chapter_list_soup.select('a.block.border.border-border.bg-card.mb-3.p-3.rounded') #select function selects the html element by class

        #prints 5 most recent chapters
        print("Five most recent chapters:")
        for i in range(5):
            print(chapter_containers[i]['href'].split('-')[-1])
        
        print("What chapter would you like to download?")
        target_number=input() #gets the number of the chapter

        target_url="" #this variable will hold the url link of the chapter we selected
        #the for loop below searches for the target chapter and retrieves it's url
        for chapter in chapter_containers:
            chapter_number=chapter['href'].split('-')[-1]
            if(chapter_number==target_number):
                target_url=chapter['href'] #url found and value placed in target_url
                break
        if(target_url==""):
            print("Chapter not found")
        else:
            print("Please wait. Downloading...")
            complete_chapter_url=base_link+target_url #combines base url and target url to make complete url
            chapter_page=requests.get(complete_chapter_url);
            if chapter_page.status_code ==requests.codes.ok:
                chapter_page_soup = bs4.BeautifulSoup(chapter_page.text, 'html.parser')
                #gets image elements on the page
                image_container=chapter_page_soup.select('.fixed-ratio-content')
                image_links=[]
                for image in image_container:
                    image_links.append(image.get('src')) #gets the src link of each image
                os.mkdir('./{}'.format(target_number)) #make new directory
                #uncomment for termux support
                #os.mkdir('./data/data/com.termux/files/home/storage/shared/{}'.format(target_number)) #make new directory
                count=0
                # adds a new container for the list of images from Pillow
                manga_pages=[]
                for link in image_links:
                    content_file=requests.get(link,stream=True)
                    content_file.raise_for_status()
                    #uncomment for termux
                    #with open(Path('/data/data/com.termux/files/home/storage/shared/{}/{}.png'.format(target_number,count)), 'wb') as f:
                    with open(Path('./{}/{}.png'.format(target_number,count)), 'wb') as f:
                        f.write(content_file.content)
                    temp_image=Image.open(r'./{}/{}.png'.format(target_number, count))
                    #uncomment for termux support
                    #temp_image=Image.open(r'/data/data/com.termux/files/home/storage/shared/{}/{}.png'.format(target_number, count))
                    manga_pages.append(temp_image.convert('RGB'))
                    count+=1
                print("Download Complete. Converting to PDF, please wait...")
                #add conversion code
                manga_pages[0].save(r'./chapter_{}.pdf'.format(target_number), save_all=True, append_images=manga_pages[1:]) #saves as pdf and appends pages
                #uncomment for termux support
                #manga_pages[0].save(r'/data/data/com.termux/files/home/storage/shared/chapter_{}.pdf'.format(target_number), save_all=True, append_images=manga_pages[1:]) #saves as pdf and appends pages
                shutil.rmtree('./{}'.format(target_number)) #removes the images folder we created.
                #uncomment for termux support
                #shutil.rmtree('/data/data/com.termux/files/home/storage/shared/{}'.format(target_number)) #removes the images folder we created.
                print("Conversion complete. Happy reading!")
            else:
                print("Something went wrong")
    else:
        print("Something went wrong")