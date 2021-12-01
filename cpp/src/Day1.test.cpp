#include "Day1.hpp"

#include <gtest/gtest.h>

static const std::vector<int> EXAMPLE_INPUT{199, 200, 208, 210, 200,
                                            207, 240, 269, 260, 263};

TEST(Day1Test, PartOne) { ASSERT_EQ(7, numTimesIncreases(EXAMPLE_INPUT)); }

TEST(Day1Test, PartTwo) {
    ASSERT_EQ(5, numTimesIncreasesSlidingWindow(EXAMPLE_INPUT));
}