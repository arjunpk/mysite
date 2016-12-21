from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

def index(request):
  redirect('/')

def upload_image(photo, request, base_dir, base_x, base_y):
  """Method to be used for uploading image
  Generic method for rescaling and uploading 
  base_dir is the path where file needs to be uploaded
  base_x and base_y are are the base resolutions given in lanndscape mode
  For ex. for 1080p base_x = 1920 and base_y = 1080
  If image is smaller than the provided resolution, no rescaling is done
  Method returns the path to the image (includes base_dir) on successful upload else returns a null string
  """
  import os
  import hashlib
  from PIL import Image
  from django.core.files.storage import default_storage as storage
  if not photo:
    return ''
  path = photo.name
  filename_base, filename_ext = os.path.splitext(path)
  new_path = base_dir + request.user.uuid + '_' + request.album.uuid + '_' + request.photo.uuid+'_'+str(base_x)+'_'+str(base_y) + '.jpg'
  try:
    # resize the original image and return url path of the thumbnail
    image = Image.open(photo)
    width, height = image.size
    x = 0
    y = 0
    if width > height:
      if width > base_x:
        x = base_x
        y = base_x * height / width
      else:
        x = width
        y = height
    else:
      if height > base_y:
        x = base_y * width / height
        y = base_y
      else:
        x = width
        y = height
    image_compressed = image.resize((x, y), Image.ANTIALIAS)
    f_compressed = storage.open(new_path, "w")
    image_compressed.convert('RGB').save(f_compressed, "JPEG", quality=95)
    f_compressed.close()
    return new_path
  except Exception, e:
    print str(Exception.message), str(e)
    return ''  
  
  
