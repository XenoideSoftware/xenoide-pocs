// Hello World client using cppzmq (the header-only C++ binding for libzmq).
#include <zmq.hpp>

#include <iostream>
#include <string>

#include "message.pb.h"

using namespace std;

int main(int argc, char *argv[]) {
    (void)argc;
    (void)argv;
    const string endpoint = "tcp://localhost:5555";

    zmq::context_t context(1);
    zmq::socket_t socket(context, zmq::socket_type::req);
    socket.connect(endpoint);

    cout << "Connecting to hello world server..." << endl;
    for (int request_nbr = 0; request_nbr != 10; request_nbr++) {
        cout << "Sending Hello " << request_nbr << "..." << endl;
        socket.send(zmq::buffer(string("Hello")), zmq::send_flags::none);

        zmq::message_t reply;
        auto received = socket.recv(reply, zmq::recv_flags::none);
        if (!received) {
            cerr << "receive failed" << endl;
            return 1;
        }
        cout << "Received World " << request_nbr << endl;
    }
    return 0;
}
