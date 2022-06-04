#include<iostream>
#include <list>

using namespace std;

class G{
public:
	int ves; list<int> *g; int *in;

	G(int ves);
	~G(){delete[] g; delete[] in;}

	void add(int v, int w){
	    g[v].push_back(w);
	    in[w]++;
    }

	bool iec(); bool isSC(); void dfshelp(int v, bool visi[]);

	G gt();
};

G::G(int ves){
	this -> ves = ves;

	g = new list<int>[ves];

	in = new int[ves]; fill(in, in + ves, 0);
}

bool G::iec(){
	if(!isSC()) return false;

	for(int i = 0; i < ves; i++){
		if(g[i].size() != in[i])
			return false;
	}

	return true;
}

void G::dfshelp(int v, bool visi[]){
	visi[v] = true;

	for(auto i = g[v].begin(); i != g[v].end(); ++i){
		if(!visi[*i])
			dfshelp(*i, visi);
    }
}

G G::gt(){
	G w(ves);

	for(int v = 0; v < ves; v++){
		for(auto i = g[v].begin(); i != g[v].end(); ++i){
			w.g[*i].push_back(v);
			w.in[v]++;
		}
	}

	return w;
}

bool G::isSC()
{
	bool visi[ves]; fill(visi, visi + ves, false);

	int n;

	for(n = 0; n < ves; n++){
		if (g[n].size() != 0)
            break;
	}

	dfshelp(n, visi);

	for (int i = 0; i < ves; i++)
		if (g[i].size() != 0 && !visi[i])
			return false;

	G gr = gt();

    fill(visi, visi + ves, false);

	gr.dfshelp(n, visi);

	for (int i = 0; i < ves; i++){
		if (g[i].size() != 0 && !visi[i])
			return false;
	}

	return true;
}

bool solve(int n, string a[]){
	G g(26);

	for (int i = 0; i < n; i++){
		string x = a[i];
		g.add(x[0] - 'a', x[x.size() - 1] - 'a');
	}

	return g.iec();
}

int main()
{
    int n; cin >> n;
	string a[n];

	for(int i = 0; i < n; i++)
        cin >> a[i];

    cout << (solve(n, a) ? "Yes" : "No") << endl;
}
