import numpy as np
import matplotlib.pyplot as plt

class NeuralNetwork:
    def __init__(self, learning_rate):
        self.weights = np.array([np.random.randn(), np.random.randn()])
        self.bias = np.random.randn()
        self.learning_rate = learning_rate

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def _sigmoid_deriv(self, x):
        return self._sigmoid(x) * (1 - self._sigmoid(x))

    def predict(self, input_vector):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self._sigmoid(layer_1)
        prediction = layer_2
        return prediction

    def _compute_gradients(self, input_vector, target):
        layer_1 = np.dot(input_vector, self.weights) + self.bias
        layer_2 = self._sigmoid(layer_1)
        prediction = layer_2
        derror_dprediction = 2 * (prediction - target)
        dprediction_dlayer1 = self._sigmoid_deriv(layer_1)
        dlayer1_dbias = 1
        dlayer1_dweights = (0 * self.weights) + (1 * input_vector)
        derror_dbias = (derror_dprediction * dprediction_dlayer1 * dlayer1_dbias)
        derror_dweights = (derror_dprediction * dprediction_dlayer1 * dlayer1_dweights)
        return derror_dbias, derror_dweights

    def _update_parameters(self, derror_dbias, derror_dweights):
        self.bias = self.bias - (derror_dbias * self.learning_rate)
        self.weights = self.weights - (derror_dweights * self.learning_rate)

    def train(self, input_vectors, targets, iterations):
        cumulative_errors = []
        for current_iteration in range(iterations):
            random_data_index = np.random.randint(len(input_vectors))
            input_vector = input_vectors[random_data_index]
            target = targets[random_data_index]
            derror_dbias, derror_dweights = self._compute_gradients(input_vector, target)

            self._update_parameters(derror_dbias, derror_dweights)

            if current_iteration % 100 == 0:
                # print(f"On current iteration {current_iteration}")
                cumulative_error = 0
                for data_instance_index in range(len(input_vectors)):
                    data_point = input_vectors[data_instance_index]
                    target = targets[data_instance_index]
                    prediction = self.predict(data_point)
                    error = np.square(prediction - target)
                    cumulative_error = cumulative_error + error
                cumulative_errors.append(cumulative_error)
        return cumulative_errors

# input_vectors = np.array([[3, 1.5],[2, 1],
#     [4, 1.5],
#     [3, 4],
#     [3.5, 0.5],
#     [2, 0.5],
#     [5.5, 1],
#     [1, 1],
#     [2, 2],
#     [1.5, 8.5],
#     [9.5, 5],[0, 0.5],])

