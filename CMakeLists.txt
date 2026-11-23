cmake_minimum_required (VERSION 3.25)
project (XEPOCS LANGUAGES CXX)

include(XenoideConfig)

set(XE_ENABLE_TESTING "${XENOIDE_ENABLE_TESTING}" CACHE BOOL "Enable the unit test suite" FORCE)

option (XE_ENABLE_POC_CLANG "Enable pocs that require clang" OFF)
option (XE_ENABLE_POC_LSP "Enable pocs that require (LSP) Language Server Protocol" OFF)
option (XE_ENABLE_POC_PROTOBUF "Enable pocs that require Google Protocol Buffers" OFF)
option (XE_ENABLE_POC_WXWIDGETS "Enable pocs that require wxWidgets" OFF)
option (XE_ENABLE_POC_ZEROMQ "Enable pocs that require ZeroMQ" OFF)

add_subdirectory("src")
