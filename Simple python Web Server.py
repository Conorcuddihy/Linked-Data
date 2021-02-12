Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import http.server
>>> import socketserver
>>> PORT = 8000
>>> Handler = http.server.SimpleHTTPRequestHandler
>>> with socketserver.TCPServer(("", PORT), Handler) as httpd:
	httpd.serve_forever()

	
127.0.0.1 - - [12/Feb/2021 14:26:09] "GET / HTTP/1.1" 200 -
