# generate any qr code using python...
    
#Solution:-
import qrcode

qr = qrcode.make("https://www.youtube.com/watch?v=X2J9ItR9OKo")
qr.save('qr.png')
