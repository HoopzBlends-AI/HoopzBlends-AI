import os

# Define the directory structure for the data folder
data_structure = {
    'data': {
        'user_profiles': {
            'profile_1.json': '{"name": "User 1", "age": 25, "interests": ["AI", "Machine Learning"]}',
            'profile_2.json': '{"name": "User 2", "age": 30, "interests": ["Data Science", "Python"]}'
            # Add more user profiles if needed
        },
        'preferences': {
            'user_preferences.json': '{"theme": "Dark", "language": "English"}',
            'system_preferences.json': '{"logging": true, "notifications": false}'
        },
        'training_data': {
            'language_data': {
                'text_corpus.txt': 'This is a sample text corpus.',
                'speech_samples': {
                    'audio_files.wav': b'fake audio content'
                }
            },
            'behavior_data': {
                'gesture_samples': {
                    'gesture_files.dat': b'fake gesture data'
                }
            }
        }
        # Add more files or subdirectories as needed
    }
}

# Define the base directory where the data structure will be created
base_directory = '/path/to/your/base_directory'

def create_data_structure(directory, items):
    for item, value in items.items():
        path = os.path.join(directory, item)
        if isinstance(value, dict):
            os.makedirs(path)
            create_data_structure(path, value)
        else:
            with open(path, 'wb') as file:
                if isinstance(value, bytes):
                    file.write(value)
                else:
                    file.write(value.encode())

# Create the data structure
create_data_structure(base_directory, data_structure)
