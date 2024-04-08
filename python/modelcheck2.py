import h5py

# Open the saved h5 file
with h5py.File('emotion_detection_model.h5', 'r') as f:
    # Print the keys of the file
    print(list(f.keys()))