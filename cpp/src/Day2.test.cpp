#include "Day2.hpp"

#include <gtest/gtest.h>

#include <string>
#include <vector>

static const std::vector<std::string> EXAMPLE_INPUT{
    "forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"};

TEST(Day2Test, PartOne) { ASSERT_EQ(150, getNewPosition(EXAMPLE_INPUT)); }

// TEST(Day1Test, PartTwo) {
//     ASSERT_EQ(5, numTimesIncreasesSlidingWindow(EXAMPLE_INPUT));
// }