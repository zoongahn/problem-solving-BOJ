#include <iostream>
using namespace std;

int main()
{
    int M, N;
    cin >> N >> M;

    int **A = new int *[N];
    int **B = new int *[N];
    for (int i = 0; i < N; i++)
    {
        A[i] = new int[M];
        B[i] = new int[M];
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> A[i][j];
        }
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cin >> B[i][j];
        }
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            A[i][j] += B[i][j];
        }
    }
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < M; j++)
        {
            cout << A[i][j] << " ";
        }
        cout << endl;
    }
}