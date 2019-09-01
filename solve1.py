from PIL import Image

f = open('challenge.txt','rb')
img_enc = f.readlines()
pixels=[]

for x in img_enc:
   x=x.strip()
   y=x.split('+')
   for m in y:
      c=m[0]
      e=int(m[2:])
      if(c=='0'):
         for i in range(e):
             pixels.append((255,255,255))
      else:
         for i in range(e):
             pixels.append((0,0,0))
img_out=Image.new('RGB',(100,len(img_enc)),'white')
img_out.putdata(pixels)
img_out.save('solution.png')
