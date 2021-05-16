// Input is two intigers - number of vertices and number of edges
#include<cstdio>
#include<ctime>
#include<cstdlib>
#include<algorithm>
#include<set>
#include<vector>

using namespace std;

typedef unsigned long long ull;

static unsigned int randomNumber(unsigned int n) {
    ull res = 0;

    for (int i = 0; i < 6; ++i) {
        res <<= 10;
        res ^= rand();
    }

    return res % n;
}


struct edge {
    ull v1, v2;
};

static set<ull> zbior;

static void wstaw(ull v1, ull v2) {
    if (v1 > v2) {
        swap(v1, v2);
    }
    zbior.insert((v2 << 32) | v1);
}

static bool sprawdz(ull v1, ull v2) {
    if (v1 > v2) {
        swap(v1, v2);
    }
    return zbior.find((v2 << 32) | v1) != zbior.end();
}

int main()
{
    srand(time(0)); rand();

    ull v;

    scanf("%llu", &v);

    if (v < 3) {
        printf("%llu 0\n", v);
        return 0;
    }

    vector<edge> edges;

    set<ull> zbior;

    if (v % 2 == 0) {
        for (ull i = 0; i < v; i += 2) {
            wstaw(i, i + 1);
        }
    }

    ull curr = 0;
    ull counter = 0;

    while (true) {
        ull next;
        do {
            next = randomNumber(v - 1);
            if (next >= curr) {
                ++next;
            }
        } while (sprawdz(curr, next));
        wstaw(curr, next);
        edge e;
        e.v1 = curr;
        e.v2 = next;
        edges.push_back(e);
        curr = next;
        if (!curr) {
            ++counter;
            if (counter > v / 10)
                break;
        }
    }

    //PRINT RESULTS

    ull* decode = new ull[v];

    for (ull i = 0; i < v; ++i) {
        decode[i] = i;
    }

    random_shuffle(decode, decode + v);

    printf("%llu %llu\n", v, (ull)edges.size());

    for (unsigned long long i = 0; i < edges.size(); ++i) {
        ull v1 = edges[i].v1;
        v1 = decode[v1] + 1;
        ull v2 = edges[i].v2;
        v2 = decode[v2] + 1;

        if (rand() % 2) {
            swap(v1, v2);
        }

        printf("%llu %llu\n", v1, v2);
    }

    delete[]decode;

    return 0;
}