input_vectors = np.array([[29, 10], [66, 18], [98.5, 1.0], [75, 43], [71, 64], [3, 73], [91.0, 94.5], [16, 8], [49, 75], [11.5, 10.5], [32.5, 55.0], [96.0, 84.0], [78.5, 70.5], [86.0, 14.0], [22, 67], [86.0, 63.5], [18, 57], [86, 1], [58, 78], [38.5, 34.0], [30.0, 24.0], [3, 4], [70, 65], [61.5, 82.5], [81, 2], [29, 4], [77, 31], [70, 53], [83.0, 75.5], [64.5, 1.5], [18, 24], [53.0, 63.5], [68, 67], [18, 26], [66, 44], [21.5, 95.5], [1, 72], [80.5, 91.0], [78, 44], [57.5, 56.5], [69.5, 47.5], [41, 52], [72.0, 51.5], [63.0, 22.0], [31.5, 59.5], [37.5, 40.5], [11, 26], [96.0, 38.5], [78.5, 92.5], [97.0, 48.0], [90, 80], [49.0, 48.0], [87, 86], [4.0, 72.0], [74.5, 71.0], [70, 97], [7.0, 94.5], [9, 89], [70, 36], [2, 4], [10.5, 95.5], [20.0, 93.0], [19, 85], [12.5, 53.0], [30, 48], [6, 92], [44, 33], [95.0, 59.5], [56, 55], [40.5, 92.0], [50, 42], [84.5, 14.0], [69, 97], [76, 11], [8, 75], [26, 60], [50.5, 22.0], [45.5, 55.5], [94.5, 77.5], [13, 27], [24.0, 85.0], [47, 5], [51, 88], [54, 4], [71.5, 21.5], [36, 87], [29, 19], [18, 14], [79.0, 2.5], [35, 8], [22.0, 31.5], [30.0, 58.0], [88, 99], [55, 85], [61.0, 94.5], [4.0, 65.0], [67.5, 32.5], [5.0, 37.0], [2, 29], [44, 64], [89, 12], [98.0, 41.5], [68.0, 7.5], [36, 6], [91.5, 91.0], [90, 82], [72.5, 50.0], [76, 53], [38.0, 81.5], [91, 8], [27.5, 47.5], [22.5, 71.5], [26, 64], [91, 67], [16, 25], [40.0, 93.0], [14, 51], [40, 32], [87.5, 19.0], [81, 25], [44.5, 50.0], [62, 29], [62.0, 1.0], [87.5, 79.0], [38.5, 72.5], [4.0, 84.0], [43.0, 72.5], [52, 87], [43, 38], [70, 96], [98, 95], [35, 74], [74, 11], [5.0, 7.5], [3.5, 90.5], [51, 19], [65, 53], [76, 12], [82, 63], [50.0, 77.5], [38, 99], [6, 17], [74, 34], [47, 2], [49, 47], [47, 69], [73, 26], [96, 18], [55.5, 23.5], [24.5, 18.0], [43.5, 79.5], [37, 38], [25.0, 9.5], [46, 29], [92, 82], [60.5, 50.0], [13, 1], [26.5, 31.5], [83.0, 87.5], [88, 91], [53.0, 88.0], [7.0, 82.5], [65.5, 17.0], [47, 77], [67, 43], [82.5, 10.5], [64, 85], [50.5, 60.0], [91, 40], [87.0, 77.5], [34, 66], [44.5, 66.0], [54.5, 79.5], [43.0, 14.0], [45.5, 78.0], [37.5, 22.5], [19.0, 61.0], [73, 38], [48.5, 15.5], [5.5, 91.0], [81.0, 55.0], [19.0, 52.5], [44, 18], [76, 73], [14, 18], [72.0, 42.0], [46, 89], [88, 16], [93.5, 9.0], [63, 80], [82.0, 5.5], [34.0, 40.0], [45.0, 72.0], [48.0, 57.0], [98, 55], [63.0, 94.0], [2.0, 14.5], [26, 70], [39, 4], [78, 59], [24.5, 72.0], [57.0, 55.5], [75.0, 38.5], [11, 36], [47, 80], [23.0, 73.5], [11.5, 1.0], [31.5, 98.5], [47, 81], [32.5, 34.0], [62, 77], [26.5, 31.5], [96, 48], [92, 19], [27.5, 71.0], [88.0, 10.0], [80.0, 8.0], [93, 57], [98.5, 25.0], [35.0, 78.5], [88, 95], [63, 82], [69, 72], [95, 32], [73, 6], [46.5, 61.0], [8, 8], [16, 33], [90, 80], [37, 67], [27.0, 2.0], [27, 63], [85.0, 93.5], [66.5, 66.0], [76, 70], [28, 20], [41, 31], [68, 59], [15.0, 25.0], [23.5, 53.5], [31.5, 7.5], [83.5, 80.0], [22, 17], [87, 1], [48.5, 31.0], [81, 98], [39.5, 13.0], [1, 61], [84.5, 12.5], [4, 94], [27, 86], [45.5, 40.5], [12, 62], [9, 2], [67, 62], [75.5, 6.5], [33, 25], [74.0, 87.0], [94, 98], [3.5, 1.0], [14.5, 69.5], [89, 87], [11, 68], [40.5, 13.5], [50, 42], [58.5, 83.0], [20, 59], [11, 22], [21.0, 81.5], [69.0, 96.5], [21, 75], [57, 85], [5.5, 59.5], [76.5, 78.5], [68.0, 48.0], [48, 42], [38.5, 5.0], [81, 97], [96.0, 37.5], [50, 96], [60.0, 76.0], [31, 46], [25, 68], [48, 5], [25, 85], [2.0, 44.0], [56, 37], [98, 37], [70.0, 47.0], [6, 26], [53.5, 72.5], [73.0, 12.5], [20.0, 12.0], [78.0, 22.5], [75, 65], [68, 66], [15, 35], [80.5, 48.5], [95, 98], [1, 78], [3.0, 91.0], [31.5, 4.0], [59.5, 90.0], [58.5, 60.5], [28.0, 16.5], [60, 25], [61.5, 37.0], [67, 66], [5.5, 11.5], [22, 86], [3, 88], [53, 37], [52.5, 45.5], [56.5, 18.0], [56.0, 61.5], [79, 87], [96.0, 36.5], [26.0, 26.5], [8.5, 20.0], [28, 20], [43.5, 79.5], [84.5, 35.0], [67, 42], [7, 92], [67.5, 81.5], [44.0, 14.0], [28, 1], [68, 25], [80.5, 56.5], [82, 56], [99, 76], [24, 82], [96, 14], [23, 92], [96, 94], [72, 18], [4, 41], [85.5, 92.5], [40.5, 54.5], [20, 46], [50, 22], [50.5, 96.0], [38, 83], [61.5, 15.0], [61.0, 13.0], [76.5, 28.0], [97, 27], [35, 19], [47.0, 87.0], [12.0, 75.5], [12, 81], [25.5, 83.0], [72, 42], [80, 22], [24.0, 11.5], [37, 34], [77.5, 17.5], [79, 43], [70.5, 56.0], [42.5, 93.0], [81, 13], [72, 7], [87, 43], [81.0, 30.0], [39, 70], [75, 3], [31.0, 11.0], [82, 30], [2, 50], [33.5, 14.5], [3, 31], [56, 82], [21, 82], [23, 18], [62, 26], [81, 63], [67.0, 74.0], [89, 7], [74.0, 12.5], [95.0, 54.5], [43, 68], [20, 37], [25.5, 1.5], [85, 59], [50.5, 88.0], [55, 2], [3, 56], [81, 64], [75.0, 2.0], [30.0, 16.5], [57.0, 91.0], [10.5, 57.0], [53.5, 43.5], [62.0, 91.0], [22.0, 56.0], [13.5, 13.5], [73.0, 12.0], [21.5, 69.0], [58.0, 69.0], [69, 95], [12, 71], [39, 93], [87.0, 97.0], [16, 70], [68, 62], [95, 12], [56.0, 59.5], [85.0, 53.5], [16, 17], [91, 39], [43, 71], [59.0, 57.5], [64.5, 6.0], [64, 85], [82.5, 14.5], [83, 11], [7, 22], [30.0, 89.5], [52, 1], [42, 19], [6.5, 36.0], [98, 31], [78.5, 43.0], [80.5, 33.0], [69, 16], [76.5, 78.5], [69.5, 7.0], [3, 7], [31.5, 40.5], [39.5, 61.0], [47, 16], [54.0, 53.0], [39, 76], [13.0, 61.5], [80.5, 68.5], [55.0, 68.0], [99, 86], [11, 15], [2, 13], [10.5, 4.5], [16, 11], [69.0, 70.5], [55, 96], [51.0, 78.5], [5.0, 42.0], [84.5, 41.0], [47, 87], [24.0, 5.5], [26, 12], [56, 31], [50, 85], [43, 16], [24, 27], [6.5, 9.5], [83.0, 8.0], [93.5, 33.0], [11, 92], [56.0, 14.5], [19, 37], [48, 91], [69.5, 42.0], [31.5, 99.0], [45, 56], [11.5, 22.0], [39, 65], [11.5, 73.5], [25.0, 89.5], [90.0, 21.5], [62.5, 86.0], [22, 26], [93.0, 48.0], [78.0, 43.5], [78, 62], [80, 43], [17, 11], [53.0, 73.0], [62.0, 10.0], [44.0, 91.0], [94, 5], [55.0, 9.5], [61, 38], [4.5, 64.5], [43.0, 48.5], [29.0, 5.5], [40.5, 45.5], [84.0, 58.5], [22.5, 85.5], [54, 85], [27.5, 56.5], [66.0, 61.5], [86, 1], [26.5, 42.5], [65.0, 20.5], [63, 50], [64, 91], [36, 86], [18.5, 46.5], [81, 97], [88, 89], [26, 78], [15.5, 71.5], [51, 71], [82.5, 32.5], [3.0, 36.0], [88, 40], [6.0, 37.5], [59, 15], [87, 22], [5, 46], [53, 68], [97, 67], [48, 75], [88, 69], [20.5, 14.5], [40.0, 19.5], [58, 63], [17, 72], [47.0, 37.0], [61, 37], [4, 95], [96.5, 54.5], [69.0, 73.0], [44, 99], [24, 2], [82.5, 97.5], [54, 25], [76.5, 75.0], [50.5, 60.0], [41.0, 70.0], [56, 63], [95, 9], [84, 64], [99, 77], [48.0, 30.5], [8, 64], [86, 30], [80.0, 58.5], [63.5, 7.0], [12, 48], [58, 84], [43.0, 33.0], [63.0, 16.0], [78, 10], [70, 3], [18, 36], [45.0, 84.0], [18.0, 86.0], [84, 93], [44.5, 15.0], [25, 29], [6, 28], [43, 75], [93, 36], [86.5, 36.0], [75, 87], [86, 54], [20, 78], [76, 15], [52, 55], [16.5, 63.0], [94, 12], [64, 83], [92.5, 84.0], [21, 55], [60.5, 6.5], [99.0, 78.5], [95, 30], [1, 77], [28, 81], [89.0, 75.0], [54.0, 83.5], [9.5, 28.0], [70.0, 83.0], [62.0, 63.0], [70.0, 46.0], [52, 58], [97.5, 71.0], [12, 59], [96.0, 54.5], [67, 60], [57.0, 26.0], [21.0, 99.5], [27, 59], [92.0, 33.0], [44.5, 98.5], [30, 47], [87, 15], [12.0, 31.0], [64, 80], [49, 12], [54, 11], [74, 8], [4, 34], [36.5, 1.5], [39, 76], [26, 95], [12, 75], [35.5, 84.5], [70.0, 91.5], [71, 91], [94.0, 32.5], [92, 75], [99.0, 32.5], [55, 65], [82, 54], [19.0, 84.5], [78.5, 58.0], [63, 71], [79.0, 71.0], [98, 4], [63.0, 5.5], [64.0, 26.5], [15, 2], [46.0, 76.0], [37.5, 77.5], [4, 57], [92, 46], [67.0, 97.0], [8.5, 72.5], [71.5, 37.5], [31, 56], [93.0, 39.5], [46.0, 86.0], [33, 81], [48.5, 23.5], [85, 34], [58.5, 41.0], [39, 52], [58.0, 77.0], [27.5, 48.5], [54, 13], [90.0, 71.0], [22, 87], [54.0, 27.5], [99, 1], [76.0, 8.5], [76.5, 50.5], [17.5, 82.0], [97.5, 23.5], [99.0, 88.5], [96.0, 72.0], [47, 4], [7, 74], [8.5, 99.0], [45.5, 80.0], [76.0, 59.0], [24, 62], [85, 98], [53.0, 16.0], [90.0, 84.0], [29.0, 56.0], [66, 21], [7.5, 62.0], [12.5, 8.0], [51, 8], [74.5, 98.0], [75, 25], [93.5, 67.5], [27.0, 21.5], [79.0, 61.5], [3.0, 71.5], [49, 14], [67.5, 85.0], [89, 4], [96, 49], [85.5, 48.0], [18, 89], [99.5, 31.0], [2.5, 37.5], [68.5, 14.5], [86, 22], [98.5, 65.5], [74.5, 5.0], [8, 17], [33, 55], [84, 48], [87.0, 81.5], [8.5, 93.0], [76.5, 39.0], [7, 47], [72, 65], [21.5, 58.5], [29, 79], [13.5, 60.5], [75.0, 95.5], [32, 67], [2.5, 50.5], [9, 51], [5, 88], [5, 18], [93.0, 70.5], [16, 66], [43.0, 8.5], [43.5, 90.5], [32, 65], [11, 96], [39.5, 17.0], [2.0, 94.0], [59, 89], [86, 58], [59, 90], [58, 29], [85.0, 5.0], [86.5, 38.5], [36, 2], [33.0, 15.5], [87.5, 36.5], [67.5, 48.5], [3.0, 93.5], [67.5, 26.0], [22.5, 86.0], [51.0, 69.0], [79, 1], [33.5, 86.5], [53.5, 44.0], [16.5, 16.5], [35, 53], [70, 2], [66, 94], [52, 25], [35, 4], [26, 52], [14, 65], [52.5, 32.5], [77, 10], [90.5, 75.0], [48, 27], [43, 39], [76.5, 3.0], [39.5, 44.5], [31, 57], [12.5, 50.0], [33, 8], [29, 57], [49, 27], [78, 91], [17.0, 14.0], [95.5, 49.0], [62.0, 14.0], [1.5, 55.5], [16.0, 34.5], [85.0, 55.5], [59.5, 38.5], [69.5, 41.0], [84, 4], [62, 11], [78.0, 35.0], [64, 6], [55.5, 58.5], [41, 33], [34, 3], [72, 46], [5, 56], [74, 47], [74, 66], [19, 18], [24.0, 73.5], [31, 21], [76, 75], [64.0, 36.5], [3.0, 81.0], [26.5, 75.0], [80, 78], [38.5, 17.0], [3.5, 23.0], [12.0, 58.5], [10, 3], [98, 13], [39, 96], [30, 48], [68, 6], [52.5, 87.5], [48, 3], [75.0, 53.5], [50.5, 16.0], [93, 64], [99, 47], [53.0, 34.5], [27, 43], [60, 54], [26, 86], [21.0, 23.0], [70, 30], [92.0, 62.5], [21, 64], [14, 64], [50, 37], [63, 33], [92.5, 17.0], [38.5, 37.5], [42, 4], [10.0, 6.0], [80, 56], [11.5, 1.5], [97.0, 68.5], [1.0, 8.0], [48, 73], [37, 15], [11.5, 25.5], [37, 14], [84.5, 5.5], [46, 48], [97, 7], [64.5, 7.0], [54, 7], [30.0, 61.0], [12.0, 9.5], [49, 25], [53.0, 69.0], [22, 98], [88.0, 7.0], [63, 85], [64.5, 4.5], [50.5, 27.0], [41.0, 79.0], [48, 65], [66, 7], [5.5, 33.5], [13, 83], [94.0, 79.5], [29, 1], [81, 91], [50.5, 13.5], [29, 34], [52, 93], [14, 29], [25.5, 28.5], [68.0, 23.5], [95, 23], [18.0, 25.0], [42.0, 29.5], [10.0, 9.5], [95, 54], [60, 92], [16, 70], [34, 42], [26, 32], [88, 67], [43, 62], [99.5, 92.5], [56, 1], [80, 31], [23, 91], [63, 53], [51.5, 67.0], [14, 14], [31, 88], [78.5, 66.5], [69, 94], [4.5, 35.0], [77.0, 65.0], [84, 12], [70, 67], [69.5, 76.0], [67, 17], [49, 25], [43, 47], [23.0, 15.5], [5, 8], [85, 74], [72.5, 70.5], [15.5, 49.5], [87, 97], [74, 85], [90.5, 30.5], [83.5, 92.5], [96, 90], [23.5, 79.5], [51.5, 15.5], [40, 66], [83.5, 46.5], [14.0, 9.5], [61, 66], [80, 77], [23, 72], [64, 29], [36.5, 18.0], [1.5, 20.5], [47.0, 70.0], [76, 94], [88, 27], [62, 11], [54.0, 16.0], [59.0, 69.5], [74.0, 59.5], [38.5, 28.0], [56.5, 21.5], [78, 56], [44.0, 31.0], [13, 49], [24.0, 18.0], [65, 40], [86, 98], [28.5, 95.5], [97.5, 27.0], [55, 38], [11.5, 56.5], [4, 97], [8, 6], [29.5, 13.5], [13.5, 57.0], [51, 7], [84.5, 76.0], [27, 53], [44.5, 93.5], [68, 78], [86, 45], [19, 37], [3.5, 26.5], [63.0, 32.0], [95, 52], [58.5, 85.5], [45, 50], [63.0, 15.5], [8, 99], [16, 60], [14.5, 53.0], [18.0, 75.5], [38.0, 59.5], [28, 3], [83, 76], [46.0, 59.5], [61.5, 12.5], [66.5, 39.0], [88.0, 50.0], [97.5, 21.5], [78, 34], [49, 25], [43.5, 64.0], [44, 47], [83, 93], [95, 44], [71, 70], [77, 35], [45.0, 60.0], [19, 61], [61.5, 73.0], [45, 23], [98.5, 86.5], [27.5, 99.0], [21.5, 97.0], [48, 70], [14, 19], [51, 50], [99.5, 22.0], [38, 87], [87.0, 67.5], [25.0, 85.5], [57.0, 55.0], [39, 90], [47, 76], [28.5, 7.0], [96.5, 40.5], [45.0, 76.5], [39.5, 46.5], [38, 94], [95, 23], [40, 25], [78, 28], [8, 22], [8, 71], [4.0, 83.0], [1.5, 18.5], [62.0, 91.5], [15, 3], [58.5, 68.5], [36.0, 12.5], [87.5, 8.0], [82.5, 47.0], [85, 70], [77.0, 82.0], [33.5, 24.5], [99, 55], [32, 13], [95.0, 3.0], [28, 95], [99, 46], [3.0, 47.5], [36.0, 43.0], [87, 58], [18.0, 55.0], [15.5, 87.5], [32.0, 75.5], [23, 61], [83, 4], [59.0, 13.0], [17.0, 67.0], [25, 31], [49.5, 73.5], [83, 23], [50.0, 71.5], [75.5, 38.0], [73.5, 50.0], [18, 14], [39.0, 1.5], [88.5, 7.0], [26.0, 85.5], [58, 78], [92, 33], [33.5, 37.0]])

# targets = np.array([0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1])
targets = np.array([1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0])
learning_rate = 0.1

myinput = [[1,2.5]]

neural_network = NeuralNetwork(learning_rate)
training_error = neural_network.train(input_vectors, targets, 5000)
print(f"There is a {neural_network._sigmoid(np.dot(myinput, neural_network.weights) + neural_network.bias) * 100}% chance it doesn't have a decimal")
print(prediction := neural_network._sigmoid(np.dot(myinput, neural_network.weights) + neural_network.bias))



plt.plot(training_error)
plt.title("Percentage of training")
plt.xlabel("Iterations")
plt.ylabel("Error for all training instances")
plt.savefig("cumulative_error.png")
# plt.show()