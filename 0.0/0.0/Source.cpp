#include <iostream>
#include <set>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream in;
    in.open("input.txt");
	string line;
    set<long> numbers;

    while(getline(in, line)) {
        numbers.insert(stoi(line));
    }
    in.close();


    long sum = 0;
    int i = 0;
   
    set <long> ::iterator it = numbers.begin();
    while (i < numbers.size()) {
        sum += *it;
        it++;
        i++;
    }
    
    ofstream out;
    out.open("output.txt");
    out << sum;

	return 0;
}