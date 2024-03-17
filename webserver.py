from http.server import HTTPServer, BaseHTTPRequestHandler
from email.message import EmailMessage
from urllib.parse import parse_qs

tasklist = ['Task 1', 'Task 2', 'Task 3']

PORT = 9000

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith('/tasklist'):
            self.send_response(200) # method is called whenever the server receives a GET request and sends a 200 OK response
            self.send_header('content-type', 'text/html')
            self.end_headers()
            
            output = ''
            output += '<html><head>'
            output += '<style>'
            output += '''
                html, head {
                    padding: 0;
                    margin: 0;
                    height: 100%;
                }

                body {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background: linear-gradient(to right, #092583, #3b18eb); 
                    background-attachment: fixed;
                    position: relative;
                }

                .container {
                    padding: 0 150px;
                    background-color: #fff;
                    height: 60%;
                    border-radius: 15px;
                    position: absolute;
                    top: 40%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                }

                .container h1 {
                    display: block;
                    width: 100%;
                    background: #fff;
                    margin: 0;
                    padding: 10px 0;
                    font-size: 50px;
                }

                h3 {
                    text-align: center;
                    font-size: 20px;
                    background: #3b18eb;
                    border-radius: 6px;
                    padding: 5px;
                    margin: 0 0 20px;
                }

                a {
                    text-align: center;
                    text-decoration: none;
                    color: #fff;                   
                }

                .task-item {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    margin-bottom: 10px;
                    font-size: 20px;
                }

                .task-item a {
                    color: white;
                    background-color: #e72f2f;
                    padding: 5px 10px;
                    border-radius: 6px;
                    text-decoration: none;
                    font-size: 16px;
                }
                '''
            output += '</style>'
            output += '</head><body>'
            output += '<div class="container">'
            output += '<h1>Tasklist</h1>'
            output += '<h3><a href="/tasklist/new">Add New Task</a></h3>'

            for task in tasklist:
                output += '<div class="task-item">'
                output += f'{task}'
                output += f'<a href="/tasklist/{task}/remove">Delete</a>'
                output += '</div>'

            output += '</div>'
            output += '</body></html>'
            self.wfile.write(output.encode()) # writes the requested path back to the client. It encodes the path string into bytes beforehand

        if self.path.endswith('/new'):
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><head>'
            output += '<style>'
            output += '''
                html, head {
                    padding: 0;
                    margin: 0;
                    height: 100%;
                }

                body {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background: linear-gradient(to right, #092583, #3b18eb); 
                    background-attachment: fixed;
                    position: relative;
                }

                .container {
                    padding: 0 100px;
                    background-color: #fff;
                    height: 60%;
                    border-radius: 15px;
                    position: absolute;
                    top: 40%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                }

                .container h1 {
                    background: #fff;
                    margin-bottom: 30px;
                    padding: 10px 0;
                    font-size: 50px;
                    white-space: nowrap;
                }

                form {
                    padding: 15px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    background: #3b18eb;
                    border-radius: 10px;
                }

                form input[type="text"],
                form input[type="submit"] {
                    width: 80%;
                    margin-bottom: 10px;
                }

                form input[type="submit"]:hover {
                    cursor: pointer;
                }

                '''
            output += '</style>'
            output += '</head><body>'
            output += '<div class="container">'
            output += '<h1>Add New Task</h1>'

            output += '<form method="POST" enctype="multipart/form-data" action="/tasklist/new">'
            output += '<input name="task" type="text" placeholder="Add new task">'
            output += '<input type="submit" value="Add">'
            output += '</form>'
            output += '</div>'
            output += '</body></html>'

            self.wfile.write(output.encode())

        if self.path.endswith('/remove'):
            listIDPath = self.path.split('/')[2] # third / in url
            self.send_response(200)
            self.send_header('content-type', 'text/html')
            self.end_headers()

            output = ''
            output += '<html><head>'
            output += '<style>'
            output += '''
                html, head {
                    padding: 0;
                    margin: 0;
                    height: 100%;
                }

                body {
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    background: linear-gradient(to right, #092583, #3b18eb); 
                    background-attachment: fixed;
                    position: relative;
                }

                .container {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    padding: 0 100px;
                    background-color: #fff;
                    height: 60%;
                    border-radius: 15px;
                    position: absolute;
                    top: 40%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                }

                .container h1 {
                    width: 100%;
                    background: #fff;
                    margin: 0 0 30px;
                    padding: 10px 0;
                    font-size: 50px;
                    white-space: nowrap;
                }

                .container h1 span {
                    padding: 5px;
                    background: #3b18eb;
                    border-radius: 6px;
                }

                .content {
                    display: flex;
                    flex-direction: row; 
                    justify-content: center;
                }

                a, form {
                    width: 100px;
                    height: 30px;
                }

                a {
                    text-decoration: none;
                    color: #fff;  
                    padding: 5px;
                    background: #3b18eb;
                    border-radius: 6px;    
                    margin-left: 10px;
                    font-size: 18px;  
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }

                form {
                    padding: 5px;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    justify-content: center;
                    background: #3b18eb;
                    border-radius: 6px;
                    margin: 0 auto;
                }

                form input[type="submit"]:hover {
                    cursor: pointer;
                }

                '''
            output += '</style>'
            output += '</head><body>'
            output += '<div class="container">'
            listIDPath_modified = listIDPath.replace('%20', ' ')
            output += f'<h1>Task to Remove: <span>{listIDPath_modified}</span></h1>'
            output += '<div class="content">'
            output += f'<form method="POST" enctype="multipart/form-data" action="/tasklist/{listIDPath}/remove">'
            output += '<input type="submit" value="Remove"></form>'
            output += '<a href="/tasklist">Cancel</a>'
            output += '</div>'
            output += '</div>'
            output += '</body></html>'

            self.wfile.write(output.encode())

    def do_POST(self):
        if self.path.endswith('/new'):
            content_type_header = self.headers.get('content-type', '')
            content_type_message = EmailMessage()
            content_type_message['Content-Type'] = content_type_header

            content_type_value = content_type_message.get_content_type()

            if content_type_value == 'multipart/form-data':
                content_length = int(self.headers.get('content-length', 0))
                body = self.rfile.read(content_length).decode('utf-8')

                # split the body using boundary markers to extract the task value
                boundary = content_type_header.split('boundary=')[1] # list that contains two elements, content-type= and boundary=
                parts = body.split('--' + boundary)
                print(boundary)
                print(parts)
                for part in parts:
                    if 'name="task"' in part:
                        new_task = part.split('\r\n\r\n')[1].strip()
                        tasklist.append(new_task)

            self.send_response(301) # redirect request
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()

        if self.path.endswith('/remove'):
            listIDPath = self.path.split('/')[2]
            content_type_header = self.headers.get('content-type', '')
            content_type_message = EmailMessage()
            content_type_message['Content-Type'] = content_type_header
            content_type_value = content_type_message.get_content_type()

            if content_type_value == 'multipart/form-data':
                list_item = listIDPath.replace('%20', ' ')
                tasklist.remove(list_item)

            self.send_response(301)
            self.send_header('content-type', 'text/html')
            self.send_header('Location', '/tasklist')
            self.end_headers()



def main():
    server_address = ('localhost', PORT)
    server = HTTPServer(server_address, requestHandler)
    print(f'Server running on port {PORT}')
    server.serve_forever()

if __name__ == '__main__':
    main()