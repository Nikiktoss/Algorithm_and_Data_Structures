#include <iostream>
using namespace std;

long long min_number_of_operations(long long** array_of_matrix, long long size) {
	long long** matrix_result = new long long* [size];
	for (int i = 0; i < size; i++) {
		matrix_result[i] = new long long[size];
	}

	for (int i = 0; i < size; i++) {
		for (int j = 0; j < size; j++) {
			matrix_result[i][j] = 0;
		}
	}

	for (int diagonal = 0; diagonal < size - 1; diagonal++) {
		for (int i = 0; i < size - diagonal - 1; i++) {
			int j = i + 1 + diagonal;
			for (int k = i; k < j; k++) {
				long long temp_num = matrix_result[i][k] + matrix_result[k + 1][j] + array_of_matrix[i][0] * array_of_matrix[j][1];

				if (matrix_result[i][j] == 0){
						matrix_result[i][j] = temp_num;
				}
				else {
					if (temp_num < matrix_result[i][j]) {
						matrix_result[i][j] = temp_num;
					}
				}
				
				
			}
		}
	}

	return matrix_result[0][size - 1];
}

int main() {
	long long num_of_cubes;
	cin >> num_of_cubes;

	long long** matrix_of_cubes = new long long* [num_of_cubes];
	for (int i = 0; i < num_of_cubes; i++) {
		matrix_of_cubes[i] = new long long[2];
	}

	for (int i = 0; i < num_of_cubes; i++) {
		for (int j = 0; j < 2; j++) {
			cin >> matrix_of_cubes[i][j];
		}
	}

	cout << min_number_of_operations(matrix_of_cubes, num_of_cubes);

	return 0;
}