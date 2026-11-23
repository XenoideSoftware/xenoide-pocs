find_package(cppzmq REQUIRED)

add_executable(zeromq-client zeromq-client-main.cpp)
target_link_libraries(zeromq-client cppzmq protobuf-protocol)
