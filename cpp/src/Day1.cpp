#include "Day1.hpp"

int numTimesIncreases(const std::vector<int>& depths) { 
    int count = 0;

    for (int i = 0; i < depths.size(); ++i) {
        const auto& depth = depths[i];

        if (i != 0 && depth > depths[i - 1]) {
            ++count;
        }
    }

    return count;
 }
