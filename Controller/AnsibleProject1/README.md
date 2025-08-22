# Ansible Project

This repository contains the Ansible configuration for managing our infrastructure.

## Project Structure

- `inventory/`: Contains host inventory files for different environments (staging, production).
- `group_vars/` & `host_vars/`: Contain variables for groups of hosts and individual hosts.
- `roles/`: Contains reusable Ansible roles.
- `playbooks/`: Contains the main playbooks to be executed.

## How to Run

`ansible-playbook -i inventory/staging playbooks/site.yml`