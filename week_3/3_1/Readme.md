# References
* https://docs.microsoft.com/pl-pl/azure/cloud-adoption-framework/ready/azure-best-practices/naming-and-tagging
* https://docs.microsoft.com/pl-pl/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming

# Naming
## Resources 
Name of the particular resource contains following information
```<Project-Reference>-<Resource-Type>-[<Workload/Application>]-<Environment>-<Region>-<Instance>```

Where:
* **Project Referece** - static prefix cs (szkola chmury)
* **Resource Type** - the name of azure resource e.g. vault (keyvault), storageaccount, cosmosdb etc.
* **Workload/Application** - to which part of the system particular resource belongs to (auth - authentication, services etc).
* **Environment** - can be:
   * sandbox
   * dev
   * qa
   * stage
   * prod
* **Region** - azure region (e.g. eastus, westus etc)
* instance - the number of instance

Example:
```sc-keyvault-auth-prod-eastus-001```
| **Azure Resource** | **Example** | **Note** |
| ------------------ | ------------ | -------- | 
| VNET| sc-vnet-sys-prod-eastus-001 |  |
| VM| sc-vm-l-elastic-prod-eastus-001, sc-vm-w-elastic-prod-eastus-002 | Postfix *l* for linux, *w* for windows |
| Storage Account |scsacssprodeastus001 | No special characters allowed, name limited to the 24 characters |
| Disks | sc-disc-vmelastic-prod-eastus-001 | Postfix determines to which VM particular disk belongs to |


# Tagging
Each resource should have following tags:
* **Type of creation:** resource created via CI/CD pipeline: **devops**, resource created manually: **manual**
* **Stage:** sbox, dev, qa, stage, prod
