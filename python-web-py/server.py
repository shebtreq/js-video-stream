import web
import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyACM0'
print ("Serial class", ser)
ser.open()
print ("Is serial port open?", ser.is_open)


#Setup server
urls = (
    '/(.*)left', 'left',
    '/(.*)right', 'right',
    '/(.*)', 'server_default',
)

class server_default:
    def GET(self, name):
        return 'server reached'

class left:
    def GET(self, name):
        ser.write(b'l');
        print('left');
        return 'servo is going left'

class right:
    def GET(self, name):
        ser.write(b'r');
        print('right');
        return 'servo is going right'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
