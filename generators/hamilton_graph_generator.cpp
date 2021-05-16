// Input is two intigers - number of vertices and number of edges
#include<cstdio>
#include<ctime>
#include<cstdlib>
#include<algorithm>

using namespace std;

static unsigned int randomNumber(unsigned int n){
    unsigned long long res = 0;

    for(int i = 0; i < 6; ++i){
        res <<= 10;
        res ^= rand();
    }

    return res % n;
}

struct vert{
    unsigned long long v;
    unsigned long long r;

    bool operator<(vert a)const{
        if(r != a.r){
            return r < a.r;
        }
        return v < a.v;
    }
};

struct arc{
    unsigned long long v1, v2;
};

int main()
{
    srand(time(0));rand();

    unsigned long long v, e;

    scanf("%llu %llu", &v, &e);

    if(v * (v - 1) / 2 < e){
        fprintf(stderr, "ERROR: Zbyt duza liczba krawedzi!\n");
        return 2;
    }
    if(e < v){
        fprintf(stderr, "ERROR: Zbyt mala liczba krawedzi!\n");
        return 1;
    }

    vert* ranks = new vert[v];

    for(unsigned long long i = 0; i < v; ++i){
        ranks[i].v = i;
        ranks[i].r = randomNumber(2000000000);
    }

    sort(ranks, ranks + v);

    arc* arcs = new arc[e];

    unsigned long long e2 = e;
    unsigned long long ptr = 0;

    for(unsigned int i = 0; i < v; ++i){
        arcs[ptr].v1 = i;
        arcs[ptr++].v2 = (i + 1) % v;
    }

    e2 -= v;

    unsigned long long* tab = new unsigned long long[v];

    for(unsigned long long i = 0; i < v - 1; ++i){
        unsigned long long maxi = (v - i - 2) * (v - i - 3) / 2;
        unsigned long long mine = 0;

        if(e2 > maxi){
            mine = e2 - maxi;
        }

        unsigned long long maxe = min(e2, v - i - 2);

        unsigned long long d = maxe - mine + 1;
        unsigned long long ran = randomNumber(randomNumber(d) + 1) + mine;

        for(unsigned long long j = 0; j < v; ++j){
            tab[j] = j;
        }

        random_shuffle(tab + i + 2, tab + v);

        for(unsigned long long j = 0; j < ran; ++j){
            arcs[ptr + j].v1 = i;
            arcs[ptr + j].v2 = tab[i + 2 + j];
        }

        ptr += ran;
        e2 -= ran;
    }

    random_shuffle(arcs, arcs + e);

    printf("%llu %llu\n", v, e);

    for(unsigned long long i = 0; i < e; ++i){
        if(rand() % 2){
            printf("%llu %llu\n", ranks[arcs[i].v1].v + 1, ranks[arcs[i].v2].v + 1);
        }
        else{
            printf("%llu %llu\n", ranks[arcs[i].v2].v + 1, ranks[arcs[i].v1].v + 1);
        }
    }

	delete []tab;
    delete []arcs;
    delete []ranks;

    return 0;
}