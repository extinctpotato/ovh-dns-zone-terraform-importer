import sys, hcl, ovh

# Parse args
creds_tf = sys.argv[1]
zone = sys.argv[2]

zone_res_name = zone.replace(".", "_dot_")

with open(creds_tf, 'r') as f:
    creds_hcl = hcl.load(f)

ovh_client = ovh.Client(**creds_hcl['provider']['ovh'])

record_ids = ovh_client.get(f'/domain/zone/{zone}/record')

for r_id in record_ids:
    record = ovh_client.get(f'/domain/zone/{zone}/record/{r_id}')

    print(f'resource "ovh_domain_zone_record" "{zone_res_name}_{r_id}" ' + '{')

    for k,v in record.items():
        print(f'    {k.lower()} = "{v}"')

    print('}\n')
