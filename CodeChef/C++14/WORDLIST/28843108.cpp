#include <bits/stdc++.h>

using namespace std;

bool is_punctuation(char c){
    for(char p: "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"){
        if(c == p)
            return true;
    }

    return false;
}

int main(){
    ios::sync_with_stdio(false); cin.tie(NULL);

    int n; cin >> n;

    cin.ignore();

    set<string> words;

    while(n--){
        string sentence; getline(cin, sentence);

        string new_sentence;

        for(char character: sentence){
            if(!is_punctuation(character))
                new_sentence += character;
        }

        string word;

        for(char character: new_sentence){
            character = tolower(character);

            if(character == ' '){
                if(word != ""){
                    words.insert(word);
                    word = "";
                }
            }

            else {
                word += character;
            }
        }

        if(word != "")
            words.insert(word);
    }

    cout << words.size() << '\n';

    for(string word: words)
        cout << word << '\n';
}
