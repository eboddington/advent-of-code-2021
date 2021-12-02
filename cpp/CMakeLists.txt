cmake_minimum_required(VERSION 3.20)
project(advent-of-code-2021)

set(CMAKE_CXX_STANDARD 20)

# The order is important here:
# 1. Include googletest with FetchContent

# Latest commit passing CI on main as of 01/12/21
include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/3e0e32ba300ce8afe695ad3ba7e81b21b7cf237a.zip
)
# For Windows: Prevent overriding the parent project's compiler/linker settings
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

# 2. Add main executables

add_executable(
        advent-of-code-2021
        src/main.cpp
)

# 3. Lastly, enable testing and add/link test executables

enable_testing()

add_executable(
        advent-of-code-2021-tests
        src/Day1.test.cpp src/Day1.cpp
        src/Day2.test.cpp src/Day2.cpp
)
target_link_libraries(
        advent-of-code-2021-tests
        gtest_main
)

include(GoogleTest)
gtest_discover_tests(advent-of-code-2021-tests)
