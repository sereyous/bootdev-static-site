import os
import shutil

def copy_static_to_public():
    current_file = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file)
    project_root = os.path.dirname(current_dir)

    static_path = os.path.join(project_root, "static")
    public_path = os.path.join(project_root, "public")

    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)

    recursive_copy(static_path, public_path)

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


copy_static_to_public()

