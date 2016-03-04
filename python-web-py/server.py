import web

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
        return 'servo is going left'

class right:
    def GET(self, name):
        return 'servo is going right'

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
