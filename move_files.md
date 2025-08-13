# This is an Ansible playbook to keep file1, file3, and file5 in /demo, and move other files to /tmp
```
ubuntu@docker:~/demo$ ls
 file1  file2  file3  file4  file5  file6  file7  file8  file9
```
```
- name: move files expect for the selected ones  # Name of the playbook task group
  hosts: docker                                 # Target host(s) for the playbook
  tasks:                                        # List of tasks to execute
    - name: Get list of files in the demo directory   # Task: find all files in /demo
      find:
        paths: /home/ubuntu/demo                      # Directory to search for files
        file_type: file                               # Only look for files (not directories)
      register: demo_files                            # Save the result as 'demo_files'

    - name: Move unwanted files to /tmp               # Task: move files except file1, file3, file5
      command: mv "{{ item.path }}" /tmp/             # Move each file to /tmp
      loop: "{{ demo_files.files }}"                  # Loop over all found files
      when: item.path | basename not in ['file1', 'file3', 'file5']  # Only move files not in
```
```
ubuntu@docker:~/demo$ ls
file1  file3  file5
```