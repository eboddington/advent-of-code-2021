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

 int numTimesIncreasesSlidingWindow(const std::vector<int>& depths) {
     std::vector<int> sums{};
     int count = 0;

     for (int i = 1; i < depths.size() - 1; ++i) {
         const auto sum = depths[i - 1] + depths[i] + depths[i + 1];

         if (sums.size() != 0 && sum > sums.back()) {
             ++count;
         }

         sums.push_back(sum);
     }

     return count;
 }
