# ovh-dns-zone-terraform-importer

This repository contains a simple script that fetches DNS zone data from [OVHcloud](https://www.ovhcloud.com/)
and converts it to a `.tf` file understood by the official [Terraform OVH provider](https://registry.terraform.io/providers/ovh/ovh/latest/docs).

Additionally, a shell script with `terraform import` commands is generated.
This way it is possible to pull the existing infrastructure state.

## Usage

> NOTE: the script doesn't work on Python 3.10 due to a [bug](https://github.com/ovh/python-ovh/issues/105) in python-ovh. 

In order to generate the files run `python3 import.py <secrets.tf file path> example.com example_com.tf example_com.sh`.
