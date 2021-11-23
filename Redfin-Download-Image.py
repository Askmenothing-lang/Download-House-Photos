## Importing Necessary Modules
from ctypes import string_at
import requests # to get image from the web
import shutil # to save it locally
import os
import string


def download_images(sequence):
    failed_counter = 0

    for x in range(1, 100):
        # Open the url image, set stream to True, this will return the stream content.
        image_url = image_base_url + "_" + str(x) + "_" + str(sequence) + ".jpg"
        print('Tring to download:', image_url)
        r = requests.get(image_url, stream = True)
        filename = image_url.split("/")[-1]
        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image sucessfully Downloaded: ',filename)
        else:
            #print('Image Couldn\'t be retreived')
            failed_counter += 1
        
        if failed_counter > 5:
            print("Exiting as download failed 5 times")
            break


def mls_entry_flow (mlsid):

    last_3_mlsid = mlsid[-3:]
    ## Set up the image URL and filename
    # "https://ssl.cdn-redfin.com/photo/8/bigphoto/300/ML81866300_1_4.jpg"
    main_image_url = "https://ssl.cdn-redfin.com/photo/8/bigphoto/" + last_3_mlsid + "/" + mlsid + "_"

    mlsid = (main_image_url.split("/")[-1]).split("_")[0]


def create_folder(mlsid):
    cwd = os.getcwd()
    directory = cwd + "/" + mlsid

    if not os.path.exists(directory): 
        os.mkdir(directory)
    os.chdir(directory)

input_main_image_url = input('Enter Redfin picture url (ex:https://ssl.cdn-redfin.com/photo/8/bigphoto/849/ML81846849_1_A.jpg):')

image_base_url = input_main_image_url.split('_')[0]
image_sequence = input_main_image_url[-5:].split('.')[0]
print (image_sequence)
mlsid = (input_main_image_url.split('_')[0]).split('/')[-1]

#input_mls = input('Enter mls id:')

create_folder(mlsid)

download_images(image_sequence)


#Find which number sequence "i" is present for the pictures https://ssl.cdn-redfin.com/photo/8/bigphoto/849/ML81846849_4_"i".jpg
for i in range(1, 20):

    image_url = main_image_url + "1_" + str(i) + ".jpg"
    if requests.get(image_url, stream = True).status_code == 200:
        print("Sequence for downloading image is %d as we found %s", i , image_url)
        download_images(i)
