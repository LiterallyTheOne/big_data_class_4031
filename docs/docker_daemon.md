# Docker Daemon

## Docker architecture

![Docker architecture](figures/docker_architecture.jpg)

## Docker Daemon vs Virtual Environment

The main difference between `Docker Daemon` and
`Virtual environment`:

* `Virtual environment`:
    * Runs a full guest operating system
        * kernel
        * libraries
        * system files
    * Uses `VM hypervisor`
        * VMWare
        * Virtual box
        * Hyper-v
        * KVM
    * `VM hypervisor` virtualizes on the hardware
    * `VM`s run on a physical host
* `Container`:
    * Shares the host's operating system
    * Each container has an isolated **user space** but doesn't need
      separate user operating system.

![dockerd vs vm](figures/docker_vs_vm.jpg)


## Different hypervisors

*