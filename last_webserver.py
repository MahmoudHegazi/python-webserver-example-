from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class WebServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            if self.path.endswith("/home"):
                self.send_response(200)
                self.send_header("Content-type", "text-html")
                self.end_headers()
                output = ""
                output += "<html><body>"
                output += "<head><style>"
                output += "body {background-color:rgb(250 250 245);text-align:center;}"
                output += "h2, p, h4 {background-color:black;color:white;width:620px;padding:20px;margin-left:27%;}"
                output += "</style></head>"
                output += "<h2>OMG I Created My First Python WebServer </h2>"
                output += "<p>Please If you Like the video subscribe to web developers</p>"
                output += "<h4>Created By Web Developers chanel Yotube</h4>"
                output += "</body></html>"
                self.wfile.write(output)
                print output
                return
        except IOError:
            self.send_error(404, "File Not Found: %s " % self.path)


def main():
    try:
        
        port = 8080
        server = HTTPServer(('', port), WebServerHandler)
        print "Server Is Now Running On Port %s " % port
        server.serve_forever()
        
    except KeyboardInterrupt:
        print "^ C entered Server Is Clossing Now..."
        server.socket.close()
        

if __name__ == '__main__':
    main()
