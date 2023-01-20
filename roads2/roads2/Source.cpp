#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>

using namespace std;
#pragma comment(linker, "/STACK:16777216")

class DisjointSetUnion {
	int* parent;
	int* size;
	int numberOfComponents;

public:
	DisjointSetUnion(int n) {
		parent = new int[n];
		size = new int[n];
		for (int i = 0; i < n; i++) {
			parent[i] = i + 1;
			size[i] = 1;
		}
		numberOfComponents = n;
	}

	~DisjointSetUnion() {
		delete[]parent;
		delete[]size;
	}

	int findParent(int x) {
		if (x == parent[x - 1]) {
			return x;
		}
		else {
			parent[x - 1] = findParent(parent[x - 1]);
			return parent[x - 1];
		}
	}

	void unionSet(int x, int y) {
		int index_x = findParent(x), index_y = findParent(y);
		if (index_x != index_y) {
			if (size[index_x - 1] < size[index_y - 1]) {
				swap(index_x, index_y);
			}
			size[index_x - 1] += size[index_y - 1];
			parent[index_y - 1] = index_x;
			numberOfComponents -= 1;
		}
	}

	int getNumberOfComponents() {
		return numberOfComponents;
	}

};

int main() {
	ifstream in("input.txt");
	int numberOfCities = 0, numberOfRequests = 0, numberOfEarthQuakes = 0;

	in >> numberOfCities;
	in >> numberOfRequests;
	in >> numberOfEarthQuakes;

	bool* isDeleted = new bool[numberOfRequests];
	for (int i = 0; i < numberOfRequests; i++) {
		isDeleted[i] = false;
	}

	int** matrixOfRequests = new int* [numberOfRequests];
	for (int i = 0; i < numberOfRequests; i++) {
		matrixOfRequests[i] = new int[2];
	}

	for (int i = 0; i < numberOfRequests; i++) {
		for (int j = 0; j < 2; j++) {
			matrixOfRequests[i][j] = 0;
		}
	}

	int city1 = 0, city2 = 0;
	for (int i = 0; i < numberOfRequests; i++) {
		in >> city1;
		in >> city2;
		matrixOfRequests[i][0] = city1;
		matrixOfRequests[i][1] = city2;
	}

	int* roads = new int[numberOfEarthQuakes];
	for (int i = 0; i < numberOfEarthQuakes; i++) {
		roads[i] = 0;
	}

	for (int i = 0; i < numberOfEarthQuakes; i++) {
		in >> roads[i];
		isDeleted[roads[i] - 1] = true;
	}

	in.close();

	DisjointSetUnion myDSU = DisjointSetUnion(numberOfCities);
	for (int i = 0; i < numberOfRequests; i++) {
		if (isDeleted[i] == false) {
			myDSU.unionSet(matrixOfRequests[i][0], matrixOfRequests[i][1]);
		}
	}

	string result = "";
	for (int i = numberOfEarthQuakes - 1; i >= 0; i--) {
		int index = roads[i] - 1, components = myDSU.getNumberOfComponents();

		myDSU.unionSet(matrixOfRequests[index][0], matrixOfRequests[index][1]);
		if (myDSU.getNumberOfComponents() == 1) {
			if (components != 1)
				result += '0';
			else
				result += '1';
			for (int j = i - 1; j >= 0; j--) {
				result += '1';
			}
			break;
		}
		else {
			result += '0';
		}

	}
	std::reverse(result.begin(), result.end());

	ofstream out("output.txt");
	out << result;
	out.close();

	delete[]isDeleted;
	delete[]roads;
	for (int i = 0; i < numberOfRequests; i++) {
		delete[]matrixOfRequests[i];
	}
	delete[]matrixOfRequests;

	return 0;
}