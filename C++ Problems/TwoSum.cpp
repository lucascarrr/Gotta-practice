#include <iostream>
#include <unordered_map>
#include <vector>

std::vector<int> twoSum(std::vector<int>& nums, int target);

int main() 
{
    std::vector<int> test_vector = {2, 7, 11, 15};
    int target = 26;

    std::vector<int> result = twoSum(test_vector, target);

    if (!result.empty()) {
        std::cout << "Indices: " << result[0] << " and " << result[1] << std::endl;
    } else {
        std::cout << "No solution found." << std::endl;
    }

    return 0;
}

std::vector<int> twoSum(std::vector<int>& nums, int target) 
{
    std::unordered_map<int, int> map;
  
    for (int i = 0; i < nums.size(); i++ )
    {
        int comp = target - nums[i];
        if (map.count(comp)) 
        {
            return {map[comp], i};
        }
        map[nums[i]] = i;
    }

    return {};
}

