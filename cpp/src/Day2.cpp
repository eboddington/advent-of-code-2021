#include "Day2.hpp"

int getNewPosition(const std::vector<std::string>& course) {
    int pos = 0;
    int depth = 0;

    for (const auto& command : course) {
        const std::string delim = " ";
        const auto spacePos = command.find(delim);
        const auto op = command.substr(0, spacePos);
        const auto distance = stoi(command.substr(spacePos + delim.length()));

        if (op == "forward") {
            pos += distance;
        } else if (op == "up") {
            depth -= distance;
        } else if (op == "down") {
            depth += distance;
        }
    }

    return pos * depth;
}