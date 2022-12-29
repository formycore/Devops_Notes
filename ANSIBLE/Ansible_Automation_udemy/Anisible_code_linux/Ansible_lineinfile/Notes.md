# Ansible Module lineinfile
    - ansible.builtin.lineinfile
    - insert update or remove a line in a file
    - https://docs.ansible.com/ansible/latest/collections/ansible/builtin/lineinfile_module.html
# Main parameters

line(string): text to insert or append to the line
insertbefore(string): insert the line before a match
insertafter(string): insert the line after a match
validate(string): validate the file before copying
create(boolean): create a file if it does not already exist
state(string): present or absent
mode/owner/group: set file permissions
settype/seuser/selevel: set SELinux security context
