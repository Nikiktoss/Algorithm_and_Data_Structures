#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

string createPalindrom(string text, string text_reverse){
	vector<vector<int>> matrix(text.size() + 1, vector<int>(text.size() + 1, 0));
	int n = text.size() + 1;
	
	for (int i = 1; i < n; i++) {
		for (int j = 1; j < n; j++) {
			if (text[i - 1] == text_reverse[j - 1]) {
				matrix[i][j] = matrix[i - 1][j - 1] + 1;
			}
			else {
				matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1]);
			}
		}
	}

	string result = "";
	int i = n - 1;
	int	j = n - 1;

	while (i != 0 && j != 0) {
		if (text[i - 1] == text_reverse[j - 1]) {
			result += text[i - 1];
			i--;
			j--;
		}
		else {
			if (matrix[i - 1][j] == matrix[i][j]) {
				i--;
			}
			else {
				j--;
			}
		}
	}
	reverse(result.begin(), result.end());
	return result;
}

int main() {
	ifstream in("input.txt");
	string line;
	in >> line;
	in.close();

	string line_reverse = line;
	reverse(line_reverse.begin(), line_reverse.end());
	string palindrom = createPalindrom(line, line_reverse);
	
	ofstream out("output.txt");
	out << palindrom.size() << endl;
	out << palindrom;
	out.close();

	return 0;
}