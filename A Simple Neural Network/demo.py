from numpy import exp, array, random, dot

class NeuralNetwork():
    def __init__(self):
        # Seed the random number generator, so it generates the same numbers
        # every time the program runs
        random.seed(1)

        # We model a single neuron, with 3 input connections and 1 output connectionsself.
        # We assign random weights to a 3 * 1 matrix, with values in the range -1

if __name__ == '__main__':

    #initialize a single neuron neural network
    neural_network = NeuralNetwork()

    print ('Random starting synaptic weights:')
    print (neural_network.synaptic_weights)

    #The training set. We have 4 examples, each consisting of 3 inout values
    # and 1 output valueself.
    training_set_inputs = array([[0,0,1], [1,1,1], [1,0,1], [0,1,1]])
    training_set_outputs = array([[0,1,1,0]]).T

    # Train the neural network using a training setself.
    # Do it 10,000 times and make small adjustments each timeself.
    neural_network.train(training_set_inputs, training_set_outputs, 10000)

    print("New synaptic weights after training:")
    print(neural_network.synaptic_weights)

    # Test the neural neural_network
    print('Considering new situation [1, 0, 0] -> ?:')
    print neural_network.think(array[1, 0, 0])
