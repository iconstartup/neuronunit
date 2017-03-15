import unittest
import sys
import os
import warnings
from scoop import futures
import os



class OptimizationTestCase(unittest.TestCase):

    def test_func2map(file2map):
        exec_string='python '+str(file2map)
        os.system(exec_string)
        return 0

    def test_main(ind,guess_attrs=None):
        vm=VirtualModel()
        if guess_attrs!=None:
            for i, p in enumerate(param):
                value=str(guess_attrs[i])
                model.name=str(model.name)+' '+str(p)+str(value)
                if i==0:
                    attrs={'//izhikevich2007Cell':{p:value }}
                else:
                    attrs['//izhikevich2007Cell'][p]=value
            vm.attrs=attrs
            guess_attrs=None#stop reentry into this condition during while,
        else:
            import copy
            vm.attrs=ind.attrs

        begin_time=time.time()
        while_true=True
        while(while_true):
            from itertools import repeat
            if len(vm.lookup)==0:
                steps2 = np.linspace(50,190,4.0)
                steps = [ i*pq.pA for i in steps2 ]
                lookup2=list(map(f,steps,repeat(vm)))#,repeat(model)))

            m = lookup2[0]
            assert(type(m))!=None

            sub=[]
            supra=[]
            import pdb
            assert(type(m.lookup))!=None
            for k,v in m.lookup.items():
                if v==1:
                    while_true=False
                    end_time=time.time()
                    total_time=end_time-begin_time
                    return (m.run_number,k,m.attrs)#a
                    break
                elif v==0:
                    sub.append(k)
                elif v>0:
                    supra.append(k)
            sub=np.array(sub)
            supra=np.array(supra)
            if len(sub) and len(supra):
                steps2 = np.linspace(sub.max(),supra.min(),4.0)
                steps = [ i*pq.pA for i in steps2 ]

            elif len(sub):
                steps2 = np.linspace(sub.max(),2*sub.max(),4.0)
                steps = [ i*pq.pA for i in steps2 ]
            elif len(supra):
                steps2 = np.linspace(-1*(supra.min()),supra.min(),4.0)
                steps = [ i*pq.pA for i in steps2 ]

            lookup2=list(map(f,steps,repeat(vm)))



    def test_build_single(rh_value):
        '''
        This method is only used to check singlular sets of hard coded parameters.
        '''
        import quantities as qt
        get_neab.suite.tests[0].prediction={}
        get_neab.suite.tests[0].prediction['value']=rh_value*qt.pA
        print(get_neab.suite.tests[0].prediction['value'])
        attrs={}
        attrs['//izhikevich2007Cell']={}
        attrs['//izhikevich2007Cell']['a']=0.045
        attrs['//izhikevich2007Cell']['b']=-5e-09
        #attrs['//izhikevich2007Cell']['vpeak']=30.0
        #attrs['//izhikevich2007Cell']['vr']=-53.4989145966
        import quantities as qt
        model.update_run_params(attrs)
        score = get_neab.suite.judge(model)#passing in model, changes model
        error = []
        error = [ abs(i.score) for i in score.unstack() ]
        return model


    def test_run_all_files():
        '''
        run all files as different CPU threads, thus saving time on travis
        Since scoop is designed to facilitate nested forking/parallel job dispatch
        This approach should be scalable to larger CPU pools.
        '''
        files_to_exec=['exhaustive_search.py','nsga.py']
        clean_or_dirty=list(futures.map(testfunc2map,files_to_exec))
        return clean_or_dirty

if __name__ == '__main__':
    unittest.main()