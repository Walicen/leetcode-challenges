class Solution {
  bool isPalindrome(String s) {
    s = s.toLowerCase();
    s = s.replaceAll(RegExp(r'[^a-z0-9]'), '');
    return s == s.split('').reversed.join('');
  }
}

void main() {
  final solution = Solution();
  print(solution.isPalindrome('arara'));
}
