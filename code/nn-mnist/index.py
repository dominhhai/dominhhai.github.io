import data_loader

training_data, validation_data, test_data = data_loader.load()

print(len(training_data))
print(len(validation_data))
print(training_data[0][0].shape)
