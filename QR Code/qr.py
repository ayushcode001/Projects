import qrcode as qr
img = qr.make("https://youtu.be/pb1Wi--lky8")
img.save('video.png')