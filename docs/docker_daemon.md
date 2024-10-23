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
        * For example:
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

* Type 1 hypervisor
    * bare-metal
    * Runs directly on the underlying physical server
    * For example:
        * Hyper-v
        * Xen
* Type 2 hypervisor
    * hosted
    * Runs on top of an operating system
    * The operating system give them access to underlying physical server
    * `OS`
        * Controls hardware
    * `hypervisor`
        * Controls vms trough `OS`
    * For example:
        * VMWare
        * Virtual box

![different hypervisors](figures/hypervisor-types.png)

:::{note}
source of the image: https://www.appviewx.com/education-center/hypervisor/
:::