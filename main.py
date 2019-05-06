m_e = 9.10938356e-31
R_inf = 10973731.568508
m_h = 1.6726219e-27 # Get source
m_d = 2*m_h

def R_h(m_n):
    return R_inf*((m_n)/(m_e+m_n))

def lambda_n(n, m_n):
    return 1/(R_h(m_n)*((0.25)-(1/(n**2))))

def lambda_ratio(m_1, m_2):
    return (1+(m_e/m_1))/(1+(m_e/m_2))

def lambda_diff(n):
    return lambda_n(n, m_h)*(1-(lambda_ratio(m_d, m_h)))

print(R_h(m_h))
print(lambda_ratio(m_h, m_d))

# print("3rd order H lambda: ", lambda_n(3, m_h)*10e9)
print("R_h for hydrogen: ", R_h(m_h))
    
print(lambda_diff(3.0)*10e9, " nm")
print(lambda_diff(4.0)*10e9, " nm")
print(lambda_diff(5.0)*10e9, " nm")
print(lambda_diff(6.0)*10e9, " nm")

