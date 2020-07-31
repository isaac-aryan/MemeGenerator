#IMPORTED STUFF
from PIL import Image, ImageFont, ImageDraw
import speech_recognition as sr
import random, textwrap

url = 'meme.jpg'
font_type = 'fonts/opensans.ttf'
placeholder = 'this text is a placeholder.'
WIDTH = 0
HEIGHT = 0

#Introduction and choice
print("Welcome to my Meme Generator! Before we create a meme, you have to choose the topic.")
print("\nEnter the number of your choice:")
choice=int(input("1] Generic Memes\n2] Football Memes\n3] Personal Memes"))


#Obtaining images from the chosen folder
def randimg():
    if choice==1:
        images=['apu','communist','cry','cupboy','ears','gordon','monkey','pewds','retard','skeleton','tom']
        randnum=random.randint(0, len(images)-1)
        imgurl="images/{}.jpg".format(images[randnum])

        try:
            img=Image.open(imgurl)
            return img
        except IOError as e:
            print("Input/Output Error.")
            return None

    elif choice==2:
        images=['cantwell','dier','eriksen','ferdinand','kane','levy','mbappe','mourinho','mourinho2','pep','team','warnock']
        randnum=random.randint(0, len(images)-1)
        imgurl="fimages/{}.jpg".format(images[randnum])

        try:
            img=Image.open(imgurl)
            return img
        except IOError as e:
            print("Input/Output Error.")
            return None
    
    elif choice==3:
        images=[]
        randnum=random.randint(0, len(images)-1)
        imgurl="cimages/{}.jpg".format(images[randnum])

        try:
            img=Image.open(imgurl)
            return img
        except IOError as e:
            print("Input/Output Error.")
            return None

    else:
        print("Error. You entered an invalid option")

#VOICE INPUT
def spokentext():
  r = sr.Recognizer()
  with sr.Microphone() as source:
      print("Say what you want your meme to say...")
      audio = r.listen(source)
  try:
      print("==> " + r.recognize_google(audio))

  except sr.UnknownValueError:
      print("Did not understand audio.")

  except sr.RequestError as e:
      print("Could not request results from Google Speech Recognition service; {0}".format(e))

  rawtext = r.recognize_google(audio)
  initialtxt = rawtext if rawtext!=None else placeholder
  txt = textwrap.fill(initialtxt, width=WIDTH/15)
  return txt


def overlay(img, txt):
  draw = ImageDraw.Draw(img)
  font = ImageFont.truetype(font_type, int(HEIGHT/25)) 
  draw.text((WIDTH/10, HEIGHT*(8/10)), txt, fill='white', font=font)
  return img

if __name__ == '__main__':
  img = randimg()

  WIDTH, HEIGHT = img.size

  # Second get the text from the user microphone
  txt = spokentext()

  # Ensure that both the txt and img are valid
  if img != None and txt != None:
    meme = overlay(img, txt)
    meme.save(url)
    meme.show()
  else:
    print("Sorry! Something went wrong.")