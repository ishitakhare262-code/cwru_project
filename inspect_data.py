import scipy.io
import os


files = {
    'Healthy': 'data/97.mat',
    'Inner Race Fault': 'data/105.mat',
    'Ball Fault': 'data/118.mat',
    'Outer Race Fault': 'data/130.mat'
}

print("--- Inspecting CWRU Dataset Keys ---\n")

for label, file_path in files.items():
    if os.path.exists(file_path):
        mat_data = scipy.io.loadmat(file_path)
        # Filter out metadata keys starting with __
        signal_keys = [k for k in mat_data.keys() if not k.startswith('__')]
        print(f"[{label}] ({file_path}):")
        for key in signal_keys:
            print(f"  -> {key} (Shape: {mat_data[key].shape})")
        print("-" * 40)
    else:
        print(f"File missing: {file_path}")