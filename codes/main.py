from production_function import FirmProduction
import numpy as np
from logging import *
import plotnine
from plotnine import ggplot, aes, geom_line

def assign_firm_labor():
    '''
    function assigns labor for a firm using zipf distribution
    
    '''
    distr_par = 4.0
    output_shape = 2000
    zipf_distr = np.random.zipf(distr_par, output_shape)
    return zipf_distr
    

def main():
    
    n = 10
    
    '''
    for i in range(1, 10):
        each_firm = FirmProduction()
        print(each_firm.cobb_douglas(i))
    '''
    
    labor_list = assign_firm_labor()
    my_x = [ f for f in labor_list]
    print(my_x)
    

if __name__ == '__main__':
    main()
