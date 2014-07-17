from support import draw_dynamics;

from nnet.pcnn import pcnn_network, pcnn_parameters;
from nnet import *;

def template_dynamic_pcnn(num_osc, steps, stimulus = None, params = None, conn_type = conn_type.NONE):
    net = pcnn_network(num_osc, stimulus, params, conn_type);
    (t, y) = net.simulate(steps, None, None, True);
    #(t, y, thr, f, l) = net.simulate(steps, None, None, True);
    
    print(net.allocate_sync_ensembles());
    
    draw_dynamics(t, y, x_title = "Time", y_title = "y(t)", separate = True);
    #draw_dynamics(t, thr, x_title = "Time", y_title = "threshold");
    #draw_dynamics(t, f, x_title = "Time", y_title = "feeding");
    #draw_dynamics(t, l, x_title = "Time", y_title = "linking");
    
def one_neuron_unstimulated():
    template_dynamic_pcnn(1, 100, [0]);
    
def one_neuron_stimulated():
    template_dynamic_pcnn(1, 100, [1]);
    
def nine_neurons_stimulated_one_sync():
    params = pcnn_parameters();
    params.AT = 0.6;    # 0.5 - two synchronous ensembles and with threshold equals 0.6 or greater - one synchronous ensemble

    template_dynamic_pcnn(9, 100, [1] * 9, params, conn_type.GRID_FOUR);
    
def nine_neurons_stimulated_two_sync():
    params = pcnn_parameters();
    params.AT = 0.4;    # less than or equal to 0.5 - two synchronous ensembles and with threshold equal 0.6 or greater - one synchronous ensemble

    template_dynamic_pcnn(9, 100, [1] * 9, params, conn_type.GRID_FOUR);
    
def nine_neurons_mix_stimulated():
    template_dynamic_pcnn(9, 100, [1, 1, 1, 
                                   0, 0, 0, 
                                   1, 1, 1], None, conn_type.GRID_FOUR);
    
def twenty_five_neurons_mix_stimulated():
    params = pcnn_parameters();
    params.AT = 0.8;    # less than or equal to 0.5 - two synchronous ensembles and with threshold equal 0.6 or greater - one synchronous ensemble
        
    template_dynamic_pcnn(25, 100, [1, 1, 0, 1, 1, 
                                    1, 1, 0, 1, 1,
                                    0, 0, 0, 0, 0,
                                    1, 1, 0, 0, 0,
                                    1, 1, 0, 0, 0], params, conn_type.GRID_FOUR);

one_neuron_unstimulated();
one_neuron_stimulated();
nine_neurons_stimulated_one_sync();
nine_neurons_stimulated_two_sync();
nine_neurons_mix_stimulated();
twenty_five_neurons_mix_stimulated();