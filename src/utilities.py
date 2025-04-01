import os
import shutil

def copy_static_to_output_dir(output_dir):
    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)
    project_root = os.path.dirname(current_dir)

    static_path = os.path.join(project_root, "static")
    output_dir  = os.path.join(project_root, output_dir)

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)

    recursive_copy(static_path, output_dir)

def recursive_copy(source_path, dest_path):
    src_files = os.listdir(source_path)
    if len(src_files) == 0:
        return
    for file in src_files:
        full_source_path = os.path.join(source_path, file)
        if os.path.isfile(full_source_path):
            shutil.copy(full_source_path, dest_path)
        else:
            new_dest = os.path.join(dest_path, file)
            os.mkdir(new_dest)
            recursive_copy(full_source_path, new_dest)

