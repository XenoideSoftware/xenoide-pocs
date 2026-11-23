// Hello World server using cppzmq (the header-only C++ binding for libzmq).
#include <zmq.hpp>

#include <chrono>
#include <iostream>
#include <string>
#include <thread>
#include <vector>

#include "message.pb.h"

using namespace std;

int main(int argc, char *argv[]) {
    (void)argc;
    (void)argv;
    const string endpoint = "tcp://*:5555";

    zmq::context_t context(1);
    zmq::socket_t socket(context, zmq::socket_type::rep);
    socket.bind(endpoint);

    int id = 0;
    while (true) {
        zmq::message_t request;
        auto received = socket.recv(request, zmq::recv_flags::none);
        if (!received) {
            cerr << "receive failed" << endl;
            return 1;
        }

        std::this_thread::sleep_for(std::chrono::seconds(1));
        cout << "Received Hello" << endl;

        Message protoMessageToSend;
        protoMessageToSend.set_id(++id);
        protoMessageToSend.set_content("World");

        std::vector<char> buffer;
        buffer.resize(protoMessageToSend.ByteSizeLong());
        protoMessageToSend.SerializeToArray(buffer.data(), static_cast<int>(buffer.size()));

        socket.send(zmq::buffer(buffer.data(), buffer.size()), zmq::send_flags::none);
    }
}
