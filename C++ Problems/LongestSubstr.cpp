#include <iostream>
#include <unordered_set>
#include <string>

#define print(X) std::cout << X 

int main()
{
  std::string s = "abcabcbb";

  int length = s.size();

  if (length < 1) 
  { 
    return 1;
  }

  std::unordered_set<char> storage;

  int p1 = 0, p2 = 0, max = 0;

  while (p2 < length) 
  {
    if (storage.count(s[p2]) == 0) 
    {
      storage.insert(s[p2]);
      max = std::max(max, p2-p1+1);
      ++p2;
    } else 
    {
      storage.erase(s[p1]);
      ++p1;
    }
    }

  print(max);
}
