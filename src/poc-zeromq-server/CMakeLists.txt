find_package(cppzmq REQUIRED)

add_executable(zeromq-server zeromq-server-main.cpp)
target_link_libraries(zeromq-server cppzmq protobuf-protocol)
