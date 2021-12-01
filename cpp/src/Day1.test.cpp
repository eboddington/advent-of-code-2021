#include "Day1.hpp"

#include <gtest/gtest.h>

TEST(Day1Test, PartOne) {
    ASSERT_EQ(7, numTimesIncreases(
                     {199, 200, 208, 210, 200, 207, 240, 269, 260, 263}));
}