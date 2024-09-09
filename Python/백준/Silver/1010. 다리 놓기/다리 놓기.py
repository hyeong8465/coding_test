T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    m_fac = 1
    for i in range(1,M+1):
        m_fac = m_fac*i
    n_fac = 1
    for i in range(1,N+1):
        n_fac = n_fac*i
    mn_fac = 1
    for i in range(1,M-N+1):
        mn_fac = mn_fac*i
    print(int(m_fac/(n_fac*mn_fac)))