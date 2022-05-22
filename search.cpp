#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main(){
	fstream resultFile;
	string search;
	resultFile.open("results.txt",ios::in);
	cout << "========Kentel=======\n";
	cout <<"Type Something:";



	cin >> search;
	cout << "\n";

	if(resultFile.is_open()){
		string r;
	    while(getline(resultFile, r)){ //read data from file object and put it into string.
	         cout << r << "\n"; //print the data of the string
	    }
	    resultFile.close();
	}

	cout <<search;
	cout << "\n";
}