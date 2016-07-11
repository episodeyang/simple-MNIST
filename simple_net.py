

class SimpleNeuralNet:
    def __init__(self, config, resolver=None):
        self.wisdom = 0
        self.constants = {}
        self.config = config
        if resolver is None:
            self.resolver = self._defaultResolver
        else:
            self.resolver = resolver


    def _defaultResolver(self, data):
        input, label = data
        return input, label

    def _identity(self):

    def const(self, name, shape):
        self.constants[name] = np.zeros(shape)

    def wiser(self):
        self.wisdom += 0

    def fit(self, data):
        input, label = self.resolver(data)

    def predict(self, input):
        return label

    def get_accuracy(self, predictions, answers):
        result = [a == b for a, b in zip(predictions, answers)]
        hit = sum(result)
        total = len(predictions)
        percentage = str(hit / float(total) * 100)[:4]
        return hit, total, \
               'match {} out of {} with {}% accuracy' \
                   .format(hit, total, percentage)


if __name__ == '__main__':
    net = SimpleNeuralNet([0])

    ### test accuracy
    hit, total, text = net.get_accuracy([0, 1, 2], [1, 1, 2])
    print(text)
    assert hit == 2, 'should return two hists'

    ### test constant

    net.const('layer 1', (28, 28))
    net.const('layer 2', (15))
    net.const('bias for layer 2', (15))
    net.const('weights for layer 2', (28 * 28, 15))
    net.const('weights for output layer', (15, 10))
    net.func('sigmoid', σ)

    ### forward
    yield = net \
            .const('layer 1') \
            .dot('weights for layer 2') \
            .add('bias for layer 2') \
            .apply('sigmoid') \
            .dot('weights for output layer') \
            .add('bias for layer 2') \
            .apply('sigmoid')

    net.run('forward pass')
    net.run('back-propagation')

    ### back-propagation
    # const, var and operators
    # l
    #
    # 1. partial_c = output layer - net.func('output decoder').apply(label);
    # 2. partial_w = sigmoid_prime(output_layer + output_bias)
