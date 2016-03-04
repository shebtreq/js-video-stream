import web
import serial

ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyACM0'
print "Serial Class:" ser
ser.open()
print "Is Serial Port open? " ser.is_open


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
        ser.write('l');
        return 'servo is going left'

class right:
    def GET(self, name):
        ser.write('r');
        return 'servo is going right'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
