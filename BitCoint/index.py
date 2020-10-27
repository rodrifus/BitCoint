import request
import rumps

class AwesomeStatusBarApp(rumps.App):
    def __init__(self):
        super(AwesomeStatusBarApp, self).__init__("Prototype")
        self.menu = ("querying API...")        
        @rumps.timer(60) 
    def sayhi (self, _):
        headers= {
            'Content-Type': 'application/json',
        }
        r = request.get("https://api.coinbase.com/v2/exchange-rates")
        print (r.json(){'data'}{'rates'}{'EUR'})
        self.title = r.json(){'data'}{'rates'}{'EUR'}

if __name__ =="__main__":
    AwesomeStatusBarApp().run()
 