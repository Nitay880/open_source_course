import socket
N = 4
M=5
"""
                                                                  
                                                                  
                                                                  
                                                                  
                          __  ,-.                         __  ,-. 
  .--.--.               ,' ,'/ /|      .---.            ,' ,'/ /| 
 /  /    '      ,---.   '  | |' |    /.  ./|    ,---.   '  | |' | 
|  :  /`./     /     \  |  |   ,'  .-' . ' |   /     \  |  |   ,' 
|  :  ;_      /    /  | '  :  /   /___/ \: |  /    /  | '  :  /   
 \  \    `.  .    ' / | |  | '    .   \  ' . .    ' / | |  | '    
  `----.   \ '   ;   /| ;  : |     \   \   ' '   ;   /| ;  : |    
 /  /`--'  / '   |  / | |  , ;      \   \    '   |  / | |  , ;    
'--'.     /  |   :    |  ---'        \   \ | |   :    |  ---'     
  `--'---'    \   \  /                '---"   \   \  /            
               `----'                          `----'             
                                                                  """


class server:
    def __init__(self, mediator_host,mediator_port):
        """
        :param sockets: i's server sockets with 0...N servers.
        """
        self._worlds = {i: [] for i in range(N)}
        self._last_elected = 0
        self._view = 0
        self._control_plane_messages = []
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self._mediator_socket:
            self._mediator_socket.connect((mediator_host, mediator_port))
            self._mediator_socket.sendall(b'Hello, world')

    def get_message(self, message):
        self._control_plane_messages.append(message)
    def start_work(self):
        while True:
            msg = self._mediator_socket.recv()
            self.get_message(msg.decode("utf-8"))
            # print(msg)
